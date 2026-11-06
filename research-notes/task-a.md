---
task_id: a
role: Vietnamese NLP Dataset Specialist
status: complete
sources_found: 7
---

## Sources

[1] HSD Shared Task in VLSP Campaign 2019: Hate Speech Detection for Social Good | https://arxiv.org/abs/2007.06493 | Source-Type: academic | As Of: 2020-07 | Authority: 8/10
[2] A Large-scale Dataset for Hate Speech Detection on Vietnamese Social Media Texts | https://arxiv.org/abs/2103.11528 | Source-Type: academic | As Of: 2021-03 | Authority: 9/10
[3] Constructive and Toxic Speech Detection for Open-domain Social Media Comments in Vietnamese | https://arxiv.org/abs/2103.10069 | Source-Type: academic | As Of: 2021-03 | Authority: 8/10
[4] ViHOS: Hate Speech Spans Detection for Vietnamese | https://aclanthology.org/2023.eacl-main.47/ | Source-Type: academic | As Of: 2023-05 | Authority: 10/10
[5] ViTHSD: Exploiting Hatred by Targets for Hate Speech Detection on Vietnamese Social Media Texts | https://arxiv.org/abs/2404.19252 | Source-Type: academic | As Of: 2024-04 | Authority: 9/10
[6] A Big Data-empowered System for Real-time Detection of Regional Discriminatory Comments on Vietnamese Social Media | https://arxiv.org/abs/2411.02587 | Source-Type: academic | As Of: 2024-10 | Authority: 8/10
[7] VIHATET5: Enhancing Hate Speech Detection in Vietnamese by T5-Based Pre-Training | https://aclanthology.org/2024.findings-acl.355/ | Source-Type: academic | As Of: 2024-08 | Authority: 10/10

## Findings

- HSD-VLSP 2019 contains 25,431 Facebook items and defines a single three-class comment-level task (CLEAN, OFFENSIVE, HATE), with no region-specific target outputs. [1]
- ViHSD contains 33,400 Facebook/YouTube comments with the same single-label CLEAN/OFFENSIVE/HATE taxonomy; its annotation workflow assigns two independent annotators, sends disagreements to a third, invokes a fourth only if all three disagree, and reports Cohen's kappa 0.52 on a 202-comment audit. [2]
- UIT-ViCTSD contains 10,000 VnExpress comments for two separate constructs (constructiveness and toxicity), uses three annotators per comment and iterative guideline refinement, but does not represent North-versus-South targets or graded regional hostility. [3]
- ViHOS contains 11,056 Facebook/YouTube comments and 26,476 human-annotated hate/offensive spans, moving the task from sentence classification to span extraction rather than distinguishing regional targets or severity by direction. [4]
- ViTHSD contains 10,000 comments annotated independently across five broad targets (individual, group, religion/creed, race/ethnicity, politics) and graded levels; it reports kappa 0.45 for target-with-level annotation, making it the closest prior design to a multi-output, multi-level North/South dataset, though it does not expose North and South as separate target axes. [5]
- ViRDC is the direct thematic predecessor: approximately 17,000 Vietnamese social-media comments labeled Other, Discrimination, or Supportive, with examples targeting Northerners, Southerners, and people from Thanh Hoa; however, it uses one global regional-discrimination label rather than separate North-target and South-target severity labels. [6]
- ViRDC benchmarks Random Forest, multinomial logistic regression, multinomial Naive Bayes, XLM-R, PhoBERT, and multilingual BERT, reports macro-F1 as the main metric, and achieves 0.9700 macro-F1 with Random Forest; therefore a new paper cannot claim the first Vietnamese regional-discrimination dataset or the first benchmark for that problem. [6]
- The 2024 VIHATET5 study treats ViHSD, ViCTSD, and ViHOS as established Vietnamese hate/toxic benchmarks and uses macro-F1 as the primary metric, supporting macro-F1 rather than accuracy as the central comparison measure for imbalanced labels. [7]
- A defensible novelty claim, conditional on a broader search finding no closer resource, is the first direction-aware Vietnamese regional hate corpus that assigns each comment two target-specific outputs (hate toward North and hate toward South) on an ordinal three-level scale; the annotation adjudication procedure itself is not novel because ViHSD already used the same two-annotator-plus-third-adjudicator structure. [2][5][6]
- The proposed corpus is smaller than ViRDC (4,423 versus about 17,000) and ViTHSD (10,000), so its scientific value must come from finer target semantics, released guidelines/disagreement data, reliability statistics, and rigorous evaluation rather than scale. [5][6]

## Deep Read Notes

### Source [2]: A Large-scale Dataset for Hate Speech Detection on Vietnamese Social Media Texts
Key data: 33,400 comments, 7:1:2 train/dev/test split, labels CLEAN/OFFENSIVE/HATE, kappa 0.52; two annotators label all samples, a third handles disagreement, and a fourth is used if all three disagree.
Key insight: The user's described adjudication workflow is a known Vietnamese hate-speech annotation design and cannot independently support novelty.
Useful for: Positioning annotation method, requiring IAA reporting, and avoiding an overclaim.

### Source [5]: ViTHSD: Exploiting Hatred by Targets
Key data: 10,000 comments; five target axes; target-specific levels; overall target-with-level Cohen-kappa average 0.45; best reported macro-F1 is 72.01% for target-only and 51.74% for target-plus-level.
Key insight: ViTHSD already establishes Vietnamese multi-target, multi-level hate detection, so novelty must be tied specifically to directional regional targets and regional prejudice/hostility semantics.
Useful for: Closest methodological comparison and a required baseline/reference.

### Source [6]: A Big Data-empowered System for Real-time Detection of Regional Discriminatory Comments
Key data: about 17,000 social-media comments; labels Other/Discrimination/Supportive; six benchmark models; reported macro-F1 values include Random Forest 0.9700 and PhoBERT 0.9187.
Key insight: ViRDC invalidates any claim of being the first Vietnamese regional-discrimination dataset/benchmark, but leaves room for a direction-aware and severity-aware resource.
Useful for: Direct related work, contribution wording, and experimental comparison.

### Source [4]: ViHOS
Key data: 11,056 comments, 26,476 annotated spans, 8,844/1,106/1,106 train/dev/test splits, collected from Facebook and YouTube.
Key insight: Vietnamese hate-speech research already includes fine-grained span supervision, so a new dataset should explicitly distinguish target-direction granularity from lexical-span granularity.
Useful for: Taxonomy comparison and scope boundaries.

## Gaps

- No peer-reviewed/public dataset was found that exposes exactly two independent North-hate and South-hate axes with NON_HATE/PREJUDICIAL/HOSTILE labels, but this is a qualified literature-search result rather than proof of absolute global firstness.
- The ViRDC paper does not report a standard IAA statistic or sufficiently detailed annotator demographics in the accessible text, which limits direct quality comparison.
- The names PREJUDICIAL and HOSTILE need operational definitions and evidence that annotators can reliably distinguish them; without per-target kappa/alpha and disagreement rates, the claimed extra granularity may be viewed as subjective label splitting.
- Alternative interpretation: because ViRDC already captures regional discrimination and ViTHSD already captures multi-target graded hate, reviewers may view the new dataset as a recombination of known ideas unless direction-aware use cases, paired-label phenomena, and empirical difficulty are demonstrated clearly.
