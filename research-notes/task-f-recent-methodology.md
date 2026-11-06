---
task_id: f
role: Recent Dataset and Benchmark Methodology Specialist
status: complete
sources_found: 7
---

## Sources

[1] Analyzing Dataset Annotation Quality Management in the Wild | https://aclanthology.org/2024.cl-3.1/ | Source-Type: academic | Accessibility: public | As Of: 2024-09 | Authority: 10/10
[2] Web(er) of Hate: A Survey on How Hate Speech Is Typed | https://aclanthology.org/2025.woah-1.9/ | Source-Type: academic | Accessibility: public | As Of: 2025-08 | Authority: 9/10
[3] When the Majority is Wrong: Modeling Annotator Disagreement for Subjective Tasks | https://aclanthology.org/2023.emnlp-main.415/ | Source-Type: academic | Accessibility: public | As Of: 2023-12 | Authority: 10/10
[4] Enhancing Data Quality through Simple De-duplication: Navigating Responsible Computational Social Science Research | https://aclanthology.org/2024.emnlp-main.694/ | Source-Type: academic | Accessibility: public | As Of: 2024-11 | Authority: 10/10
[5] ViSoBERT: A Pre-Trained Language Model for Vietnamese Social Media Text Processing | https://aclanthology.org/2023.emnlp-main.315/ | Source-Type: academic | Accessibility: public | As Of: 2023-12 | Authority: 10/10
[6] On Efficient and Statistical Quality Estimation for Data Annotation | https://aclanthology.org/2024.acl-long.837/ | Source-Type: academic | Accessibility: public | As Of: 2024-08 | Authority: 10/10
[7] ACL Ethics Committee — Responsible Research Checklist for Researchers | https://ethics.aclweb.org/roles/researchers/ | Source-Type: official | Accessibility: public | As Of: 2026-11 | Authority: 10/10

## Findings

- A review of 591 text-dataset papers found that 30% used subpar annotation quality management and identified recurring errors in inter-annotator agreement, error-rate estimation, annotator reporting, and adjudication; the new paper should therefore report its pilot/training process, the five-annotator pool, pre-adjudication pairwise agreement, missing-label handling, and adjudication rules explicitly. [1]
- A 2025 survey of 135 hate-speech datasets found that most assign two annotators per instance, 48 use majority voting, 27 use additional annotators, and eight use moderation meetings, confirming that the proposed two-independent-annotator plus third-adjudicator workflow is defensible but not itself novel. [2]
- The same survey reports that 78 of 135 datasets omit annotator demographics and argues that location and lived experience matter; because the task concerns North--South identity, the paper should disclose annotators' regional backgrounds in aggregate where ethically permissible and discuss possible positional bias. [2]
- Majority aggregation in subjective hate-speech tasks can erase systematic differences linked to target-group membership, so the corpus should retain raw independent annotations and disagreement/adjudication indicators even if the benchmark uses a single prescriptive gold label. [3]
- An audit of 20 social-media datasets shows that duplicate and near-duplicate texts can produce inconsistent labels, train--test leakage, altered rankings, and inflated effectiveness claims; canonicalized and semantic duplicate checks should occur before splitting. [4]
- ViSoBERT is the first monolingual pretrained model developed specifically for Vietnamese social-media text and was evaluated on hate-speech classification and hate-span detection; it is a directly relevant modern benchmark that should be added to the current PhoBERT-centered experiments or listed as an explicitly deferred baseline. [5]
- Statistical quality estimates based on small or unjustified audit samples can be imprecise; the paper must clearly describe that Cohen's kappa was evaluated on a shared 300-comment sample, state the sampling procedure, and avoid treating the mean of ten pairwise kappas as a single multi-rater coefficient. [6]
- Current ACL responsible-research guidance requires dataset coverage/statistics, licenses, privacy and anonymization, full annotator instructions, recruitment/consent/compensation and demographics, limitations/risks, hyperparameters/search strategy, compute, software versions, and result variability; these items should appear in the Dataset, Ethics, Experimental Setup, and Limitations sections. [7]
- The strongest use of recent methodology citations is to justify transparent decisions and limitations, not to imply that moderate kappa proves correctness: the observed mean pairwise kappas near 0.50 quantify consistency under the chosen taxonomy but do not validate the social or normative definition of PREJUDICIAL versus HOSTILE. [1][2][3]

## Deep Read Notes

### Source [1]: Analyzing Dataset Annotation Quality Management in the Wild
Key data: Computational Linguistics 2024 audit of 591 dataset papers; 30% rated subpar; recurrent issues include inadequate IAA interpretation, small agreement samples, incomplete reporting of annotator management, adjudication, and validation.
Key insight: Agreement is one component of a quality-management process, not a stand-alone certificate of label correctness.
Useful for: Annotation Protocol, Inter-Annotator Agreement, Limitations.

### Source [2]: Web(er) of Hate
Key data: 135 hate-speech datasets across 36 languages; most use two annotators per item; disagreement resolution includes majority vote (48), additional annotators (27), moderation meetings (8), and discarding disagreement (9); 78 omit demographics.
Key insight: The paper must state whether its gold labels are prescriptive moderation labels or a descriptive record of social judgments, and document the assumptions encoded by the North/South severity taxonomy.
Useful for: Related Work, Annotation Design, positionality and taxonomy caveats.

### Source [4]: Enhancing Data Quality through Simple De-duplication
Key data: EMNLP 2024 audit of 20 widely used social-media datasets; duplication can cause label conflicts, train--test leakage, model-rank changes, and overestimated real-world performance.
Key insight: Exact case-sensitive deduplication is insufficient when models lowercase text; normalized and near-duplicate groups must be kept within a single split.
Useful for: Data Cleaning, Split Construction, Limitations.

### Source [5]: ViSoBERT
Key data: EMNLP 2023 Vietnamese social-media PLM using an XLM-R architecture; evaluated on emotion, hate-speech detection, sentiment, spam-review detection, and hate-speech span detection, with fewer parameters than several general-domain alternatives.
Key insight: A benchmark paper on Vietnamese social-media hate that includes PhoBERT but omits ViSoBERT needs either to add it or explicitly frame the current results as initial baselines rather than comprehensive modern coverage.
Useful for: Related Work and Benchmark Models.

## Gaps

- No recent source can retrospectively supply missing project metadata such as platform-specific collection dates, queries, consent/ethics review, annotator compensation, or regional demographics; these must come from the authors and remain placeholders in the first draft.
- Cohen's kappa on the 300-item audit is pairwise while five annotators participated; a multi-rater coefficient such as Krippendorff's alpha or Fleiss' kappa would be a useful robustness analysis but is not yet available.
- ViSoBERT is strongly relevant, but adding its citation without running it weakens any claim that the five-model benchmark is comprehensive; the draft should label it as future/required evaluation if results are unavailable.
- The current benchmark uses one split and one seed for neural models, so recent reporting guidance supports presenting the existing scores as preliminary until multiple seeds, uncertainty intervals, and leakage-corrected splits are available.
- Alternative interpretation: preserving disagreement may be scientifically preferable for descriptive regional-attitude research, whereas adjudicated single labels are appropriate for a prescriptive moderation benchmark; the paper must choose and state its intended epistemic stance.

## END
