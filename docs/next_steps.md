# Next Steps

Last updated: 2026-05-27 end of session.

## Step 1: PJM API client module — COMPLETE

Committed as 2d627e0. Empirical archive boundary pinned at 2024-05-26 (731 days from 2026-05-27). Module at src/pjm_siting/pjm_api.py implements PJMClient with rate limiting (6 requests per 60 seconds, sliding-window deque), archive vs standard tier routing per request range, parquet cache at data/cache/lmps/<pnode_id>/<year>.parquet for completed past years, and pagination against JSON body totalRows. Archive segments require pnode_type and filter type-wide responses client-side. Live-API tests at tests/test_pjm_api.py — four tests, all green in 48s, skip cleanly when PJM_API_KEY is unset.

## Step 2: Plant-to-pnode mapping — NEXT

Build a lookup from the 480 candidate plants in Form 860 (filtered to 138 kV and above in notebooks/01_eia860_exploration.ipynb) to PJM pricing nodes. This is the highest-leverage conceptual decision in week 1 because it determines what subsequent LMP analysis actually measures.

Three implementation strategies considered:

(a) Snap each plant to its nearest gen-bus pnode by lat/long. Most accurate for BTM cases. Requires PJM bus list with coordinates at usable resolution; whether this exists publicly at fine resolution is uncertain.

(b) Use Form 860 Transmission or Distribution System Owner field to assign each plant to its operating zonal hub. Fast and clean but throws away within-zone congestion variation that is the entire point of the third filter in the five-filter site selection methodology.

(c) Hybrid: zonal hub default, gen-bus mapping only for BTM candidates and high-voltage sites where congestion regime classification matters.

Planned approach is (c). Deliverable: notebooks/02_pnode_mapping.ipynb plus data/processed/plant_pnode_map.parquet lookup table plus a half-page methods note in docs/methods.md documenting which mapping was used for which subset and why. Estimated one to two days.

## Step 3: LMP pulls and congestion regime classification

Pull 24 months of day-ahead hourly LMPs for the candidate pnode set. Volume: ~480 pnodes × 24 months × 24 hours = ~8.4M rows, fragmenting to roughly 170-300 API requests under the 6/min rate limit. Half-day to one-day wall-clock pulling, plus another day for classification.

Classify each candidate as congestion-discount, zonal-typical, or congestion-premium against its zonal hub via average basis and high-load-hour basis. Produce stratified short list of 50-150 ahead of hand-cut to 20.

Deliverable: data/processed/lmp_da_2024_2026.parquet and notebooks/03_congestion_regimes.ipynb with per-site basis distributions and stratification matrix. Estimated two days.

Together these three land the week 1 milestone: 20-site list locked and initial PJM data pulled.

## Open questions for step 2

Whether the PJM pnode endpoint returns bus-level pricing nodes with enough location metadata to snap Form 860 lat/long against. If not, fallback to pnode_name string matching against Form 860 plant names, which is messy but workable. Validation plan needs definition before any code is written.

How to handle plants connecting at multiple voltage levels (Grid Voltage, Grid Voltage 2, Grid Voltage 3 in Form 860). Likely use the highest voltage as the primary interconnection.

Which subset of the 480 sites genuinely needs bus-level mapping versus zonal hub. Initial cut: the two BTM candidates plus the top 50 highest-voltage sites. Open to revision once the data is in hand.
