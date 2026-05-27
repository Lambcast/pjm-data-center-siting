# PJM Data Center Siting Project Brief

Last updated: 2026-05-27

## Project framing

Public, developer-perspective NPV ranking of 20 candidate hyperscale data center sites across the PJM Interconnection footprint. Six cost components monetized per site: energy (LMP), capacity (zonal UCAP × clearing price), interconnection (amortized network upgrade), property tax (state and county effective rates with PILOT/CRA/TIF), carbon ($100/tCO2 base, $190 EPA SCC comparator), and policy risk (probability-weighted by jurisdiction). Site rankings reported with simultaneous confidence sets via Mogstad-Romano-Shaikh-Wilhelm (2024), with covariance from Monte Carlo over parameter distributions.

The contribution is the developer-perspective ranking and the explicit policy-risk treatment. Existing public work (Shao et al. 2025, Kim et al. 2026) takes the system-planner perspective and does not price policy risk by jurisdiction.

## Locked decisions

**Methodology trio.** Mogstad-Romano-Shaikh-Wilhelm (2024, ReStud canonical) for rank inference; Swartzentruber and Sims (2026, SSRN 5404735) for risk-vs-ambiguity framing; Lade (2026) for host-community positioning anchor. Not Bistline; that was an attribution error caught and corrected.

**Site scope.** 20 sites, all PJM footprint (DOM, AEP, COMED, BGE, PSEG, PEPCO, APS, PPL, DPL, AECO, JCPL, METED, PENELEC, ATSI plus edges). 500 MW base facility, sensitivities at 250 and 1000 MW. 0.85-0.90 capacity factor. 20-year facility life. 8% nominal discount rate base, 6% and 10% sensitivities. Two BTM sites included (Susquehanna-adjacent confirmed; second BTM site to be picked from Calvert Cliffs, Peach Bottom, Limerick, or AEP-Ohio nuclear).

**Tech stack.** Python 3.12 with uv (Astral) for dependency management. DuckDB for analytical SQL. pandas, numpy, requests, python-dotenv, pyarrow, matplotlib for runtime. pytest, ruff, ipykernel for dev. openpyxl added 2026-05-26 for Excel reads. R subprocess in scripts/r/ for csranks rank inference. VS Code editor. Vercel for frontend. Windows/PowerShell development environment.

**Deliverables format.** Brattle-style PDF report (25-40 pages with appendices), hosted on lambcast.net and SSRN. Derived lambcast post 3000-5000 words. Vercel interactive frontend for sensitivity exploration. GitHub repository as technical backbone. NOT academic working paper format; the audience is hyperscaler hiring managers who read consulting reports daily.

**Voice and writing.** Clarity over sophistication. Joseph Mitchell and James Baldwin as reference voice. Brattle / JLARC / Synapse report register. Lade four-part series as style template. No em dashes. Prose for analysis, bullets only for action items and technical steps. Direct pushback when reasoning is weak. Invite collaboration; show work.

**Frontend architecture.** Static React/Vite on Vercel with pre-computed parameter grid stored as Parquet (~5MB). DuckDB-WASM in browser reads the parquet. No backend, no solver, no server-side computation. Frontend serves only derived outputs (NPVs, rankings, confidence sets) per PJM Data Miner redistribution restriction.

**Timeline.** 5 weeks of execution plus 1 buffer week. Current position: week 1, day 2. Week 1 ends with locked 20-site list, methodology note in docs/methods.md, initial PJM data pulled. Week 2 builds cost-stack functions and unit tests. Week 3 runs full sensitivity grid and rank inference. Week 4 builds frontend. Week 5 drafts report and SSRN submission. Week 6 buffer for revisions and coordinated launch.

## Current state

**Repo.** C:\Projects\pjm-data-center-siting, public at github.com/Lambcast/pjm-data-center-siting. 10+ commits pushed to origin/main as of 2026-05-27.

**Documentation.** docs/overview.md (project framing), docs/decisions.md (decision log), docs/methods.md (skeleton, to be filled week 3), docs/flow.md (living workflow document), docs/references.bib (48 verified BibTeX entries), docs/source_inventory.md (download checklist).

**PJM data access.** Public-tier access active for alamb2 / account 3522 effective 2026-05-19. Data Miner 2 Non-Member API access active effective 2026-05-26. Subscription key stored in .env (gitignored), authenticated against api.pjm.com production endpoint, confirmed working with metadata and real data pulls on 2026-05-27.

**Site selection universe.** Form 860 (2024 release) loaded and filtered. 16,132 nationwide plants reduced to 2,234 PJM-footprint plants reduced to 480 candidate plants at transmission voltages (138 kV and above). State-by-voltage stratification matrix in notebooks/01_eia860_exploration.ipynb. PA, VA, IL, OH, MD hold most of the high-voltage mass.

**API integration baseline.** Subscription key authentication via Ocp-Apim-Subscription-Key header confirmed. Standard tier accepts pnode_id; archive tier rejects pnode_id and requires date plus type plus row_is_current plus version_nbr filters with client-side narrowing on pnode. Archive boundary confirmed empirically at exactly 731 days back from current date, matching the metadata field; today's effective boundary is 2024-05-26. Maximum 50,000 rows per response. Rate limit 6 requests per minute for non-members. Client module shipped as src/pjm_siting/pjm_api.py (200 lines) with live-API tests at tests/test_pjm_api.py; committed as 2d627e0.

## Not yet decided

**20-site list.** Universe is 480; need final cut to 20. Stratification logic must cover the six major PJM operating zones (Dominion, AEP, COMED, PSEG, PPL, BGE/PEPCO) with at least one congestion-discount and one congestion-premium site per zone where data supports it. Two BTM sites identified (Susquehanna; second TBD). Final cut needs LMP history to identify congestion regimes, which requires either standard-tier pulls for recent years or archive-tier pulls for 2022-2023.

**Carbon price internal logic.** $100/tCO2 base case is researcher-chosen approximation of implicit shadow price under 24/7 CFE commitments, not Microsoft's $15/ton internal fee. The justification language for the report needs careful drafting; the carbon price is the most contestable input and needs to be defended explicitly.

**Property tax data sources.** State effective rates are tractable; county-level PILOTs and CRAs require parcel-by-parcel research. The methodology must be defensible without claiming completeness; document the data gaps in the methods appendix.

**Frontend parameter grid scope.** 3 facility sizes × 3 discount rates × 4 carbon prices × 3 capacity scenarios × 3 LMP scenarios × 3 policy risk scenarios × 20 sites = ~20K rows of pre-computed NPVs. Final grid scope decided week 3 when analysis reveals what the frontend should expose.

## Known constraints

**PJM data redistribution.** Non-member API access permits internal business use only. Vercel frontend serves only derived outputs (NPVs, rankings, summary statistics). No raw LMPs or capacity prices on the frontend or in the report. The Brattle / Synapse / IEEFA precedent confirms this is workable.

**PJM CEII restriction.** PJM does not publish coordinate data for substations or generators. EIA Form 860 and HIFLD substations are the workaround. Form 860 also includes Transmission or Distribution System Owner per plant, which provides direct generation-to-zone mapping; HIFLD is now planned as supplement rather than primary source.

**Rate limit.** 6 requests per minute for non-members vs. 600 for members. Associate membership is $2,500 per year and not justified for this project's scope.

## Honest project boundaries

This is not a machine learning project. The Monte Carlo wrapper and bootstrap-based rank inference are not ML. When describing the work in interviews, frame it as applied econometric modeling and structural cost analysis, not ML. The Applied ML class next semester is where the ML learning happens; the follow-up project will demonstrate ML.

The project does not promise to identify the single best site. It promises to rank a defensible candidate set under transparent assumptions, providing the framework an in-house hyperscaler team would build on top of. The intellectual contribution is the methodology and the comparative framing, not the specific recommendations.

## Failure modes to watch for

User's stated tendency: stacking learning tasks and building infrastructure when the analytical path feels uncertain. If the user starts opening docs/overview.md to "polish framing" instead of doing the analytical work in front of them, that is yak-shaving and should be called out. The framing is locked. Progress is in the data pipeline, the cost model, the parameter grid, the report writing. Not in scaffolding refinement.

A second pattern: the user is new to the tooling (pandas, SQL, DuckDB, git workflows) and benefits from explicit framing of what each tool is doing and why. Do not skip the conceptual frame to get to the syntax. The syntax becomes muscle memory; the conceptual understanding is what makes the project portable to future work.

A third pattern: the project sits at an intersection of applied economics and corporate financial analysis. The deliverable will look like spreadsheets and dollar values. The methodological choices (rank inference, policy risk pricing, comparative framing) are what make this economics rather than FP&A. Lead with methodology; let the cost tables follow.