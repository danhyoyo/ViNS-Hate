---
task_id: b
role: Social Computing and Regional Hate Speech Specialist
status: complete
sources_found: 8
---

## Sources

[1] A Big Data-empowered System for Real-time Detection of Regional Discriminatory Comments on Vietnamese Social Media | https://arxiv.org/abs/2411.02587 | Source-Type: academic | As Of: 2024-10 | Authority: 8/10
[2] Vietnamese-Regional-Discrimination-Detection (ViRDC repository) | https://github.com/anhuynh219/Vietnamese-Regional-Discrimination-Detection | Source-Type: official | As Of: 2026-11 | Authority: 7/10
[3] ViTHSD: Exploiting Hatred by Targets for Hate Speech Detection on Vietnamese Social Media Texts | https://arxiv.org/abs/2404.19252 | Source-Type: academic | As Of: 2024-04 | Authority: 8/10
[4] Multilingual and Multi-Aspect Hate Speech Analysis | https://aclanthology.org/D19-1474/ | Source-Type: academic | As Of: 2019-11 | Authority: 9/10
[5] Korean Online Hate Speech Dataset for Multilabel Classification: How Can Social Science Improve Dataset on Hate Speech? | https://arxiv.org/abs/2204.03262 | Source-Type: academic | As Of: 2022-04 | Authority: 7/10
[6] HateBR: A Large Expert Annotated Corpus of Brazilian Instagram Comments for Offensive Language and Hate Speech Detection | https://arxiv.org/abs/2103.14972 | Source-Type: academic | As Of: 2021-03 | Authority: 8/10
[7] The salience of the Northern and Southern identity in Vietnam | https://onlinelibrary.wiley.com/doi/abs/10.1111/aspp.12567 | Source-Type: academic | As Of: 2021-02 | Authority: 9/10
[8] Multi-label Hate Speech and Abusive Language Detection in Indonesian Twitter | https://aclanthology.org/W19-3506/ | Source-Type: academic | As Of: 2019-08 | Authority: 9/10

## Findings

- The contribution cannot be framed as the first Vietnamese regional-discrimination dataset: ViRDC already targets this problem with regional social-media comments, three classes (Other, Discrimination, Supportive), and ML/Transformer benchmarks. [1][2]
- ViRDC does not expose the same task formulation as the proposed corpus: it collapses all regional discrimination into one class rather than assigning separate North-target and South-target severity labels, so a defensible novelty claim is a direction-aware, target-specific North/South annotation scheme rather than first regional-hate detection. [1][2]
- ViRDC's documentation is internally inconsistent about scale—the paper says roughly 17,000 collected comments while the current repository README says 4,000 samples—creating an opportunity for a better documented, versioned, reproducible data statement, but also requiring the authors to compare against the downloadable ViRDC release directly. [1][2]
- The contribution also cannot be framed as the first Vietnamese target-aware hate-speech dataset: ViTHSD contains about 10,000 comments with five targets (individual, group, religion/creed, race/ethnicity, politics) and per-target levels, using a multi-label/multi-head task formulation. [3]
- ViTHSD reports only moderate agreement for target-with-level annotation (average Cohen's kappa about 0.45), supporting the importance of reporting agreement before adjudication and disagreement/adjudication rates for the proposed subjective three-level labels. [3]
- Fine-grained hostility or severity is not globally novel: the multilingual MIMa corpus labels directness, multiple hostility types, target attributes and target groups, while HateBR separately annotates three offensiveness levels and nine hate groups. [4][6]
- Regionalism is an established target category outside Vietnam: the Korean multilabel corpus includes Regionalism among seven hate categories and reports 35K total examples with Krippendorff's alpha of 0.713. [5]
- Southeast Asian literature already treats hate target, category and level as a multi-label problem: the Indonesian Twitter work explicitly predicts all three and benchmarks SVM, Naive Bayes and Random Forest variants. [8]
- The most credible distinctive contribution is therefore a Vietnamese corpus that jointly distinguishes who is attacked (North versus South) and how severely (NON_HATE/PREJUDICIAL/HOSTILE), enabling directional asymmetry, co-occurrence and per-target error analysis that a single ViRDC discrimination label cannot provide. [1][3][4]
- A substantive motivation for separate directional targets exists: survey and focus-group research finds North–South identity in Vietnam to be asymmetric but less salient than commonly assumed, so the paper should test asymmetry empirically without generalizing corpus frequencies into population-level prevalence. [7]

## Deep Read Notes

### Source [1]: ViRDC paper
Key data: The paper describes about 17,000 self-collected social-media comments, labels Other/Discrimination/Supportive, and benchmarks Random Forest, multinomial logistic regression, multinomial NB, PhoBERT, XLM-R and multilingual BERT; reported macro-F1 ranges from 0.83 to 0.97.
Key insight: This is direct prior art for Vietnamese regional-discrimination detection, but its single discrimination label does not identify the attacked region or severity.
Useful for: Replacing an invalid "first dataset" claim with a precise direction-aware and severity-aware novelty claim.

### Source [3]: ViTHSD
Key data: 10,000 comments, five target heads, four states including absence/normal and Clean/Offensive/Hate; target-with-level Cohen-kappa average is 0.45.
Key insight: It is the closest methodological prior art for a multi-target, per-target severity formulation in Vietnamese, even though North and South are not separate targets.
Useful for: Task formulation, annotation comparison, multi-task baselines and IAA expectations.

### Source [4]: MIMa multilingual multi-aspect corpus
Key data: 5,647 English, 4,014 French and 3,353 Arabic tweets; each final tweet assigned to five annotators with majority voting; annotations include directness, hostility, target attribute, target group and annotator reaction; IAA is low (Krippendorff alpha 0.153/0.244/0.202).
Key insight: Fine-grained hostility and target structure are established but highly subjective, so transparent guidelines and disagreement reporting are contributions to dataset quality, not evidence of conceptual firstness.
Useful for: Positioning PREJUDICIAL versus HOSTILE and justifying rigorous annotation analysis.

### Source [7]: North–South identity in Vietnam
Key data: Based on Asian Barometer survey data and 14 focus groups; reports asymmetric ingroup bias, with stronger ingroup favoritism/outgroup discrimination among southerners, while warning that North–South identity salience is limited and crosscut by other identities.
Key insight: The two directional labels can support a socially meaningful asymmetry analysis, but social-media sample frequencies cannot be treated as nationally representative prevalence.
Useful for: Social-science motivation, research questions and limitations.

## Gaps

- No reviewed source was found with the exact combination of Vietnamese comments, two simultaneous target heads specifically for Northern and Southern people, and the three levels NON_HATE/PREJUDICIAL/HOSTILE; this supports a cautious "to our knowledge, first direction-aware North/South severity corpus" claim only after a final search of Google Scholar/Scopus and direct inspection of ViRDC files.
- The proposed corpus excludes Central Vietnam while ViRDC examples cover Northern, Central and Southern identities; the paper must justify this scope or rename the task narrowly as North–South regional hate rather than Vietnamese regional discrimination generally.
- ViRDC's paper/repository sample-count discrepancy and unclear mapping in its current README mean comparisons should be made against a pinned release/commit, not only prose descriptions.
- Alternative interpretation: separate North and South heads may be viewed as merely a narrower relabeling of regional discrimination unless the paper demonstrates phenomena unavailable to ViRDC, such as comments targeting both groups, target-direction confusion, asymmetrical class distributions, and per-direction model behavior.
