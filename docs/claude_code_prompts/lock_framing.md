We're locking the project framing today after two weeks of literature
search and several conversations with another instance of Claude in the
web UI. This session will update the references file, the overview
document, the decisions log, and create a new methods document.

There are five phases. Please confirm completion of each phase before
moving to the next, and ask me clarifying questions whenever you need
to.

# Phase 1: Audit current state

Read the current state of:
- docs/references.bib
- docs/overview.md
- docs/decisions.md
- docs/methods.md
- README.md

Report back what entries exist in references.bib already, and what the
current state of each document is. Do not make changes yet.

# Phase 2: Expand references.bib

Add the following entries to docs/references.bib. For each entry,
include the full bibliographic detail and a URL or DOI. Use BibTeX
citation keys in the format author_year_shortdescription
(e.g., slattery_2020_incentives). Verify each entry by web search if you
have any uncertainty about authors, dates, or publication details. Do
not invent details.

Direct competitors and methodology references:

1. Mogstad, Magne; Romano, Joseph P.; Shaikh, Azeem; Wilhelm, Daniel.
   "Inference for Ranks with Applications to Mobility Across
   Neighborhoods and Academic Achievement Across Countries." NBER
   Working Paper 26883, March 2020, revised January 2022. URL:
   https://www.nber.org/papers/w26883. Type: @techreport.
   Key: mogstad_2022_ranks_nber.

2. Mogstad, Magne; Romano, Joseph P.; Shaikh, Azeem; Wilhelm, Daniel.
   "Statistical Uncertainty in the Ranking of Journals and
   Universities." AEA Papers and Proceedings, Vol. 112, pp. 626-631,
   2022. Key: mogstad_2022_journals_universities.

3. Kim, Dongjoo; Dong, L.; Xie, Le. "Flexibility-Aware Framework for
   Efficient Planner-Initiated Siting of Data Center." arXiv preprint
   2605.14714, May 14, 2026. URL: https://arxiv.org/abs/2605.14714.
   Type: @misc. Key: kim_2026_flexibility_siting.

4. Bistline, John. Recent paper on policy risk vs ambiguity in energy
   investment decisions, Energy Economics, 2026. Search for the exact
   title and bibliographic detail before writing the entry. Key:
   bistline_2026_risk_ambiguity.

5. Snyder, Lawrence V. "Facility Location Under Uncertainty: A Review."
   IIE Transactions, Vol. 38, No. 7, pp. 547-564, 2006. DOI:
   10.1080/07408170500216480. Key: snyder_2006_facility_location.

Urban and regional economics anchor references:

6. Slattery, Cailin R.; Zidar, Owen M. "Evaluating State and Local
   Business Incentives." Journal of Economic Perspectives, Vol. 34,
   No. 2, Spring 2020, pp. 90-118. DOI: 10.1257/jep.34.2.90. Also
   available as NBER Working Paper 26603. URL:
   https://www.aeaweb.org/articles?id=10.1257/jep.34.2.90. Key:
   slattery_2020_incentives_jep.

7. Bartik, Timothy J. "'But For' Percentages for Economic Development
   Incentives: What percentage estimates are plausible based on the
   research literature?" Upjohn Institute Working Paper 18-289, 2018.
   Key: bartik_2018_butfor.

8. Bartik, Timothy J. "Making Sense of Incentives: Taming Business
   Incentives to Produce Prosperity." W.E. Upjohn Institute for
   Employment Research, 2019. Book. Key: bartik_2019_makingsense.

9. Suárez Serrato, Juan Carlos; Zidar, Owen M. "Who Benefits from State
   Corporate Tax Cuts? A Local Labor Markets Approach with
   Heterogeneous Firms." American Economic Review, Vol. 106, No. 9,
   September 2016, pp. 2582-2624. Key: suarezserrato_2016_taxcuts.

10. Fajgelbaum, Pablo D.; Morales, Eduardo; Suárez Serrato, Juan
    Carlos; Zidar, Owen M. "State Taxes and Spatial Misallocation."
    Review of Economic Studies, Vol. 86, No. 1, 2019, pp. 333-376.
    Key: fajgelbaum_2019_spatial.

11. Partridge, Mark; Messenger, Nicholas. Franklin County Auditor
    economist report on data center foregone property tax revenue,
    November 2025. Search for exact title. URL likely at
    franklincountyauditor.com. Key: partridge_2025_franklin.

Host community and policy framework references:

12. Lade, Gabriel E. "Ohio's AI Boom: An Economist's Perspective on
    Data Centers." Substack post on Gabriel E. Lade newsletter, first
    in a four-part series. Use the actual URL
    https://gelade1.substack.com/p/ohios-ai-boom-an-economists-perspective
    Type: @misc. Key: lade_2026_ohio_intro.

13. Lade, Gabriel E. "Fiscal Costs of Data Centers." Substack post,
    March 12, 2026, second in series. URL
    https://gelade1.substack.com/p/fiscal-costs-of-data-centers
    Key: lade_2026_fiscal.

14. Lade, Gabriel E. "Data Centers: What Stays Local, What Doesn't."
    Substack post, third in series. URL
    https://gelade1.substack.com/p/data-centers-what-stays-local-what
    Key: lade_2026_local.

15. Lade, Gabriel E. "Data Centers Are Infrastructure." Substack post,
    May 18, 2026, fourth in series. URL
    https://gelade1.substack.com/p/data-centers-are-infrastructure
    Key: lade_2026_infrastructure.

16. Ross, Justin. "Sales Tax Exemptions for Data Centers." Substack
    post on Capital and Capitol newsletter. URL
    https://justinross.substack.com/p/sales-tax-exemptions-for-data-centers
    Key: ross_2026_salestax.

Complementary literature on data center electricity systems:

17. Atkinson, Carmen; Brancucci, Carlo; Jenkins, Jesse D.; et al.
    "Flexible Data Centers: A Faster, More Affordable Path to Power."
    Camus Energy / Princeton ZERO Lab / encoord report, December
    2025. Search for the exact title, authorship, and URL. Key:
    atkinson_2025_flexible_datacenters.

18. Synapse Energy Economics. "Risks of Rapid Data Center Growth in
    PJM." Prepared for Sierra Club, December 2024. Search for the
    exact title and URL. Key: synapse_2024_pjm_risks.

19. Lu, Xin; et al. "Grid Integration of Gigawatt-Scale AI Data
    Centers under Connect-and-Manage." arXiv preprint 2605.14109,
    May 2026. URL https://arxiv.org/abs/2605.14109. Key:
    lu_2026_connectmanage.

20. Aoyama, Toshiyuki; et al. (or correct authorship). "Risk-Aware
    Allocation of Transmission Capacity for AI Data Centers." arXiv
    preprint 2604.08854, April 2026. Search for correct authorship
    and details. Key: arxiv_2026_riskaware_transmission.

Regulatory primary sources (use @misc with full URLs and access dates):

21. Federal Energy Regulatory Commission. "Order Regarding Intent to
    Act, Docket No. RM26-4-000." April 16, 2026. Find official URL
    on ferc.gov. Key: ferc_2026_rm26_4_intent.

22. Federal Energy Regulatory Commission. "Order Directing
    Co-Location Tariff Revisions, Docket No. ER25-X-000 (PJM
    Co-Location Directive)." December 18, 2025. Find official URL.
    Key: ferc_2025_colocation_directive.

23. PJM Interconnection LLC. "Compliance Filing on Behind-the-Meter
    Generation Tariff Revisions." February 23, 2026. Find URL on
    pjm.com filings page. Key: pjm_2026_btmg_compliance.

24. PJM Interconnection LLC. "Expedited Interconnection Track
    Filing." February 27, 2026. Find URL. Key: pjm_2026_eit_filing.

25. PJM Interconnection LLC. "2026 Long-Term Load Forecast Report."
    January 14, 2026. URL
    https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2026-load-report.pdf
    Key: pjm_2026_load_forecast.

26. PJM Board of Managers. "Decisional Letter on Large Load
    Additions." January 16, 2026. URL on insidelines.pjm.com or
    pjm.com. Key: pjm_2026_board_letter.

27. Maryland Office of People's Counsel. "Complaint Filed at FERC
    Regarding PJM Cost Allocation for Data Center-Driven Transmission
    Upgrades." 2026. Search for filing date and docket number. Key:
    md_opc_2026_complaint.

28. White House and PJM State Governors. "Joint Statement of
    Principles on Data Center Load Growth." January 2026. Find
    official URL. Key: whitehouse_2026_pjm_principles.

State legislative actions, all as @misc entries with bill text URLs.
Search for the most recent enacted or pending version and link to the
official state legislature page, not a news article:

29. New Jersey SB 484 (consumptive-use permitting framework for >=50
    MW data centers, effective July 1, 2026). Key:
    nj_sb484_2026.

30. Texas SB 6 (regulates >=75 MW loads with disconnection
    protocols). Key: tx_sb6_2025.

31. Alabama SB 270 (>=150 MW ratepayer benefit test). Key:
    al_sb270_2025.

32. Maine LD 713 (eliminated key tax incentives, requires study).
    Key: me_ld713_2025.

33. North Carolina HB 1063 (Ratepayer and Resource Protection Act,
    limits hyperscale incentives). Key: nc_hb1063_2026.

34. Ohio data center sales tax exemption situation, ORC 122.175,
    including DeWine veto and pending override. Key:
    oh_orc_122_175_status.

35. Virginia State Corporation Commission GS-5 rate class approval
    (November 2025). Key: va_scc_gs5_2025.

PJM market and capacity primary sources:

36. PJM Capacity Auction clearing price reports for 2024/25, 2025/26,
    and 2026/27 delivery years. Find URLs for each. Key:
    pjm_capacity_auctions_2024_2027.

37. Monitoring Analytics LLC. "State of the Market Report for PJM,
    Q1 2026." Find URL. Key: monitoring_analytics_2026_q1.

Cross-cutting references on data center electricity demand:

38. Lawrence Berkeley National Laboratory (Shehabi, Arman et al.).
    "2024 United States Data Center Energy Usage Report." LBNL
    Report Number LBNL-2001637. December 2024. Already in
    references.bib but verify entry is complete.

39. Cote, J. and Sun, X. "Marginal Emissions Factors for Long-Run
    Carbon Accounting in Electricity Systems." arXiv preprint
    2512.18819, December 2025. Already in references.bib but verify.

40. Brattle Group / Energy Systems Integration Group (ESIG). "Impacts
    of Large Loads on Electricity Rates: A Primer." 2026. Find URL.
    Key: brattle_esig_2026_largeloads_primer.

Additional methodology and supporting references:

41. Bulan, Laarni; Mayer, Christopher; Somerville, C. Tsuriel.
    "Irreversible investment, real options, and competition: Evidence
    from real estate development." Journal of Urban Economics, Vol. 65,
    2009, pp. 237-251. Key: bulan_2009_realoptions.

42. Siler-Evans, Kyle; Azevedo, Inês Lima; Morgan, M. Granger.
    "Marginal Emissions Factors for the U.S. Electricity System."
    Environmental Science & Technology, Vol. 46, No. 9, 2012,
    pp. 4742-4748. Key: silerevans_2012_mef.

43. Chen, Xiaohong; Christensen, Timothy M.; Tamer, Elie. "Monte Carlo
    Confidence Sets for Identified Sets." Econometrica, Vol. 86, No. 6,
    November 2018, pp. 1965-2018. Key: chen_2018_mcconfidencesets.

44. Hold and Stien et al. ICRanks alternative rank inference method.
    Search for exact reference. Key: hold_2018_icranks.

For each entry, if you cannot verify the exact bibliographic detail by
web search, flag it in a comment in the .bib file (e.g., "% TODO:
verify journal volume/issue") rather than guessing. Do not fabricate
details.

# Phase 3: Create source_inventory.md

Create a new file docs/source_inventory.md that lists every reference
in references.bib with:
- Citation key
- Author(s) and title
- Whether the PDF is freely available online (yes/no/paywall)
- The URL where the PDF or article can be obtained
- Whether the source is already downloaded to the references/ folder
- A status field (downloaded / needs download / paywalled / TBD)

This file will serve as the to-do list for me to walk through and
download what I want.

Then create a references/ subfolder in the repo root with a .gitkeep
file so the folder is tracked even when empty. Files downloaded into
references/ should be added to .gitignore so we don't commit
copyrighted PDFs to a public repo. Add the following to .gitignore:
references/*.pdf
references/*.docx
!references/.gitkeep
!references/README.md
And create references/README.md explaining that this folder is for
local PDF copies of papers cited in the project, not tracked in git
for copyright reasons.

# Phase 4: Update overview document and decisions log

Update docs/overview.md with:

(a) The locked contribution claim (insert at the top of the document
or in the existing "Contribution" section, whichever is more
appropriate):

> First publicly available developer-perspective NPV ranking of PJM
> data center sites under transparent cost assumptions and explicit
> jurisdictional policy variation. The model integrates six cost
> components (energy, capacity, interconnection, property tax,
> carbon, policy risk) and monetizes every component into NPV rather
> than using multi-criteria weighting, trading criterion breadth for
> transparency in cost weighting. Policy risk enters as a priced cost
> line by jurisdiction, drawing on Bistline (2026) on the distinction
> between quantifiable risk and unquantifiable ambiguity. Site
> rankings are reported with simultaneous confidence sets following
> Mogstad, Romano, Shaikh, and Wilhelm (2022), with the covariance
> structure estimated by Monte Carlo over parameter distributions to
> capture shared-exposure correlations between sites. The
> developer-perspective findings are positioned against the
> host-community framework articulated by Lade (2026) and the broader
> empirical literature on firm-specific tax incentives (Slattery and
> Zidar 2020). The work contributes to a rapidly developing public
> literature on data center siting (Shao et al. 2025, Kim et al.
> 2026) by providing the developer-side ranking and explicit
> policy-risk treatment that these system-perspective analyses do not
> address. An interactive frontend on Vercel lets readers test their
> own assumptions against the static parameter grid.

(b) A new section "Prior work and positioning" with the following
content. Use plain prose, not bullets, as per the user's preferences.
Match this draft, but adapt to fit the document structure:

> This work sits at the intersection of three literatures. The first
> is the rapidly developing public literature on data center siting
> in electricity markets. Shao, Yu, and Wong (2025) study PJM siting
> from a system-planner perspective with stochastic decarbonization
> objectives. Kim, Dong, and Xie (2026) propose a flexibility-aware
> framework for planner-initiated siting on a synthetic Texas grid
> using entropy-weighted multi-criteria scoring. Both take the system
> perspective; this paper takes the developer perspective and
> monetizes all criteria into NPV. The second is the empirical
> literature on firm-specific tax incentives. Slattery and Zidar
> (2020) find evidence of direct employment gains from attracting
> firms but little evidence of broader economic growth at the state
> or local level. Bartik (2017) estimates that incentives affect 2 to
> 25 percent of firm location decisions. This paper does not test
> these claims directly but positions its developer-perspective cost
> ranking against the empirical case that public-side benefits are
> systematically overestimated. The third is the host-community
> framework articulated by Lade (2026) and others, which treats data
> centers as infrastructure rather than economic development. Under
> that framing, communities being asked to host data centers are
> being asked to absorb concentrated local costs for diffuse benefits
> consumed elsewhere. This paper provides the developer-side
> counterpart to that analysis, making the gap between
> developer-optimal and community-acceptable terms explicit.

(c) Replace or augment the existing "Risks and known limitations"
section with this sentence:

> The developer-perspective framing of this analysis is one side of
> a structured negotiation; the model does not address the
> public-finance consequences of data center siting that Lade (2026),
> Partridge and Messenger (2025), Slattery and Zidar (2020), and
> others document. A complete welfare analysis would integrate the
> developer-side ranking with the community-side cost-allocation
> analysis. This work positions itself as the developer-side input to
> that broader analysis.

(d) Add a new short section "Methodology positioning vs MCDA" with
this content:

> The closest contemporaneous methodological alternative to monetized
> NPV ranking is multi-criteria decision analysis with explicit
> weighting of non-monetary criteria. Kim et al. (2026) use
> entropy-weighted MCDA to combine price impact, congestion, and
> operational feasibility into a composite siting score. MCDA has the
> advantage of accommodating criteria that cannot be cleanly
> monetized; NPV has the advantage of forcing explicit treatment of
> how each component matters in dollar terms. This paper takes the
> NPV approach because the audience for the work is a hyperscaler or
> developer making a capital allocation decision, and capital
> allocation decisions live in dollars. The trade-off is explicit.

(e) Add a new section "Eight things that need explicit treatment"
covering the items previously identified:

1. Developer-perspective NPV model, not welfare analysis
2. Policy risk treated as priced cost line by jurisdiction, proxy for
   real costs of community opposition and ratepayer harm
3. Carbon at $100/tCO2 base case (proxy for implicit shadow price
   under 24/7 CFE commitments, not Microsoft's $15/ton internal fee)
   with $190/tCO2 EPA SCC for comparison, acknowledging federal SCC
   functional deprecation in 2025-26
4. Applied economics treatment, not power systems engineering or
   finance specialist
5. Demand response and behind-the-meter minimal modeling (DR as
   sensitivity only, BTM at two specific sites near Susquehanna and
   another major dispatchable generator)
6. Static v1 interactive deliverable (Vercel/React/Vite), robust
   versions in future work
7. Site list locked end of week one of execution, no additions after
8. Lade framing: positions developer-side analysis as one side of a
   structured negotiation, not as an answer to the public-side
   policy question

# Phase 5: Update decisions log and create methods.md

Update docs/decisions.md with new entries (using the existing
date/decision/options/weighing/choice/rationale format) for:

1. Carbon price re-characterization: $100/tCO2 base case is a
   researcher-chosen approximation of implicit shadow price, not
   Microsoft's $15/ton internal fee.

2. Mogstad-Romano-Shaikh-Wilhelm method locked for rank inference,
   using R subprocess to csranks package, with covariance matrix
   estimated via Monte Carlo over parameter distributions.

3. Bistline 2026 risk-vs-ambiguity framing adopted for policy risk
   treatment.

4. Lade 2026 host-community framework adopted as positioning anchor,
   developer-perspective lead with community framing as supporting
   positioning rather than centerpiece.

5. NPV-over-MCDA methodological position locked, with explicit
   trade-off acknowledgment vs Kim et al. 2026 entropy-weighted
   approach.

6. Slattery-Zidar 2020 JEP locked as academic anchor for broader
   empirical literature on firm-specific tax incentives.

Create docs/methods.md (or expand the existing skeleton) with sections:
- Cost components and monetization approach
- Site selection methodology (to be filled in week 1)
- Parameter distributions for Monte Carlo
- Rank inference via Mogstad et al. (2022)
- Policy risk scoring framework
- Limitations and what the model does not address

For each section, write a one-paragraph placeholder describing what
will go there. Do not fill in the technical detail yet; that comes
during week-one execution.

# Final step

Show me a git diff of all changes, then commit and push with the
following commit message:

"docs: lock framing after lit review

- expanded references.bib with 40+ entries covering direct competitors,
  methodology, urban econ, host-community framework, regulatory
  primary sources, and state legislation
- added contribution claim, prior work positioning, methodology
  positioning vs MCDA, and eight framing items to overview.md
- updated decisions log with carbon re-characterization, Mogstad lock,
  Bistline framing, Lade positioning, NPV vs MCDA decision
- created source_inventory.md as PDF download checklist
- created methods.md skeleton with placeholders for week-1 fill-in
- added references/ folder for local PDF copies (gitignored)

Framing locked after deliberate four-bucket lit review covering OR
facility location, urban economics, real estate finance, and recent
(Oct 2025-May 2026) academic preprints. Contribution claim survives
intact with sharpening on MCDA contrast and updated literature
positioning."

Confirm completion of each phase before moving to the next. Ask me
clarifying questions whenever you need to.