# Source Inventory

PDF download checklist for every entry in `docs/references.bib`. Use this to plan manual download time and to flag entries that need manual lookup at FERC eLibrary, journal subscriptions, or paywalled databases.

## How to read this file

**Column key:**

- **Key** — BibTeX citation key.
- **Reference** — Author(s) and short title.
- **Access** — How the source is gated. Values:
  - `open` — Freely available, no login or payment required.
  - `paywall + preprint` — Final published version is paywalled, but a freely available preprint (NBER WP, arXiv, SSRN, working paper) exists.
  - `paywall` — Paywalled with no known free version. Need institutional access.
  - `agency portal` — Hosted on an agency website that may require navigation or search.
  - `eLibrary lookup` — Specific filing accession requires manual search at FERC eLibrary or a state docket system.
  - `TODO` — Entry has an unresolved attribution or content issue (see `references.bib` notes).
- **URL verified** — Whether the URL was directly fetched during this lock session.
  - `Y` — Page directly fetched via WebFetch and content confirmed.
  - `N` — URL obtained from search results or known URL pattern, not directly fetched. Still likely valid but should be sanity-checked before relying on it.
  - `partial` — URL works but the content was unreadable (e.g., binary PDF that the fetcher couldn't parse). Manual verification recommended.
- **Local** — Whether a copy is downloaded to `references/`. Always starts as `no`. Update as you download.
- **Status** — `downloaded`, `needs download`, `paywalled`, `TBD`.

**Workflow tip:** Start with `Access: open` + `URL verified: Y` entries — those are the cheapest downloads. Save `eLibrary lookup` and `TODO` entries for a focused session at a computer with eLibrary access.

---

## Direct competitors and rank-inference methodology

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `shao_2025_pjm_siting` | Shao, Yu, Wong (2025), "Stochastic Long-Term Joint Decarbonization Planning ... PJM" (arXiv 2510.25118) | open | Y | no | needs download |
| `kim_2026_flexibility_siting` | Kim, Dong, Xie (2026), "Flexibility-Aware Framework ... Data Center" (arXiv 2605.14714) | open | Y | no | needs download |
| `mogstad_2020_ranks_nber` | Mogstad, Romano, Shaikh, Wilhelm (2020), "Inference for Ranks ..." (NBER WP 26883) | open | Y | no | needs download |
| `mogstad_2024_ranks_restud` | Mogstad, Romano, Shaikh, Wilhelm (2024), same paper, Review of Economic Studies version | paywall + preprint | N | no | needs download (use NBER preprint if no Oxford access) |
| `mogstad_2022_journals_aeapp` | Mogstad, Romano, Shaikh, Wilhelm (2022), "Statistical Uncertainty ... Journals and Universities" (AEA P&P) | open | Y | no | needs download |
| `chetverikov_2024_csranks` | Chetverikov et al. (2024), "csranks: An R Package ..." (arXiv 2401.15205) | open | Y | no | needs download |
| `chen_2018_mcconfidencesets` | Chen, Christensen, Tamer (2018), "Monte Carlo Confidence Sets ..." (Econometrica 86:6) | paywall + preprint | N | no | needs download (preprint at tmchristensen.com/ECTA14525.pdf) |
| `swartzentruber_2026_risk_ambiguity` | Swartzentruber, Sims (2026), "Policy Uncertainty and Electric Utility Investments" (SSRN 5404735) | paywall + preprint | N | no | needs download (SSRN preprint open; ScienceDirect blocked WebFetch with 403) |
| `bistline_2024_reform_options` | Bistline et al. (2024), "Climate Policy Reform Options in 2025" (NBER WP 32168) | open | N | no | needs download |
| `snyder_2006_facility_location` | Snyder (2006), "Facility Location Under Uncertainty: A Review" (IIE Transactions 38:7) | paywall + preprint | N | no | needs download (preprint at coral.ise.lehigh.edu/larry/files/pubs/stochloc.pdf) |

## Urban and regional economics anchor references

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `slattery_2020_incentives_jep` | Slattery, Zidar (2020), "Evaluating State and Local Business Incentives" (JEP 34:2) | open | Y | no | needs download |
| `bartik_2018_butfor` | Bartik (2018), "'But For' Percentages ..." (Upjohn WP 18-289) | open | N | no | needs download |
| `bartik_2019_makingsense` | Bartik (2019), *Making Sense of Incentives* (Upjohn Institute book; free PDF) | open | N | no | needs download |
| `suarezserrato_2016_taxcuts` | Suárez Serrato, Zidar (2016), "Who Benefits from State Corporate Tax Cuts?" (AER 106:9) | paywall + preprint | N | no | needs download (NBER WP 20289 preprint is open) |
| `fajgelbaum_2019_spatial` | Fajgelbaum, Morales, Suárez Serrato, Zidar (2019), "State Taxes and Spatial Misallocation" (ReStud 86:1) | paywall + preprint | N | no | needs download (NBER WP 21760 preprint is open) |
| `partridge_2025_franklin` | Partridge, Messenger (2025), 2025 Franklin County TIRC Report | open | partial | no | needs download (URL had 301 redirect; main TIRC PDF should still be accessible from franklincountyauditor.com) |

## Host community and policy framework references

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `lade_2026_ohio_intro` | Lade (2026-03-10), "Ohio's AI Boom" (Substack, post 1/4) | open | Y | no | needs download (save as PDF from browser) |
| `lade_2026_fiscal` | Lade (2026-03-12), "Fiscal Costs of Data Centers" (Substack, post 2/4) | open | Y | no | needs download |
| `lade_2026_local` | Lade (2026-04-27), "What Stays Local, What Doesn't" (Substack, post 3/4) | open | Y | no | needs download |
| `lade_2026_infrastructure` | Lade (2026-05-18), "Data Centers are Infrastructure" (Substack, post 4/4) | open | Y | no | needs download |
| `ross_2026_salestax` | Ross (2026-02-23), "Sales Tax Exemptions ... Aren't Subsidies" (Capital & Capitol Substack) | open | Y | no | needs download |

## Complementary literature on data center electricity systems

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `atkinson_2025_flexible_datacenters` | Camus / encoord / Princeton ZERO Lab (2025), "Flexible Data Centers: A Faster, More Affordable Path to Power" | open | Y | no | needs download (whitepaper download link on camus.energy) |
| `synapse_2024_pjm_risks` | Synapse Energy Economics (2024), "Risks of Rapid Data Center Growth in PJM" (prepared for Sierra Club) | open | N | no | needs download |
| `lu_2026_connectmanage` | Lu, Xu (2026), "Grid Integration of Gigawatt-Scale AI Data Centers under Connect-and-Manage" (arXiv 2605.14109) | open | Y | no | needs download |
| `li_2026_riskaware_transmission` | Li, Fang, Chen (2026), "Risk-Aware Allocation of Transmission Capacity ..." (arXiv 2604.08854) | open | Y | no | needs download |
| `cote_2025_lme` | Cote, Sun (2025), "Locational Marginal Emissions ..." (arXiv 2512.18819) | open | Y | no | needs download |

## Regulatory primary sources

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `ferc_2026_rm26_4_intent` | FERC (2026-04-16), Order Regarding Intent to Act, Docket RM26-4-000 | agency portal | N | no | needs download (ferc.gov/rm26-4 hub; order PDF accessible from that page) |
| `ferc_2025_colocation_directive` | FERC (2025-12-18), Co-Location Order, Docket EL25-49-000 | agency portal | N | no | needs download (order PDF accessible via FERC eLibrary in EL25-49-000) |
| `pjm_2026_btmg_compliance` | PJM (2026-02-23), BTMG Compliance Filing in EL25-49-000 | eLibrary lookup | N | no | TBD — specific accession # requires FERC eLibrary search by filer "PJM Interconnection" in docket EL25-49-000 on filing date 2026-02-23 |
| `pjm_2026_eit_filing` | PJM (2026-02-27), Expedited Interconnection Track filing, Docket ER26-1563-000 | open | Y | no | needs download (primary PDF on pjm.com confirmed) |
| `pjm_2026_load_forecast` | PJM (2026-01), 2026 PJM Load Forecast Report | open | partial | no | needs download (URL works; PDF was binary-unreadable by fetcher, normal browser download should succeed) |
| `pjm_2026_board_letter` | PJM Board of Managers (2026-01-16), Decisional Letter on Large Load Additions | open | N | no | needs download (URL pattern on pjm.com public disclosures) |
| `md_opc_2026_complaint` | Maryland OPC (2026-05-07), FERC complaint re PJM RTEP cost allocation | eLibrary lookup | partial | no | TBD — OPC complaint PDF URL fetched but binary-unreadable; FERC docket # to be confirmed in eLibrary by filer + date |
| `whitehouse_2026_pjm_principles` | White House NEDC + PJM Governors (2026-01-15), Statement of Principles Regarding PJM | agency portal | N | no | needs download (energy.gov hosts the joint statement) |

## State legislative actions

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `tx_sb6_2025` | Texas SB 6 (89th R.S.) — large load interconnection/curtailment | open | N | no | needs download (capitol.texas.gov bill history page) |
| `al_sb270_2025` | Alabama SB 270 (2026 R.S.) — PSC review of large load contracts | open | Y | no | needs download (enrolled PDF on alison.legislature.state.al.us confirmed) |
| `me_ld713_2025` | Maine LD 713 (132nd Leg.; P.L. Ch. 768) — data center exclusion from BETE/Dirigo | open | Y | no | needs download (mainelegislature.org bill page confirmed) |
| `nc_hb1063_2026` | NC HB 1063 — Ratepayer and Resource Protection Act | open | N | no | needs download (ncleg.gov primary PDF) |
| `oh_orc_122_175_status` | Ohio Revised Code § 122.175 — data center sales tax exemption | open | N | no | needs download (codes.ohio.gov; also need to track DeWine veto + override status separately) |
| `va_scc_gs5_2025` | Virginia SCC Final Order, Case PUR-2025-00058 — GS-5 rate class | agency portal | N | no | needs download (SCC press release page; full order may require docket search at scc.virginia.gov/docketsearch) |

## PJM market and capacity primary sources

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `pjm_capacity_auctions_2024_2027` | PJM Base Residual Auction reports for 2024/25, 2025/26, 2026/27 delivery years | open | N | no | needs download (three separate PDFs linked in bib note; all on pjm.com) |
| `monitoring_analytics_2026_q1` | Monitoring Analytics (2026), Q1 2026 State of the Market Report for PJM | open | N | no | needs download (monitoringanalytics.com PDF) |

## Cross-cutting references on data center electricity demand

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `shehabi_2024_lbnl` | Shehabi et al. (2024), LBNL Data Center Energy Usage Report (LBNL-2001637) | open | N | no | needs download (existing entry; URL not re-fetched this session) |
| `brattle_esig_2026_largeloads_primer` | Brattle / ESIG (2026-05-12), "Impacts of Large Loads on Electricity Rates: A Primer" | open | N | no | needs download (esig.energy page links to PDF) |
| `jlarc_2024_vadcs` | JLARC (2024), Virginia Data Center Study Final Presentation | open | N | no | needs download (existing entry; URL not re-fetched) |
| `newell_2025_brattle` | Newell, Hledik, Pfeifenberger (2025), "Meeting Unprecedented Load Growth" (Brattle whitepaper) | open | N | no | needs download (existing entry; URL not re-fetched) |

## Additional methodology and supporting references

| Key | Reference | Access | URL verified | Local | Status |
|---|---|---|---|---|---|
| `bulan_2009_realoptions` | Bulan, Mayer, Somerville (2009), "Irreversible Investment, Real Options ..." (JUE 65:3) | paywall + preprint | N | no | needs download (NBER WP 12486 preprint is open) |
| `silerevans_2012_mef` | Siler-Evans, Azevedo, Morgan (2012), "Marginal Emissions Factors ..." (ES&T 46:9) | paywall | N | no | needs download (ACS journal paywall; check CMU repository for an open copy) |

---

## Summary tally

- **Total entries:** 48
- **Open access, URL verified this session:** 18
- **Open access, URL inferred (needs sanity check):** 22
- **Paywall + preprint available:** 7
- **Paywall, no known preprint:** 1 (`silerevans_2012_mef`)
- **eLibrary lookup / TBD:** 2 (`pjm_2026_btmg_compliance`, `md_opc_2026_complaint`)

## Open TODOs in `references.bib` (not download issues — content issues)

These are flagged in the bib file itself, not download blockers, but they affect whether the entry is locked-and-final:

- `atkinson_2025_flexible_datacenters` — Citing institutionally (Camus / encoord / Princeton ZERO Lab). Individual authorship intentionally not inferred.
- `swartzentruber_2026_risk_ambiguity` — Attribution corrected from "Bistline" (in original prompt) to Swartzentruber & Sims after web verification. The risk-vs-ambiguity citation now lives at this key. `bistline_2024_reform_options` is a separate entry kept for completeness in case a Bistline anchor citation is needed.
- `pjm_2026_btmg_compliance` and `md_opc_2026_complaint` — Specific FERC eLibrary accession numbers still TBD; umbrella dockets known.
- The dropped NJ SB 484 entry (no NJ bill matched the substantive description; comment block in bib explains).
