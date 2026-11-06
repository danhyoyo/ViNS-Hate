# Paper Citation Registry

AS_OF: 2026-11-05  
Scope: sources cited in `north_south_regional_hate_paper.tex`  
Accessibility: all public; five core papers were also supplied by the user as PDFs.

## Approved academic sources

1. Vu et al. (2020), HSD Shared Task in VLSP Campaign 2019 — https://arxiv.org/abs/2007.06493 — academic — authority 8/10.
2. Luu et al. (2021), A Large-scale Dataset for Hate Speech Detection on Vietnamese Social Media Texts — https://doi.org/10.1007/978-3-030-79457-6_35 — academic — authority 9/10.
3. Nguyen et al. (2021), Constructive and Toxic Speech Detection for Open-domain Social Media Comments in Vietnamese — https://doi.org/10.1007/978-3-030-79457-6_49 — academic — authority 8/10.
4. Nguyen and Nguyen (2020), PhoBERT — https://aclanthology.org/2020.findings-emnlp.92/ — academic — authority 10/10.
5. Hoang et al. (2023), ViHOS — https://aclanthology.org/2023.eacl-main.47/ — academic — authority 10/10.
6. Nguyen et al. (2023), ViSoBERT — https://aclanthology.org/2023.emnlp-main.315/ — academic — authority 10/10.
7. Huynh et al. (2024), ViRDC — https://arxiv.org/abs/2411.02587 — academic — authority 8/10.
8. Vo et al. (2025), ViTHSD — https://doi.org/10.1007/s42001-024-00348-6 — academic — authority 9/10.
9. Nguyen (2024), ViHateT5 — https://aclanthology.org/2024.findings-acl.355/ — academic — authority 10/10.
10. Ng et al. (2026), SEAHateCheck — https://arxiv.org/abs/2603.16070 — academic, accepted manuscript — authority 9/10.
11. Klie et al. (2024), Analyzing Dataset Annotation Quality Management in the Wild — https://aclanthology.org/2024.cl-3.1/ — academic — authority 10/10.
12. Wang et al. (2025), Web(er) of Hate — https://aclanthology.org/2025.woah-1.9/ — academic — authority 9/10.
13. Fleisig et al. (2023), When the Majority is Wrong — https://aclanthology.org/2023.emnlp-main.415/ — academic — authority 10/10.
14. Mu et al. (2024), Enhancing Data Quality through Simple De-duplication — https://aclanthology.org/2024.emnlp-main.694/ — academic — authority 10/10.
15. Bender and Friedman (2018), Data Statements for NLP — https://aclanthology.org/Q18-1041/ — academic — authority 10/10.
16. Dodge et al. (2019), Show Your Work — https://aclanthology.org/D19-1224/ — academic — authority 10/10.

## Internal primary evidence

- `SEG301_Prj_annotations_merged.ipynb` and `model_comparison_multitask.csv` — user-provided experiment artifacts.
- `data/processed/{train,val,test}.csv` — user-provided dataset splits.
- `Kappa/cohen_kappa_results.xlsx` — formula-verified pairwise Cohen's kappa results.
- `VRD15K_5_Annotators_Protocol.md` — user-provided annotation protocol.

## Dropped or deferred

- BamiBERT (2026 preprint): deferred from the core manuscript because it does not yet report hate-speech evaluation; may be added as an optional future baseline.
- ViHateOff (2026): deferred because it is a span-detection model and does not directly address target direction or severity.
- Generic blogs, search-result summaries, and aggregator pages: dropped because primary papers were available.

## Governance summary

- 16/16 bibliography entries are primary academic sources.
- Six sources are from 2024--2026; one accepted 2026 paper is explicitly marked by status.
- Public domains include ACL Anthology, Springer/DOI, and arXiv; user-provided PDFs were used as exclusive copies of public third-party papers.
- Novelty is phrased as `to the best of our knowledge`; no absolute-first claim is treated as proven.
