# Cohen's kappa results for the paper

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
| Hate toward Northern people (`Bac_hate`) | 0.500 | 0.095 | 0.389–0.671 | 81.3% |
| Hate toward Southern people (`Nam_hate`) | 0.506 | 0.104 | 0.360–0.686 | 93.2% |
| Macro across both targets | 0.503 | 0.097 | 0.360–0.686 | 87.2% |

Using conventional descriptive bands, the average pairwise agreement is moderate for both targets. The difference between high raw agreement and moderate kappa, especially for `Nam_hate`, is consistent with strong label-prevalence imbalance: expected chance agreement is high because most annotations are `NON_HATE`.

## Vietnamese paragraph ready for the manuscript

Độ nhất quán liên chú giải được đánh giá trên một tập kiểm định chung gồm 300 bình luận, được năm annotator gán nhãn độc lập cho hai đích Bắc và Nam. Cohen's kappa không trọng số được tính riêng cho toàn bộ 10 cặp annotator trên từng đích. Đối với nhãn hướng tới người miền Bắc, kappa trung bình theo cặp đạt κ = 0.500 (SD = 0.095, khoảng 0.389–0.671), với tỷ lệ đồng thuận quan sát trung bình 81.3%. Đối với nhãn hướng tới người miền Nam, kappa trung bình đạt κ = 0.506 (SD = 0.104, khoảng 0.360–0.686), với tỷ lệ đồng thuận quan sát trung bình 93.2%. Trung bình gộp mô tả trên cả hai đích là κ = 0.503. Các kết quả cho thấy mức độ đồng thuận trung bình; chênh lệch giữa tỷ lệ đồng thuận thô cao và kappa vừa phải, đặc biệt ở nhãn miền Nam, phản ánh ảnh hưởng của phân bố nhãn mất cân bằng mạnh.

## English paragraph ready for the manuscript

Inter-annotator reliability was evaluated on a shared sample of 300 comments independently labeled by five annotators for the North- and South-targeted tasks. Unweighted Cohen's kappa was computed separately for all 10 annotator pairs for each target. For hate directed toward Northerners, the mean pairwise kappa was κ = 0.500 (SD = 0.095, range 0.389–0.671), with a mean observed agreement of 81.3%. For hate directed toward Southerners, the mean pairwise kappa was κ = 0.506 (SD = 0.104, range 0.360–0.686), with a mean observed agreement of 93.2%. The descriptive macro-average across both targets was κ = 0.503. The gap between high raw agreement and moderate kappa, particularly for the South-targeted labels, reflects the strong prevalence imbalance toward the `NON_HATE` category.
