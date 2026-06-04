# KỊCH BẢN V3 — PART IV, V, VI
## (Mathematical Assumptions → Causal View → Reweighting)

---

# PART IV — MATHEMATICAL ASSUMPTIONS: "Mô hình toán học của Shortcut"

---

## Scene 1.4A — Generative Model của Spurious Features
**~2 phút**

### VISUAL
- Màn hình đen. Công thức xuất hiện từng số hạng:
  `x = y·φ* + y·z·ψ* + ξ`
- Bảng giải thích từng thành phần xuất hiện từng dòng:
  | Ký hiệu | Tên | Ý nghĩa |
  |---------|-----|---------|
  | x | Input | Bệnh án / Bức ảnh |
  | y | Label | Bệnh / Loài vật |
  | φ* | Causal feature direction | Hướng đặc trưng nhân quả |
  | z | Spurious attribute | Thuộc tính ảo (bệnh viện A/B) |
  | ψ* | Spurious feature direction | Hướng đặc trưng ảo |
  | ξ | Noise | Nhiễu ngẫu nhiên |
- Animate: x bị phân tích thành 3 vector trong không gian: φ* [BLUE_D], ψ* [RED], ξ [GRAY]
- Highlight RED `y·z·ψ*`: "Đây là phần spurious — phụ thuộc VÀO cả nhãn Y VÀ môi trường Z"

### AUDIO
"Để hiểu tại sao gradient descent luôn chọn shortcut, ta cần một mô hình toán học chính xác cho dữ liệu.

Mô hình tuyến tính đơn giản nhất: x bằng y nhân phi-star, cộng y nhân z nhân psi-star, cộng nhiễu xi.

Phi-star là hướng của causal feature trong không gian đặc trưng — hình dáng con vật, triệu chứng thật. Psi-star là hướng của spurious feature — màu nền, phong cách viết bác sĩ. Z là biến môi trường — bệnh viện A hay B, Bắc Cực hay sa mạc.

Chú ý số hạng spurious: nó phụ thuộc vào cả Y và Z. Khi Z bằng 1, spurious feature và causal feature đều hữu ích để dự đoán Y. Khi Z thay đổi giữa các môi trường, spurious feature trở nên không đáng tin.

Câu hỏi là: trong mô hình này, gradient descent sẽ học φ* hay ψ* trước?"

---

## Scene 1.4B — Nhóm Đa Số và Nhóm Thiểu Số
**~90 giây**

### VISUAL
- Pie chart xuất hiện với 2 phần:
  - 95% BLUE_D: "Majority: Z = Y (spurious khớp nhãn)"
  - 5% RED: "Minority: Z ≠ Y (spurious trái nhãn)"
- Công thức:
  `P(Z = Y) = 0.95`
  `P(Z ≠ Y) = 0.05`
- Ví dụ cụ thể:
  - Majority (95%): penguin trên tuyết + camel trên cát → shortcut đúng
  - Minority (5%): penguin trên cát + camel trên tuyết → shortcut sai
- Animate: chấm RED nhỏ ở minority, rất khó nhìn thấy trong đám đông BLUE_D.
- Text: "95-5 split — không bất thường. Đây là cấu trúc của hầu hết dataset thực tế."

### AUDIO
"Trong dataset thực tế, spurious correlation hiếm khi hoàn hảo 100 phần trăm. Cấu trúc phổ biến: 95 phần trăm dữ liệu là nhóm đa số — spurious attribute khớp với nhãn. Chỉ 5 phần trăm là nhóm thiểu số — spurious attribute trái chiều nhãn.

Penguin trên tuyết và camel trên cát chiếm 95 phần trăm. Penguin trên cát và camel trên tuyết chỉ 5 phần trăm.

Với ERM, 5 phần trăm thiểu số này hầu như vô hình. Chúng đóng góp quá nhỏ vào average loss để buộc model học đặc trưng đúng.

Nhưng khi test distribution thay đổi — bệnh viện mới, quốc gia mới — nhóm thiểu số đó đột nhiên chiếm đa số. Và model sụp đổ."

---

## Scene 1.4C — Simplicity Bias: Tại sao GD chọn Z trước
**~2 phút**

### VISUAL
- Không gian tham số 2D: trục x = "trọng số theo φ* (causal)", trục y = "trọng số theo ψ* (spurious)"
- Điểm xuất phát: origin (0,0).
- Loss landscape: đường đồng mức (contour). Quan trọng: ψ* có gradient DỐC HƠN so với φ* ở gần origin.
- Animate: gradient descent step đầu tiên → bước lớn hơn theo trục ψ* (spurious).
- Sau nhiều bước: mô hình nằm gần trục ψ*, ít dùng φ*.
- Text: "Spurious feature có gradient lớn hơn → Gradient Descent chọn nó trước"
- Hộp giải thích:
  ψ* dễ học vì: signal mạnh (95% data), feature đơn giản (1 bit: bệnh viện A hay B)
  φ* khó học vì: cần kết hợp nhiều chiều, phức tạp hơn

### AUDIO
"Đây là Simplicity Bias — một trong những insight quan trọng nhất của tutorial.

Trong không gian tham số, gradient descent bắt đầu từ điểm khởi tạo ngẫu nhiên. Nó di chuyển theo hướng giảm loss nhanh nhất.

Câu hỏi: hướng nào nhanh hơn — theo phi-star hay psi-star?

Spurious feature psi-star có gradient lớn hơn ở gần origin vì hai lý do. Thứ nhất, signal của nó mạnh: 95 phần trăm dữ liệu có spurious correlation. Thứ hai, feature này đơn giản — chỉ cần 1 bit thông tin: bệnh viện A hay B.

Causal feature phi-star phức tạp hơn nhiều — cần tổng hợp nhiều chiều để nhận dạng hình thái học của penguin.

Kết quả: gradient descent chọn psi-star trước, đặt nhiều trọng số vào spurious direction. Nó có thể bao giờ quay lại học phi-star không? Có — nhưng chỉ khi spurious feature không đủ để giảm loss nữa. Và với 95 phần trăm data ủng hộ nó, điều đó hiếm khi xảy ra.

Đây không phải lỗi kỹ thuật. Đây là thuộc tính cơ bản của gradient-based optimization. Và chính vì vậy, ta cần can thiệp có chủ đích."

---
---

# PART V — CAUSAL VIEW: "Tại sao, không chỉ là Như thế nào"

---

## Scene 3.1 — Structural Causal Model
**~2.5 phút**

### VISUAL
- Node GOLD ở trung tâm: Y (Nhãn)
- Node BLUE_D bên trái: X_core (Causal features — hình dáng con vật)
  Mũi tên dày BLUE_D: X_core → Y. Label: "Nhân quả thật"
- Node ORANGE góc trên: E (Môi trường)
  Mũi tên ORANGE: E → X_spur
- Node RED bên phải: X_spur (Spurious features — màu nền)
  Mũi tên RED: Y → X_spur. Label: "Y gây ra ngữ cảnh → ngữ cảnh gây ra nền"
- Toàn bộ SCM:
  ```
       E (Môi trường)
      ↙              ↘
  X_core ──→ Y ──→ X_spur
  [BLUE_D]  [GOLD]  [RED]
  ```
- Mũi tên đứt RED từ X_spur → Y: "AI đang học điều này ←" + ký hiệu gạch chéo

### AUDIO
"Hãy xây dựng Structural Causal Model cho bài toán này.

Bắt đầu từ Y — nhãn. Con vật là penguin hay camel. Y quyết định đặc trưng vật lý: X_core. Bốn chân hay hai chân, lưng thẳng hay lưng bướu. Đây là mũi tên nhân quả thật.

Nhưng màu nền đến từ đâu? Khi nhiếp ảnh gia chụp penguin, họ đến Bắc Cực. Đây là quyết định của môi trường E. Môi trường E tạo ra X_spur — màu nền trắng. Không phải penguin trực tiếp chọn màu nền.

Tuy nhiên vì trong train data penguin đi với E là Bắc Cực, có tương quan giữa Y và X_spur. AI nhìn thấy tương quan này và học nó. Đây là bẫy: AI đang dự đoán ngược chiều nhân quả — từ hệ quả suy ra nguyên nhân.

Khi E thay đổi — penguin ở sa mạc — tương quan đó biến mất. Chỉ mũi tên X_core đến Y là không bao giờ thay đổi."

---

## Scene 3.2 — Môi Trường thay đổi, Liên Kết ảo vỡ tan
**~1.5 phút**

### VISUAL
- Giữ SCM từ 3.1. Node E sáng lên. Text E thay đổi 3 lần:
  "Đồng cỏ" → "Bãi biển" → "Sa mạc"
- Mỗi lần E đổi: mũi tên Y→X_spur nhấp nháy RED, sau đó fracture (vỡ vụn, mảnh fly out).
- Sau 3 lần: mũi tên RED biến mất. Chỉ còn X_core→Y [BLUE_D sáng, glow].
- Text: "Causal Features = INVARIANT | Spurious Features = BRITTLE"
- Câu hỏi xuất hiện: "Làm thế nào để buộc AI chỉ học những thứ bất biến?"

### AUDIO
"Hãy xem điều gì xảy ra khi môi trường thay đổi.

E bằng đồng cỏ: mối liên hệ giữa Y và X_spur tồn tại — penguin đi với nền trắng. E bằng bãi biển: mối liên hệ đó lung lay. E bằng sa mạc: biến mất hoàn toàn.

Nhưng mũi tên từ X_core đến Y không bao giờ thay đổi. Dù ở đồng cỏ, bãi biển, hay sa mạc — penguin vẫn có hình dáng penguin.

SCM cho ta thấy rõ: spurious features là hệ quả của môi trường, không phải nguyên nhân của nhãn. Khi môi trường thay đổi, chúng thay đổi theo. Causal features thì không.

Câu hỏi là: làm thế nào buộc mô hình chỉ học X_core? Chính vì bài toán có cấu trúc nhân quả rõ ràng như vậy, ta có nhiều hướng tiếp cận. Và hướng đầu tiên — đơn giản nhất — là reweighting."

---
---

# PART VI — REWEIGHTING FAMILY: "Cân bằng lại Trọng số"

---

## Scene RW1 — Reweighting Principle: Ý tưởng cơ bản
**~90 giây**

### VISUAL
- Công thức ERM gốc: `L = (1/n) Σᵢ ℓᵢ`
- TransformMatchingTex: `(1/n)` → `wᵢ`:
  `L = Σᵢ wᵢ · ℓᵢ`
- Scatter plot: điểm majority [BLUE_D, nhỏ] và minority [RED, nhỏ].
- Animate: điểm minority được "phóng to" (glow, circle to ra xung quanh).
  Trọng số wᵢ: majority = 0.5, minority = 10.
- Text: "Reweighting = cho thiểu số tiếng nói lớn hơn trong loss function"
- Constraint: `Σᵢ wᵢ = 1` (vẫn là xác suất hợp lệ)

### AUDIO
"Ý tưởng đơn giản nhất để chống shortcut: thay vì để mọi điểm dữ liệu đóng góp bằng nhau vào loss, ta gán trọng số lớn hơn cho nhóm thiểu số.

Công thức thay đổi từ trung bình đều sang trung bình có trọng số: L bằng tổng wᵢ nhân ℓᵢ.

Nếu minority chỉ chiếm 5 phần trăm nhưng ta gán trọng số 10 lần lớn hơn, chúng chiếm 50 phần trăm contribution vào loss. Model bây giờ phải quan tâm đến nhóm đó.

Nhưng vấn đề là: làm sao ta biết trọng số đúng phải là bao nhiêu?"

---

## Scene RW2 — Oracle Reweighting: Nếu biết tất cả
**~60 giây**

### VISUAL
- Hộp GOLD: "Oracle setting — giả sử ta biết phân phối thật"
- Công thức trọng số tối ưu:
  `wᵢ = P_test(Xᵢ, Yᵢ) / P_train(Xᵢ, Yᵢ)`
  hoặc đơn giản hơn:
  `wᵢ ∝ 1 / P_train(Z=zᵢ | Y=yᵢ)`
- Giải thích: điểm nào hiếm trong train (P_train nhỏ) → trọng số lớn
- Ví dụ: penguin trên cát (P_train = 5%) → w = 20 lần
- Text: "Nếu biết P(Z|Y), oracle reweighting loại bỏ hoàn toàn spurious correlation"

### AUDIO
"Trong trường hợp lý tưởng — oracle setting — nếu ta biết phân phối thật, trọng số tối ưu là tỉ lệ giữa phân phối test và train.

Đơn giản hơn: điểm nào hiếm trong tập train — tức là không được đại diện đủ — nhận trọng số lớn hơn. Penguin trên cát, xuất hiện chỉ 5 phần trăm trong train, nhận trọng số 20 lần so với trung bình.

Với oracle reweighting hoàn hảo, spurious correlation bị loại bỏ hoàn toàn về mặt lý thuyết. Nhưng đây là oracle — ta không biết P_train(Z|Y) trong thực tế.

Và ngay cả khi ta ước lượng được trọng số tốt, vẫn còn một vấn đề căn bản hơn."

---

## Scene RW3 — Tại sao Reweighting Thất bại: Interpolation
**~2 phút**

### VISUAL
- Scatter plot: minority dots [RED] với trọng số lớn (circles to).
- Mô hình nhỏ (3-4 neurons): loss landscape có valley rõ ràng theo minority.
  Model học được minority đúng. ✓
- Animate: model size tăng (nhiều layers hơn, connections nhiều hơn) [PURPLE].
- Loss landscape mới: model lớn có thể "uốn" đường quyết định qua từng điểm.
- Animate: loss → 0 từng bước. Text: "Loss = 0 — mô hình interpolate hoàn hảo"
- Hộp RED: "Khi loss = 0 → gradient = 0 → trọng số wᵢ không có ý nghĩa gì nữa"
- Text: "INTERPOLATION: Neural network đủ lớn luôn fit mọi điểm → Reweighting mất tác dụng"

### AUDIO
"Đây là vấn đề cơ bản của reweighting với neural networks hiện đại.

Với mô hình nhỏ, trọng số lớn cho minority thực sự ép model học nhóm đó. Loss landscape có cấu trúc rõ ràng, valley sâu nhất nằm ở nơi model hoạt động tốt cả majority lẫn minority.

Nhưng với neural networks lớn — và trong thực tế ta luôn dùng mạng đủ lớn — có một hiện tượng gọi là interpolation: mạng đủ capacity để fit HOÀN HẢO mọi điểm training, kể cả minority.

Khi loss bằng 0, gradient bằng 0. Trọng số wᵢ lớn nhân với gradient bằng 0 vẫn bằng 0. Reweighting hoàn toàn mất tác dụng.

Mô hình vẫn học shortcut — vì shortcut cho loss thấp nhất nhanh nhất — rồi sau đó dùng capacity dư để memorize các điểm minority mà không thực sự học đặc trưng đúng.

Đây là lý do reweighting đơn thuần không đủ. Ta cần can thiệp vào cấu trúc học, không chỉ trọng số. Và đó chính là ý tưởng đằng sau IRM và DRO.

Nhưng trước khi đến các phương pháp đó, ta cần hiểu một nhánh khác: làm thế nào phát hiện chính xác đặc trưng nào là nuisance để loại bỏ. Đây là bài toán mà NuRD giải quyết."

---

## Scene RW4 — Group Balancing và JTT Preview
**~60 giây**

### VISUAL
- 4 ô grid (2×2): Majority+ [lớn, BLUE_D], Majority- [lớn, YELLOW_D], Minority+ [nhỏ, RED], Minority- [nhỏ, ORANGE]
- Animate: ERM → chỉ ô lớn được tối ưu. Minority bị bỏ qua.
- Group Balancing: mỗi ô được upweight đến bằng nhau.
- Text: "Group Balancing = extreme reweighting: mọi nhóm đóng góp bằng nhau"
- Preview: "Nhưng nếu không biết nhóm nào là thiểu số? → JTT (sau)"

### AUDIO
"Một biến thể của reweighting là Group Balancing: thay vì trọng số liên tục, ta đơn giản đảm bảo mỗi nhóm đóng góp bằng nhau vào loss — 25 phần trăm mỗi nhóm, dù kích thước thực tế khác nhau nhiều.

Group Balancing mạnh hơn reweighting thông thường trong nhiều setting. Nhưng nó vẫn cần biết nhóm nào là thiểu số.

Sau này ta sẽ thấy JTT — Just Train Twice — một cách thông minh để tìm minority mà không cần nhãn nhóm. Nhưng trước tiên, hãy đến phương pháp có nền tảng lý thuyết vững chắc nhất: IRM."
