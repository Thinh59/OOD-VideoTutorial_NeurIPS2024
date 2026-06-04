# KỊCH BẢN V3 — PART XI
## Benchmark Crisis

---

# PART XI — BENCHMARKS & REALITY CHECK

---

## Scene B1 — Gallery Benchmark: 4 Chiến trường Thực tế
**~2 phút**

### VISUAL
- Grid 2×2, mỗi ô là một benchmark. Xuất hiện lần lượt:

**[Waterbirds]** [BLUE_D frame]
- Icon: chim + nước/đất
- Task: phân loại waterbird vs landbird
- Spurious: background (water vs land)
- Train: 4,795 ảnh. WG Gap: ~50%
- Note: "Được tạo nhân tạo — spurious correlation kiểm soát được"

**[CelebA]** [GREEN_D frame]
- Icon: khuôn mặt
- Task: hair color (blonde vs non-blonde)
- Spurious: gender
- Train: 162,770 ảnh. WG Gap: ~40%
- Note: "Dataset thực tế — bias gender thực trong celebrity photos"

**[CivilComments-WILDS]** [YELLOW_D frame]
- Icon: text bubble
- Task: toxicity detection
- Spurious: demographic identity (race, religion, gender)
- Train: 269,038 comments. WG Gap: ~35%
- Note: "High stakes — AI moderation thực tế"

**[Camelyon17-WILDS]** [PURPLE frame]
- Icon: kính hiển vi
- Task: tumor detection
- Spurious: hospital (scanner artifacts)
- Train: 302,436 patches. WG Gap: ~30%
- Note: "Medical AI — different hospitals = different scanners"

### AUDIO
"Cộng đồng xây dựng bốn benchmark chuẩn để đánh giá các phương pháp robust.

Waterbirds: dataset nhân tạo, spurious correlation được kiểm soát chính xác. Lý tưởng để test phương pháp trong môi trường clean.

CelebA: khuôn mặt celebrity. Task là phát hiện tóc vàng, nhưng trong dataset, tóc vàng tương quan mạnh với giới tính nữ. AI học được: blonde equals female, và ngược lại.

CivilComments: moderation nội dung độc hại online. Nhưng từ ngữ nhận diện nhóm dân số — như tên tôn giáo hay chủng tộc — tương quan với việc bị gán nhãn toxic, dù không phải nguyên nhân. AI học bias nguy hiểm.

Camelyon17: phát hiện khối u từ ảnh kính hiển vi. Spurious là artifact của máy scanner từ các bệnh viện khác nhau. AI học cách nhận ra máy, không phải khối u."

---

## Scene B2 — Benchmark Disagreement: Kết quả Lẫn lộn
**~2 phút**

### VISUAL
- Grouped bar chart: 5 phương pháp × 4 datasets
  ERM [GRAY], IRM [BLUE_D], Group DRO [GREEN_D], JTT [YELLOW_D], CORAL [PURPLE]
- Quan sát quan trọng — animate từng điểm:
  1. ERM được tuning tốt ≈ state-of-the-art ở 2/4 datasets [ORANGE highlight]
  2. IRM win ở Waterbirds nhưng thua ở CivilComments [RED dashes]
  3. Group DRO win khi có labels, nhưng không phải luôn [GREEN]
  4. Không có phương pháp nào win tất cả 4 [RED X lớn]
- Pearson correlation heatmap giữa performance trên các dataset:
  Nhiều ô màu LẠNH (correlation thấp) → "Win ở dataset này không đảm bảo win ở dataset kia"
- Text: "BENCHMARK DISAGREEMENT — không có silver bullet"

### AUDIO
"Và đây là sự thật phũ phàng từ benchmark.

Nhìn vào kết quả thực nghiệm: không có phương pháp nào thống trị tuyệt đối. Tệ hơn: ERM được tuning cẩn thận — chọn learning rate, weight decay và augmentation tốt — thường cạnh tranh được với các phương pháp phức tạp hơn nhiều.

IRM win ở Waterbirds nhưng thua ở CivilComments. Group DRO mạnh khi có labels đầy đủ nhưng fragile khi labels ồn. JTT ổn định hơn nhưng không đỉnh cao.

Pearson correlation heatmap giữa performance trên các dataset: correlation thấp. Win ở Waterbirds không báo hiệu win ở CivilComments. Hai benchmark đang đo hai thứ khác nhau.

Điều này đặt ra câu hỏi sâu hơn: có phải phương pháp không tốt, hay chính benchmark đang có vấn đề?"

---

## Scene B3 — Are Benchmarks Realistic?
**~90 giây**

### VISUAL
- Waterbirds được tạo nhân tạo: correlation 95% được set thủ công.
  Câu hỏi: "Trong thực tế, correlation có mạnh đến 95% không?"
- CelebA: celebrity photos — không đại diện cho dân số thật.
  "Bias của celebrity ≠ bias trong ứng dụng thật"
- Biểu đồ: OOD gap ở Waterbirds (lab) vs OOD gap ở hospital EHR (real).
  Lab gap: predictable, structured. Real gap: messy, multi-source.
- Text: "Benchmark tốt về kiểm soát, nhưng đơn giản hóa quá mức"
- Hộp ORANGE: "Algorithms win benchmark ≠ algorithms work in deployment"

### AUDIO
"Một câu hỏi quan trọng thường bị bỏ qua: liệu các benchmark này có thực sự phản ánh vấn đề ngoài đời thực không?

Waterbirds có spurious correlation 95 phần trăm được set thủ công. Trong thực tế, distribution shift không đơn giản và có cấu trúc như vậy. Nó noisy, multi-source, và thay đổi không theo quy luật rõ ràng.

CelebA dùng ảnh celebrity — một nhóm dân số rất đặc biệt, không đại diện cho deployment thực tế.

Kết quả: thuật toán được thiết kế để win benchmark có thể khai thác cấu trúc nhân tạo của benchmark, không phải học robustness thật sự. Đây là model selection problem ở cấp độ meta: benchmark selection."

---

## Scene B4 — Model Selection Paradox
**~90 giây**

### VISUAL
- Vòng lặp luẩn quẩn (circular arrows, xoay):
  "Muốn chọn model OOD tốt nhất"
  → "Cần validation set OOD"
  → "Nếu có OOD val set → sao không train trực tiếp?"
  → "Đưa vào train → không còn là OOD nữa!"
  → (quay lại đầu)
- Text trung tâm: "MODEL SELECTION PARADOX" [GOLD]
- Hai lựa chọn không hoàn hảo:
  A: Dùng ID validation → không đảm bảo OOD performance
  B: Giả định biết test distribution → không thực tế
- Text: "Open Problem — chưa có lời giải hoàn hảo"

### AUDIO
"Một nghịch lý thực tiễn không có lời giải hoàn hảo.

Sau khi train ERM, IRM, và Group DRO, bạn cần chọn model nào để deploy. Bạn cần validation set OOD để đánh giá.

Nhưng nếu đã có OOD validation set, tại sao không dùng nó để train? Và nếu dùng để train, nó không còn là OOD nữa.

Dùng ID validation set thường không tương quan tốt với OOD performance. Tutorial gọi đây là một trong những open problems quan trọng nhất của lĩnh vực.

Và kể cả khi giải quyết được model selection — vẫn còn một câu hỏi lớn hơn: liệu Foundation Models có thay đổi toàn bộ bức tranh này không? Câu trả lời phức tạp hơn ta nghĩ."

---

## Scene B5 — Best Practices: Flowchart Thực tiễn
**~2 phút**

### VISUAL
- Decision flowchart, từng nhánh sáng lên theo lời đọc:
  ```
  START
    ↓
  Loại Distribution Shift?
  (Covariate / Label / Spurious)
    ↓
  Có Group Labels không?
    ├─ CÓ  → Group DRO
    └─ KHÔNG → JTT hoặc NuRD
    ↓
  Có Environments đa dạng?
    ├─ CÓ  → Thêm IRM penalty
    └─ KHÔNG → Tập trung vào data collection
    ↓
  Đang dùng Foundation Model?
    ├─ CÓ  → PfR / Last Layer Retraining trước
    └─ KHÔNG → Tune ERM kỹ làm baseline
    ↓
  LUÔN report Worst-Group Accuracy
  ```
- Cuối cùng toàn bộ cây sáng [GOLD glow].

### AUDIO
"Tutorial đúc kết thành bảy nguyên tắc thực tiễn.

Một: hiểu rõ loại distribution shift trước khi chọn phương pháp. Hai: luôn report Worst-Group Accuracy, không chỉ average. Ba: tune ERM thật kỹ làm baseline — đừng bỏ qua bước này. Bốn: nếu có group labels, Group DRO là lựa chọn mạnh nhất. Năm: nếu không, JTT hoặc NuRD là điểm khởi đầu tốt. Sáu: với foundation models, thử Last Layer Retraining trước khi fine-tune toàn bộ. Bảy: thu thập thêm dữ liệu đa dạng môi trường — data collection thường hiệu quả hơn mọi algorithmic fix.

Bây giờ ta đã có bức tranh đầy đủ về các phương pháp và benchmark. Câu hỏi cuối cùng: trong thời đại của GPT, CLIP, và Gemini — Foundation Models có thay đổi mọi thứ không?"
