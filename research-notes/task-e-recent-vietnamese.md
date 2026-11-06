---
task_id: e
role: Recent Vietnamese Hate-Speech Literature Specialist
status: complete
sources_found: 6
---

## Sources

[1] ViHateT5: Enhancing Hate Speech Detection in Vietnamese With a Unified Text-to-Text Transformer Model | https://aclanthology.org/2024.findings-acl.355/ | Source-Type: academic | As Of: 2024-08 | Authority: 10/10
[2] ViTHSD: Exploiting Hatred by Targets for Hate Speech Detection on Vietnamese Social Media Texts | https://arxiv.org/abs/2404.19252 | Source-Type: academic | As Of: 2025-02 | Authority: 9/10
[3] A Big Data-empowered System for Real-time Detection of Regional Discriminatory Comments on Vietnamese Social Media | https://arxiv.org/abs/2411.02587 | Source-Type: academic | As Of: 2024-10 | Authority: 8/10
[4] BamiBERT: A New BERT-based Language Model for Vietnamese | https://arxiv.org/abs/2607.02259 | Source-Type: academic | As Of: 2026-07 | Authority: 7/10
[5] SEAHateCheck: Functional Tests for Detecting Hate Speech in Low-Resource Languages of Southeast Asia | https://arxiv.org/abs/2603.16070 | Source-Type: academic | As Of: 2026-03 | Authority: 9/10
[6] Enhanced Framework for Detecting Vietnamese Hate and Offensive Spans | https://ijai.iaescore.com/index.php/IJAI/article/view/29389 | Source-Type: academic | As Of: 2026-02 | Authority: 7/10

## Findings

- ViHateT5 is the most important recent model paper to add: it pre-trains a unified T5 model on VOZ-HSD, about 10.8 million automatically labeled forum comments, then jointly addresses Vietnamese hate classification, toxic-speech classification, and hate-span detection; it strengthens the case that domain-specific social-media pre-training matters but does not introduce regional target labels. [1]
- ViTHSD is the closest recent dataset formulation: its journal version contains 10,000 comments, five target axes, and target-specific clean/offensive/hate levels, with mean pairwise Cohen's kappa of 0.45 for target-with-level labels; therefore the proposed paper must define novelty specifically as North-versus-South direction and severity rather than Vietnamese multi-target hate detection in general. [2]
- ViTHSD explicitly computes Cohen's kappa for every annotator pair and averages the values, making the proposed dataset's mean pairwise kappa of about 0.50 directly comparable in form and broadly similar in magnitude. [2]
- ViRDC remains the direct regional-discrimination predecessor: it introduces Vietnamese regional-discrimination detection and a benchmark, but its single global Other/Discrimination/Supportive label does not identify which regional group is attacked or grade the target-specific severity. [3]
- BamiBERT is a July 2026 preprint that supports raw input, a 2,048-token context, and reports leading or second-place results on most of eight Vietnamese benchmarks; although it does not evaluate hate speech, it is a timely optional baseline or future-work model because it avoids PhoBERT's external word-segmentation requirement. [4]
- SEAHateCheck, accepted by TALLIP in 2026, adds culturally grounded Vietnamese functional tests covering explicit and implicit hate, slang, negation, benign protected-group mentions, quoted hate, and counter-speech; it shows why a random held-out split alone cannot diagnose whether models learn regional slurs rather than target-conditioned semantics. [5]
- SEAHateCheck uses native-speaker validation and reports Fleiss' kappa of 0.85 for gold test cases; its Vietnamese component includes 22 functional tests and high-quality filtering, providing a recent methodological reference for culturally specific evaluation and annotation documentation. [5]
- ViHateOff is a 2026 span-detection model that augments PhoBERT-large with a hate-speech dictionary derived from ViHOS and reports F1 of 0.8693 on all-span and 0.8709 on multiple-span subsets; it is relevant only for distinguishing sentence-level direction/severity annotation from lexical rationale extraction. [6]
- The most useful recent additions to the paper's core Related Work are ViHateT5, the final ViTHSD journal version, ViRDC, and SEAHateCheck; BamiBERT belongs in the benchmark/future-work discussion, while ViHateOff is a secondary span-level comparison. [1][2][3][4][5][6]
- Across the 2024--2026 sources reviewed, no dataset was found that assigns every Vietnamese comment two simultaneous North-targeted and South-targeted severity labels, supporting only a cautious “to the best of our knowledge” novelty statement. [1][2][3][5]

## Deep Read Notes

### Source [1]: ViHateT5 (ACL Findings 2024)
Key data: VOZ-HSD contains 10.8M automatically labeled VOZ Forum comments, including more than 500K labeled harmful; a ViSoBERT classifier trained from a binarized ViHSD labels the raw corpus; the resulting T5 model is evaluated on ViHSD, ViCTSD, and ViHOS.
Key insight: Recent Vietnamese HSD progress emphasizes domain-specific pre-training and unified task modeling, so the new paper's contribution should be the human-annotated direction-aware resource rather than claiming model novelty from PhoBERT fine-tuning.
Useful for: Related work on recent Vietnamese models, motivation for social-media language, and future baselines.

### Source [2]: ViTHSD (2025 journal version / arXiv v3)
Key data: 10,000 comments; five targets (individual, group, religion/creed, race/ethnicity, politics); per-target states include target absence and clean/offensive/hate levels; mean pairwise Cohen's kappa is 0.45 for target-with-level labels and 0.51 for target-only labels.
Key insight: It is the strongest prior art against a broad multi-target novelty claim and also validates reporting the mean over all pairwise Cohen kappas when multiple annotators label a shared sample.
Useful for: Closest dataset comparison, annotation-method comparison, and multi-head benchmark design.

### Source [5]: SEAHateCheck (TALLIP accepted, 2026)
Key data: Vietnamese is among four low-resource languages receiving localized tests; the framework covers 22 functional tests, uses local experts/native speakers, and reports Fleiss' kappa 0.85 on validated gold cases; tests include slang, implicit hate, non-hateful contrasts, quoted hate, and counter-speech.
Key insight: Modern evaluation is moving from a single random test score toward functional diagnostics that reveal shortcut learning and culturally specific failures.
Useful for: Motivating a small challenge set or qualitative error taxonomy for regional slurs, implicit prejudice, target confusion, and counter-speech.

### Source [4]: BamiBERT (2026 preprint)
Key data: trained from scratch on 129GB for 20 epochs; maximum context 2,048; raw-text input without external segmentation; best on 11 of 15 metrics and second on three across eight reported Vietnamese benchmarks.
Key insight: The paper is recent but not peer-reviewed and does not test hate speech, so it should be cited cautiously as a potential contemporary encoder rather than evidence about regional-hate performance.
Useful for: Future-work paragraph and optional additional baseline if compute permits.

## Gaps

- No peer-reviewed 2024--2026 source was found with the exact combination of Vietnamese North/South target direction and NON_HATE/PREJUDICIAL/HOSTILE severity; absence in this search is not proof of absolute firstness.
- BamiBERT and SEAHateCheck appeared in 2026 and should be labeled by status: BamiBERT is an arXiv preprint, whereas SEAHateCheck states TALLIP acceptance but its final bibliographic volume/pages were not available on the retrieved page.
- ViHateT5's 10.8M VOZ-HSD labels are machine-generated, so it is not evidence that scale replaces careful human annotation or agreement reporting.
- ViHateOff improves span extraction on ViHOS but does not address target direction or severity; giving it too much space would dilute the new paper's central dataset contribution.
- Counter-claim: reviewers may still view North and South as two narrower instances of ViTHSD's generic group/race targets unless the paper demonstrates target-confusion errors, directional asymmetry, dual-target cases, and analysis unavailable from a single global regional-discrimination label.
