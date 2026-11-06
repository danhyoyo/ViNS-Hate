---
task_id: d
role: Provided-Paper Evidence Extractor
status: complete
sources_found: 5
---

## Sources

[1] Huynh, An-Nghiep; Do, Thanh-Dat; Do, Trong-Hop — A Big Data-empowered System for Real-time Detection of Regional Discriminatory Comments on Vietnamese Social Media | https://arxiv.org/abs/2411.02587 | Source-Type: academic | As Of: 2024-10 | Authority: 8/10
[2] Luu, Son T.; Nguyen, Kiet Van; Nguyen, Ngan Luu-Thuy — A Large-scale Dataset for Hate Speech Detection on Vietnamese Social Media Texts | https://doi.org/10.1007/978-3-030-79457-6_35 | Source-Type: academic | As Of: 2021-07 | Authority: 9/10
[3] Hoang, Phu Gia; Luu, Canh Duc; Tran, Khanh Quoc; Nguyen, Kiet Van; Nguyen, Ngan Luu-Thuy — ViHOS: Hate Speech Spans Detection for Vietnamese | https://aclanthology.org/2023.eacl-main.47/ | Source-Type: academic | As Of: 2023-05 | Authority: 10/10
[4] Nguyen, Quoc-Nam; Phan, Thang Chau; Nguyen, Duc-Vu; Nguyen, Kiet Van — ViSoBERT: A Pre-Trained Language Model for Vietnamese Social Media Text Processing | https://aclanthology.org/2023.emnlp-main.315/ | Source-Type: academic | As Of: 2023-12 | Authority: 10/10
[5] Vo, Cuong Nhat; Huynh, Khanh Bao; Luu, Son T.; Do, Trong-Hop — ViTHSD: Exploiting Hatred by Targets for Hate Speech Detection on Vietnamese Social Media Texts | https://doi.org/10.1007/s42001-024-00348-6 | Source-Type: academic | As Of: 2025-02 | Authority: 9/10

## Findings

- ViRDC is the direct prior work on Vietnamese regional discrimination: the paper describes about 17,000 social-media comments labeled `Other`, `Discrimination`, or `Supportive`, but collapses all attacked regions and intensities into one discrimination class and does not report a standard inter-annotator agreement statistic. [1]
- ViRDC benchmarks Random Forest, multinomial logistic regression, multinomial Naive Bayes, XLM-R, PhoBERT, and multilingual BERT; its reported best result is Random Forest with 0.9700 macro-F1, making it impossible to claim the first dataset or first benchmark for Vietnamese regional-discrimination detection. [1]
- ViHSD contains 33,400 Facebook/YouTube comments labeled `CLEAN`, `OFFENSIVE`, or `HATE`; two annotators label the full data, a third labels disagreements, a fourth is used when all three disagree, and a 202-comment four-rater audit reports mean Cohen's kappa of 0.52. [2]
- ViHSD uses a 70/10/20 train/dev/test split and reports a best test macro-F1 of 62.69% from multilingual BERT cased, while its error analysis attributes many failures to slang, abbreviations, teencode, figurative meaning, and irregular spelling. [2]
- ViHOS contains 11,056 comments and 26,467 annotated hate/offensive spans, uses a three-phase six-annotator protocol, obtains F1=0.86 and Cohen's kappa=0.72 on a 600-comment ground-truth set, and reports XLM-R Large as the best full-data baseline with F1=0.7770 averaged over more than ten runs. [3]
- ViSoBERT is a 97M-parameter Vietnamese social-media model pre-trained on 1GB of Facebook, TikTok, and YouTube text collected over 2016–2022; without task-specific preprocessing it reaches 68.77% macro-F1 on ViHSD, outperforming the compared PhoBERT and multilingual/social-media PLMs in that setup. [4]
- ViTHSD is the closest task-formulation precedent: 10,000 comments receive four states (`NORMAL`, `CLEAN`, `OFFENSIVE`, `HATE`) for each of five targets (individual, group, religion/creed, race/ethnicity, politics); mean pairwise Cohen's kappa is 0.45 with levels and 0.51 without levels. [5]
- ViTHSD's best model, XLM-R combined with Bi-GRU-LSTM-CNN, reports macro-F1 of 72.01% for target detection but only 51.74% for target-plus-level detection, demonstrating that jointly predicting target and severity is substantially harder than target identification alone. [5]
- Across these five papers, no resource uses exactly two simultaneous regional directions (`north_hate` and `south_hate`) with `NON_HATE/PREJUDICIAL/HOSTILE`; a defensible contribution is therefore direction-specific North–South severity annotation, not the general concepts of Vietnamese hate speech, regional discrimination, target-aware labeling, adjudication, or multi-model benchmarking. [1][2][5]
- The recurring limitations in the supplied literature—class/target imbalance, context-free comments, noisy Vietnamese social-media language, subjective severity boundaries, and potential misuse of released abusive content—must be addressed explicitly through per-class metrics, transparent collection/annotation documentation, multiple-run evaluation, anonymization, licensing, and an ethics/limitations section. [2][3][4][5]

## Deep Read Notes

### Source [1]: ViRDC
Key data: Approximately 17,000 self-collected comments; labels `Other/Discrimination/Supportive`; preprocessing includes lowercasing, URL/tag/icon removal, Unicode/accent normalization, teencode expansion, and VnCoreNLP word segmentation; reported macro-F1 values are RF 0.9700, logistic regression 0.9100, NB 0.8300, XLM-R 0.8902, PhoBERT 0.9187, and mBERT 0.9154.
Key insight: This paper forecloses any claim of being the first Vietnamese regional-discrimination dataset or benchmark, but its global label does not identify whether Northerners or Southerners are attacked and does not distinguish prejudice from hostility.
Useful for: Direct related-work comparison, dataset table, motivation for direction-aware labels, and matching classical/Transformer baselines.

### Source [2]: ViHSD
Key data: 33,400 comments; 27,624 CLEAN, 2,262 OFFENSIVE, and 3,514 HATE; split 70/10/20; two initial annotators plus third/fourth escalation; pairwise kappas on 202 items range 0.46–0.65, average 0.52; best macro-F1 62.69%.
Key insight: The proposed annotation routing is established prior art; publishable quality comes from explicit guidelines, pre-adjudication reliability, disagreement analysis, and transparent adjudication rather than the routing procedure itself.
Useful for: Annotation-method section, kappa comparison, label-definition discussion, and social-media error taxonomy.

### Source [3]: ViHOS
Key data: 11,056 comments (8,844/1,106/1,106), 26,467 spans, six trained undergraduate annotators, 600-comment adjudicated ground truth with F1=0.86 and kappa=0.72, public research-only release, and XLM-R Large F1=0.7770 over 10+ runs.
Key insight: ViHOS is a strong model for how to report annotator qualifications, staged training, agreement thresholds, compensation, privacy, misuse risks, multiple seeds, and error categories; its granularity is lexical-span rather than target-directional.
Useful for: Annotation protocol figure, ethics section, dataset statement, reproducibility checklist, and limitations.

### Source [4]: ViSoBERT
Key data: 1GB uncompressed pretraining data from verified Facebook/TikTok/YouTube accounts collected in 2016–2022; XLM-R-style 97M-parameter architecture, 15K custom SentencePiece vocabulary, raw-text operation, and ViHSD macro-F1 68.77%.
Key insight: A Vietnamese social-media-specific encoder is a highly relevant modern baseline because it directly models emojis, teencode, missing diacritics, and informal vocabulary; relying only on unsegmented PhoBERT underuses the available modeling literature.
Useful for: Model selection, experimental discussion, and a future benchmark revision adding ViSoBERT.

### Source [5]: ViTHSD
Key data: 10,000 comments derived from ViHSD; five target heads; four states per head; approximately 70/10/20 split; mean pairwise kappa 0.45 with severity and 0.51 without; best macro-F1 72.01% target-only and 51.74% target-plus-level.
Key insight: ViTHSD already establishes Vietnamese target-conditioned severity modeling and even averages pairwise Cohen's kappas across annotator pairs, so novelty must be tied specifically to explicit North-versus-South direction and the prejudice/hostility boundary.
Useful for: Closest-method comparison, kappa reporting precedent, multi-head task formulation, and benchmark difficulty framing.

## Gaps

- The five supplied papers alone cannot prove absolute firstness; the exact North/South two-head claim still requires a recent Scholar/Scopus-style search and should be phrased “to the best of our knowledge.”
- ViRDC describes approximately 17,000 collected comments but its accessible repository/documentation has changed over time; comparisons should cite a pinned dataset version and avoid presenting its scale as unambiguous.
- ViRDC gives only a high-level statement about relabeling low-consensus cases and does not provide standard IAA, annotator demographics, disagreement rate, or a reproducible split description.
- ViTHSD's five broad targets do not explicitly reveal whether Vietnamese regional identity was included inside race/ethnicity or group annotations; direct inspection of released examples is needed before making a stronger exclusion claim.
- The supplied papers do not provide evidence about the user's collection platforms, time window, queries, sampling frame, annotator compensation/demographics, consent, or release license; these must remain placeholders until supplied.
- Alternative interpretation: two North/South heads may be seen as a narrow relabeling of ViRDC plus ViTHSD unless the paper demonstrates target-direction confusion, directional asymmetry, dual-target cases, and benefits over a simpler single target-plus-severity representation.
