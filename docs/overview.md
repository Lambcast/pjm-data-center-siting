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

This work is the first publicly available developer-perspective NPV ranking of PJM data center sites under transparent cost assumptions and explicit jurisdictional policy variation. The model integrates six cost components (energy, capacity, interconnection, property tax, carbon, policy risk) and monetizes every component into NPV rather than using multi-criteria weighting, trading criterion breadth for transparency in cost weighting. Policy risk enters as a priced cost line by jurisdiction, drawing on Swartzentruber and Sims (2026) on the distinction between quantifiable risk and unquantifiable ambiguity. Site rankings are reported with simultaneous confidence sets following Mogstad, Romano, Shaikh, and Wilhelm (2024), with the covariance structure estimated by Monte Carlo over parameter distributions to capture shared-exposure correlations between sites. The developer-perspective findings are positioned against the host-community framework articulated by Lade (2026) and the broader empirical literature on firm-specific tax incentives (Slattery and Zidar 2020). The work contributes to a rapidly developing public literature on data center siting (Shao, Yu, and Wong 2025; Kim, Dong, and Xie 2026) by providing the developer-side ranking and explicit policy-risk treatment that these system-perspective analyses do not address. An interactive frontend on Vercel lets readers test their own assumptions against the static parameter grid.

## Prior work and positioning

This work sits at the intersection of three literatures. The first is the rapidly developing public literature on data center siting in electricity markets. Shao, Yu, and Wong (2025) study PJM siting from a system-planner perspective with stochastic decarbonization objectives. Kim, Dong, and Xie (2026) propose a flexibility-aware framework for planner-initiated siting on a synthetic Texas grid using entropy-weighted multi-criteria scoring. Both take the system perspective; this paper takes the developer perspective and monetizes all criteria into NPV.

The second is the empirical literature on firm-specific tax incentives. Slattery and Zidar (2020) find evidence of direct employment gains from attracting firms but little evidence of broader economic growth at the state or local level. Bartik (2018) estimates that incentives affect somewhere between 2 and 25 percent of firm location decisions. This paper does not test these claims directly but positions its developer-perspective cost ranking against the empirical case that public-side benefits are systematically overestimated.

The third is the host-community framework articulated by Lade (2026) and others, which treats data centers as infrastructure rather than economic development. Under that framing, communities being asked to host data centers are being asked to absorb concentrated local costs for diffuse benefits consumed elsewhere. This paper provides the developer-side counterpart to that analysis, making the gap between developer-optimal and community-acceptable terms explicit.

## Methodology positioning vs MCDA

The closest contemporaneous methodological alternative to monetized NPV ranking is multi-criteria decision analysis with explicit weighting of non-monetary criteria. Kim, Dong, and Xie (2026) use entropy-weighted MCDA to combine price impact, congestion, and operational feasibility into a composite siting score. MCDA has the advantage of accommodating criteria that cannot be cleanly monetized; NPV has the advantage of forcing explicit treatment of how each component matters in dollar terms. This paper takes the NPV approach because the audience for the work is a hyperscaler or developer making a capital allocation decision, and capital allocation decisions live in dollars. The trade-off is explicit.

## Eight things that need explicit treatment

The framing below names the eight commitments that bound the scope of this paper and the claims it can support. They are listed as a numbered set because each is load-bearing for the result; collapsing them into prose would obscure which constraints are doing the work.

1. **Developer-perspective NPV model, not welfare analysis.** The output ranks sites by expected present-value cost to a single developer. It is not a social welfare function and does not attempt to balance developer, ratepayer, host community, and regional emissions interests in a single objective.
2. **Policy risk as a priced cost line by jurisdiction.** Policy risk enters the NPV as a probability-weighted dollar adjustment to the relevant component. The priced cost line is a proxy for the real economic costs of community opposition, moratoria, ratepayer-protection legislation, and transmission cost reallocation. It is not a probabilistic forecast of any specific regulatory action.
3. **Carbon at $100/tCO2 base case, $190/tCO2 comparison.** The base-case carbon price is a researcher-chosen approximation of the implicit shadow price major hyperscalers carry under 24/7 CFE commitments. It is not Microsoft's published $15/ton internal fee, which understates the implicit cost of the firm-level zero-carbon commitment. The $190/tCO2 EPA Social Cost of Carbon serves as the social-cost comparison, with explicit acknowledgment that the federal SCC has been functionally deprecated in 2025-26 federal guidance.
4. **Applied economics treatment, not power systems engineering or finance specialist.** Locational prices, capacity prices, and interconnection costs are inputs to the model, not outputs of a power-flow solver. The discount rate, facility life, and amortization schedule are transparent NPV conventions rather than a full project finance waterfall.
5. **Demand response and behind-the-meter receive minimal modeling.** Demand response enters only as a sensitivity, not in the base case. Behind-the-meter generation is modeled only at two specific candidate sites: one adjacent to Susquehanna (matching the Talen-Amazon arrangement) and one adjacent to another major dispatchable generator identified during site selection.
6. **Static v1 interactive deliverable.** The frontend is a static React/Vite site deployed to Vercel, serving pre-computed scenarios across a defined parameter grid. A robust scenario-input version, with live solver calls and arbitrary parameter combinations, is named as future work rather than promised in v1.
7. **Site list locked at end of week one.** Once the twenty candidate sites are selected, no additions are made. Data acquisition, modeling, sensitivities, and frontend pre-computation all target a fixed site list.
8. **Lade framing as one side of a structured negotiation.** The work positions the developer-side cost ranking as one side of a structured negotiation between hyperscalers and host communities. It is not offered as an answer to the public-side policy question of whether, where, or on what terms communities should accept data centers.

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

The developer-perspective framing of this analysis is one side of a structured negotiation; the model does not address the public-finance consequences of data center siting that Lade (2026), Partridge and Messenger (2025), Slattery and Zidar (2020), and others document. A complete welfare analysis would integrate the developer-side ranking with the community-side cost-allocation analysis. This work positions itself as the developer-side input to that broader analysis.

*(Placeholder: update as limitations become more specific during construction.)*
