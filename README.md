# ViNS-Hate

ViNS-Hate is a Vietnamese social-media dataset and benchmark for detecting regional prejudice and hostility directed toward Northerners and Southerners. Each comment receives two independent target-specific labels:

- `NON_HATE`: no prejudice or hostility toward the specified target;
- `PREJUDICIAL`: a negative regional stereotype or generalization without direct abusive hostility;
- `HOSTILE`: direct insults, slurs used as attacks, dehumanization, exclusion, threats, or wishes of harm.

The corpus contains 4,423 comments collected from social-media videos posted between 2024 and 2026. The released split contains 3,095 training, 664 validation, and 664 test comments. The benchmark compares TF--IDF classifiers, a multi-task BiLSTM with attention, and PhoBERT.

## Repository contents

```text
ViNS-Hate/
├── data/processed/                 # Frozen train/validation/test CSV files
├── figures/                         # Paper figures, including annotation workflow
├── Kappa/                           # Annotation files and Cohen's kappa scripts/results
├── research-notes/                  # Literature and review notes
├── SEG301_Prj_annotations_merged.ipynb  # Main preprocessing/training/evaluation notebook
├── run_three_seeds.py               # Reproduces seeds 42, 43, and 44 on the fixed split
├── generate_paper_figures.ps1       # Regenerates the paper figures on Windows PowerShell
├── model_comparison_multitask.csv   # Compact benchmark summary
├── results_three_seeds/seed_*.csv   # Compact per-seed validation/test results
├── VRD15K_Annotation_Guideline_v4_final_review_updated.md
└── north_south_regional_hate_paper.tex  # Single-file LaTeX manuscript
```

Large model binaries and training checkpoints are intentionally excluded from GitHub because GitHub rejects files above 100 MB. Their local paths and the download location are listed in [Model files](#model-files).

## Dataset format

The processed CSV files have three columns:

| Column | Description |
|---|---|
| `comment` | Vietnamese social-media comment text |
| `north_hate` | Harm label relative to Northerners |
| `south_hate` | Harm label relative to Southerners |

The label values are `NON_HATE`, `PREJUDICIAL`, and `HOSTILE`. The two target dimensions are evaluated independently, so a comment may be harmful toward one target and non-harmful toward the other.

## Quick start

The project was developed as a Python notebook workflow. Python 3.10+ is recommended. The notebook's dependency line uses the following packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib seaborn scikit-learn torch transformers accelerate sentencepiece openpyxl joblib
```

Open `SEG301_Prj_annotations_merged.ipynb` and run the cells in order. The notebook reads the processed data from `data/processed/` and writes figures and model-result summaries into the project folders.

## Reproduce the auxiliary analyses

### Cohen's kappa

From the repository root:

```powershell
python Kappa\calculate_kappa.py
```

This reads the five annotator workbooks in `Kappa/` and regenerates the pairwise coefficients, report, and formatted workbook.

### Three-seed benchmark

```powershell
python run_three_seeds.py
```

The script executes the notebook's training cells with seeds 42, 43, and 44 on the existing fixed split and writes compact summaries to `results_three_seeds/seed_42.csv`, `seed_43.csv`, and `seed_44.csv`. PhoBERT training requires a locally available base checkpoint and substantial disk space; the script currently uses an offline local Hugging Face cache path, so adapt that path for another machine.

### Paper figures

```powershell
powershell -ExecutionPolicy Bypass -File .\generate_paper_figures.ps1
```

The script regenerates the English paper figures in `figures/` from the processed split files and the benchmark values encoded in the script.

## Model files

The following model artifacts are present locally but are not committed to GitHub:

| Model/artifact | Local path | Approximate size |
|---|---|---:|
| TF--IDF baseline bundle | `tfidf_baselines.joblib` | 72 MB |
| Multi-task BiLSTM with attention | `bilstm_attention_multitask.pt` | 2.6 MB |
| Final North PhoBERT | `saved_phobert/north_hate/` | 516 MB |
| Final South PhoBERT | `saved_phobert/south_hate/` | 516 MB |
| PhoBERT training checkpoints | `phobert_checkpoints/` | 3.1 GB |
| Three-seed checkpoints | `results_three_seeds/seed_42/`, `seed_43/`, `seed_44/` | 9.3 GB |

The current shared model folder is:

[Google Drive model folder](https://drive.google.com/drive/folders/1c5cXgUlzW-JK1tx0p5KGJzc9iRG5ibbx?usp=sharing)

For normal inference, upload the two `saved_phobert/` folders and the compact TF--IDF/BiLSTM artifacts. The optimizer files under `phobert_checkpoints/` and the repeated three-seed checkpoints are only needed to resume training or audit every run.

## Current benchmark summary

The manuscript reports three-seed results on one fixed 70/15/15 split. The best mean test macro-F1 is PhoBERT: `0.62 ± 0.02` after rounding to two decimal places. The South-targeted `PREJUDICIAL` class remains difficult and receives zero F1 in the reported PhoBERT runs.

These scores are preliminary benchmark results. The current PhoBERT run uses raw rather than Vietnamese word-segmented input, and the final release should use normalized duplicate-aware splitting and multi-seed evaluation consistently.

## Paper

The manuscript source is [`north_south_regional_hate_paper.tex`](north_south_regional_hate_paper.tex). It can be opened directly in Overleaf together with the `figures/` directory. The paper uses an inline bibliography, so no separate `.bib` file is required.

## Data governance

The comments originate from Vietnamese social-media discussions and may contain offensive language. The processed files retain comment text and target labels but do not include usernames or profile links. Before redistribution, check the source platforms' policies, privacy requirements, and any institutional ethics requirements. Do not use the labels or model predictions to profile regional communities or as the sole basis for punitive action.

## License and citation

No open-source license has been declared for this repository yet. Until the authors add a license and release statement, reuse should be requested from the authors.

If you use this resource, cite the accompanying ViNS-Hate manuscript and link to this repository.
