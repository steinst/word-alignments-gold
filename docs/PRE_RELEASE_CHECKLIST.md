# Before publishing on GitHub

1. Read `docs/REDISTRIBUTION.md` and skim each resource's terms.
2. Check all URLs you care about; this release's offline validator checks syntax and references, not whether websites are live.
3. Replace the provisional `@misc` bibliographic citations as complete paper metadata becomes verified.
4. Choose your own license for **original repository metadata and scripts**. Upstream dataset terms are separate. No blanket MIT/CC license is asserted over their contents.
5. Do not commit third-party text/alignments until a reviewer confirms permissions and appropriate notices.
6. Run `python3 scripts/validate.py` then `python3 scripts/build_catalog.py`.
7. Commit the source-linked metadata first; add verified original data in separately reviewed commits.
