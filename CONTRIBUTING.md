# Contributing

To add or correct a gold set:

1. Add an entry to `catalog/gold_datasets.json`; separate each independent gold dataset rather than collapsing by language pair.
2. Include the original **publisher or archival publication** URL, access page, annotated unit, actual license evidence URL, and rights decision.
3. Add all linked training corpora to `catalog/training_corpora.json` (with publisher URLs and access/licensing terms).
4. Add accurate BibTeX entries to `CITATIONS.bib`, citing dataset authors when known; do not invent missing fields.
5. Run `python3 scripts/validate.py` and `python3 scripts/build_catalog.py` and commit generated pages.
6. Do not commit downloaded corpus data until checked against `docs/REDISTRIBUTION.md`.

Improve the catalogue by opening issues for broken URLs, incomplete references, or permission changes.
