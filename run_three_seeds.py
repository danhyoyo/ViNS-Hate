"""Re-run the notebook's five model families on its frozen 70/15/15 split."""
import json
import os
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
notebook = json.loads((ROOT / "SEG301_Prj_annotations_merged.ipynb").read_text(encoding="utf-8"))
sources = {i: "".join(cell["source"]) for i, cell in enumerate(notebook["cells"])}
outdir = ROOT / "results_three_seeds"
outdir.mkdir(exist_ok=True)
base_model = (Path.home() / ".cache/huggingface/hub/models--vinai--phobert-base-v2"
              / "snapshots/86cd7fd4c148980922ac11a2cf5e257f2ba639e1")
assert (base_model / "pytorch_model.bin").is_file()
os.environ["HF_HUB_OFFLINE"] = "1"

def execute(index, namespace, replacements=()):
    source = sources[index]
    for old, new in replacements:
        assert old in source, (index, old)
        source = source.replace(old, new)
    exec(compile(source, f"notebook-cell-{index}", "exec"), namespace)

for seed in (42, 43, 44):
    print(f"=== Seed {seed} ===", flush=True)
    ns = {"__name__": "__main__"}
    execute(3, ns, (("SEED = 42", f"SEED = {seed}"),))
    ns["train_df"] = pd.read_csv(ROOT / "data/processed/train.csv", encoding="utf-8-sig")
    ns["val_df"] = pd.read_csv(ROOT / "data/processed/val.csv", encoding="utf-8-sig")
    ns["test_df"] = pd.read_csv(ROOT / "data/processed/test.csv", encoding="utf-8-sig")
    execute(14, ns)
    execute(16, ns)
    for index in (18, 20, 22, 24, 25):
        # Single worker avoids a restricted Windows process/pipe creation path.
        execute(index, ns, (("n_jobs=-1", "n_jobs=1"),) if index == 18 else ())
    execute(27, ns, (
        ('BASE_MODEL = "vinai/phobert-base-v2"', f'BASE_MODEL = r"{base_model}"'),
        ('AutoTokenizer.from_pretrained(BASE_MODEL, use_fast=False)',
         'AutoTokenizer.from_pretrained("saved_phobert/north_hate", use_fast=False, local_files_only=True)'),
        ('output_dir=f"phobert_checkpoints/{target}"',
         f'output_dir=f"results_three_seeds/seed_{seed}/phobert_{{target}}"'),
    ))
    rows = []
    for name, target_results in ns["model_results"].items():
        for target in ns["TARGETS"]:
            for split in ("val", "test"):
                result = target_results[target][split]
                rows.append({
                    "seed": seed, "model": name, "target": target, "split": split,
                    "accuracy": result["accuracy"], "macro_f1": result["macro_f1"],
                    "confusion_matrix": json.dumps(result["confusion_matrix"]),
                    "classification_report": json.dumps(result["classification_report"]),
                })
    pd.DataFrame(rows).to_csv(outdir / f"seed_{seed}.csv", index=False)
    print(f"Saved seed {seed}", flush=True)
