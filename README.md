# Word Alignment Gold

**A source-linked, citation-ready catalogue of word-alignment evaluation datasets and matching parallel training corpora.**

This repository is **metadata-first**. No third-party corpus files are bundled in the initial release. It aims to cover the evaluation pairs discussed for classical statistical word aligners, including GIZA++, fast_align, eflomal, Berkeley Aligner, and subsequent models. Not a claim of exhaustive global coverage.

## What it contains

- [Browse all language pairs](docs/BY_LANGUAGE_PAIR.md), mapping multiple gold sets to the same pair.
- [Complete gold dataset inventory](docs/DATASETS.md), including source publication pages, license status, BibTeX key and suggested parallel corpora.
- [Parallel training corpus catalogue](docs/TRAINING.md) with publisher links and access/licensing notes.
- [`catalog/gold_datasets.json`](catalog/gold_datasets.json): structured records for individual datasets (distinct datasets for the same language pair are kept separate).
- [`CITATIONS.bib`](CITATIONS.bib): all cited original dataset references and training-corpus references.
- [`datasets/`](datasets/): one navigable README per record, with original publication, bibliographic reference, terms, and training options.
- [`docs/REDISTRIBUTION.md`](docs/REDISTRIBUTION.md): evidence-based policy and checklist.

## Status meanings

| Status | Meaning | Files committed? |
|---|---|---|
| `eligible-after-review` | Open publisher license found, but full content/attribution/version must still be checked | No, until review |
| `restricted-link-default` | CC non-commercial or no-derivatives restrictions; link-only is safest default | No |
| `component-only` | Only some annotations/components have an open license | No, until separated and reviewed |
| `contact-required` | Contact source for access | No |
| `controlled-access` | LDC or similar licensed access | No |
| `link-only` | No clear redistribution grant established | No |

**IMPORTANT:** Publication links, GitHub availability, or a download button are not permission to republish. Repository scripts' license does not change upstream dataset licenses. See [redistribution policy](docs/REDISTRIBUTION.md).

## Get started

```bash
python3 scripts/validate.py
python3 scripts/build_catalog.py
```

To download a dataset, follow its original publisher link in the catalogue, check its license, and save it **locally** (the `data/` directory is gitignored). Never auto-download restricted datasets.

## Gold vs. training

A gold set contains manually annotated word links. Sentence-aligned training corpora are not gold. XL-WA `train.tsv` is **silver**, not gold; HELFI is **morpheme-level**; PUD annotations follow **different link guidelines**; ZurichNLP document-level material reorganizes preexisting gold and is **not independent gold**. Keep these tracks separate in evaluation.

## Citations

Each dataset page gives a human-readable reference and a key in [`CITATIONS.bib`](CITATIONS.bib). Some old resources lack a verifiable formal publication citation; their BibTeX uses a publisher-page `@misc` record and flags missing bibliographic details rather than inventing them. Training sources also have BibTeX entries.

## Next steps

1. Review the entries and licenses, particularly the underlying sentence texts.
2. Mirror only datasets that have passed the checklist and retain original notices.
3. Pin archives, versions, checksums and corpus source editions.
4. Create normalized evaluation formats only when adaptation is allowed.
5. Add verified dataset releases and reproducible test fixtures as separate, clearly licensed commits.

See [contributing](CONTRIBUTING.md). Metadata last prepared 2026-11-18.
