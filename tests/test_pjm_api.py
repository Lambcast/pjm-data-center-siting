"""Live-API tests for pjm_siting.pjm_api.

These tests hit the real PJM Data Miner 2 endpoint and are skipped when
``PJM_API_KEY`` is not set in the environment (or ``.env``). They use a
small WESTERN HUB pull to keep wall-clock time and rate-limit pressure low.
"""

from __future__ import annotations

import os
from datetime import date, timedelta

import pytest
from dotenv import load_dotenv

from pjm_siting.pjm_api import (
    ARCHIVE_CUTOFF_DAYS,
    PJMClient,
    archive_boundary,
)

load_dotenv()

WESTERN_HUB_PNODE = 51288
WESTERN_HUB_TYPE = "HUB"

EXPECTED_COLUMNS = {
    "datetime_beginning_ept",
    "pnode_id",
    "pnode_name",
    "total_lmp_da",
    "system_energy_price_da",
    "congestion_price_da",
    "marginal_loss_price_da",
}


pytestmark = pytest.mark.skipif(
    not os.getenv("PJM_API_KEY"),
    reason="PJM_API_KEY not set; live-API tests skipped.",
)


def test_archive_boundary_matches_constant():
    today = date(2026, 5, 27)
    assert archive_boundary(today) == today - timedelta(days=ARCHIVE_CUTOFF_DAYS)


def test_pull_standard_tier_two_days(tmp_path):
    client = PJMClient(cache_dir=tmp_path)
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=1)

    df = client.pull_da_lmps(WESTERN_HUB_PNODE, start, end)

    assert not df.empty, "expected day-ahead LMP rows for WESTERN HUB"
    assert EXPECTED_COLUMNS.issubset(set(df.columns))
    assert (df["pnode_id"] == WESTERN_HUB_PNODE).all()
    assert 40 <= len(df) <= 50  # 24 hours x 2 days, allowing for boundary edges
    assert df["total_lmp_da"].between(-100, 1000).all()


def test_pull_archive_tier_one_day(tmp_path):
    client = PJMClient(cache_dir=tmp_path)
    archive_day = archive_boundary() - timedelta(days=30)

    df = client.pull_da_lmps(
        WESTERN_HUB_PNODE,
        archive_day,
        archive_day,
        pnode_type=WESTERN_HUB_TYPE,
    )

    assert not df.empty, "expected archive-tier rows for WESTERN HUB"
    assert (df["pnode_id"] == WESTERN_HUB_PNODE).all()
    assert len(df) == 24


def test_archive_pull_without_type_raises(tmp_path):
    client = PJMClient(cache_dir=tmp_path)
    archive_day = archive_boundary() - timedelta(days=30)

    with pytest.raises(ValueError, match="pnode_type"):
        client.pull_da_lmps(WESTERN_HUB_PNODE, archive_day, archive_day)
