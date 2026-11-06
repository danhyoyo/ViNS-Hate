from collections import Counter
from itertools import combinations
from pathlib import Path
import csv
import statistics

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo


ROOT = Path(__file__).resolve().parent
INPUTS = sorted(ROOT.glob("300_KAPPA_*.xlsx"))
LABELS = ("NON_HATE", "PREJUDICIAL", "HOSTILE")
TARGETS = ("Bac", "Nam")
LABEL_MAP = {
    "NON_HATE": "NON_HATE",
    "PREJUDICIAL": "PREJUDICIAL",
    "HOSTILE": "HOSTILE",
    "Định kiến/Quy chụp": "PREJUDICIAL",
}


def normalize_label(value):
    if value is None or str(value).strip() == "":
        return None
    text = str(value).strip()
    if text not in LABEL_MAP:
        raise ValueError(f"Unknown label: {text!r}")
    return LABEL_MAP[text]


def read_inputs():
    data = {}
    base_comments = None
    for path in INPUTS:
        annotator = path.stem.rsplit("_", 1)[-1]
        ws = load_workbook(path, read_only=True, data_only=True).active
        rows = list(ws.iter_rows(min_row=2, values_only=True))
        comments = [row[0] for row in rows]
        if len(rows) != 300:
            raise ValueError(f"{path.name}: expected 300 rows, found {len(rows)}")
        if base_comments is None:
            base_comments = comments
        elif comments != base_comments:
            raise ValueError(f"{path.name}: comments/order differ from other workbooks")
        data[annotator] = {
            "Bac": [normalize_label(row[1]) for row in rows],
            "Nam": [normalize_label(row[2]) for row in rows],
            "review": [bool(row[3]) if len(row) > 3 and row[3] is not None else False for row in rows],
            "source": path.name,
        }
    return base_comments, data


def cohen_kappa(values_a, values_b):
    paired = [(a, b) for a, b in zip(values_a, values_b) if a and b]
    n = len(paired)
    count_a = Counter(a for a, _ in paired)
    count_b = Counter(b for _, b in paired)
    observed = sum(a == b for a, b in paired) / n
    expected = sum(count_a[label] * count_b[label] for label in LABELS) / (n * n)
    kappa = (observed - expected) / (1 - expected) if expected != 1 else None
    matrix = {
        (row_label, col_label): sum(
            a == row_label and b == col_label for a, b in paired
        )
        for row_label in LABELS
        for col_label in LABELS
    }
    return {
        "n": n,
        "observed": observed,
        "expected": expected,
        "kappa": kappa,
        "matrix": matrix,
    }


def band(value):
    if value is None:
        return "Undefined"
    if value < 0:
        return "Poor"
    if value < 0.20:
        return "Slight"
    if value < 0.40:
        return "Fair"
    if value < 0.60:
        return "Moderate"
    if value < 0.80:
        return "Substantial"
    return "Almost perfect"


def build_results(data):
    results = []
    annotators = list(data)
    for target in TARGETS:
        for ann_a, ann_b in combinations(annotators, 2):
            result = cohen_kappa(data[ann_a][target], data[ann_b][target])
            results.append(
                {
                    "target": target,
                    "annotator_a": ann_a,
                    "annotator_b": ann_b,
                    **result,
                }
            )
    return results


def style_workbook(wb):
    navy = "17365D"
    blue = "D9EAF7"
    light = "EAF2F8"
    green = "E2F0D9"
    gray = "E7E6E6"
    thin = Side(style="thin", color="B7B7B7")
    for ws in wb.worksheets:
        ws.sheet_view.showGridLines = False
        for row in ws.iter_rows():
            for cell in row:
                cell.font = Font(name="Arial", size=10)
                cell.alignment = Alignment(vertical="top", wrap_text=True)
        for cell in ws[1]:
            cell.font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor=navy)
    summary = wb["Summary"]
    summary["A1"].font = Font(name="Arial", size=16, bold=True, color="FFFFFF")
    for row in (7, 31):
        for cell in summary[row]:
            if cell.value is not None:
                cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
                cell.fill = PatternFill("solid", fgColor=navy)
                cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
                cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row in summary.iter_rows(min_row=8, max_row=27, min_col=1, max_col=9):
        for cell in row:
            cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for row in summary.iter_rows(min_row=32, max_row=34, min_col=1, max_col=7):
        for cell in row:
            cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
            if cell.row in (32, 33):
                cell.fill = PatternFill("solid", fgColor=green)
    summary.freeze_panes = "A8"
    summary.auto_filter.ref = "A7:I27"
    widths = {"A": 11, "B": 14, "C": 14, "D": 9, "E": 14, "F": 14, "G": 15, "H": 15, "I": 20}
    for col, width in widths.items():
        summary.column_dimensions[col].width = width
    normalized = wb["Normalized_Labels"]
    normalized.freeze_panes = "C2"
    normalized.column_dimensions["A"].width = 11
    normalized.column_dimensions["B"].width = 75
    for col in range(3, normalized.max_column + 1):
        normalized.column_dimensions[get_column_letter(col)].width = 16
    for cell in normalized[1]:
        cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=navy)
    audit = wb["Data_Audit"]
    audit.freeze_panes = "A9"
    for row in audit.iter_rows(min_row=8, max_row=audit.max_row, min_col=1, max_col=9):
        for cell in row:
            cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for cell in audit[8]:
        cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=navy)
    for col, width in {"A": 16, "B": 30, "C": 12, "D": 12, "E": 15, "F": 15, "G": 15, "H": 15, "I": 15}.items():
        audit.column_dimensions[col].width = width
    confusion = wb["Confusion_Matrices"]
    confusion.column_dimensions["A"].width = 22
    for col in "BCDE":
        confusion.column_dimensions[col].width = 16
    for row in range(1, confusion.max_row + 1):
        if confusion.cell(row, 1).value and str(confusion.cell(row, 1).value).startswith("Target="):
            for col in range(1, 6):
                cell = confusion.cell(row, col)
                cell.fill = PatternFill("solid", fgColor=navy)
                cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        elif confusion.cell(row, 1).value == "Annotator A \\ Annotator B":
            for col in range(1, 6):
                cell = confusion.cell(row, col)
                cell.fill = PatternFill("solid", fgColor=blue)
                cell.font = Font(name="Arial", size=10, bold=True)
        for col in range(1, 6):
            if confusion.cell(row, col).value is not None:
                confusion.cell(row, col).border = Border(left=thin, right=thin, top=thin, bottom=thin)
    for ws in wb.worksheets:
        ws.auto_filter


def create_workbook(comments, data, results, output_path):
    wb = Workbook()
    summary = wb.active
    summary.title = "Summary"
    summary.merge_cells("A1:I1")
    summary["A1"] = "Pairwise Cohen's Kappa — North/South Regional Hate Annotation"
    summary["A2"] = "Scope"
    summary["B2"] = "5 annotators × 300 shared comments × 2 target-specific labels"
    summary["A3"] = "Primary statistic"
    summary["B3"] = "Unweighted nominal Cohen's kappa, computed for all 10 annotator pairs per target"
    summary["A4"] = "Missing-data rule"
    summary["B4"] = "Pairwise complete cases; THANG has one missing Nam label (sample_id 59)"
    summary["A5"] = "Normalization"
    summary["B5"] = "Định kiến/Quy chụp → PREJUDICIAL; review_flag is documented but not used to filter labels"
    headers = [
        "Target", "Annotator A", "Annotator B", "N", "Observed agreement (Po)",
        "Expected agreement (Pe)", "Cohen's kappa", "Percent agreement", "Descriptive band",
    ]
    summary.append([])
    summary.append(headers)

    normalized = wb.create_sheet("Normalized_Labels")
    norm_headers = ["sample_id", "comment"]
    annotators = list(data)
    for ann in annotators:
        norm_headers.extend([f"Bac_{ann}", f"Nam_{ann}", f"Review_{ann}"])
    normalized.append(norm_headers)
    for idx, comment in enumerate(comments, start=1):
        row = [idx, comment]
        for ann in annotators:
            row.extend([data[ann]["Bac"][idx - 1], data[ann]["Nam"][idx - 1], data[ann]["review"][idx - 1]])
        normalized.append(row)
    table = Table(displayName="NormalizedLabels", ref=f"A1:{get_column_letter(normalized.max_column)}{normalized.max_row}")
    table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True, showFirstColumn=False, showLastColumn=False)
    normalized.add_table(table)

    col_map = {}
    for col_idx, header in enumerate(norm_headers, start=1):
        if header.startswith("Bac_") or header.startswith("Nam_"):
            target, ann = header.split("_", 1)
            col_map[(target, ann)] = get_column_letter(col_idx)

    confusion = wb.create_sheet("Confusion_Matrices")
    confusion.append(["Pairwise confusion matrices; rows = Annotator A, columns = Annotator B"])
    block_refs = []
    start_row = 3
    for result in results:
        target = result["target"]
        ann_a = result["annotator_a"]
        ann_b = result["annotator_b"]
        col_a = col_map[(target, ann_a)]
        col_b = col_map[(target, ann_b)]
        r = start_row
        confusion.cell(r, 1, f"Target={target}; {ann_a} vs {ann_b}")
        confusion.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        confusion.cell(r + 1, 1, "Annotator A \\ Annotator B")
        for j, label in enumerate(LABELS, start=2):
            confusion.cell(r + 1, j, label)
        confusion.cell(r + 1, 5, "Row total")
        for i, row_label in enumerate(LABELS, start=r + 2):
            confusion.cell(i, 1, row_label)
            for j, col_label in enumerate(LABELS, start=2):
                formula = (
                    f'=COUNTIFS(Normalized_Labels!${col_a}$2:${col_a}$301,$A{i},'
                    f'Normalized_Labels!${col_b}$2:${col_b}$301,{get_column_letter(j)}${r + 1})'
                )
                confusion.cell(i, j, formula)
            confusion.cell(i, 5, f"=SUM(B{i}:D{i})")
        total_row = r + 5
        confusion.cell(total_row, 1, "Column total")
        for j in range(2, 5):
            letter = get_column_letter(j)
            confusion.cell(total_row, j, f"=SUM({letter}{r + 2}:{letter}{r + 4})")
        confusion.cell(total_row, 5, f"=SUM(E{r + 2}:E{r + 4})")
        confusion.cell(r + 6, 1, "Observed agreement (Po)")
        confusion.cell(r + 6, 2, f"=(B{r + 2}+C{r + 3}+D{r + 4})/E{total_row}")
        confusion.cell(r + 7, 1, "Expected agreement (Pe)")
        confusion.cell(
            r + 7,
            2,
            f"=(E{r + 2}*B{total_row}+E{r + 3}*C{total_row}+E{r + 4}*D{total_row})/E{total_row}^2",
        )
        confusion.cell(r + 8, 1, "Cohen's kappa")
        confusion.cell(r + 8, 2, f'=IF(1-B{r + 7}=0,"",(B{r + 6}-B{r + 7})/(1-B{r + 7}))')
        confusion.cell(r + 9, 1, "Percent agreement")
        confusion.cell(r + 9, 2, f"=B{r + 6}")
        for stats_row in (r + 6, r + 7, r + 8, r + 9):
            confusion.cell(stats_row, 2).number_format = "0.0000"
        block_refs.append(
            {
                "n": f"Confusion_Matrices!E{total_row}",
                "po": f"Confusion_Matrices!B{r + 6}",
                "pe": f"Confusion_Matrices!B{r + 7}",
                "kappa": f"Confusion_Matrices!B{r + 8}",
                "agreement": f"Confusion_Matrices!B{r + 9}",
            }
        )
        start_row += 12

    for idx, (result, refs) in enumerate(zip(results, block_refs), start=8):
        summary.cell(idx, 1, result["target"])
        summary.cell(idx, 2, result["annotator_a"])
        summary.cell(idx, 3, result["annotator_b"])
        summary.cell(idx, 4, f"={refs['n']}")
        summary.cell(idx, 5, f"={refs['po']}")
        summary.cell(idx, 6, f"={refs['pe']}")
        summary.cell(idx, 7, f"={refs['kappa']}")
        summary.cell(idx, 8, f"={refs['agreement']}")
        summary.cell(
            idx,
            9,
            f'=IF(G{idx}="","Undefined",IF(G{idx}<0,"Poor",IF(G{idx}<0.2,"Slight",IF(G{idx}<0.4,"Fair",IF(G{idx}<0.6,"Moderate",IF(G{idx}<0.8,"Substantial","Almost perfect"))))))',
        )
        for col in (5, 6, 7, 8):
            summary.cell(idx, col).number_format = "0.0000"

    summary["A31"] = "Aggregate"
    aggregate_headers = ["Target", "Mean kappa", "SD", "Minimum", "Maximum", "Mean agreement", "Pairwise comparisons"]
    for col, value in enumerate(aggregate_headers, start=1):
        summary.cell(31, col, value)
    summary["A32"] = "Bac"
    summary["B32"] = "=AVERAGE(G8:G17)"
    summary["C32"] = "=STDEV.S(G8:G17)"
    summary["D32"] = "=MIN(G8:G17)"
    summary["E32"] = "=MAX(G8:G17)"
    summary["F32"] = "=AVERAGE(H8:H17)"
    summary["G32"] = "=COUNT(G8:G17)"
    summary["A33"] = "Nam"
    summary["B33"] = "=AVERAGE(G18:G27)"
    summary["C33"] = "=STDEV.S(G18:G27)"
    summary["D33"] = "=MIN(G18:G27)"
    summary["E33"] = "=MAX(G18:G27)"
    summary["F33"] = "=AVERAGE(H18:H27)"
    summary["G33"] = "=COUNT(G18:G27)"
    summary["A34"] = "Macro (both targets)"
    summary["B34"] = "=AVERAGE(G8:G27)"
    summary["C34"] = "=STDEV.S(G8:G27)"
    summary["D34"] = "=MIN(G8:G27)"
    summary["E34"] = "=MAX(G8:G27)"
    summary["F34"] = "=AVERAGE(H8:H27)"
    summary["G34"] = "=COUNT(G8:G27)"
    for row in range(32, 35):
        for col in range(2, 7):
            summary.cell(row, col).number_format = "0.0000"

    audit = wb.create_sheet("Data_Audit")
    audit.merge_cells("A1:I1")
    audit["A1"] = "Data audit and label distributions"
    audit["A3"] = "Validation"
    audit["B3"] = "All five files contain the same 300 comments in the same order."
    audit["A4"] = "Normalized label"
    audit["B4"] = "Định kiến/Quy chụp was treated as PREJUDICIAL."
    audit["A5"] = "Missing value"
    audit["B5"] = "300_KAPPA_THANG.xlsx, sample_id 59, Nam_hate is blank."
    audit["A6"] = "Exclusion"
    audit["B6"] = "Only the missing label is excluded, and only from Nam pairwise comparisons involving THANG."
    audit_headers = [
        "Annotator", "Source file", "Rows", "Missing Bac", "Missing Nam",
        "Bac NON_HATE", "Bac PREJUDICIAL", "Bac HOSTILE", "Nam NON_HATE / PREJUDICIAL / HOSTILE",
    ]
    for col, value in enumerate(audit_headers, start=1):
        audit.cell(8, col, value)
    for row_idx, ann in enumerate(annotators, start=9):
        audit.cell(row_idx, 1, ann)
        audit.cell(row_idx, 2, data[ann]["source"])
        audit.cell(row_idx, 3, "=COUNTA(Normalized_Labels!$A$2:$A$301)")
        bac_col = col_map[("Bac", ann)]
        nam_col = col_map[("Nam", ann)]
        audit.cell(row_idx, 4, f'=COUNTBLANK(Normalized_Labels!${bac_col}$2:${bac_col}$301)')
        audit.cell(row_idx, 5, f'=COUNTBLANK(Normalized_Labels!${nam_col}$2:${nam_col}$301)')
        audit.cell(row_idx, 6, f'=COUNTIF(Normalized_Labels!${bac_col}$2:${bac_col}$301,"NON_HATE")')
        audit.cell(row_idx, 7, f'=COUNTIF(Normalized_Labels!${bac_col}$2:${bac_col}$301,"PREJUDICIAL")')
        audit.cell(row_idx, 8, f'=COUNTIF(Normalized_Labels!${bac_col}$2:${bac_col}$301,"HOSTILE")')
        audit.cell(
            row_idx,
            9,
            f'=COUNTIF(Normalized_Labels!${nam_col}$2:${nam_col}$301,"NON_HATE")&" / "&COUNTIF(Normalized_Labels!${nam_col}$2:${nam_col}$301,"PREJUDICIAL")&" / "&COUNTIF(Normalized_Labels!${nam_col}$2:${nam_col}$301,"HOSTILE")',
        )

    style_workbook(wb)
    wb.calculation.fullCalcOnLoad = True
    wb.calculation.forceFullCalc = True
    wb.calculation.calcMode = "auto"
    wb.save(output_path)


def write_csv(results, output_path):
    with output_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["target", "annotator_a", "annotator_b", "n", "observed_agreement", "expected_agreement", "cohen_kappa", "descriptive_band"]
        )
        for result in results:
            writer.writerow(
                [
                    result["target"], result["annotator_a"], result["annotator_b"], result["n"],
                    f"{result['observed']:.6f}", f"{result['expected']:.6f}", f"{result['kappa']:.6f}", band(result["kappa"]),
                ]
            )


def write_report(results, output_path):
    by_target = {target: [r for r in results if r["target"] == target] for target in TARGETS}
    stats = {}
    for target, rows in by_target.items():
        kappas = [r["kappa"] for r in rows]
        agreements = [r["observed"] for r in rows]
        stats[target] = {
            "mean": statistics.mean(kappas),
            "sd": statistics.stdev(kappas),
            "min": min(kappas),
            "max": max(kappas),
            "agreement": statistics.mean(agreements),
        }
    all_kappas = [r["kappa"] for r in results]
    macro = statistics.mean(all_kappas)
    text = f"""# Cohen's kappa results for the paper

## Data and calculation

- Five annotators independently labeled the same 300 comments.
- Cohen's kappa was calculated pairwise for all 10 annotator pairs, separately for `Bac_hate` and `Nam_hate`.
- Labels were treated as nominal; this report presents unweighted Cohen's kappa.
- `Định kiến/Quy chụp` was normalized to `PREJUDICIAL`.
- One `Nam_hate` label is missing for THANG at sample 59. Pairwise complete cases were used, giving N=299 for Nam comparisons involving THANG and N=300 otherwise.
- `review_flag` was not used to filter the independently assigned labels.
- The mean of pairwise Cohen's kappas is a descriptive summary, not a separate multi-rater Cohen's kappa statistic.

## Results

| Target | Mean pairwise κ | SD | Range | Mean observed agreement |
|---|---:|---:|---:|---:|
| Hate toward Northern people (`Bac_hate`) | {stats['Bac']['mean']:.3f} | {stats['Bac']['sd']:.3f} | {stats['Bac']['min']:.3f}–{stats['Bac']['max']:.3f} | {stats['Bac']['agreement']:.1%} |
| Hate toward Southern people (`Nam_hate`) | {stats['Nam']['mean']:.3f} | {stats['Nam']['sd']:.3f} | {stats['Nam']['min']:.3f}–{stats['Nam']['max']:.3f} | {stats['Nam']['agreement']:.1%} |
| Macro across both targets | {macro:.3f} | {statistics.stdev(all_kappas):.3f} | {min(all_kappas):.3f}–{max(all_kappas):.3f} | {statistics.mean(r['observed'] for r in results):.1%} |

Using conventional descriptive bands, the average pairwise agreement is moderate for both targets. The difference between high raw agreement and moderate kappa, especially for `Nam_hate`, is consistent with strong label-prevalence imbalance: expected chance agreement is high because most annotations are `NON_HATE`.

## Vietnamese paragraph ready for the manuscript

Độ nhất quán liên chú giải được đánh giá trên một tập kiểm định chung gồm 300 bình luận, được năm annotator gán nhãn độc lập cho hai đích Bắc và Nam. Cohen's kappa không trọng số được tính riêng cho toàn bộ 10 cặp annotator trên từng đích. Đối với nhãn hướng tới người miền Bắc, kappa trung bình theo cặp đạt κ = {stats['Bac']['mean']:.3f} (SD = {stats['Bac']['sd']:.3f}, khoảng {stats['Bac']['min']:.3f}–{stats['Bac']['max']:.3f}), với tỷ lệ đồng thuận quan sát trung bình {stats['Bac']['agreement']:.1%}. Đối với nhãn hướng tới người miền Nam, kappa trung bình đạt κ = {stats['Nam']['mean']:.3f} (SD = {stats['Nam']['sd']:.3f}, khoảng {stats['Nam']['min']:.3f}–{stats['Nam']['max']:.3f}), với tỷ lệ đồng thuận quan sát trung bình {stats['Nam']['agreement']:.1%}. Trung bình gộp mô tả trên cả hai đích là κ = {macro:.3f}. Các kết quả cho thấy mức độ đồng thuận trung bình; chênh lệch giữa tỷ lệ đồng thuận thô cao và kappa vừa phải, đặc biệt ở nhãn miền Nam, phản ánh ảnh hưởng của phân bố nhãn mất cân bằng mạnh.

## English paragraph ready for the manuscript

Inter-annotator reliability was evaluated on a shared sample of 300 comments independently labeled by five annotators for the North- and South-targeted tasks. Unweighted Cohen's kappa was computed separately for all 10 annotator pairs for each target. For hate directed toward Northerners, the mean pairwise kappa was κ = {stats['Bac']['mean']:.3f} (SD = {stats['Bac']['sd']:.3f}, range {stats['Bac']['min']:.3f}–{stats['Bac']['max']:.3f}), with a mean observed agreement of {stats['Bac']['agreement']:.1%}. For hate directed toward Southerners, the mean pairwise kappa was κ = {stats['Nam']['mean']:.3f} (SD = {stats['Nam']['sd']:.3f}, range {stats['Nam']['min']:.3f}–{stats['Nam']['max']:.3f}), with a mean observed agreement of {stats['Nam']['agreement']:.1%}. The descriptive macro-average across both targets was κ = {macro:.3f}. The gap between high raw agreement and moderate kappa, particularly for the South-targeted labels, reflects the strong prevalence imbalance toward the `NON_HATE` category.
"""
    output_path.write_text(text, encoding="utf-8")


def main():
    comments, data = read_inputs()
    results = build_results(data)
    create_workbook(comments, data, results, ROOT / "cohen_kappa_results.xlsx")
    write_csv(results, ROOT / "cohen_kappa_pairwise.csv")
    write_report(results, ROOT / "cohen_kappa_report.md")
    print("Created cohen_kappa_results.xlsx, cohen_kappa_pairwise.csv, and cohen_kappa_report.md")


if __name__ == "__main__":
    main()
