# PJM Data Center Siting: Overview

Living document. Updated as the model develops.

## Project framing

A developer-perspective NPV model for siting a hyperscale data center across twenty candidate locations in the PJM Interconnection footprint. The output ranks sites by expected net present value to a single developer over a fixed facility life, under explicit assumptions about energy and capacity costs, interconnection, property tax, carbon, and policy risk.

This is an applied economics treatment of a problem that also has physics, finance, and regulatory dimensions. The model does not solve power flow, does not run a full project finance waterfall, and does not predict regulatory outcomes. It produces a defensible ordering of candidate sites under a transparent set of assumptions, with sensitivities that expose where the ranking is robust and where it is not.

## Objective function

Maximize the developer's expected NPV at site $i$:

$$\text{NPV}_i = \sum_{t=0}^{T} \frac{R_t - C_{i,t}}{(1+r)^t}$$

where $C_{i,t}$ is the site-specific annual cost stack, $r$ is the nominal discount rate, and $T$ is facility life. Revenue $R_t$ is treated as site-invariant in the base case (a hyperscaler is indifferent across sites on the revenue side), so site ranking reduces to minimizing the present value of total cost.

## Scope decisions

| Decision | Value | Sensitivities |
|---|---|---|
| Candidate sites | 20 across PJM | locked at end of week one |
| Facility size | 500 MW | 250 MW, 1000 MW |
| Facility life | 20 years | none in base run |
| Discount rate (nominal) | 8% | 6%, 10% |
| Internal carbon price | $100/tCO2 (hyperscaler internal) | $190/tCO2 (EPA SCC) |
| Demand response | excluded | flagged as future work |
| Behind-the-meter | two candidate sites near major dispatchable generators | |
| Frontend | static deployment via Vercel, pre-computed scenarios | |

## Cost stack components

1. **Energy.** Locational marginal price by node or zone, scaled to facility load profile.
2. **Capacity.** PJM capacity auction clearing price by LDA, scaled to UCAP obligation.
3. **Interconnection.** Network upgrade cost allocation, treated as a one-time capital charge amortized over facility life.
4. **Property tax.** State and county effective rates applied to assessed value.
5. **Carbon.** Internal price applied to facility emissions, computed from grid emissions intensity at the relevant node or zone.
6. **Policy risk.** Probability-weighted adjustment to one or more of the above (see next section).

*(Placeholder: data sources and unit conventions per component to be documented in [methods.md](methods.md).)*

## Policy risk treatment

Policy risk is treated as a probability-weighted adjustment by jurisdiction (state, and where relevant, county). For each candidate site, identified policy risks (large-load tariff changes, moratoria, special assessments, transmission cost reallocation) are assigned a probability and a cost impact. The expected cost adjustment enters the NPV through the relevant component.

*(Placeholder: scoring methodology in [methods.md](methods.md). Decision rationale in [decisions.md](decisions.md).)*

## Prior work and contribution

*(Placeholder: to be filled during the week-one literature survey. Anchors: AI Infrastructure paper and FERC brief on lambcast.net.)*

## Timeline

| Week | Focus |
|---|---|
| 1 | Literature survey, data acquisition, site list locked |
| 2 | Model construction |
| 3 | Sensitivity analysis and pre-computation |
| 4 | Frontend (React/Vite, Vercel) |
| 5 | Writeup |
| 6 | Buffer |

## Risks and known limitations

- **Not a power-flow model.** Locational price is treated as a data input. Interconnection costs are taken from public studies or modeled with simple heuristics, not solved.
- **Not a project finance model.** No debt/equity structure, no tax equity, no depreciation schedule beyond what's needed for a transparent NPV.
- **Static policy risk.** Probabilities are point estimates rather than distributions in the base case.
- **Single-developer perspective.** The model does not consider strategic interaction, queue dynamics, or competition for the same node.
- **Twenty sites is a small set.** Sites are chosen for coverage, not statistical representativeness.

*(Placeholder: update as limitations become more specific during construction.)*
