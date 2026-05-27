"""PJM Data Miner 2 client (Non-Member tier).

Minimal client for the ``da_hrl_lmps`` feed. Loads ``PJM_API_KEY`` from ``.env``,
enforces the 6-requests-per-minute non-member rate limit, paginates against the
JSON body's ``totalRows`` field, routes standard vs archive tier per request
range, and caches completed past years as parquet under
``data/cache/lmps/<pnode_id>/<year>.parquet``.

The current year is never cached (subsequent days are not yet available, so the
on-disk file would silently go stale). Cached year files always contain the
full calendar year for that pnode; partial-year files are not written.

Archive-tier requests reject ``pnode_id`` filtering. The archive path therefore
requires the caller to pass ``pnode_type`` (e.g. ``"HUB"``, ``"ZONE"``) so the
response can be filtered client-side for the target ``pnode_id``.
"""

from __future__ import annotations

import os
import time
from collections import deque
from datetime import date, timedelta
from pathlib import Path
from typing import Iterator

import pandas as pd
import requests
from dotenv import load_dotenv

BASE_URL = "https://api.pjm.com/api/v1"
ARCHIVE_CUTOFF_DAYS = 731
MAX_ROWS_PER_REQUEST = 50_000
RATE_LIMIT_REQUESTS = 6
RATE_LIMIT_WINDOW_SECONDS = 60
DEFAULT_CACHE_DIR = Path("data/cache/lmps")


def archive_boundary(today: date | None = None) -> date:
    """Return the inclusive cutoff: requests strictly older go to archive tier."""
    today = today or date.today()
    return today - timedelta(days=ARCHIVE_CUTOFF_DAYS)


class PJMClient:
    """Minimal PJM Data Miner 2 Non-Member client.

    Loads ``PJM_API_KEY`` from the environment (and from ``.env`` via
    ``python-dotenv``) on construction. All HTTP requests pass through
    :meth:`_rate_limit`, which enforces the 6-requests-per-60-seconds
    non-member tier limit using a sliding window of request timestamps.
    """

    def __init__(self, cache_dir: Path | str = DEFAULT_CACHE_DIR) -> None:
        load_dotenv()
        key = os.getenv("PJM_API_KEY")
        if not key:
            raise RuntimeError(
                "PJM_API_KEY not set. Add it to .env or export it in the shell."
            )
        self._headers = {"Ocp-Apim-Subscription-Key": key}
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._request_times: deque[float] = deque(maxlen=RATE_LIMIT_REQUESTS)

    def _rate_limit(self) -> None:
        if len(self._request_times) < RATE_LIMIT_REQUESTS:
            return
        oldest = self._request_times[0]
        elapsed = time.monotonic() - oldest
        if elapsed < RATE_LIMIT_WINDOW_SECONDS:
            time.sleep(RATE_LIMIT_WINDOW_SECONDS - elapsed + 0.1)

    def _get(self, path: str, params: dict) -> dict:
        self._rate_limit()
        r = requests.get(
            f"{BASE_URL}/{path}", headers=self._headers, params=params, timeout=60
        )
        self._request_times.append(time.monotonic())
        if r.status_code != 200:
            raise RuntimeError(
                f"PJM API {r.status_code} for {path} with {params}: {r.text[:500]}"
            )
        return r.json()

    def _paginate(self, path: str, base_params: dict) -> Iterator[dict]:
        # X-TotalRows is not populated for da_hrl_lmps; use the JSON body's totalRows.
        start_row = 1
        params = dict(base_params)
        params.setdefault("rowCount", MAX_ROWS_PER_REQUEST)
        while True:
            params["startRow"] = start_row
            body = self._get(path, params)
            items = body.get("items", [])
            yield from items
            total = body.get("totalRows", 0)
            next_row = start_row + len(items)
            if not items or next_row > total:
                return
            start_row = next_row

    def pull_da_lmps(
        self,
        pnode_id: int,
        start_date: date,
        end_date: date,
        pnode_type: str | None = None,
    ) -> pd.DataFrame:
        """Pull day-ahead hourly LMPs for one pnode, ``start_date`` to ``end_date`` inclusive.

        Past calendar years hit (or populate) the parquet cache at
        ``<cache_dir>/<pnode_id>/<year>.parquet`` with the full year of data.
        The current calendar year always fetches the requested range fresh.

        Standard vs archive tier is decided per fetched segment against
        :func:`archive_boundary`. Archive segments require ``pnode_type``.
        """
        if start_date > end_date:
            raise ValueError(f"start_date {start_date} after end_date {end_date}")
        today = date.today()
        frames: list[pd.DataFrame] = []
        for year in range(start_date.year, end_date.year + 1):
            req_start = max(start_date, date(year, 1, 1))
            req_end = min(end_date, date(year, 12, 31), today)
            if req_end < req_start:
                continue
            if year < today.year:
                cache_path = self.cache_dir / str(pnode_id) / f"{year}.parquet"
                if cache_path.exists():
                    df = pd.read_parquet(cache_path)
                else:
                    df = self._fetch_range(
                        pnode_id, date(year, 1, 1), date(year, 12, 31), pnode_type
                    )
                    cache_path.parent.mkdir(parents=True, exist_ok=True)
                    df.to_parquet(cache_path, index=False)
                frames.append(_slice_to_range(df, req_start, req_end))
            else:
                frames.append(
                    self._fetch_range(pnode_id, req_start, req_end, pnode_type)
                )
        return (
            pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
        )

    def _fetch_range(
        self,
        pnode_id: int,
        start_date: date,
        end_date: date,
        pnode_type: str | None,
    ) -> pd.DataFrame:
        boundary = archive_boundary()
        if end_date < boundary:
            return self._fetch_archive(pnode_id, start_date, end_date, pnode_type)
        if start_date >= boundary:
            return self._fetch_standard(pnode_id, start_date, end_date)
        a = self._fetch_archive(
            pnode_id, start_date, boundary - timedelta(days=1), pnode_type
        )
        b = self._fetch_standard(pnode_id, boundary, end_date)
        return pd.concat([a, b], ignore_index=True)

    def _fetch_standard(
        self, pnode_id: int, start_date: date, end_date: date
    ) -> pd.DataFrame:
        params = {
            "datetime_beginning_ept": _fmt_range(start_date, end_date),
            "pnode_id": pnode_id,
            "row_is_current": "true",
            "format": "json",
        }
        return pd.DataFrame(list(self._paginate("da_hrl_lmps", params)))

    def _fetch_archive(
        self,
        pnode_id: int,
        start_date: date,
        end_date: date,
        pnode_type: str | None,
    ) -> pd.DataFrame:
        if pnode_type is None:
            raise ValueError(
                f"Archive-tier pull for {start_date}..{end_date} requires pnode_type "
                "(e.g. 'HUB', 'ZONE'); the archive API rejects pnode_id filtering."
            )
        params = {
            "datetime_beginning_ept": _fmt_range(start_date, end_date),
            "type": pnode_type,
            "row_is_current": "true",
            "version_nbr": 1,
            "format": "json",
        }
        df = pd.DataFrame(list(self._paginate("da_hrl_lmps", params)))
        if not df.empty:
            df = df[df["pnode_id"] == pnode_id].reset_index(drop=True)
        return df


def _fmt_range(start_date: date, end_date: date) -> str:
    return f"{start_date.isoformat()} 00:00 to {end_date.isoformat()} 23:59"


def _slice_to_range(df: pd.DataFrame, start_date: date, end_date: date) -> pd.DataFrame:
    if df.empty:
        return df
    ts = pd.to_datetime(df["datetime_beginning_ept"])
    mask = (ts.dt.date >= start_date) & (ts.dt.date <= end_date)
    return df.loc[mask].reset_index(drop=True)
