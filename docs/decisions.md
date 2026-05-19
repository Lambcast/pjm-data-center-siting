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
