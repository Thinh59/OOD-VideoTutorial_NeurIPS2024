# KỊCH BẢN V3 — PART VIII, IX, X
## NuRD + Group DRO + JTT

---

# PART VIII — NuRD: "Lọc Sạch Nuisance"

---

## Scene N1 — NuRD: Ý tưởng cốt lõi
**~90 giây**

### VISUAL
- Tiêu đề: "NuRD — Nuisance-Randomized Distillation"
- Pipeline đơn giản:
  `[X] → [Φ: Encoder] → [Φ(X): Representation] → [w] → [Ŷ]`
- Câu hỏi: "Làm sao biết Φ(X) có còn chứa Z (nuisance) không?"
- Điều kiện độc lập xuất hiện:
  `Y ⊥ Z | Φ(X)`
- Giải thích từng phần:
  - Y ⊥ Z: "Y và Z độc lập..."
  - | Φ(X): "...khi đã biết representation"
  - Nghĩa là: "Φ(X) không còn thông tin về Z ngoài những gì cần để predict Y"
- Diagram: Z bị lọc ra khỏi Φ(X). Chỉ còn Y-relevant information.

### AUDIO
"Chính vì IRM gặp khó khăn khi environment không đủ đa dạng, NuRD — Nuisance-Randomized Distillation — tiếp cận vấn đề từ một góc khác: thay vì tìm invariance qua environments, hãy trực tiếp loại bỏ nuisance khỏi representation.

Điều kiện cốt lõi của NuRD: Y độc lập với Z khi đã có Φ(X). Nói dễ hiểu: representation Φ(X) không được chứa thêm thông tin về nuisance Z ngoài những gì đã được encode vào Y.

Nếu điều kiện này thỏa mãn, bất kỳ bộ phân loại nào train trên Φ(X) cũng không thể khai thác Z — vì Z đã bị lọc ra.

Nhưng câu hỏi thực tế là: làm sao phát hiện được Z là gì để mà lọc?"

---

## Scene N2 — Phát hiện Nuisance: Semantic Corruption
**~90 giây**

### VISUAL
- Ví dụ NLP: câu gốc "The movie was incredible and the acting superb."
- Bước 1 — N-gram randomization: xáo trộn thứ tự từ:
  "incredible was The movie and superb acting the."
  Label: "N-gram randomized — ngữ nghĩa mất, n-gram bias còn"
- Bước 2 — Cho model dự đoán trên câu bị xáo trộn.
  Nếu model vẫn predict đúng → đang dùng n-gram shortcut, không phải ngữ nghĩa.
- Animate: câu gốc [BLUE_D] → xáo trộn [ORANGE] → model predict → accuracy vẫn cao [RED flash]
- Text: "Semantic Corruption = can thiệp vật lý để lộ shortcut"
- Bổ sung ví dụ vision: ảnh X-ray → che patch ngẫu nhiên → model vẫn predict ung thư.
  "Model đang nhìn vào artifact của máy, không phải khối u."

### AUDIO
"Câu hỏi căn bản: làm sao biết model đang dùng spurious feature nào?

Kỹ thuật đầu tiên: Semantic Corruption. Ý tưởng: nếu ta phá hủy ngữ nghĩa thực sự của input nhưng giữ lại spurious feature, model vẫn predict tốt thì nó đang dùng shortcut.

Trong NLP: xáo trộn thứ tự từ. Câu văn mất ngữ nghĩa hoàn toàn — nhưng n-gram statistics, tần suất từ, vẫn còn. Nếu model sentiment analysis vẫn đúng 80 phần trăm sau khi xáo trộn, nó đang đếm từ, không hiểu câu.

Trong vision: che random patches của ảnh X-ray. Nếu model vẫn detect ung thư — và khối u nằm trong patch bị che — model đang dùng artifact của thiết bị chụp, không phải khối u thật.

Semantic Corruption cho ta map: shortcut nào đang được khai thác."

---

## Scene N3 — Vision Masking: Phát hiện bằng Che
**~90 giây**

### VISUAL
- Ảnh chim trên nền nước [BLUE_D frame].
- GradCAM / Attention map: model ERM tập trung vào NỀN, không phải con chim.
  Highlight vùng nền [RED glow].
- Bước Masking: che nền → chỉ còn con chim.
  Model mới predict: "Waterbird" → nhưng accuracy DROP xuống 60%.
  "Bằng chứng: model đang dùng nền."
- Bước ngược: che con chim → chỉ còn nền.
  Model cũ vẫn predict đúng với accuracy cao.
  [RED flash] "Confirmational: nền = spurious feature chính"
- Text: "Vision Masking = Semantic Corruption cho ảnh"

### AUDIO
"Với dữ liệu hình ảnh, Semantic Corruption có dạng Vision Masking — che đi các phần của ảnh.

Cách làm: lấy model ERM đã train, xem attention map hoặc GradCAM — bản đồ cho thấy model đang nhìn vào vùng nào. Với Waterbirds, model ERM chủ yếu nhìn vào nền — nước hay đất — chứ không phải con chim.

Kiểm chứng: che nền đi, chỉ để lại con chim. Accuracy model ERM giảm mạnh — bằng chứng nó đang dùng nền.

Che con chim đi, chỉ để lại nền. Accuracy vẫn cao — xác nhận nền là shortcut chính.

Vision Masking là công cụ diagnostic mạnh: nó không chỉ nói 'model đang dùng shortcut' mà còn nói 'shortcut nằm ở đâu'."

---

## Scene N4 — Teacher-Student Distillation
**~2 phút**

### VISUAL
- Hai mô hình song song:
  - Teacher [ORANGE, lớn]: được train trên corrupted input (n-gram shuffled / masked)
    → Teacher chỉ có thể học shortcut Z, không có ngữ nghĩa thật
  - Student [BLUE_D, nhỏ hơn]: được train trên original input
- Quá trình distillation:
  `Teacher(X_corrupted) → soft labels [p₁, p₂, ...]`
  `Student học: predict Y AND diverge from Teacher`
- Công thức:
  `L_student = L_CE(ŷ, y) + α · L_KL(f_student(X) ‖ f_teacher(X_corrupted))`
  Với dấu NGƯỢC: student bị phạt khi GIỐNG teacher → ép student học điều KHÁC teacher.
- Animate: Teacher confident về nền → Student bị ép phải tìm signal khác → học hình dáng con vật.
- Text: "Teacher dạy student những gì KHÔNG nên học"

### AUDIO
"NuRD dùng một kỹ thuật tinh tế: Teacher-Student distillation ngược.

Ý tưởng: train một Teacher model trên corrupted input — ví dụ câu văn đã bị xáo trộn, hoặc ảnh đã che mất semantic content. Teacher này CHỈ có thể học shortcuts vì semantic content đã bị phá hủy.

Student model được train trên input gốc, với hai mục tiêu đồng thời: một, predict đúng nhãn Y. Hai, và đây là phần quan trọng, diverge khỏi Teacher — tức là đưa ra prediction KHÁC Teacher khi có thể.

Vì Teacher đã học hết shortcuts, divergence penalty ép Student phải tìm signal khác — những gì Teacher không thể học từ corrupted input. Đó chính là semantic signal, causal features.

Đây là một cơ chế elegant: Teacher không dạy Student những gì đúng, mà dạy những gì sai để Student tránh."

---

## Scene N5 — Mutual Information Intuition
**~90 giây**

### VISUAL
- Diagram Venn: 3 vòng tròn chồng nhau:
  I(Φ(X); Y) [BLUE_D] — thông tin về nhãn
  I(Φ(X); Z) [RED] — thông tin về nuisance
  I(Φ(X); X) [GRAY] — tổng thông tin
- Mục tiêu NuRD được visualize:
  `maximize I(Φ(X); Y)` → vòng BLUE_D lớn ra
  `minimize I(Φ(X); Z)` → vòng RED nhỏ lại
- Vùng chồng lấp: "Thông tin về Z mà không cần để predict Y → đây là spurious"
- Công thức đầy đủ:
  `max_Φ  I(Φ(X); Y)  −  β · I(Φ(X); Z)`
- Text: "NuRD = Information Bottleneck có định hướng"

### AUDIO
"Nhìn NuRD qua lăng kính information theory cho thấy bức tranh đầy đủ hơn.

Mục tiêu: maximize thông tin mà Φ(X) chứa về Y — để predict tốt — trong khi minimize thông tin mà Φ(X) chứa về Z — để không dùng shortcut.

Đây là dạng Information Bottleneck có định hướng: thay vì chỉ compress thông tin tổng quát, ta compress theo hướng loại bỏ Z cụ thể.

Tham số β kiểm soát trade-off: β lớn → loại Z triệt để hơn nhưng có thể mất một số thông tin về Y. β nhỏ → an toàn hơn nhưng Z có thể lọt qua.

Kết hợp với Teacher-Student distillation và Semantic Corruption, NuRD tạo thành một pipeline hoàn chỉnh: phát hiện nuisance → loại bỏ nuisance → train representation sạch.

Chính vì những kết quả đầy hứa hẹn của NuRD trên NLP, cộng đồng bắt đầu tìm kiếm phương pháp tương tự cho structured data — nơi mà group labels đôi khi có thể thu thập được. Và đó là bối cảnh ra đời của Group DRO."

---
---

# PART IX — GROUP DRO: "Tối ưu cho Kẻ Yếu Nhất"

---

## Scene 5.1 — Group DRO: Công thức Đầy đủ
**~2.5 phút**

### VISUAL
- Pie chart Waterbirds (4 mảnh):
  Waterbird+Water: 45% [BLUE_D], Landbird+Land: 45% [GREEN_D]
  Waterbird+Land: 5% [RED nhấp nháy], Landbird+Water: 5% [RED nhấp nháy]
- Công thức ERM: `min_θ Σ_g p_g · 𝔼_g[ℓ]`
  Mũi tên: "p_g nhỏ → bị bỏ qua"
- TransformMatchingTex: `Σ_g p_g` → `max_g`:
  ```
  min_h  max_{g∈G}  𝔼_{(x,y)~P_g} [ℓ(h(x), y)]
  ```
- "max" xuất hiện GOLD, glow. Text: "Thay trung bình bằng worst-case"
- Expand công thức thành 2 phần:
  - **Inner maximization**: `max_{g∈G} R_g(h)` → tìm group đang tệ nhất
  - **Outer minimization**: `min_h` → tối ưu model cho group đó
- Vòng lặp animate:
  Step 1: tính R_g cho mọi group → highlight group tệ nhất
  Step 2: upweight group đó → update h
  Step 3: quay lại Step 1

### AUDIO
"Group DRO thay đổi mục tiêu bằng một từ: max.

ERM minimize trung bình có trọng số. Nhóm nhỏ có trọng số nhỏ — tự động bị bỏ qua.

Group DRO viết lại bài toán hoàn toàn: minimize over h, maximize over g. Hai lớp tối ưu lồng nhau.

Inner maximization: với mô hình h hiện tại, tìm group nào đang có risk cao nhất. Đây là worst-case group.

Outer minimization: cập nhật h để giảm risk của worst-case group đó.

Thuật toán lặp lại: group nào tệ nhất thì được upweight, h phải quan tâm đến group đó. Vòng tiếp theo, có thể group khác tệ hơn — lại upweight group mới.

Kết quả: mọi group đều được bảo vệ. Không group nào bị bỏ lại phía sau."

---

## Scene 5.2 — Oracle vs Practical: Giới hạn của Group DRO
**~90 giây**

### VISUAL
- Hai cột: "Oracle Setting" [GOLD] vs "Practical Setting" [GRAY]
- Oracle:
  - Biết chính xác group label (g) của mọi điểm training
  - Biết R_g cho mọi g
  - Group DRO hoạt động hoàn hảo
- Practical:
  - Group label cần annotation thủ công → tốn kém
  - Với Waterbirds: phải gán nhãn "nền là nước hay đất" cho hàng vạn ảnh
  - Với CivilComments: phải gán nhãn demographic identity cho mọi comment
- Bảng chi phí annotation:
  | Dataset | Số mẫu | Chi phí ước tính |
  |---------|--------|-----------------|
  | Waterbirds | 4,795 | ~$500 |
  | CelebA | 202,599 | ~$20,000 |
  | CivilComments | 448,000 | ~$45,000 |
- Text: "Oracle Group DRO rất mạnh. Nhưng ai trả tiền annotation?"

### AUDIO
"Group DRO có một điểm mạnh rõ ràng: khi group labels đầy đủ, nó consistently là phương pháp tốt nhất trên hầu hết benchmark.

Nhưng đây là vấn đề thực tế. Group DRO cần biết group label của từng điểm training. Với Waterbirds: mỗi ảnh cần nhãn 'nền là nước hay đất'. Với CelebA: mỗi khuôn mặt cần nhãn giới tính. Với CivilComments: mỗi comment cần nhãn demographic.

Annotation thủ công cho hàng trăm nghìn mẫu không khả thi. Và kể cả khi có ngân sách, annotation con người có sai số và bias.

Chính vì limitation này, cộng đồng đã phát triển hai hướng: một là tự động hóa annotation bằng Foundation Models — đó là PfR ta sẽ thấy sau. Hai là không cần annotation group — đó là JTT ngay bây giờ."

---
---

# PART X — JTT: "Để ERM Tự Chỉ Ra Điểm Yếu"

---

## Scene 6.1 — JTT: Hai vòng Train
**~2.5 phút**

### VISUAL
- Câu hỏi lớn: "Nếu không biết mỗi điểm thuộc nhóm nào... làm sao tìm được nhóm thiểu số?"
- Text xuất hiện: "Hãy để ERM tự chỉ ra."
- Timeline 2 giai đoạn:

**GIAI ĐOẠN 1 — ERM sơ bộ (5 epochs):**
- Thanh progress ngắn.
- Kết quả: 2 rổ xuất hiện:
  - Rổ GRAY (đúng): mờ. "Dễ — shortcut hoạt động"
  - Rổ GOLD (sai): sáng, nhấp nháy. "Khó — shortcut sai hướng!"
- Giải thích: (Penguin, tuyết) → shortcut đúng → rổ GRAY. (Penguin, cát) → shortcut sai → rổ GOLD.

**GIAI ĐOẠN 2 — Train robust:**
- Lấy rổ GOLD. Nhân bản K=20 lần (animate: con số K=20 xuất hiện to).
- Dataset mới: rổ GOLD chiếm tỉ lệ lớn hơn. Train mô hình thứ 2.

**Kết quả:**
- ERM: Worst-Group = 32% [RED]
- JTT: Worst-Group = 71% [GREEN]
- Label: "← Không cần một nhãn nhóm nào!"

### AUDIO
"JTT — Just Train Twice — có câu trả lời thanh lịch: hãy để ERM tự chỉ ra điểm yếu.

Bước một: train một mô hình ERM nhỏ trong vài epochs — đủ để nó học shortcuts, nhưng chưa memorize. Nhìn vào những điểm mà mô hình này dự đoán sai.

Tại sao những điểm bị sai lại quan trọng? Vì mô hình ERM học shortcuts ngay lập tức. Điểm nào thuộc nhóm đa số — shortcut hoạt động — dự đoán đúng. Điểm nào thuộc nhóm thiểu số — shortcut sai hướng — dự đoán sai.

Những điểm bị sai chính xác là minority: penguin trên cát, bò trên cát — những trường hợp mà shortcut 'nền màu gì' chỉ sai hướng.

Bước hai: gom những điểm sai đó, nhân bản K=20 lần, tạo dataset mới cân bằng hơn. Train mô hình thứ hai trên dataset này.

Kết quả trên Waterbirds: Worst-group accuracy tăng từ 32 lên 71 phần trăm — mà không cần một nhãn nhóm thủ công nào.

ERM đã tự lộ ra điểm yếu của chính mình."

---

## Scene 6.2 — So sánh Methods: Ai tốt khi nào?
**~90 giây**

### VISUAL
- Bảng so sánh 5 methods:

| Method | Cần group labels? | Cần environments? | Worst-Group Acc | Phù hợp khi |
|--------|------------------|-------------------|-----------------|-------------|
| ERM | Không | Không | Thấp | Baseline |
| Reweighting | Có (hoặc ước lượng) | Không | Trung bình | Dataset nhỏ |
| IRM | Không | CÓ (đa dạng) | Cao (nếu environments tốt) | Environments rõ |
| NuRD | Không | Không | Cao (NLP) | NLP, vision có corruption |
| Group DRO | CÓ | Không | Cao nhất | Có oracle labels |
| JTT | Không | Không | Cao | Không có labels/environments |

- Highlight: không có phương pháp nào win tất cả.
- Hộp GOLD: "Chọn method = chọn giả định phù hợp với bài toán của bạn"

### AUDIO
"Sau khi đi qua năm phương pháp, cần nhìn toàn cảnh: không có silver bullet.

Reweighting đơn giản nhưng thất bại với mạng lớn. IRM thanh lịch về lý thuyết nhưng cần environments chất lượng cao. NuRD mạnh với NLP nhưng cần thiết kế corruption cẩn thận. Group DRO mạnh nhất khi có labels. JTT linh hoạt nhất khi không có gì.

Chọn phương pháp nào phụ thuộc vào giả định bạn có thể làm: bạn có environments không? Bạn có group labels không? Bạn có thể thiết kế corruption không?

Hiểu điều này quan trọng hơn là nhớ công thức. Mỗi phương pháp là lời giải cho một bài toán có giả định cụ thể.

Nhưng trong thực tế — kể cả khi bạn chọn đúng phương pháp — còn một câu hỏi lớn hơn: các benchmark ta đang dùng để đánh giá có thực sự phản ánh robustness thật không? Đây là câu hỏi mà phần tiếp theo sẽ trả lời, và câu trả lời không dễ chịu."
