---
task_id: c
role: NLP Dataset Annotation and Benchmark Methodology Specialist
status: complete
sources_found: 10
---

## Sources

[1] Analyzing Dataset Annotation Quality Management in the Wild | https://aclanthology.org/anthology-files/pdf/cl/2024.cl-3.1.pdf | Source-Type: academic | As Of: 2024-09 | Authority: 10/10
[2] Web(er) of Hate: A Survey on How Hate Speech Is Typed | https://aclanthology.org/2025.woah-1.9/ | Source-Type: academic | As Of: 2025-08 | Authority: 9/10
[3] When the Majority is Wrong: Modeling Annotator Disagreement for Subjective Tasks | https://aclanthology.org/2023.emnlp-main.415/ | Source-Type: academic | As Of: 2023-12 | Authority: 9/10
[4] Hate Speech Criteria: A Modular Approach to Task-Specific Hate Speech Definitions | https://aclanthology.org/2022.woah-1.17/ | Source-Type: academic | As Of: 2022-07 | Authority: 9/10
[5] Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science | https://aclanthology.org/Q18-1041/ | Source-Type: academic | As Of: 2018-12 | Authority: 10/10
[6] A Network Perspective on Stratification of Multi-Label Data | https://arxiv.org/abs/1704.08756 | Source-Type: academic | As Of: 2017-04 | Authority: 8/10
[7] Enhancing Data Quality through Simple De-duplication: Navigating Responsible Computational Social Science Research | https://aclanthology.org/2024.emnlp-main.694/ | Source-Type: academic | As Of: 2024-11 | Authority: 9/10
[8] Show Your Work: Improved Reporting of Experimental Results | https://aclanthology.org/D19-1224/ | Source-Type: academic | As Of: 2019-11 | Authority: 10/10
[9] ACL Ethics — Responsible Research Checklist for Researchers | https://ethics.aclweb.org/roles/researchers/ | Source-Type: official | As Of: 2026-11 | Authority: 10/10
[10] VinAIResearch/PhoBERT Official README | https://github.com/VinAIResearch/PhoBERT | Source-Type: official | As Of: 2026-11 | Authority: 10/10

## Findings

- Having two independent annotators per item and a third adjudicator is a defensible, commonly used prescriptive annotation design, but it becomes publishable evidence only when pre-adjudication agreement, adjudication rate, annotator training/backgrounds, guideline iterations, and post-adjudication validation are reported; percent agreement alone is inadequate, while Krippendorff's alpha is broadly recommended and Cohen's kappa is also suitable when exactly two annotators label every item. [1][2]
- Hate-speech disagreement should not automatically be treated as random error: target-group membership and lived experience can systematically change judgments, so the dataset should retain the two raw labels and a disagreement/adjudication indicator even if it releases one prescriptive gold label. [2][3]
- The paper must operationally define the boundary among NON_HATE, PREJUDICIAL, and HOSTILE with positive, negative, and boundary examples, and explicitly state target groups, dominance assumptions, perpetrator/target scope, negative interaction criteria, and consequence/severity because hate-speech taxonomies encode value judgments rather than universal ground truth. [2][4]
- For a dataset with two correlated outputs, stratifying only on `north_hate` does not preserve rare `south_hate` labels or North/South label combinations; iterative or second-order stratification is designed to preserve single-label and label-pair evidence and reduce fold-to-fold variance. [6]
- Exact deduplication before splitting is necessary but not sufficient for social-media text: near-duplicates and repeated users/threads/events can cross splits, cause leakage, and overestimate model effectiveness, so grouping by source post/thread/user/time where metadata permits and auditing normalized near-duplicates are recommended. [7]
- Sorting models by test Macro-F1 or choosing the “best model” on test data violates the held-out-test role; model family, hyperparameters, epoch, and threshold must be selected on validation data, with test evaluated once after choices are frozen. [8]
- A credible benchmark should report per-target and per-class precision/recall/F1, macro-F1 as the primary imbalance-aware metric, class supports, confusion matrices, multiple-seed mean and standard deviation or confidence intervals, hyperparameter-search budget, hardware/software versions, training cost, and ideally paired significance/bootstrapped uncertainty rather than one point estimate. [8][9]
- Dataset documentation should cover motivation, collection platform/query/time window, inclusion and filtering criteria, language varieties, target population, annotator demographics and compensation, label definitions, split statistics, intended and out-of-scope uses, license, privacy/PII handling, limitations, potential misuse, and maintenance/versioning. [5][9]
- The official PhoBERT documentation requires raw Vietnamese input to be word-segmented (recommended RDRSegmenter/VnCoreNLP) before tokenization; feeding the notebook's unsegmented comments directly to `vinai/phobert-base-v2` is therefore a benchmark validity issue that should be fixed and rerun. [10]
- The strongest defensible contribution is not “we used five models” but a documented, target-specific Vietnamese regional-prejudice resource with reliable adjudicated labels and a reproducible benchmark protocol; five model families are useful coverage only if comparisons use the same frozen split, fair tuning budgets, multiple seeds, and no test-set model selection. [1][5][8][9]

## Deep Read Notes

### Source [1]: Analyzing Dataset Annotation Quality Management in the Wild
Key data: The study reviews 591 dataset papers; it recommends Krippendorff's alpha broadly, Cohen's kappa for two fixed annotators, and says percent agreement should rarely be used and never alone; it also recommends whole-dataset agreement or a justified large subset (about 500 items).
Key insight: Agreement is evidence about reliability, not proof of correctness; manual validation, adjudication/error-rate estimation, annotator backgrounds, judgment counts, and sample size must be documented.
Useful for: Defending the two-annotator-plus-adjudicator design while specifying the missing reliability evidence reviewers will expect.

### Source [2]: Web(er) of Hate: A Survey on How Hate Speech Is Typed
Key data: Across 135 surveyed datasets, most assign two annotators per item; 48 use majority rule, 27 use additional adjudicators, eight use moderation meetings, 78 do not report annotator demographics, and 69 do not clearly report quality-assurance procedures.
Key insight: A single adjudicated gold label is appropriate under an explicitly prescriptive goal, but aggregating away disagreement is counterproductive for a descriptive/perspectivist goal; raw disagreement remains scientifically valuable.
Useful for: Positioning the proposed annotation pipeline as common and defensible, not itself novel, and motivating transparency about regional identities and disagreement.

### Source [6]: A Network Perspective on Stratification of Multi-Label Data
Key data: The paper shows ordinary splits can leave rare labels or label pairs without positive evidence; second-order iterative stratification preserves label-pair distributions and lowers variance of classification quality while maintaining competitive label-wise balance.
Key insight: Two target columns should be treated jointly during split construction, especially where `south_hate` minority classes are extremely rare.
Useful for: Replacing the current `stratify=north_hate` 70/15/15 split with a frozen, joint-label-aware split.

### Source [7]: Enhancing Data Quality through Simple De-duplication
Key data: The EMNLP 2024 audit examines 20 social-media datasets and finds duplicate/near-duplicate content can create inconsistent labels, train-test leakage, altered model rankings, and overestimated performance.
Key insight: Removing exact duplicate comments before a random split is a good first step, but a release-quality benchmark also needs normalized near-duplicate and provenance-group leakage audits.
Useful for: Dataset hygiene and split validation.

### Source [8]: Show Your Work
Key data: The paper demonstrates that test scores alone can produce inaccurate model rankings and recommends reporting validation behavior and computational/hyperparameter-search budget.
Key insight: The notebook currently warns against test-based selection but then sorts by `test_mean_macro_f1` and declares the first row best; this contradiction is a concrete reviewer-facing flaw.
Useful for: Freezing a correct model-selection protocol and making the five-model benchmark fair and reproducible.

### Source [10]: VinAIResearch/PhoBERT Official README
Key data: The model authors explicitly state that PhoBERT input must already be word-segmented and recommend the VnCoreNLP RDRSegmenter for raw Vietnamese.
Key insight: `AutoTokenizer` does not remove this preprocessing requirement; the existing direct raw-comment tokenization makes the current PhoBERT score unsuitable as a final benchmark result.
Useful for: Correcting and rerunning the strongest baseline before publication.

## Gaps

- The available files do not include the two annotators' original labels, annotator identifiers/backgrounds, disagreement counts, adjudicator decisions, pilot protocol, guideline document, or ethics/consent record; without them, inter-annotator agreement and adjudication quality cannot be independently verified.
- Reviewer-rejection risk (critical): the notebook selects and names the best model using test Macro-F1 despite stating test should be used only once; freeze selection on validation and rerun final test evaluation.
- Reviewer-rejection risk (critical): `south_hate` is not used for stratification; the current test support is only 14 PREJUDICIAL and 9 HOSTILE examples, making its Macro-F1 highly unstable and susceptible to a few predictions; rebuild a joint-label-aware split or use repeated/nested stratified evaluation while preserving a final untouched test set.
- Reviewer-rejection risk (critical): PhoBERT receives raw unsegmented Vietnamese contrary to its official preprocessing requirement; word-segment and rerun all relevant comparisons.
- Reviewer-rejection risk (high): all neural results appear to be single-seed, and tuning budgets differ substantially among RF/LR/NB, BiLSTM, and PhoBERT; report 3-5 seeds, mean/SD or confidence intervals, and equal/declared tuning budgets.
- Reviewer-rejection risk (high): exact duplicate removal is shown, but near-duplicate, user/thread/event, and temporal leakage are not audited; preserve source metadata internally and use grouped or temporal robustness tests if legally and ethically possible.
- Reviewer-rejection risk (high): the contribution cannot be claimed as the annotation protocol or as “five-model novelty”; the defensible novelty must come from the regional target taxonomy/data coverage and public, reusable benchmark artifact, which depends on the separate literature search for prior Vietnamese regional-hate datasets.
- Alternative interpretation: if the authors intend a perspectivist/descriptive dataset rather than a prescriptive moderation benchmark, third-person adjudication into one gold label is methodologically misaligned; release raw annotations/disagreement distributions and model soft-label or annotator-conditioned outcomes instead.
