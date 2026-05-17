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
