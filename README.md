# ViNS-Hate: Code, Dataset, and Benchmark Results

This repository contains the training/evaluation code, processed dataset, and benchmark results for ViNS-Hate, a Vietnamese social-media dataset with target-specific labels for regional prejudice and hostility toward Northerners and Southerners.

## Repository scope

Only the following materials are tracked here:

- model training and evaluation code;
- processed train/validation/test data;
- Cohen's kappa calculation code and annotation-agreement results;
- benchmark result summaries for the three random seeds.

The manuscript, figures, literature notes, and other project documents are intentionally kept outside this repository.

## Contents

```text
ViNS-Hate/
├── data/processed/
│   ├── train.csv
│   ├── val.csv
│   └── test.csv
├── Kappa/
│   ├── calculate_kappa.py
│   ├── cohen_kappa_pairwise.csv
│   ├── cohen_kappa_report.md
│   └── cohen_kappa_results.xlsx
├── SEG301_Prj_annotations_merged.ipynb  # Main training/evaluation notebook
├── run_three_seeds.py                   # Runs seeds 42, 43, and 44
├── model_comparison_multitask.csv       # Compact benchmark summary
└── results_three_seeds/
    ├── seed_42.csv
    ├── seed_43.csv
    └── seed_44.csv
```

Large model binaries and checkpoints are not tracked in GitHub. They are listed in the model section below.

## Dataset

The processed CSV files contain 4,423 comments split into 3,095 training, 664 validation, and 664 test instances. Each file has three columns:

| Column | Meaning |
|---|---|
| `comment` | Vietnamese social-media comment |
| `north_hate` | Label relative to Northerners |
| `south_hate` | Label relative to Southerners |

Allowed labels are `NON_HATE`, `PREJUDICIAL`, and `HOSTILE`. The North and South labels are assigned independently.

## Installation

The notebook uses the following Python packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib seaborn scikit-learn torch transformers accelerate sentencepiece openpyxl joblib
```

No dependency lock file is included yet; package versions should be recorded before a final archival release.

## Training and evaluation

Open `SEG301_Prj_annotations_merged.ipynb` and execute the cells in order. The notebook reads the frozen split from `data/processed/` and evaluates TF--IDF models, the multi-task BiLSTM, and PhoBERT.

To run the three-seed benchmark:

```powershell
python run_three_seeds.py
```

This runs seeds 42, 43, and 44 on the fixed split and writes compact summaries to `results_three_seeds/`. The script currently expects a local offline PhoBERT base checkpoint; adapt its `base_model` path when running on another machine.

## Cohen's kappa

```powershell
python Kappa\calculate_kappa.py
```

The script reads the five annotator workbooks and regenerates the pairwise coefficients and summary report in `Kappa/`.

## Benchmark results

The result CSV files contain validation and test metrics for the five model families over seeds 42, 43, and 44. The current best mean test macro-F1 is PhoBERT (`0.62 ± 0.02`, rounded to two decimals). The South-targeted `PREJUDICIAL` class remains difficult and receives zero F1 in the reported PhoBERT runs.

## Model files kept outside GitHub

The local model artifacts are:

```text
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\saved_phobert\north_hate\
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\saved_phobert\south_hate\
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\bilstm_attention_multitask.pt
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\tfidf_baselines.joblib
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\phobert_checkpoints\
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\results_three_seeds\seed_42\
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\results_three_seeds\seed_43\
D:\FPTU LEARNING MATERIAL\TNMG\North_South_paper\results_three_seeds\seed_44\
```

For inference, upload the two `saved_phobert` folders and the compact BiLSTM/TF--IDF artifacts. The repeated seed checkpoints and optimizer files are only needed to resume or audit training.

## Data-use note

The dataset contains user-generated social-media text and potentially offensive language. Check platform policies and privacy/ethics requirements before redistribution or deployment. Model predictions should not be used to profile regional communities or as the sole basis for punitive decisions.

## License

No open-source license has been declared for this repository yet. Reuse should therefore be requested from the authors until a license is added.
