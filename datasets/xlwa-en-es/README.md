# XL-WA manually annotated evaluation gold: English–ES

- **Language pairs:** en-es
- **Annotation type:** `word`
- **Original publication:** https://github.com/SapienzaNLP/XL-WA
- **Original dataset/access page:** https://github.com/SapienzaNLP/XL-WA
- **Access mode:** `public`
- **Rights/license:** `CC-BY-NC-SA-4.0`
- **Evidence for terms:** https://github.com/SapienzaNLP/XL-WA/blob/main/LICENSE.txt
- **Evidence status:** `verified-publisher`
- **Repository decision:** `restricted-link-default`
- **Verified on:** 2026-11-18

## Terms and permissions

CC BY-NC-SA 4.0 permits noncommercial sharing with attribution and share-alike, but this catalogue defaults to linking, not mirroring; verify whether source text has additional rights.

**No third-party data files are bundled.** See [redistribution policy](../../docs/REDISTRIBUTION.md).

## Original bibliographic reference

Federico Martelli et al. (2023). XL-WA: a Gold Evaluation Benchmark for Word Alignment in 14 Language Pairs. CLiC-it 2023.

**BibTeX key(s):** `martelli2023xlwa` — [CITATIONS.bib](../../CITATIONS.bib)

## Recommended parallel training corpora

- **[OPUS-100 multilingual parallel corpus](https://opus.nlpl.eu/opus-100.php)** — Underlying OPUS source corpus conditions vary; verify actual data license. Convenient stratified capped training benchmark, not word-alignment gold.  Citation: `zhang2020opus100`.
- **[OPUS parallel corpora](https://opus.nlpl.eu/)** — Licenses vary by subcorpus; no umbrella redistribution grant. Choose e.g. Europarl/JRC/SETIMES/OpenSubtitles; inspect per-subcorpus terms.  Citation: `tiedemann2012opus`.
- **[Europarl parallel corpus](https://opus.nlpl.eu/Europarl.php)** — Check particular Europarl/OPUS release attribution and underlying rights. Especially relevant for EN-FR/DE/ES/SV/IT/NL and some EU languages.  Citation: `koehn2005europarl`.

## Counts / partitions

- **evaluation_split:** manual dev/test; silver train is not gold

## Important notes

XL-WA training TSV contains automatically generated silver links; only dev and test are gold.

[Back to catalogue](../../docs/DATASETS.md)
