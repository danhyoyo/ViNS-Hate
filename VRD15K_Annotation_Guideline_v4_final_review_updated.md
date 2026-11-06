# VRD15K Annotation Guideline v4 — North–South Regional Hate

## 1. Mục tiêu

Mỗi bình luận được gán 3 trường:

```yaml
north_hate:
    0 = NON_HATE
    1 = PREJUDICIAL
    2 = HOSTILE

south_hate:
    0 = NON_HATE
    1 = PREJUDICIAL
    2 = HOSTILE

review_flag:
    0 = không cần review
    1 = cần review/adjudication
```

Hai miền **Bắc** và **Nam** luôn được đánh giá **độc lập**.

Câu hỏi cần trả lời:

- Người viết có thể hiện prejudice/hostility với **người miền Bắc** không? Mức nào?
- Người viết có thể hiện prejudice/hostility với **người miền Nam** không? Mức nào?

Không gán nhãn chỉ dựa trên từ khóa như `Bắc`, `Nam`, `Bắc Kỳ`, `Nam Kỳ`, `parky`, `namki`, tên tỉnh thành, từ tục hoặc emoji. Luôn xét **ý nghĩa toàn câu và lập trường của người viết**.

---

## 2. Ba mức nhãn

### 0 — `NON_HATE`

Không có prejudice hoặc hostility hướng vào target đó.

Bao gồm:

- Không nhắc đến target.
- Nhắc trung tính hoặc cung cấp thông tin.
- Khen, bảo vệ, phản đối kỳ thị.
- Phàn nàn về khí hậu, đồ ăn, giao thông, địa điểm, dịch vụ hoặc trải nghiệm cá nhân nhưng **không quy chụp con người theo vùng**.
- Trích dẫn hate để phản đối hoặc phân tích trung tính.

Ví dụ:

> “Tôi đang sống ở miền Bắc.”

```text
north_hate = 0
south_hate = 0
```

> “Tôi không thích thời tiết miền Bắc.”

```text
north_hate = 0
south_hate = 0
```

> “Đừng gọi người Bắc là parky.”

```text
north_hate = 0
south_hate = 0
```

### 1 — `PREJUDICIAL`

Người viết quy chụp, stereotype hoặc gán đặc điểm tiêu cực cho con người dựa trên căn tính vùng miền, nhưng chưa có miệt thị/hạ nhục trực tiếp, loại trừ hoặc đe dọa.

Dấu hiệu thường gặp:

- Khái quát từ cá nhân ra cả cộng đồng.
- Gắn tính cách, đạo đức, năng lực hoặc hành vi xấu với vùng miền.
- Dùng cách nói như “ai cũng”, “toàn”, “bản chất”, “lúc nào cũng”; tuy nhiên các từ này **không bắt buộc**.

Ví dụ:

> “Người Bắc thường sống giả tạo.”

```text
north_hate = 1
south_hate = 0
```

> “Người miền Nam ai cũng không biết tiết kiệm.”

```text
north_hate = 0
south_hate = 1
```

### 2 — `HOSTILE`

Người viết thể hiện hostility trực tiếp đối với target vì căn tính vùng miền.

Bao gồm:

- Miệt thị, hạ nhục, gọi nhóm bằng từ mang tính xúc phạm.
- Dùng slur vùng miền để trực tiếp gọi/công kích nhóm.
- Từ tục nhắm trực tiếp vào nhóm.
- Phi nhân hóa.
- Xua đuổi hoặc loại trừ.
- Từ chối tuyển dụng, phục vụ, cho thuê... chỉ vì nguồn gốc vùng miền.
- Mong tai họa hoặc tổn hại xảy đến với nhóm.
- Đe dọa, cổ vũ hoặc kêu gọi gây hại.

Ví dụ:

> “Bọn Bắc Kỳ là lũ không ra gì.”

```text
north_hate = 2
south_hate = 0
```

> “Không cho người miền Nam thuê nhà.”

```text
north_hate = 0
south_hate = 2
```

---

## 3. Phân biệt `0` và `1`

Câu hỏi chính:

> Người viết đang chê một **sự việc/đặc điểm cụ thể**, hay đang biến **căn tính vùng miền thành căn cứ để đánh giá xấu con người**?

| Ví dụ | Nhãn |
|---|---|
| “Giao thông miền Bắc khá tệ.” | `north_hate = 0` |
| “Người Bắc làm dịch vụ lúc nào cũng khó chịu.” | `north_hate = 1` |
| “Tôi không hợp đồ ăn miền Nam.” | `south_hate = 0` |
| “Người miền Nam vốn không trung thực.” | `south_hate = 1` |

---

## 4. Phân biệt `1` và `2`

Câu hỏi chính:

> Câu chỉ đang nêu một stereotype tiêu cực, hay đã trực tiếp hạ nhục/miệt thị/loại trừ/gây hại cho nhóm?

| `PREJUDICIAL = 1` | `HOSTILE = 2` |
|---|---|
| Quy chụp, stereotype | Miệt thị/hạ nhục trực tiếp |
| Không cần từ tục | Có thể có slur/từ tục nhắm vào nhóm |
| Không loại trừ | Xua đuổi hoặc loại trừ |
| Không đe dọa | Đe dọa hoặc mong gây hại |

Ví dụ:

> “Người Bắc thường tính toán.” → `north_hate = 1`

> “Lũ Bắc Kỳ khốn nạn.” → `north_hate = 2`

---

## 5. Đánh giá Bắc và Nam độc lập

Không dùng nhãn `both`.

> “Người Bắc chăm chỉ, chứ người Nam ai cũng lười.”

```text
north_hate = 0
south_hate = 1
```

> “Người Bắc tính toán, còn bọn Namki thì không ra gì.”

```text
north_hate = 1
south_hate = 2
```

> “Bắc thì gian, Nam thì lười.”

```text
north_hate = 1
south_hate = 1
```

Nếu cùng một target có nhiều mức, chọn mức cao nhất mà **chính người viết trực tiếp thể hiện hoặc tán thành**:

```text
HOSTILE (2) > PREJUDICIAL (1) > NON_HATE (0)
```

---

## 6. Slur và từ miệt thị

Danh sách ban đầu trong codebook:

```text
North: parky | parki | bake | bắc cầy
South: namki | namkiki | nameky
```

Các biến thể mới chỉ được thêm sau khi adjudication xác nhận.

Không gán `HOSTILE` chỉ vì slur xuất hiện. Phải xét cách dùng:

| Cách dùng | Nhãn |
|---|---|
| Dùng trực tiếp để gọi/công kích nhóm | `2` cho target tương ứng |
| Nhắc lại để phản đối/bảo vệ nhóm | `0` |
| Phân tích/tường thuật từ ngữ trung tính | `0` |
| Tự xưng, không công kích chính nhóm đó | `0` |
| Không rõ đang công kích, tự xưng, trích dẫn hay mỉa mai | `review_flag = 1` |

`Bắc Kỳ` và `Nam Kỳ` theo nghĩa lịch sử–địa lý không tự động là hostile.

---

## 7. Trường hợp đặc biệt

### Công kích cá nhân có nhắc quê quán

> “Anh A là người miền Bắc. Anh ta nói sai trong video.” → `north_hate = 0`

> “Nó nói dối vì đúng bản chất người Bắc.” → `north_hate = 1`

### Địa danh

Tên tỉnh/thành không tự động đại diện cho target vùng miền.

> “Hà Nội hôm nay tắc đường.” → `north_hate = 0`

> “Dân Hà Nội ai cũng ích kỷ.” → có thể `north_hate = 1` **chỉ khi codebook quy ước Hà Nội là proxy cho target miền Bắc**.

Không tự ép địa danh miền Trung hoặc ngoài phạm vi dự án vào Bắc/Nam.

### Trích dẫn và phản đối

Gán theo lập trường của người viết.

> “Nó bảo người Nam toàn lười, nói thế là kỳ thị.” → `south_hate = 0`

> “‘Người Nam toàn lười’ — nói chuẩn.” → `south_hate = 1`

### Phủ định

> “Không phải người miền Nam nào cũng thiếu tiết kiệm.” → `south_hate = 0`

### Mỉa mai

Nếu ý nghĩa mỉa mai rõ, gán theo ý nghĩa thực tế. Nếu không đủ ngữ cảnh để xác định, dùng `review_flag = 1`.

---

## 8. `review_flag`

`review_flag` chỉ dùng để đánh dấu **lỗi/chất lượng văn bản hoặc anonymization**, không dùng để biểu diễn sự phân vân của annotator về nhãn.

```yaml
review_flag:
    0 = text/dữ liệu hợp lệ
    1 = text có vấn đề kỹ thuật, chất lượng hoặc anonymization
```

### Khi nào gán `review_flag = 1`?

Dùng `review_flag = 1` khi comment có một trong các vấn đề sau:

- Lỗi encoding hoặc ký tự bị hỏng.
- Quá nhiều ký tự rác khiến không còn đọc được nội dung.
- Text bị cắt, mất đoạn hoặc hỏng cấu trúc.
- Comment chỉ còn tag/mention và gần như không có nội dung để annotate.
- Username thật vẫn còn xuất hiện và chưa được anonymize.
- Quá trình anonymization làm mất hoặc phá hỏng phần nội dung cần thiết.

Ví dụ:

> “@@@ ### � � @USER ///”

```text
review_flag = 1
```

### Khi nào không cần review?

Không gán `review_flag = 1` chỉ vì comment có ký tự đặc biệt, emoji hoặc từ lóng nếu nội dung vẫn đủ rõ để label.

Ví dụ:

> “parky @@@@ 😂 ???”

Nếu vẫn xác định được đây là cách dùng `parky` để công kích người miền Bắc thì:

```text
north_hate = 2
south_hate = 0
review_flag = 0
```

Tương tự, nếu comment có `@USER` nhưng phần nội dung còn lại vẫn đầy đủ và đã được anonymize đúng cách thì:

```text
review_flag = 0
```

### Không dùng `review_flag` cho disagreement về nhãn

Nếu annotator phân vân giữa:

```text
0 vs 1
1 vs 2
North vs South
```

thì vẫn chọn nhãn mà annotator cho là phù hợp nhất.

Các bất đồng này được xử lý bằng:

```text
multiple annotators + adjudication
```

Không dùng `review_flag` để thay cho annotation disagreement.

### Quy tắc ngắn gọn

```text
Text/dữ liệu hợp lệ → review_flag = 0
Text bị lỗi/hỏng hoặc anonymization có vấn đề → review_flag = 1
```

---

## 9. Những shortcut không được dùng

Không được suy luận:

```text
Có “Bắc/Nam”            → có hate
Có từ tục               → HOSTILE
Có slur                  → luôn HOSTILE
Có đánh giá tiêu cực    → PREJUDICIAL
Có địa danh              → tự động map Bắc/Nam
Có quote chứa hate       → tác giả cũng hate
Có emoji/câu đùa         → không thể HOSTILE
```

Luôn xét:

```text
target + stance + meaning
```

---

## 10. Decision rule rút gọn

Đối với **North**, sau đó lặp lại độc lập cho **South**:

```text
1. Có prejudice/hostility đối với target vì căn tính vùng miền không?
   ├─ Không → 0 = NON_HATE
   └─ Có
       ├─ Chỉ quy chụp/stereotype/bản chất hóa → 1 = PREJUDICIAL
       └─ Miệt thị/slur attack/hạ nhục/loại trừ/
          xua đuổi/mong harm/đe dọa → 2 = HOSTILE
```

Cuối cùng:

```text
Nếu thiếu context hoặc ambiguity thực sự → review_flag = 1
Ngược lại → review_flag = 0
```

---

## 11. Ví dụ tổng hợp

| Bình luận | North | South | Review |
|---|---:|---:|---:|
| “Video này vui thật.” | 0 | 0 | 0 |
| “Tôi sống ở miền Nam.” | 0 | 0 | 0 |
| “Ngoài Bắc gọi là X, trong Nam gọi là Y.” | 0 | 0 | 0 |
| “Người Bắc rất đáng mến.” | 0 | 0 | 0 |
| “Tôi không hợp đồ ăn miền Nam.” | 0 | 0 | 0 |
| “Người Bắc ai cũng khôn lỏi.” | 1 | 0 | 0 |
| “Người Nam vốn không biết tiết kiệm.” | 0 | 1 | 0 |
| “Bắc thì tính toán, Nam thì lười.” | 1 | 1 | 0 |
| “Người Bắc tốt, người Nam toàn lười.” | 0 | 1 | 0 |
| “Bọn Bắc Kỳ là lũ không ra gì.” | 2 | 0 | 0 |
| “Không cho người Nam thuê nhà.” | 0 | 2 | 0 |
| “Đuổi cả dân Bắc lẫn dân Nam đi.” | 2 | 2 | 0 |
| “Người Bắc tính toán, bọn Namki thì rác.” | 1 | 2 | 0 |
| “Đừng gọi người Bắc là parky.” | 0 | 0 | 0 |
| “Từ parky nghĩa là gì?” | 0 | 0 | 0 |
| “Dân ngoài ấy ai cũng giả tạo.” | ? | ? | 1 |

---

## 12. Checklist cuối

1. Tôi đang label **regional hate**, hay chỉ sentiment tiêu cực nói chung?
2. Tôi đã đánh giá North và South **độc lập** chưa?
3. Nếu chọn `1`, có thật sự có stereotype/quy chụp theo căn tính vùng miền không?
4. Nếu chọn `2`, có miệt thị/hạ nhục/slur attack/loại trừ/gây hại không?
5. Tôi có đang gán theo từ khóa thay vì stance không?
6. Nếu có quote/phủ định/mỉa mai, tôi đã xác định lập trường của người viết chưa?
7. Nếu không đủ bằng chứng, tôi đã dùng `review_flag = 1` chưa?

### Ghi nhớ

```text
0 = Không có prejudice/hostility đối với target.
1 = Quy chụp hoặc stereotype tiêu cực theo căn tính vùng miền.
2 = Thù địch trực tiếp: miệt thị, hạ nhục, loại trừ hoặc gây hại.

North và South luôn được đánh giá độc lập.
```
