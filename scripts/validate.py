#!/usr/bin/env python3
"""Offline metadata / BibTeX-key integrity check; uses only Python stdlib."""
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
datasets=json.loads((ROOT/'catalog/gold_datasets.json').read_text(encoding='utf-8'))
training=json.loads((ROOT/'catalog/training_corpora.json').read_text(encoding='utf-8'))
bib=(ROOT/'CITATIONS.bib').read_text(encoding='utf-8')
keys=set(re.findall(r'^\s*@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,',bib,re.M))
valid_statuses={'eligible-after-review','restricted-link-default','component-only','contact-required','controlled-access','link-only'}
fail=[]
train_idx={x['id']:x for x in training}
if len(train_idx)!=len(training):fail.append('Duplicate training ids')
ids=[x['id'] for x in datasets]
if len(ids)!=len(set(ids)):fail.append('Duplicate gold ids')
for group, rows in [('gold',datasets),('training',training)]:
  for x in rows:
    ident=x['id']
    if not x.get('citation_keys'): fail.append(f'{group} {ident}: missing citations')
    for k in x.get('citation_keys',[]):
      if k not in keys:fail.append(f'{group} {ident}: missing BibTeX entry {k}')
    for key in (['original_publication_url','source_url'] if group=='gold' else ['publisher_url']):
      if not str(x.get(key,'')).startswith(('https://','http://')):fail.append(f'{group} {ident}: invalid {key}')
    if group=='gold':
      if not x['language_pairs']:fail.append(f'{ident}: no language pairs')
      if not x.get('bibliographic_reference'):fail.append(f'{ident}: missing human-readable reference')
      lic=x.get('license',{})
      if lic.get('redistribution_decision') not in valid_statuses:fail.append(f'{ident}: invalid redistribution status')
      if not str(lic.get('evidence_url','')).startswith(('https://','http://')):fail.append(f'{ident}: missing license evidence URL')
      for tid in x.get('training_corpus_ids',[]):
        if tid not in train_idx:fail.append(f'{ident}: missing training record {tid}')
print(f'{len(datasets)} gold/related resource records; {len(training)} training corpus records; {len(keys)} BibTeX keys.')
if fail:
    print('VALIDATION FAILED:')
    for f in fail:print(' - '+f)
    sys.exit(1)
print('PASS: referential integrity checks (NOT an external license or URL audit).')
