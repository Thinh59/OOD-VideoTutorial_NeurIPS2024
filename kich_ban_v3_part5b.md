# KỊCH BẢN V3 — PART XII & XIII
## Foundation Models + AI Fixing AI + Kết luận

---

# PART XII — FOUNDATION MODELS: "Hứa hẹn, Vỡ mộng, và Tái sinh"

---

## Scene 7.0 — The Promise of Scale: Accuracy on the Line
**~2 phút**

### VISUAL
- Đồ thị scatter: trục x = ID accuracy, trục y = OOD accuracy.
  Nhiều model khác nhau (chấm) — nhỏ đến lớn.
- Đường thẳng fit qua các chấm: "Accuracy on the Line"
  Correlation cao: ID tốt → OOD tốt.
- Text: "Nếu scale model → ID accuracy tăng → OOD accuracy tăng theo?"
- Animate: chấm lớn dần (model lớn hơn) di chuyển lên đường thẳng.
- Evidence bars: "Verified across 36 datasets — ImageNet shifts, CIFAR shifts, NLP benchmarks"
- Hộp GOLD: "Scale Law → OOD cũng được? Cộng đồng hào hứng."

### AUDIO
"Năm 2021-2022, một hiện tượng thú vị được phát hiện: Accuracy on the Line.

Khi vẽ scatter plot giữa ID accuracy và OOD accuracy của nhiều model khác nhau, chúng nằm gần như trên một đường thẳng. Model nào tốt hơn trong distribution thì cũng tốt hơn ngoài distribution.

Và scale law nói rằng: model lớn hơn, train lâu hơn, data nhiều hơn sẽ có ID accuracy cao hơn. Nếu đường thẳng đó đúng — scale cũng giải quyết OOD.

Evidence từ 36 datasets khác nhau. Cộng đồng bắt đầu hào hứng: có phải chúng ta chỉ cần scale là xong?

Câu trả lời — như thường lệ trong machine learning — phức tạp hơn nhiều."

---

## Scene 7.1 — Scale Không Giải Quyết Được: Bằng Chứng Thực
**~2 phút**

### VISUAL
- Đồ thị Worst-Group Accuracy vs Model Size:
  ERM [RED]: tăng nhẹ rồi plateau ở ~55%
  Group DRO [BLUE_D]: tăng đáng kể hơn, đạt ~75%
- Vùng Large Models (>10B params): cả hai đường đều plateau.
  Icon GPT/Gemini nằm trên đường plateau ERM.
- Text: "Bigger ≠ More Robust (for worst-group)"
- Thêm biểu đồ: Average Accuracy vs Worst-Group Accuracy cho Large Models.
  Average tăng mạnh theo scale. Worst-Group gần như không tăng.
- Animation: model lớn hơn → nhiều shortcut tinh vi hơn xuất hiện [RED, nhiều nhánh].
  "Scale amplifies capacity to memorize spurious, not to ignore them"

### AUDIO
"Nhìn vào Worst-Group Accuracy — thước đo ta thực sự quan tâm — bức tranh rất khác.

Khi model size tăng nhưng vẫn train theo ERM, worst-group accuracy gần như không tăng sau một điểm nhất định. Scale giúp average accuracy — nhưng không giải quyết spurious correlations.

Tệ hơn: mô hình lớn hơn có capacity lớn hơn để memorize spurious features tinh vi hơn. Chúng không đơn giản là màu nền — chúng là các pattern phức tạp, cross-modal, khó detect hơn.

Accuracy on the Line đúng cho distribution shifts đơn giản — như ImageNet-V2. Nhưng với spurious correlation shift — loại shift ta thực sự lo — scale không giúp ích.

Nhưng điều thú vị là với CLIP — model được train theo cách rất khác — câu chuyện có vẻ khác."

---

## Scene 7.2 — CLIP và Hứa hẹn Zero-Shot
**~2 phút**

### VISUAL
- Kiến trúc CLIP:
  `[Ảnh] → [Image Encoder] ─┐`
  `[Text] → [Text Encoder] ─┴→ Cosine Similarity → Score`
  "Train trên 400M cặp ảnh-văn bản từ internet"
- Zero-shot performance: CLIP vs ERM trên Waterbirds.
  CLIP zero-shot: ~75% worst-group. ERM: ~32%. [GREEN vs RED]
- Hộp GOLD: "CLIP không thấy Waterbirds trong train — vẫn robust hơn?"
- Giải thích trực giác: CLIP học từ diverse web data → ít bị anchor vào spurious correlation đơn lẻ.
- Nhưng... thêm counter-example:
  Gender bias trong CLIP: "doctor" → predict nam mạnh hơn nữ.
  Histogram: score "doctor" theo gender — lệch sang nam rõ ràng.

### AUDIO
"CLIP là một case study thú vị. Được train trên 400 triệu cặp ảnh-văn bản từ internet với contrastive learning — không phải supervised classification thông thường.

Zero-shot performance của CLIP trên Waterbirds đáng kinh ngạc: 75 phần trăm worst-group accuracy mà không train một lần nào trên dataset đó. ERM chỉ đạt 32 phần trăm.

Tại sao? Vì web data đa dạng hơn nhiều. CLIP đã thấy penguin ở nhiều ngữ cảnh khác nhau — không chỉ trên tuyết. Spurious correlation 'penguin equals tuyết' không đủ mạnh để dominate.

Nghe như scale thật sự cứu được OOD — ít nhất với CLIP?

Nhưng nhìn vào gender bias: từ 'doctor' trong văn bản đi kèm ảnh người trên web — phần lớn là nam. CLIP học tương quan này. Với 400 triệu ví dụ, đây trông như pattern thật."

---

## Scene 7.3 — Broken Promises: Vertical, Horizontal, No Trend
**~2 phút**

### VISUAL
- 4 scatter plots nhỏ cạnh nhau (ID acc vs OOD acc):

**Plot 1 — Vertical Line [GRAY]:**
Nhiều model cùng ID accuracy nhưng OOD accuracy khác nhau nhiều.
"Scale ID accuracy → OOD không đổi"

**Plot 2 — Horizontal Line [ORANGE]:**
Nhiều model cùng OOD accuracy dù ID accuracy khác.
"OOD bão hòa — scale không giúp"

**Plot 3 — No Trend [RED]:**
Scatter ngẫu nhiên, không có correlation.
"Với spurious shift cụ thể: không có relationship"

**Plot 4 — Negative Correlation [RED đậm]:**
Model lớn hơn → OOD TỆ HƠN.
"REVERSE SCALING — đây là cái gây sốc nhất"

- Text lớn: "Accuracy on the Line là trường hợp đặc biệt, không phải quy luật chung"

### AUDIO
"Nhìn kỹ hơn vào Accuracy on the Line trên nhiều loại shift khác nhau — bức tranh vỡ vụn.

Với một số loại shift: scale ID accuracy trong khi OOD không đổi — vertical line. Model lớn hơn chỉ memorize training distribution tốt hơn.

Với loại khác: OOD accuracy bão hòa ở một mức — horizontal line. Scale không giúp gì thêm.

Với spurious shift cụ thể: không có correlation nào cả. Đường thẳng không tồn tại.

Và đây là phát hiện gây sốc nhất: với một số loại spurious shift — đặc biệt là ICL shortcuts trong LLMs — model lớn hơn có OOD accuracy TỆ HƠN.

Accuracy on the Line là trường hợp đặc biệt khi shift đơn giản và smooth. Không phải quy luật chung."

---

## Scene 7.4 — In-Context Learning Shortcuts & Reverse Scaling
**~2 phút**

### VISUAL
- Prompt ICL:
  ```
  "The movie was incredible!" → Positive
  "Best movie of the year!"   → Positive
  "I loved this movie!"       → Positive

  "The food was terrible."    → ???
  ```
- LLM predict: "Positive" ✗. Highlight ORANGE: từ "movie" trong 3 ví dụ Positive.
- Shortcut: "movie" → Positive (spurious, chỉ do cách viết prompt)
- Đồ thị Reverse Scaling:
  x = Model Size (2.7B → 7B → 13B), y = % bị shortcut chi phối
  Đường đi LÊN [RED]: 30% → 52% → 71%
- Giải thích: "Model lớn hơn đọc context tốt hơn → nhạy hơn với pattern trong prompt → dễ bị lừa hơn"
- Text lớn: "REVERSE SCALING — Scale làm mọi thứ TỆ HƠN"

### AUDIO
"Trong thế giới LLMs, spurious shortcuts xuất hiện ở nơi bất ngờ: trong chính prompt bạn viết.

Tất cả ba ví dụ Positive đều chứa từ 'movie'. LLM học: 'movie' trong prompt → Positive. Khi gặp câu về food — không phải movie — LLM vẫn bị ảnh hưởng bởi absence của 'movie'.

Và đây là Reverse Scaling: mô hình 13 tỷ tham số bị ảnh hưởng bởi shortcut này nhiều hơn mô hình 2.7 tỷ.

Tại sao? Vì mô hình lớn hơn rất giỏi đọc và nắm bắt pattern trong context. Đây chính là khả năng tạo nên ICL. Nhưng nó cũng có nghĩa mô hình lớn hơn 'quá nhạy' với mọi pattern — kể cả pattern không liên quan.

Scale không phải thuốc chữa bách bệnh. Trong trường hợp ICL, scale còn làm bệnh nặng hơn.

Vậy là ta có một nghịch lý đẹp: scale tạo ra vấn đề mới. Nhưng chính scale cũng có thể là chìa khóa để giải quyết — chỉ cần dùng đúng cách."

---

# PART XIII — AI FIXING AI: "Dùng Scale để Sửa Scale"

---

## Scene 7.5 — PfR: Prompting for Robustness
**~2 phút**

### VISUAL
- Câu hỏi: "Group DRO cần nhãn nhóm. Annotation tốn kém. Giải pháp?"
- Pipeline PfR (3 khối):
  `[Ảnh Waterbirds] → [VLM/GPT-4V + Prompt] → [Nhãn phông nền tự động]`
  Prompt: "Describe the background: water or land?"
  Output: "water", "land", "water", ...
- Animate: ảnh đi vào VLM, nhãn bắn ra như conveyor belt.
- Kết hợp:
  `[Nhãn phông nền từ VLM] + [Nhãn bird type thủ công] → [Group DRO]`
- Kết quả:
  ```
  ERM baseline:          32%  [RED]
  Group DRO (manual):    91%  [GREEN]
  PfR (VLM labels):      91.05% [GREEN+GOLD]
  ```
- Text: "PfR = Prompting for Robustness. AI lớn gán nhãn cho AI nhỏ."

### AUDIO
"Đây là giải pháp đột phá: PfR — Prompting for Robustness.

Vấn đề cốt lõi: Group DRO cần nhãn nhóm — phải biết nền mỗi ảnh là nước hay đất. Gán nhãn thủ công cho hàng vạn ảnh rất tốn kém.

Giải pháp: dùng chính một Foundation Model lớn như GPT-4V để gán nhãn phông nền. Prompt đơn giản: 'Hãy mô tả background của ảnh này.' VLM trả về nhãn chính xác với chi phí gần như bằng không.

Kết quả trên Waterbirds: PfR đạt 91.05 phần trăm worst-group accuracy — gần bằng Group DRO với oracle labels thủ công, và gấp gần 3 lần ERM baseline.

Đây là arc đẹp nhất của câu chuyện: Scale tạo ra spurious correlation trong CLIP. Nhưng chính Scale — dưới dạng VLM mạnh — lại giúp ta gán nhãn để chạy Group DRO. Dùng AI để sửa AI."

---

## Scene 7.6 — CATO: Counterfactual Data Generation
**~2 phút**

### VISUAL
- Câu hỏi: "Ngay cả khi biết group, nếu minority quá ít để train hiệu quả?"
- Pipeline CATO:
  ```
  Bước 1: Phân tích SCM → xác định Z (spurious)
           "Z = background (water/land)"

  Bước 2: LLM + Causal Reasoning → sinh counterfactual
           "Waterbird trên đất" (đảo ngược nền)
           "Landbird trên nước" (đảo ngược nền)

  Bước 3: Dataset mới = Original + Counterfactual
           → Train model robust hơn
  ```
- Animate: từ 2 nhóm nhỏ (5% mỗi loại), CATO sinh thêm data.
  Pie chart cân bằng: từ 5%/5%/45%/45% → gần đều 4 nhóm.
- Text: "CATO = Causal Augmentation + LLM"
- Kết quả: Worst-group accuracy tăng thêm 3-5% so với PfR đơn thuần.

### AUDIO
"PfR giải quyết vấn đề annotation. Nhưng còn một vấn đề khác: dù biết group, số lượng minority samples vẫn quá ít để train hiệu quả.

CATO — Causal Augmentation — giải quyết điều này bằng cách dùng LLM và suy luận nhân quả để SINH ra dữ liệu counterfactual.

Từ SCM đã xây dựng, ta biết spurious feature là phông nền. CATO yêu cầu LLM: hãy tưởng tượng waterbird này đứng trên đất thay vì nước. Mô tả lại cảnh đó.

LLM sinh ra mô tả — hoặc thậm chí ảnh tổng hợp — của các trường hợp counterfactual. Dataset mới cân bằng hơn nhiều. Model được train trên dataset augmented này robust hơn đáng kể.

CATO là hướng kết hợp giữa nhân quả và generative AI — một trong những xu hướng nghiên cứu nóng nhất năm 2024.

Và đây chính là arc hoàn chỉnh: Scale hứa hẹn giải quyết OOD → Scale tạo ra spurious mới và phức tạp hơn → Scale thậm chí làm vấn đề tệ hơn trong ICL → Nhưng ta dùng chính Scale để gán nhãn và sinh dữ liệu → Scale sửa lỗi của Scale."

---
---

# PART XIV — KẾT LUẬN

---

## Scene 9.1 — Hành trình Tổng hợp
**~2 phút**

### VISUAL
- Camera zoom lùi chậm. Bản đồ khái niệm toàn bộ xuất hiện:
  ```
  [Intuition]         [Formalism]        [Risk Aggregation]
       ↓                   ↓                    ↓
  [ERM Failure] ──→ [OOD Definition] ──→ [Mean/Max/CVaR/DRO]
       ↓                                         ↓
  [Causal View]                          [Why Methods Differ]
  [SCM, Invariant]                              ↓
       ↓                              [Reweighting → fails]
  [Methods]                                     ↓
  [IRM → NuRD → DRO → JTT]              [IRM → NuRD → DRO]
       ↓                                         ↓
  [Benchmarks]              [Foundation Models]
  [Reality Check]           [Promise → Broken → Fix]
       ↓                          ↓
               [PfR + CATO: AI Fixes AI]
  ```
- Mọi thứ mờ dần. 3 từ xuất hiện lần lượt:
  CORRELATION [GRAY] → CAUSATION [BLUE_D] → STABILITY [GOLD, glow]
- STABILITY to nhất, particle effect nhẹ xung quanh.
- Dưới cùng: "Đây là ranh giới tiếp theo của Trí tuệ Nhân tạo."

### AUDIO
"Chúng ta đã đi một hành trình dài.

Bắt đầu từ một câu hỏi đơn giản: tại sao AI học sai? ERM tối ưu trung bình, và trung bình cho phép hy sinh thiểu số để đổi lấy majority.

Chúng ta hình thức hóa vấn đề: OOD generalization là học tốt khi phân phối thay đổi. Risk aggregation cho thấy các thuật toán khác nhau chỉ khác nhau ở cách gộp rủi ro — mean, max, CVaR, hay DRO.

Simplicity bias giải thích tại sao gradient descent luôn chọn shortcut: đặc trưng đơn giản có gradient lớn hơn.

SCM cho thấy cấu trúc nhân quả: spurious features là hệ quả của môi trường, causal features là bất biến.

Năm phương pháp — Reweighting, IRM, NuRD, Group DRO, JTT — mỗi cái là lời giải cho một giả định cụ thể. Không có silver bullet.

Benchmark cho thấy thực tế phức tạp hơn lý thuyết. Và Foundation Models — Scale thất bại nhưng Scale cứu được bằng cách khác.

Tất cả dẫn về một từ: Stability. AI ổn định không phải AI không bao giờ gặp phân phối mới. Mà là AI biết điều gì thực sự quan trọng và giữ vững điều đó dù hoàn cảnh thay đổi."

---

## Scene 9.2 — Open Problems & Credits
**~45 giây**

### VISUAL
- 3 cánh cửa chưa mở (ánh sáng hé ra từ khe):
  1. "Lý thuyết OOD cho Foundation Models"
  2. "Model Selection không cần OOD validation"
  3. "OOD trong Multimodal & Agentic AI"
- Fade in credits trên nền đen:
  ```
  Based on:
  NeurIPS 2024 Tutorial
  "Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability"
  Maggie Makar · Aahlad Manas Puli · Yoav Wald

  Produced by:
  Phan Huỳnh Châu Thịnh (Na) · Mỹ Linh · Hồng Thanh · Trọng Hòa
  Nhập Môn Học Máy · HCMUS
  GitHub: [link]
  ```

### AUDIO
"Tutorial để lại ba cánh cửa mở: lý thuyết OOD cho foundation models, model selection không cần OOD validation, và OOD trong thế giới multimodal và agentic AI.

Đây là biên giới tiếp theo. Cảm ơn các bạn đã theo dõi. Link tutorial gốc, slides, và source code Manim đều có trong phần mô tả."
