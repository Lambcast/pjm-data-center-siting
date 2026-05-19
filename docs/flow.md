# Project Flow

Living document. Captures how the project moves from raw data through finished artifacts. Updated as choices are made and as reality diverges from plan. Read alongside overview.md (which locks framing) and decisions.md (which logs choices). This document explains how the pieces connect; the other two documents explain what they are.

Last updated: 2026-05-19

## The whole project in one paragraph

Pull a defined set of PJM market data and policy data. Use it to score and pick twenty candidate substations across PJM that span the relevant variation. Build a cost model that converts site-specific inputs into a 20-year NPV for a 500 MW data center. Run that model across a parameter grid that captures the assumptions a reader might want to test. Report rankings with confidence sets. Write up the findings as a Brattle-style report with executive summary and methods appendix. Derive a shorter blog post from the report. Ship a Vercel frontend that lets readers explore the parameter grid. Post the whole thing publicly. The report is the artifact that makes the work portable. The frontend is what makes it interactive. The repo is what makes it credible to a technical reviewer.

## How the data flows

Three categories of data, distinct sources, different update frequencies.

Market data from PJM (Data Miner 2 API and the public planning pages) covers locational marginal prices, capacity auction clearing prices, and the new services queue. This is the bulk of the energy and capacity cost lines. Pull once for the historical window (2022 through 2025) and it does not change after.

Site-specific physical and parcel data covers substation locations, interconnection upgrade costs from public studies, transmission topology around candidate sites, and dispatchable generation within 25 miles. Some lives in the PJM queue, some in state utility commission filings, some in public-domain GIS layers. Assemble once per site as sites are selected.

Policy and jurisdictional data covers state legislation, county property tax rates, rate-class structures, FERC rulemaking status, governor statements, and OPSB or equivalent siting board jurisdiction. This category changes weekly right now. Document the as-of date for everything; freeze inputs at the start of week three. The writeup acknowledges that the regulatory baseline is a snapshot.

All three categories feed into the same DuckDB database. Query the database to build the cost stack for each site. The frontend reads from a pre-computed Parquet file that is the output of all the cost-stack runs.

## How sites get selected

The point of the twenty is not to identify the twenty best parcels in PJM; the point is to produce a ranking framework that captures real cost variation across PJM, with a sample that any reasonable reader would accept as representative of the choices a developer actually faces. A real developer's site selection team has people on the ground checking parcel availability, talking to local economic development offices, verifying fiber routes. This project does not. The defensible substitute is a documented methodology that any reader can interrogate.

The methodology uses five filters in sequence.

### First filter: candidate pool

All PJM transmission substations meeting a minimum voltage threshold (probably 500 kV, possibly 230 kV in some zones). PJM publishes the substation list as part of its transmission planning materials. This yields roughly 200 to 400 candidate substations.

### Second filter: zonal coverage

At least one site in every meaningful LDA, with multiple in the zones that matter most (DOM, AEP, COMED, PL).

### Third filter: congestion regime

Within each zone, at least one site that historically clears at a discount to the zonal price (negative basis, often near generation) and one that clears at a premium (positive basis, often near load centers). The 2022 to 2025 LMP data determines this directly.

### Fourth filter: parcel proximity to physical realities

Within roughly 5 miles of areas zoned for industrial or commercial use, within reasonable distance of fiber backbones, with the surrounding area not obviously inappropriate (national forest, dense residential, wetland). Done from public GIS layers, county zoning maps, and satellite view. The methods note acknowledges this filter is coarser than what a real site selection team would do.

### Fifth filter: behind-the-meter candidates

Two specific sites adjacent to or co-located with major dispatchable generators. Susquehanna nuclear (matching the Talen-Amazon arrangement) is one. The second is chosen based on what the policy environment makes most interesting; candidates include Calvert Cliffs, Peach Bottom, Limerick, and AEP coal-to-gas sites in Ohio.

### Final cut

The five filters run as a scored Python pipeline producing a shortlist of 50 to 150 sites. The final cut to twenty is done by hand with explicit reasoning written down for each cut. The reasoning gets documented in the methods appendix. A reader who disagrees with the selection can read the reasoning and form their own opinion; the contribution claim does not depend on the twenty being optimal, it depends on the twenty being defensible.

## How the model gets built

The cost model is six functions, one per cost component, each taking a site identifier and a parameter set and returning a dollar value per year over the facility life. Total NPV is the discounted sum. Functions live in src/pjm_siting/costs/. One file per component: energy.py, capacity.py, interconnection.py, property_tax.py, carbon.py, policy_risk.py. Each function shares a signature and returns a float. A top-level orchestration function in src/pjm_siting/npv.py calls all six per site per year and discounts.

The model is deterministic for any given parameter set. Monte Carlo machinery samples parameter sets from specified distributions and runs the deterministic model many times. The csranks R subprocess takes the resulting NPVs and their empirical covariance matrix and returns confidence sets for ranks.

Testing is per-component: unit tests in tests/test_costs/ confirm each function returns sensible values for known inputs. The energy cost for a 500 MW facility in DOM at $50/MWh average LMP and 0.87 capacity factor should be about $190 million per year. If a function returns $19 million or $1.9 billion, there is a bug. Each component has at least three test cases: a base case, an edge case, and a known-good comparison against a published reference. Orchestration is tested at the integration level: the full NPV for a known site under known assumptions should match a hand-computed answer, and rankings should be stable under irrelevant permutations.

## How the parameter grid works

The frontend is static, which means every scenario the user can request is pre-computed. The grid dimensions are facility size (250, 500, 1000 MW), discount rate (6, 8, 10 percent), internal carbon price (0, 51, 100, 190 dollars per tonne), capacity price scenario (low, base, high), LMP scenario (low, base, high), and policy risk scenario (optimistic, base, pessimistic). Total scenarios are 3 times 3 times 4 times 3 times 3 times 3 = 972 per site, 20 sites, roughly 20,000 rows in the output Parquet file.

The grid is a design choice. Fewer dimensions makes pre-computation faster and the frontend simpler. More dimensions makes the interactive experience richer but harder to navigate. The final grid will be decided in week three when the analysis reveals what the frontend should expose.

## How the writeup happens

The Brattle report and the lambcast post are not separate writing projects; they are one writing project with two outputs. The report is the primary document; the post is a derivative.

Methodology and appendix sections of the report get written in week three as the analysis happens. This is the part most projects underestimate. The methods are much faster to write while inside the analysis than to reconstruct two weeks later. Every methodological choice (which LMP series, how to handle missing capacity prices, how to specify the policy risk distributions) gets a paragraph written immediately into the report draft. By the end of week three the methods appendix is complete.

The findings section gets written in week four as the parameter grid finalizes. The findings organize around the rankings: which sites win under base assumptions, which are robust across scenarios, which are sensitive to specific parameter choices. Three to five tables and figures carry the findings. Prose gets written around the figures.

The executive summary, context, and implications sections get written in week five. The executive summary is the last thing written, not the first; it gets written when the findings are actually known. The context section pulls forward the policy environment from the regulatory primary sources in the bib. The implications section is where the Lade framing pays off: the developer-side findings get positioned explicitly against the community-side policy questions.

The lambcast post gets derived from the report in late week five. Cut the appendices. Loosen the register. Strengthen the lead. Add inline links to primary sources. Target 3,000 to 5,000 words.

## How the frontend gets built

Week four. React/Vite, single-page app, deploys to Vercel. The UI has three regions: a parameter selection panel on the left, a ranked site display in the middle, a cost stack visualization on the right. The user changes parameters; the display updates by indexing into the pre-computed Parquet file.

The frontend is deliberately simple. No backend. No solver. No server-side computation. The Parquet file is loaded once on page load (roughly 5 MB after compression) and queried in-memory using DuckDB-WASM or a similar in-browser query engine. The user experience is instant response to parameter changes, which is the right experience for an exploration tool.

The frontend is where the work feels real to a reader who is not going to read the Brattle report. A hiring manager who spends 90 seconds clicking around gets a more visceral sense of what the model does than someone who reads the executive summary. The frontend signals that the work can ship as product, not just paper.

## How publication and launch happen

End of week five: submit to SSRN. SSRN review takes 24 hours to two weeks; budget two weeks. The submission includes the PDF report, an abstract, and author info.

Week six (buffer): if SSRN comes back with revisions, fix them. If everything is clean, launch.

Launch is coordinated across four channels. The SSRN posting goes live. The PDF goes onto lambcast.net at a stable URL. The Vercel frontend goes live at a stable URL. The lambcast post goes up linking to both. Announcement happens on professional channels. The four artifacts cross-link: the post links to the PDF and frontend, the PDF links to the frontend and repo, the frontend links to the PDF and repo, the repo README links to all three.

A reader who finds any one of the four can navigate to all four. That is the point of the cross-linking.

## Risks worth tracking

Site selection is the most defensible-but-also-most-attackable piece. A reviewer who knows PJM will look at the twenty sites and either nod or shake their head. The defense is documented methodology. Two days in week one is the minimum.

Policy risk scoring is the most novel and most contestable piece. The defense is documented methodology, transparent inputs, and sensitivity analysis. Make the policy risk component easy to interrogate from the frontend so a skeptical reader can plug in their own probabilities.

The timeline is tight. Five weeks plus buffer is enough if every week goes well. The most common failure mode is week one site selection slipping by three days and compounding. Hard checkpoint at the end of each week. If week one does not end with a locked site list and an initial data pull, stop and replan rather than push forward into week two with a soft foundation.

## How to use this document

Read this when uncertain about what the next concrete step is. Read this when tempted to redesign the methodology mid-execution (the methodology is already chosen; trust the past version of yourself that chose it). Read this when the timeline starts slipping and the temptation is to add scope (the scope is already bounded; trust the bounded version).

Update this document when reality diverges from plan. If site selection takes a week instead of two days, update the timeline section here and the timeline in overview.md to match. If the parameter grid collapses from 972 scenarios to 200, update the parameter grid section. If a new data source becomes necessary, update the data flow section.

This document does not lock decisions; decisions.md does that. This document explains how the locked decisions connect into a coherent project.
