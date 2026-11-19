#!/usr/bin/env python3
"""Regenerate Markdown catalogues and per-resource pages from JSON metadata."""
from pathlib import Path
import json, urllib.parse
ROOT=Path(__file__).resolve().parents[1]
gold=json.loads((ROOT/'catalog/gold_datasets.json').read_text(encoding='utf-8'))
train=json.loads((ROOT/'catalog/training_corpora.json').read_text(encoding='utf-8'))
byid={x['id']:x for x in train}
md=lambda s:str(s).replace('|',r'\|').replace('\n',' ')
lines=['# Gold alignment dataset catalogue','','Each row is a **dataset resource**, not merely a unique language pair. For complete descriptions, click the dataset entry. All upstream data files are omitted from this initial repository.','','| Resource | Pairs | Kind | Redistributability | Publisher / access | Citation |','|---|---|---|---|---|---|']
for x in gold:
    lines.append(f"| [{md(x['title'])}](../datasets/{x['id']}/README.md) | {', '.join(x['language_pairs'])} | {x['annotation_type']} | `{x['license']['redistribution_decision']}` | [Source]({x['source_url']}) | `{', '.join(x['citation_keys'])}` |")
lines+=['','See [training corpus catalogue](TRAINING.md) and [redistribution policy](REDISTRIBUTION.md).','']
(ROOT/'docs'/'DATASETS.md').write_text('\n'.join(lines),encoding='utf-8')
lines=['# Parallel training corpora','','All are **sentence-aligned training sources**, not word-alignment gold. Licensing may depend on the particular download or subcorpus.','','| Corpus | Language coverage | Access | License considerations | Citation |','|---|---|---|---|---|']
for x in train:
    pp='Any supported pair' if x['language_pairs']=='*' else ', '.join(x['language_pairs'])
    lines.append(f"| [{md(x['title'])}]({x['publisher_url']}) | {pp} | {x['access']} | {md(x['license_summary'])} | `{', '.join(x['citation_keys'])}` |")
lines+=['','See [dataset catalogue](DATASETS.md).','']
(ROOT/'docs'/'TRAINING.md').write_text('\n'.join(lines),encoding='utf-8')
for x in gold:
    out=ROOT/'datasets'/x['id'];out.mkdir(parents=True,exist_ok=True)
    lic=x['license']
    txt=[f"# {x['title']}",'',f"- **Language pairs:** {', '.join(x['language_pairs'])}",f"- **Annotation type:** `{x['annotation_type']}`",f"- **Original publication:** {x['original_publication_url']}",f"- **Original dataset/access page:** {x['source_url']}",f"- **Access mode:** `{x['access']}`",f"- **Rights/license:** `{lic['identifier']}`",f"- **Evidence for terms:** {lic['evidence_url']}",f"- **Evidence status:** `{lic['evidence_status']}`",f"- **Repository decision:** `{lic['redistribution_decision']}`",f"- **Verified on:** {x['verified_on']}",'','## Terms and permissions','',lic['terms_summary'],'','**No third-party data files are bundled.** See [redistribution policy](../../docs/REDISTRIBUTION.md).','','## Original bibliographic reference','',x['bibliographic_reference'],'',f"**BibTeX key(s):** {', '.join('`'+k+'`' for k in x['citation_keys'])} — [CITATIONS.bib](../../CITATIONS.bib)",'','## Recommended parallel training corpora','']
    for id in x['training_corpus_ids']:
        c=byid[id]
        txt += [f"- **[{c['title']}]({c['publisher_url']})** — {c['license_summary']} {c['notes']}  Citation: {', '.join('`'+k+'`' for k in c['citation_keys'])}."]
    if x['counts']: txt+=['','## Counts / partitions','',*[f"- **{k}:** {v}" for k,v in x['counts'].items()]]
    if x['notes']:txt+=['','## Important notes','',x['notes']]
    txt+=['','[Back to catalogue](../../docs/DATASETS.md)','']
    (out/'README.md').write_text('\n'.join(txt),encoding='utf-8')

# Per-language-pair index; direction is normalized only for DISCOVERY, not for link coordinates.
from collections import defaultdict
pairs=defaultdict(list)
for x in gold:
    for lang_pair in x['language_pairs']:
        pair_key='–'.join(sorted(lang_pair.split('-')))
        pairs[pair_key].append((lang_pair,x))
lines=['# Browse by language pair','','The language codes are direction-neutral *for browsing only*. The original source/target order is preserved in each dataset record and must be respected when reading alignment indices.','','| Language pair | Gold / related resources | Suggested training corpora |','|---|---|---|']
for pair_key, group in sorted(pairs.items()):
    refs='; '.join(f"[{x['id']}](../datasets/{x['id']}/README.md)" for _,x in group)
    corpus_ids=sorted({t for _,x in group for t in x['training_corpus_ids']})
    corpus_list=', '.join(f"[{tid}]({byid[tid]['publisher_url']})" for tid in corpus_ids)
    lines.append(f'| **{pair_key}** | {refs} | {corpus_list} |')
lines+=['','[Full dataset catalogue](DATASETS.md) · [Training sources](TRAINING.md)','']
(ROOT/'docs'/'BY_LANGUAGE_PAIR.md').write_text('\n'.join(lines),encoding='utf-8')

print(f'Generated {len(gold)} resource pages, both catalogue tables and per-pair index.')
