# references/

Local PDF copies of papers and primary-source documents cited in `docs/references.bib`.

## What goes here

PDFs and DOCX files of:

- Academic papers and working papers
- Agency orders and tariff filings (FERC, PJM, state PUCs)
- Reports, primers, and whitepapers
- Substack posts and other secondary commentary saved as PDF for offline reference

## What does **not** go here

This folder is **gitignored** for PDF and DOCX files. Do not commit copyrighted material to a public repository. See `.gitignore`:

```
references/*.pdf
references/*.docx
!references/.gitkeep
!references/README.md
```

Only `.gitkeep` and this `README.md` are tracked.

## Naming convention

Match the BibTeX citation key from `docs/references.bib`, lowercase, `.pdf`:

- `shao_2025_pjm_siting.pdf`
- `mogstad_2020_ranks_nber.pdf`
- `lade_2026_fiscal.pdf`

For multi-part sources (e.g., the PJM capacity auction reports under `pjm_capacity_auctions_2024_2027`), suffix with the delivery year:

- `pjm_capacity_auctions_2024_2027__2024-25.pdf`
- `pjm_capacity_auctions_2024_2027__2025-26.pdf`
- `pjm_capacity_auctions_2024_2027__2026-27.pdf`

## Download workflow

See `docs/source_inventory.md` for the per-entry download checklist with verified URLs, access status (open / paywalled / agency portal / eLibrary lookup), and status field. Start with entries marked `Access: open` and `URL verified: Y`; save `eLibrary lookup` items for a focused session.
