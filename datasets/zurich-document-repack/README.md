# ZurichNLP reconstructed document-level word alignment dataset

- **Language pairs:** en-fr, en-ro, en-ja, en-zh, en-cs, la-grc
- **Annotation type:** `derived-document`
- **Original publication:** https://huggingface.co/datasets/ZurichNLP/document-level-word-alignment
- **Original dataset/access page:** https://huggingface.co/datasets/ZurichNLP/document-level-word-alignment
- **Access mode:** `public`
- **Rights/license:** `mixed-upstream`
- **Evidence for terms:** https://huggingface.co/datasets/ZurichNLP/document-level-word-alignment
- **Evidence status:** `verified-publisher`
- **Repository decision:** `link-only`
- **Verified on:** 2026-11-18

## Terms and permissions

Recombines preexisting human gold standards, including WPT and Tsinghua with unspecified redistribution licenses. Catalogue upstream sources; never treat derivative packaging as new blanket license.

**No third-party data files are bundled.** See [redistribution policy](../../docs/REDISTRIBUTION.md).

## Original bibliographic reference

ZurichNLP, Scaling Unsupervised Word Alignment to Documents with Structural Constraints (project/dataset page).

**BibTeX key(s):** `zurichsource` — [CITATIONS.bib](../../CITATIONS.bib)

## Recommended parallel training corpora

- **[WPT 2003 shared-task training material](https://web.eecs.umich.edu/~mihalcea/wpt/)** — No explicit redistribution license established. Use original train split for historical comparability.  Citation: `mihalcea2003evaluation`.
- **[Kyoto Free Translation Task](https://www.phontron.com/kftt/)** — Publisher describes CC BY-SA 3.0. Domain-matched JA-EN training/test; avoid data leakage.  Citation: `neubig2011kftt`.
- **[CzEng 2.0](https://ufal.mff.cuni.cz/czeng)** — Non-commercial research and registration conditions; do not mirror by default. Large-scale high-quality parallel Czech–English corpus.  Citation: `czeng2020`.
- **[Tsinghua Chinese–English training set](https://nlp.csai.tsinghua.edu.cn/~ly/systems/TsinghuaAligner/TsinghuaAligner.html)** — No explicit redistribution license established on source page. Publisher describes 700k parallel sentence pairs; download from source.  Citation: `tsinghuasource`.

## Important notes

Not independent annotation: avoid double-counting data across sources.

[Back to catalogue](../../docs/DATASETS.md)
