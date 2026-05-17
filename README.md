# PJM Data Center Siting

A developer-perspective NPV model for siting a hyperscale data center across twenty candidate locations in the PJM Interconnection footprint, with explicit treatment of policy risk and carbon pricing.

## Motivation

This project extends prior work on AI infrastructure economics and FERC's evolving treatment of large-load interconnection. See the companion AI Infrastructure paper and FERC brief at [lambcast.net](https://lambcast.net) for the framing this model operationalizes.

*(Placeholder: expand once the literature survey is complete.)*

## What this project produces

- A Python NPV model evaluating twenty PJM candidate sites under a configurable cost stack (energy, capacity, interconnection, property tax, carbon, policy risk).
- Pre-computed sensitivity results across facility size, discount rate, and carbon price.
- A React/Vite frontend, deployed to Vercel, exposing the sensitivity surface interactively.
- A writeup posted to [lambcast.net](https://lambcast.net).

## Repository structure

````
docs/         Master document, methods notes, decision log, references
data/         raw/ (gitignored), processed/, reference/
src/pjm_siting/   Python package
scripts/      Runnable data pulls and analysis entry points
notebooks/    Exploration
tests/        Unit tests
frontend/     React/Vite app (deployed to Vercel)
results/      figures/, tables/, precomputed/
````

## How to run

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12.

```powershell
uv sync
uv run python scripts/<entry_point>.py
```

*(Placeholder: list actual entry points as scripts are written.)*

## Key decisions

See [docs/decisions.md](docs/decisions.md) for the running decision log.

## References

See [docs/references.bib](docs/references.bib).

## Citation

*(Placeholder: add citation block once the writeup is published.)*

## License

*(Placeholder: license to be selected.)*
