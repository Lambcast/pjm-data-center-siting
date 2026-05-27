# Decision Log

Running log of project decisions. Newest at the top.

Format for each entry:

- **Date.**
- **Decision.** What was decided.
- **Options considered.** What was on the table.
- **Weighing.** What pulled in each direction.
- **Choice.** What was picked.
- **Rationale.** Why.

---

## 2026-05-27: EIA Form 860 (2024 release) loaded; 480-plant transmission-voltage candidate pool

- **Decision.** Use EIA Form 860 (2024 release) as the source for the candidate site universe. Filter to PJM balancing authority, then to plants connected at transmission voltages (138 kV and above). Use Form 860's Transmission or Distribution System Owner field as the direct generation-to-PJM-zone mapping. Defer HIFLD substation data as a possible later supplement rather than the primary geographic source for site selection.
- **Options considered.** EIA Form 860 with a 138 kV-and-above transmission filter (chosen); Form 860 with a broader voltage threshold to retain more candidates; HIFLD substation layer as the primary geographic source with Form 860 used only for ownership and generator attributes; PJM's published substation list as the primary source (CEII-restricted; coordinates not public).
- **Weighing.** Form 860 is updated annually, includes coordinates, and carries the Transmission or Distribution System Owner field that yields a direct mapping from each candidate plant to a PJM operating zone without a manual cross-walk. The 138 kV threshold is the conventional cut for "could plausibly host a 500 MW interconnection" and reduces 2,234 PJM-footprint plants to 480 candidates concentrated in PA, VA, IL, OH, and MD. A lower threshold inflates the candidate set with sites that cannot realistically host a hyperscale interconnection. HIFLD has more substation points than Form 860 has plants, but it lacks ownership and generator attributes and would still require manual zonal assignment.
- **Choice.** Form 860 (2024) with PJM-balancing-authority filter and the 138 kV-and-above voltage filter. 480 candidate plants. State-by-voltage stratification matrix in `notebooks/01_eia860_exploration.ipynb`.
- **Rationale.** A single source supplies everything first-pass site scoring needs: location, voltage, ownership, and zonal assignment. HIFLD is held in reserve for the case where a substation-level (rather than plant-adjacent) candidate becomes necessary downstream.

---

## 2026-05-27: PJM Data Miner 2 Non-Member API access provisioned and confirmed working

- **Decision.** Use the PJM Data Miner 2 Non-Member API as the source for LMP and capacity-market data, authenticated via subscription key. Production endpoint is `https://api.pjm.com/api/v1/`. The subscription key is stored in `.env` (gitignored) and loaded via `python-dotenv`. Access was provisioned on 2026-05-26 and confirmed end-to-end on 2026-05-27 against metadata and a 24-row WESTERN HUB day-ahead LMP pull.
- **Options considered.** Non-Member API (chosen; free, 6 requests per minute); Associate Member API ($2,500/year, 600 requests per minute); manual CSV downloads from the Data Miner 2 web UI; third-party scraped LMP archives.
- **Weighing.** Associate membership lifts the rate cap but is not justified at this scope: 6 requests per minute is slow but workable for a one-time historical pull. Manual CSV downloads are not reproducible. Third-party archives carry data-provenance risk and require separate validation against PJM's published series. The non-member API is the authoritative source with a defensible audit trail; the rate limit shapes pull design rather than blocking it.
- **Choice.** Non-Member API. Authentication via the `Ocp-Apim-Subscription-Key` header. Standard-tier requests accept a `pnode_id` filter; archive-tier requests reject `pnode_id` and require filtering by `datetime_beginning_ept` plus `type`, `row_is_current`, and `version_nbr`. Maximum 50,000 rows per response. Archive boundary empirically between February 2025 and May 2026; exact cutoff TBD before the historical pull strategy is finalized.
- **Rationale.** The free tier is sufficient for a one-time historical pull at this scope. The `pnode_id` restriction on archived data shapes the historical pull strategy but does not foreclose it. An upgrade to Associate membership can be revisited only if a substantive bottleneck emerges; none has.

---

## 2026-05-27: Archive boundary pinned empirically to a rolling 731 days

- **Decision.** Treat the standard/archive boundary on `da_hrl_lmps` as exactly `today - 731 days`, matching the `archiveCutoffDays: 731` value PJM returns in the feed metadata. Use this constant (`ARCHIVE_CUTOFF_DAYS = 731`) for routing in the API client.
- **Options considered.** Trust the metadata field as authoritative (chosen); leave the cutoff as TBD pending more empirical probing; pad the cutoff inward (say 720 days) to leave headroom in case PJM's accounting is non-inclusive at the boundary.
- **Weighing.** Probes on 2026-05-27 at 2024-05-25, 2024-05-29, 2025-01-01, and 2025-06-01 returned ARCHIVE_REJECT, OK, OK, OK respectively. The boundary sits exactly between 2024-05-25 and 2024-05-29, which is `today - 731 days = 2024-05-26`. Padding inward sacrifices recent archive data for no observed benefit; PJM's metadata and the empirical probes agree to within one day. The earlier note that "yesterday's 2025-02-01 pull returned archive error" appears to have been a misremembered date: the actual failed probe in `notebooks/01_eia860_exploration.ipynb` was 2024-01-15, which is deep archive territory and consistent with the 731-day rule.
- **Choice.** `ARCHIVE_CUTOFF_DAYS = 731` as a module constant in `src/pjm_siting/pjm_api.py`. Routing logic: if any part of a request range is older than `today - 731 days`, that segment must use archive-tier filters (no `pnode_id`; require `type` plus `row_is_current` plus `version_nbr`); requests at or after the boundary use the standard-tier filters.
- **Rationale.** The metadata field is authoritative and matches direct probing. No need to keep this as TBD or to pad.

---

## 2026-05-27: PJM data redistribution boundary and frontend output scope

- **Decision.** Treat the PJM Data Miner Non-Member terms (internal business use only; redistribution requires a separate license) as a hard constraint on what reaches the frontend and the report. Publish only derived outputs: NPVs, rankings, confidence sets, and summary statistics. Do not republish raw LMPs or capacity-market prices. Exclude raw data files from the repository via `.gitignore`.
- **Options considered.** Strict no-republication of raw inputs (chosen); republish raw data with attribution under a fair-use argument; pursue a separate redistribution license from PJM; restrict the frontend to PJM-member readers.
- **Weighing.** PJM's terms are explicit, and the precedent set by Brattle, Synapse, and IEEFA in their public reports is to publish only derived outputs and let readers replicate against PJM directly. A fair-use argument is not winnable and would put the lambcast post and the SSRN deposit at risk. A separate license is overkill for a portfolio project. Restricting the frontend to members defeats the public-facing purpose of the work. The restriction has no practical effect on the analytical contribution; rankings and NPVs are the products that matter.
- **Choice.** Vercel frontend serves only derived outputs (NPVs, rankings, confidence sets, summary statistics). Raw LMPs and capacity prices are not republished in the frontend, the report, or the repository. Repository `.gitignore` excludes raw data files.
- **Rationale.** Compliance with PJM's terms is non-negotiable. The deliverables the audience cares about (rankings under transparent assumptions, sensitivity analysis) do not require republishing raw inputs. Documented methodology plus a pointer to PJM as the source lets any reader replicate the analysis independently.

---

## 2026-05-19: Report format committed to Brattle/JLARC/Synapse register

- **Decision.** The primary written deliverable is a Brattle-style PDF report of roughly 25 to 40 pages including appendices, not an academic working paper. The lambcast post is a shorter derivative; the Vercel frontend is the interactive complement; the GitHub repository is the technical backbone.
- **Options considered.** Academic working paper in the standard NBER/SSRN economics register; Brattle-style consulting report following the format conventions of Brattle, Synapse, and JLARC; hybrid producing both an academic version and a consulting version from a shared analytical core.
- **Weighing.** The hybrid doubles the writing load for a five-week solo project and produces two artifacts neither audience reads natively. The academic working paper is the format I am most comfortable defending on technical content but is not the format the intended audience reads in the course of their work. Hyperscaler in-house energy strategy teams and developer-side hiring managers read Brattle, Synapse, and JLARC reports daily and academic papers rarely. Matching their working format is itself a signal that I understand who the work is for. The Brattle register also fits the stated voice preferences (plain prose, Mitchell and Baldwin register, clarity over sophistication) more naturally than the academic register, which rewards hedged construction and a literature-review front matter the consulting format does not require. SSRN accepts both registers and posting matches the prior pattern from the AI Infrastructure paper, so the citation infrastructure does not change with the format choice.
- **Choice.** Brattle-style PDF report as the primary written deliverable. Lambcast post derived from it. SSRN posting for indexing. Academic working paper format not pursued.
- **Rationale.** Format match to the audience is a signal of audience understanding. The Brattle register also aligns the writing voice with the stated preferences. The hybrid path is not worth its cost on a five-week timeline.

---

## 2026-05-19: Carbon price re-characterization ($100 as researcher-chosen proxy)

- **Decision.** Re-characterize the $100/tCO2 base case carbon price as a researcher-chosen approximation of the implicit shadow price major hyperscalers carry under 24/7 CFE commitments, not as a published hyperscaler internal fee.
- **Options considered.** Cite Microsoft's published $15/ton internal fee directly; cite $100/tCO2 as a generic "hyperscaler internal" price without further qualification (the 2026-05-17 framing); cite $100/tCO2 as a researcher-chosen proxy for the implicit shadow price (new framing).
- **Weighing.** The $15/ton Microsoft fee is the only published hyperscaler number, but it understates the implicit cost a firm with a binding zero-carbon commitment actually carries to honor that commitment. Citing $100 as "hyperscaler internal" without explanation invites the reasonable question of which hyperscaler, which document, and which year. Calling it a researcher-chosen proxy is honest about the assumption and lets reviewers contest it on the right grounds rather than chasing a citation that does not exist.
- **Choice.** Researcher-chosen proxy framing. The $100/tCO2 base case stands; the $190/tCO2 EPA SCC comparison stands.
- **Rationale.** Accuracy about the source of the number is more important than the apparent authority of "hyperscaler internal." The $100 value brackets the published $15 and the social $190 and is defensible as a proxy for the implicit shadow price; pretending otherwise would invite a citation challenge the framing cannot survive.

---

## 2026-05-19: Rank inference method locked (Mogstad et al. 2024 via csranks)

- **Decision.** Lock the rank inference procedure for site rankings to the Mogstad, Romano, Shaikh, and Wilhelm (2024) framework, implemented via the `csranks` R package called from the Python pipeline as a subprocess, with the covariance matrix between site NPVs estimated by Monte Carlo over parameter distributions.
- **Options considered.** `csranks` (canonical implementation by the method's authors); a hand-rolled bootstrap reimplementing the same procedure in Python; report only point rankings with no uncertainty quantification; report point rankings with naive marginal confidence intervals that assume independence across sites.
- **Weighing.** Point rankings without uncertainty hide the substantive question of whether the top-ranked sites are genuinely separated from the rest of the field. Naive marginal intervals are misleading when sites share exposure to common shocks (a regional capacity-price spike, a federal rule change). A hand-rolled bootstrap is feasible but reinvents what `csranks` already implements correctly. Calling out to R from Python adds a process boundary and a dependency on a working R install, but the dependency is contained to one well-defined step.
- **Choice.** `csranks` via Python subprocess, with the covariance matrix estimated by Monte Carlo over parameter distributions, producing both marginal and simultaneous confidence sets.
- **Rationale.** Use the canonical implementation by the method's authors rather than rebuild it. Estimating the covariance from Monte Carlo lets shared-exposure correlations feed into the confidence sets, which is the substantive value of using simultaneous rather than marginal intervals in the first place.

---

## 2026-05-19: NPV-over-MCDA methodological position locked

- **Decision.** Use monetized NPV ranking with a single objective rather than multi-criteria decision analysis with weighted non-monetary criteria.
- **Options considered.** Monetized NPV (single objective); entropy-weighted MCDA following Kim, Dong, and Xie (2026); analytic hierarchy process; explicit weighted-sum with researcher-chosen weights over a mix of monetary and non-monetary criteria.
- **Weighing.** MCDA accommodates criteria that resist clean monetization, such as reliability headroom or congestion exposure, but pays for that breadth by hiding the question of how each criterion translates to dollars. Monetized NPV forces explicit treatment of how each component matters in dollar terms but accepts a narrower criterion set. For a developer audience making a capital-allocation decision, the dollar-weighting is the relevant question; for a system-planner audience, MCDA may be more natural.
- **Choice.** Monetized NPV. The trade-off is named explicitly in overview.md so readers can position the work against the MCDA-style alternative that Kim, Dong, and Xie (2026) and similar papers use.
- **Rationale.** Capital allocation decisions live in dollars. The audience for this work is a hyperscaler or developer choosing where to allocate capital, not a system planner balancing reliability against decarbonization against rates. Choosing NPV signals that audience and forces the cost-weighting discipline that makes the ranking contestable on the right grounds.

---

## 2026-05-19: Risk-vs-ambiguity framing adopted for policy risk (Swartzentruber and Sims 2026)

- **Decision.** Adopt the risk-vs-ambiguity distinction from Swartzentruber and Sims (2026), "Policy Uncertainty and Electric Utility Investments," for the policy risk treatment. Quantifiable risk (known probabilities over known outcomes) and unquantifiable ambiguity (probabilities themselves uncertain) are scored separately and each enter the NPV as a priced cost line.
- **Options considered.** Treat policy risk as a single probability-weighted cost line with no inner distinction (the 2026-05-17 framing); separate quantifiable risk from unquantifiable ambiguity following Swartzentruber and Sims (2026); cite Knightian uncertainty in general terms without operationalizing the distinction.
- **Weighing.** Conflating quantifiable and unquantifiable policy uncertainty understates the cost of jurisdictions where the outcome distribution itself is unknown (Ohio's pending veto-override on the sales tax exemption, FERC's RM26-4 rulemaking, the Maryland OPC complaint). Naming ambiguity separately keeps the model honest about what is a known distribution versus an unknown distribution. The Swartzentruber and Sims paper makes the distinction operational for utility investment, which is the closest available analog.
- **Choice.** Adopt the distinction. Jurisdictions are scored on quantifiable risk and on ambiguity separately; both enter the NPV as priced cost lines.
- **Rationale.** The distinction matters substantively for the PJM jurisdictions this paper covers, where several states are mid-flight on consequential legislation or regulatory action. The risk-vs-ambiguity framing surfaces this in the model rather than hiding it inside an averaged probability.
- **Note on attribution.** The original framing prompt named "Bistline (2026)" as the source for this framing. Primary-source verification (web search against arXiv, NBER, SSRN, ScienceDirect) found no Bistline paper matching the substantive description. The paper that does match (SSRN 5404735) is by Swartzentruber and Sims. The bib entry, the overview framing, and this decision log entry all reflect the corrected attribution.

---

## 2026-05-19: Lade host-community framework adopted as positioning anchor

- **Decision.** Adopt Lade's (2026) "data centers as infrastructure" framework as the positioning anchor for the host-community side of the analysis. The developer perspective leads the paper; the community framing is the explicit counterpart, not the centerpiece.
- **Options considered.** Lade as positioning anchor with developer-side lead (chosen); Slattery and Zidar (2020) as positioning anchor without a host-community frame; generic public-finance framing with no named anchor; lead with the community framing and treat developer-perspective NPV as secondary.
- **Weighing.** Slattery and Zidar is the academic anchor for the empirical claim that firm-specific incentives produce direct employment gains but little broader growth, and it stays in the bibliography as such. But the firm-specific-incentives literature does not supply the "infrastructure rather than economic development" reframe that does the substantive positioning work. Without Lade, the developer-side ranking risks being read as the whole picture rather than as one side of a structured negotiation. Leading with the community framing would change the paper from a developer NPV ranking into a welfare analysis, which it is not.
- **Choice.** Lade is the positioning anchor; the developer perspective leads; community framing is explicit but secondary.
- **Rationale.** The paper's contribution is the developer-side ranking and explicit policy-risk treatment. Using Lade as positioning anchor makes the gap between developer-optimal and community-acceptable terms explicit without pretending the paper resolves it.

---

## 2026-05-19: Slattery and Zidar (2020 JEP) locked as academic anchor for incentives literature

- **Decision.** Lock Slattery and Zidar (2020), "Evaluating State and Local Business Incentives" (Journal of Economic Perspectives 34(2)), as the academic anchor for the broader empirical literature on firm-specific tax incentives. Bartik and Suárez Serrato references remain in the bibliography for readers who want the deeper case.
- **Options considered.** Slattery and Zidar (2020) JEP (chosen); Bartik (2018) Upjohn WP 18-289 on "but for" percentages; Suárez Serrato and Zidar (2016) AER on tax incidence; Fajgelbaum, Morales, Suárez Serrato, and Zidar (2019) ReStud on spatial misallocation; cite multiple without designating an anchor.
- **Weighing.** The paper needs a single named anchor in the framing for readers who are not economists, with deeper Bartik and Suárez Serrato references available for those who want them. JEP is the right register: peer-reviewed, accessible to non-specialists, and the conclusion ("direct employment gains, weak broader-growth evidence") is what the framing actually leans on. Bartik (2018) is narrower (the 2-to-25 percent but-for finding) and is cited specifically where that empirical magnitude does the work; it is not the right anchor for the broader literature claim.
- **Choice.** Slattery and Zidar (2020) JEP as the anchor.
- **Rationale.** Best register for the framing, accessible, and the substantive conclusion fits the positioning. Bartik and Suárez Serrato sit behind it as deeper references rather than competing for the anchor slot.

---

## 2026-05-17: Repository structure (monorepo)

- **Decision.** Use a single repository for Python model, frontend, docs, and data.
- **Options considered.** Monorepo; split repos (Python package, frontend, docs as separate projects).
- **Weighing.** Split repos give cleaner separation and are more typical of multi-person teams. Monorepo simplifies cross-references (frontend reads pre-computed results, docs link to code, decisions touch everything), keeps one history, and is easier for a solo developer to navigate.
- **Choice.** Monorepo.
- **Rationale.** Solo project, five-week scope. The cleanliness benefit of split repos does not pay back at this size, and the friction of keeping three repos in sync is real.

---

## 2026-05-17: Python tooling (uv)

- **Decision.** Use `uv` for dependency management and execution.
- **Options considered.** `uv`; `pip` + `venv`; `poetry`; `conda`.
- **Weighing.** `pip` is universal but slow and leaves resolution to the user. `poetry` is mature but adds its own conventions. `conda` is heavy and not needed for pure-Python deps. `uv` is fast, single-binary, produces a real lockfile, and is becoming the modern default.
- **Choice.** `uv`.
- **Rationale.** Project is small enough that any tool works, so go with the one that signals current practice and has the best ergonomics.

---

## 2026-05-17: Frontend deployment (static via Vercel)

- **Decision.** Deploy the interactive frontend as a static React/Vite site to Vercel, serving pre-computed scenarios.
- **Options considered.** Static deployment with pre-computed scenarios; live Python backend (FastAPI on Fly.io or Render); Streamlit; Observable notebook.
- **Weighing.** A live backend allows arbitrary scenario inputs but adds hosting cost, cold-start latency, and a service to maintain. Streamlit and Observable lower the polish ceiling. Static pre-computation requires bounding the scenario space but has zero infra cost, fast load, and a polish ceiling that matches a portfolio piece.
- **Choice.** Static deployment, pre-computed scenarios.
- **Rationale.** Base scenario space (3 facility sizes x 3 discount rates x 2 carbon prices = 18 grids) is small enough to pre-compute and ship as JSON. No backend to maintain, no recurring cost, and the constraint forces clean scenario design.

---

## 2026-05-17: Site list lock date (end of week one)

- **Decision.** Lock the twenty candidate site list at the end of week one.
- **Options considered.** Lock at end of week one; lock as needed during model construction; leave open through week three.
- **Weighing.** Leaving the list open lets data availability drive site selection and could improve coverage. It also invites endless tinkering, which is the biggest risk on a five-week solo project.
- **Choice.** Lock at end of week one.
- **Rationale.** Scope discipline. Once the list is locked, all downstream work (data pulls, model, sensitivities, frontend) has a fixed target.

---

## 2026-05-17: Carbon pricing (base $100, comparison $190)

- **Decision.** Use $100/tCO2 as the base-case carbon price (typical hyperscaler internal price) and $190/tCO2 (EPA central social cost of carbon) as the comparison.
- **Options considered.** $0 (no carbon); $51 (Interagency Working Group, 2010-2016 central value); $100 (hyperscaler internal); $190 (current EPA SCC); rising price schedule.
- **Weighing.** $0 ignores the constraint hyperscalers actually operate under. $51 is dated. A rising schedule adds complexity without changing the site ranking qualitatively over a 20-year horizon. $100 matches what major hyperscalers (Microsoft, Google) use internally for capital decisions. $190 is the current EPA central value and the right benchmark for the private/social gap.
- **Choice.** $100 base, $190 comparison.
- **Rationale.** The base case should reflect what a developer at a hyperscaler would actually use for site selection. The comparison surfaces the gap between private and social cost, which is the policy-relevant framing.

---

## 2026-05-17: Facility life (20 years)

- **Decision.** Use a 20-year facility life in the base case.
- **Options considered.** 10, 15, 20, 25, 30 years.
- **Weighing.** Physical buildings last 30+ years but server churn is much faster. PPA tenors and infrastructure project finance horizons cluster around 15 to 25 years. Longer life amortizes interconnection costs more aggressively and makes capital-heavy sites look better.
- **Choice.** 20 years.
- **Rationale.** Matches typical PPA tenor and project finance horizons. Conservative enough on amortization that interconnection-heavy sites are not flattered.

---

## 2026-05-17: Discount rate (8% nominal, sensitivities at 6 and 10)

- **Decision.** Use 8% nominal as the base discount rate, with sensitivities at 6% and 10%.
- **Options considered.** Hyperscaler corporate WACC (4 to 6% nominal); project-level hurdle (8 to 10%); regulated utility cost of capital (7 to 8%); 8% as midpoint.
- **Weighing.** Hyperscaler WACC is lower than what they would use for a discrete capital project. Project-level hurdle rates for infrastructure cluster at 8 to 10%. The right rate depends on whether the data center is treated as a corporate asset or a project.
- **Choice.** 8% base, 6% and 10% sensitivities.
- **Rationale.** 8% is a defensible project-level midpoint. The 6% sensitivity covers the corporate-WACC view; the 10% sensitivity covers a more risk-adjusted view. The range brackets the realistic decision-maker.

---

## 2026-05-17: Behind-the-meter scope (two specific candidate sites)

- **Decision.** Model behind-the-meter (BTM) only at two specific candidate sites near major dispatchable generators.
- **Options considered.** Exclude BTM entirely; include BTM as an option at all sites; include BTM only at sites where it is physically plausible.
- **Weighing.** Excluding BTM misses a strategy hyperscalers actively pursue (the Talen-Amazon Susquehanna deal being the visible example). Allowing BTM at all sites is unrealistic since it requires colocation with a dispatchable plant of suitable size. Two specific sites captures the strategy without overstating availability.
- **Choice.** Two specific candidate sites near major dispatchable generators, identified during week-one site selection.
- **Rationale.** BTM is real and consequential but not site-agnostic. Two realistic sites preserve the strategy in the comparison without distorting it.
