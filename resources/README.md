# Road resource inventory

This directory is intended to become a GTM-quality public index of useful road/traffic engineering resources, not a random link dump.

## Inclusion rule

Each entry should record:

- authoritative source/provenance;
- what problem it solves;
- geographic/traffic regime;
- whether it contains code/data/method only;
- license/access status;
- how Road Space Lab plans to use it;
- whether it has been reproduced/validated here.

## Status vocabulary

- `priority` — directly useful to the first benchmark;
- `baseline` — established method/standard we must compare against;
- `benchmark` — an external method to reproduce;
- `review` — promising, but license/provenance/technical fit still needs inspection;
- `reference` — important context, not necessarily reusable code/data.

## License rule

A GitHub repository, Kaggle page or downloadable PDF is **not automatically reusable**. Preserve upstream licenses and cite original authors. When the source is ambiguous, catalog it as `VERIFY`, do not vendor it.

The machine-readable inventory is [`catalog.csv`](catalog.csv).
