# Counter-review of the first LaTeX manuscript

Date: 2026-11-05  
File: `north_south_regional_hate_paper.tex`

## Critical issues found

1. **Direction ambiguity.** The data identifies the target of harm, not the author's regional origin. The title and manuscript were revised from broad `direction-aware` wording to `target-specific`, with an explicit warning that no source-to-target regional relation is observed.
2. **Construct validity.** `PREJUDICIAL` versus `HOSTILE` and the target-relative meaning of `NON_HATE` require a frozen codebook and boundary examples. The draft now states this limitation and reserves a comment-example table.
3. **Missing provenance and ethics.** Platforms, dates, queries, filtering, consent/ethics, annotator compensation, and release terms are unknown. Dedicated collection and ethics placeholders remain rather than invented details.
4. **Benchmark validity.** The current split has capitalization-normalized leakage, South minority test supports of only 14/9, one seed, raw unsegmented PhoBERT input, and no ViSoBERT baseline. Scores are explicitly marked preliminary and a required rerun protocol is listed.
5. **Two-output value not demonstrated.** Only 15 comments are harmful toward both targets, and the strongest baseline trains separate PhoBERT classifiers. The revised draft adds RQ2 and requires matched ablations, paired exact match, Hamming loss, and target-swap analysis.
6. **Kappa interpretation.** Mean pairwise Cohen's kappa is descriptive and pairwise SD is not uncertainty. The draft now calls it the arithmetic mean of ten pairwise coefficients, distinguishes between-pair dispersion from confidence intervals, and requests a multi-rater robustness statistic.

## Additional fixes applied

- Added a prior-dataset comparison table covering VLSP-HSD, ViHSD, ViRDC, ViTHSD, and this work.
- Added three formal research questions.
- Added a majority-class baseline to the results table.
- Removed incorrect bolding of PhoBERT accuracy where Random Forest was higher.
- Replaced a causal claim about pretraining with a configuration-qualified comparison.
- Clarified that current model ranking must not feed back into model development.
- Clarified that current artifacts do not yet report every promised class-level metric or confusion matrix.
- Revised the author block to avoid `\and` affiliation layout problems.
- Replaced dense `[H]` float placement with `[tbp]` and added prose references to previously orphaned placeholders.

## Static verification

- Environments balanced; braces balanced.
- 16 citation keys, all matched to 16 bibliography entries.
- No duplicate labels or unresolved references.
- No external `\input`, `\include`, `\includegraphics`, BibTeX, or Biber dependency; the manuscript is a single `.tex` source.
- A LaTeX engine is not installed in the workspace, so dynamic compilation still needs to be run on the authors' TeX/Overleaf environment with at least two passes.
