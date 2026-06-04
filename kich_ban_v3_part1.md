# KỊCH BẢN V3 — PART I & II
## Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability
### NeurIPS 2024 Tutorial — Makar, Puli, Wald

---

# PART I — INTUITION: "Khi AI tự tin mà sai"

---

## Scene 0.1 — Opening: Bệnh án của Bác sĩ
**~90 giây**

### VISUAL
- Màn hình đen → text trắng: "Một AI được huấn luyện để dự đoán bệnh từ hồ sơ bệnh án điện tử."
- 2 bệnh án xuất hiện (hộp viền trắng):
  - BA1: "89 yr old MAN, polyuria..." → AI: Diabetes ✓
  - BA2: "70 yr old GENTLEMAN, joint pain..." → AI: Arthritis ✓
  - Thanh accuracy: Hospital A — 95% [GREEN]
- Pan sang phải → Hospital B:
  - BA3: "65 yr old MAN, joint pain..." → AI: Diabetes ✗
  - Thanh: Hospital B — 72% [RED]. Dấu "?" GOLD nhấp nháy.
- Zoom vào BA1, BA2. Highlight RED: "MAN" → Diabetes, "GENTLEMAN" → Arthritis.
- Text: "AI không đọc chỉ số y khoa. Nó học thói quen viết của bác sĩ."

### AUDIO
"Hãy bắt đầu với một ví dụ thực tế. Một AI được huấn luyện để dự đoán bệnh từ hồ sơ bệnh án điện tử. Tại Bệnh viện A, nó đạt 95 phần trăm — ấn tượng.

Nhưng khi chuyển sang Bệnh viện B, accuracy rớt xuống 72 phần trăm.

Điều gì đã xảy ra? Nhìn kỹ vào dữ liệu huấn luyện. Tại Viện A, một bác sĩ cụ thể có thói quen: ông ta viết 'man' khi ghi hồ sơ bệnh nhân tiểu đường, và 'gentleman' khi ghi bệnh nhân viêm khớp. Hai từ đồng nghĩa — nhưng AI đã học được sự phân biệt này và dùng nó như một đường tắt.

Khi sang Viện B, bác sĩ mới không có thói quen đó. Shortcut biến mất. Mô hình sụp đổ.

Đây chính là vấn đề trọng tâm của tutorial này. Không phải AI thiếu dữ liệu hay thiếu tham số. Mà là AI đang học sai thứ."

---

## Scene 0.2 — Road Map
**~50 giây**

### VISUAL
- Đường ngang trái→phải, 2 lane GRAY. Biển "XUẤT PHÁT" bên trái.
- 8 trạm dừng xuất hiện lần lượt:
  [Intuition] → [Formalism] → [Risk] → [Causality] → [Methods] → [Benchmarks] → [Foundation Models] → [AI Fixing AI]
  ORANGE → GOLD → RED → BLUE_D → GREEN_D → YELLOW_D → PURPLE → TEAL
- Xe WHITE chạy từ trái, dừng ở node 1, node sáng lên.

### AUDIO
"Trong video này chúng ta sẽ đi qua tám chặng. Bắt đầu bằng trực giác về vấn đề, sau đó hình thức hóa bằng toán học, định nghĩa risk và cách đo lường robustness, nhìn qua lăng kính nhân quả, khám phá các phương pháp giải quyết từ reweighting đến IRM và DRO, đánh giá thực tế qua benchmark, rồi xem foundation models thay đổi bài toán như thế nào. Và cuối cùng, liệu AI có thể tự sửa lỗi của chính mình. Đi thôi."

---

## Scene 1.1 — ERM và Ảo ảnh Accuracy Cao
**~2 phút**

### VISUAL
- Không gian 2D: trục x = "màu nền" (trắng→vàng), trục y = "hình dáng con vật".
- 20 điểm xuất hiện: 10 BLUE_D (penguin, góc trên-trái) + 10 YELLOW_D (camel, góc dưới-phải).
- Đường phân loại WHITE 45° trượt vào. Text: "Train Accuracy = 98% ✓" [GREEN].
- Zoom vào đường → mũi tên đỏ: đường đi theo trục x (màu nền), không theo trục y.
- Điểm BLUE_D mới ở góc dưới-phải (penguin trên cát). Model predict Camel. ✗ RED.
- Đường đổi RED, pulsing. Text: "Đường này đọc MÀU NỀN — không phải CON VẬT"

### AUDIO
"Hãy bắt đầu bằng ví dụ kinh điển trong tutorial. Bạn xây dựng AI phân loại chim cánh cụt và lạc đà.

Tập dữ liệu huấn luyện: chim cánh cụt luôn đứng trên tuyết trắng, lạc đà luôn đứng trên cát vàng. Trong không gian đặc trưng hai chiều, dữ liệu chia thành hai cụm tách biệt hoàn hảo.

Thuật toán học và vẽ được một đường phân loại. Accuracy 98 phần trăm. Tuyệt vời.

Nhưng chú ý kỹ đường này đang làm gì. Nó đi theo trục ngang — đọc màu nền. Không phải trục dọc — hình dáng con vật.

Khi một chú chim cánh cụt bị đặt trên cát vàng, đường phân loại không ngần ngại: đây là lạc đà. Sai hoàn toàn.

Để hiểu tại sao, chúng ta cần nhìn vào trái tim của mọi thuật toán học máy hiện đại."

---

## Scene 1.2 — Giải phẫu ERM: Tại sao nó lười?
**~2.5 phút**

### VISUAL
- Công thức ERM xuất hiện từng phần:
  1. `min_θ` → "Tìm bộ tham số tốt nhất..."
  2. `𝔼_{(x,y)∼P_train}` → hộp ORANGE bao P_train → "...trên train data..."
  3. `[ℓ(f_θ(x), y)]` → "...giảm sai số trung bình."
- Zoom vào P_train: "ERM chỉ thấy P_train. Không hơn. Không kém."
- 2 con đường INPUT→OUTPUT:
  - Đường 1 BLUE_D (dày): "Phân tích cấu trúc hình thái" + đồng hồ cát dài
  - Đường 2 RED (đứt, ⚡): "Đếm pixel trắng/vàng" + tia chớp, 1 bước
- Viên bi WHITE lao vào Đường 2. Text: "Gradient Descent chọn con đường giảm Loss nhanh nhất"
- Đường 2 sáng, Đường 1 mờ. Text lớn: "SPURIOUS FEATURE" [RED viền GOLD]

### AUDIO
"ERM, Empirical Risk Minimization, là thuật toán học máy tiêu chuẩn. Ý tưởng đơn giản: tìm bộ tham số theta để minimize sai số trung bình trên tập train.

Nhưng chú ý: ERM chỉ có một mục tiêu duy nhất — giảm Loss. Nó không biết, không quan tâm, liệu sự giảm đó đến từ hiểu thật sự hay từ đường tắt.

Hãy hình dung từ góc nhìn Gradient Descent. Có hai con đường: phân tích hình thái học — tốn nhiều bước, khó học. Hoặc đếm pixel nền — một phép tính đơn giản.

Gradient Descent luôn chọn con đường hai. Không phải vì nó xấu xa, mà vì đó là chiều gradient giảm nhanh nhất.

Chúng ta gọi những đặc trưng như màu nền đó là Spurious Features — đặc trưng ảo. Chúng trông giống tín hiệu hữu ích trong train data, nhưng chỉ là sự trùng hợp của ngữ cảnh.

Và câu hỏi tự nhiên tiếp theo là: làm sao ta phân biệt chính xác giữa đặc trưng thật và đặc trưng ảo?"

---

## Scene 1.3 — Spurious Feature: Chính xác là gì?
**~1.5 phút**

### VISUAL
- Timeline trái→phải:
  [Nhiếp ảnh gia chụp PENGUIN] → [Chọn: Bắc Cực — Tuyết] → [Ảnh: nền trắng + penguin]
- Mũi tên BLUE_D: "PENGUIN (Y)" → "NỀN TRẮNG (X_spur)" = nhân quả thật
- Mũi tên RED đứt ngược: NỀN TRẮNG → PENGUIN. Label: "AI đang học điều này — Ngược chiều nhân quả!"
- Animate: E thay đổi "Bắc Cực"→"Sa mạc". Mũi tên RED vỡ vụn. Mũi tên BLUE_D sáng lên.
- Text: "Causal Features = INVARIANT (bất biến) | Spurious Features = BRITTLE (dễ vỡ)"

### AUDIO
"Vậy spurious feature là gì, chính xác?

Hãy nghĩ về chuỗi sự kiện tạo ra dữ liệu. Nhiếp ảnh gia muốn chụp chim cánh cụt, họ đến Bắc Cực. Con chim là nguyên nhân, nền tuyết trắng là kết quả. Mũi tên nhân quả đi từ nhãn sang nền.

Nhưng AI đang đọc ngược lại: thấy nền trắng, kết luận chim cánh cụt. Đây là dự đoán ngược chiều nhân quả.

Khi môi trường thay đổi — chim cánh cụt xuất hiện ở sa mạc — tương quan đó tan biến. Nhưng mối quan hệ nhân quả thật vẫn còn: chim cánh cụt có hình dáng chim cánh cụt dù đứng ở đâu.

Causal features ổn định qua mọi môi trường. Spurious features chỉ tồn tại ở một hoàn cảnh cụ thể.

Nhưng cho đến giờ, tất cả những gì ta nói vẫn là trực giác. Để thực sự giải quyết vấn đề, ta cần một ngôn ngữ toán học chính xác."

---
---

# PART II — FORMALIZING THE PROBLEM: "Đặt tên cho trực giác"

---

## Scene F1 — Từ Ví Dụ Lâm Sàng đến Toán Học
**~90 giây**

### VISUAL
- Bảng 3 cột xuất hiện từng hàng:
  | Ký hiệu | Ý nghĩa | Ví dụ Bệnh viện |
  |----------|---------|-----------------|
  | X | Input (đầu vào) | Bệnh án điện tử |
  | Y | Label (nhãn) | Bệnh (Diabetes/Arthritis) |
  | E | Environment (môi trường) | Bệnh viện (A hoặc B) |
- Hộp ORANGE bao "E": "Đây là biến mà ERM bỏ qua hoàn toàn"
- Ví dụ penguin xuất hiện song song:
  X = ảnh, Y = loài (penguin/camel), E = địa điểm (Bắc Cực/Sa mạc)
- Mũi tên nối 2 ví dụ → text: "Cùng một cấu trúc toán học"

### AUDIO
"Ví dụ bệnh viện và chim cánh cụt vừa rồi nghe trực giác. Nhưng để giải quyết vấn đề, ta cần đặt tên chính xác cho từng thành phần.

Ba ký hiệu cơ bản. X là input — bệnh án điện tử, hoặc bức ảnh. Y là label — loại bệnh, hoặc loài động vật. Và E là environment — môi trường — bệnh viện A hay B, Bắc Cực hay sa mạc.

Chú ý: ERM truyền thống gộp tất cả dữ liệu từ mọi môi trường lại và tối ưu trung bình. Nó không bao giờ nhìn thấy biến E. Và chính sự mù quáng đó là nguồn gốc của vấn đề.

Bây giờ ta đã có ký hiệu, hãy định nghĩa chính xác thế nào là 'học tốt ngoài phân phối'."

---

## Scene F2 — OOD Generalization là gì?
**~90 giây**

### VISUAL
- Hai hộp lớn cạnh nhau:
  - Hộp trái BLUE_D: "IN-DISTRIBUTION (ID)" → `(X,Y) ~ P_train`
  - Hộp phải GREEN_D: "OUT-OF-DISTRIBUTION (OOD)" → `(X,Y) ~ P_test`
- Dấu "≠" lớn RED giữa hai hộp: `P_train ≠ P_test`
- Animate: đám mây điểm train (BLUE_D) ở trái. Đám mây test (GREEN_D) ở phải, hình dạng khác.
- Đường phân loại fit train → kéo sang test → sai nhiều. Flash RED.
- Text: "OOD Generalization = hoạt động tốt khi P_test ≠ P_train"

### AUDIO
"Trong machine learning truyền thống, ta giả định train và test đến từ cùng một phân phối. Đây gọi là In-Distribution.

Nhưng trong thực tế, phân phối test luôn khác train. Bệnh viện mới, quốc gia mới, năm mới. Đây là Out-of-Distribution.

OOD Generalization là khả năng mô hình hoạt động tốt khi phân phối test khác phân phối train. Không phải khác một chút — mà khác về cấu trúc.

Và để nói chính xác 'khác như thế nào', ta cần khái niệm môi trường."

---

## Scene F3 — Phân Phối theo Môi Trường
**~90 giây**

### VISUAL
- Node "e" xuất hiện giữa. Text: "e ∈ E (environment)"
- 3 đám mây phân phối xuất hiện xung quanh, mỗi cái khác hình:
  - e₁ [GREEN_D]: P_{e₁}(X,Y) — đám mây hẹp, nghiêng trái
  - e₂ [YELLOW_D]: P_{e₂}(X,Y) — đám mây rộng, đối xứng
  - e₃ [PURPLE]: P_{e₃}(X,Y) — đám mây nhỏ, nghiêng phải
- Công thức: "Mỗi môi trường e tạo ra phân phối P_e(X,Y) riêng"
- Ví dụ cụ thể:
  e₁ = Bệnh viện A, e₂ = Bệnh viện B, e₃ = Bệnh viện C
- Mũi tên từ e → P_e: "Cùng bệnh, cùng triệu chứng, khác ngữ cảnh"

### AUDIO
"Mỗi môi trường e thuộc tập E tạo ra một phân phối dữ liệu riêng: P_e của X và Y.

Bệnh viện A có phân phối bệnh nhân khác Bệnh viện B. Không phải vì bệnh khác, mà vì ngữ cảnh khác — cách ghi hồ sơ, thiết bị chẩn đoán, nhân khẩu học vùng miền.

Quan trọng là: mối quan hệ nhân quả giữa triệu chứng thật và bệnh không đổi qua các môi trường. Chỉ có mối quan hệ giữa spurious features và nhãn mới thay đổi.

Và khi ta có nhiều môi trường, câu hỏi trở thành: ta muốn mô hình tốt trên MỘT phân phối cụ thể, hay trên TẤT CẢ phân phối có thể?"

---

## Scene F4 — Tập Hợp Mọi Thế Giới Có Thể
**~90 giây**

### VISUAL
- Tập hợp P xuất hiện (hình oval lớn GOLD viền):
  P = {p₁, p₂, p₃, ...}
- Bên trong: nhiều đám mây nhỏ, mỗi cái = 1 phân phối, dao động nhẹ.
- ERM: mũi tên chỉ vào 1 đám mây duy nhất (p_train). Text: "ERM chỉ tối ưu trên đây"
- Robust Learning: vòng tròn bao TOÀN BỘ P. Text: "Ta muốn tốt trên CẢ HỌ phân phối"
- Công thức xuất hiện:
  `ERM:  min_θ R_{p_train}(θ)`
  `Robust: min_θ sup_{p∈P} R_p(θ)`
- Hộp highlight GOLD: "Đây là sự khác biệt cốt lõi"

### AUDIO
"Đây là slide then chốt. Gọi P là tập hợp tất cả phân phối có thể xảy ra — tất cả bệnh viện, tất cả quốc gia, tất cả ngữ cảnh mà mô hình có thể gặp.

ERM tối ưu trên đúng một phân phối: p train. Nó không biết và không quan tâm đến phần còn lại của P.

Robust Learning thay đổi mục tiêu: ta muốn tìm mô hình hoạt động tốt trên mọi phân phối trong P. Không phải tốt trung bình — mà tốt ngay cả trong trường hợp xấu nhất.

Nhưng 'tốt' nghĩa là gì? Ta cần một cách đo lường chính xác. Và đó chính là khái niệm Risk — rủi ro."

---
---

# PART III — RISK AGGREGATION: "Đo lường Robustness"

---

## Scene R1 — Expected Risk: Rủi ro trên Một Phân Phối
**~60 giây**

### VISUAL
- Công thức xuất hiện từng phần:
  `R(h) = 𝔼_{(X,Y)~P} [L(h(X), Y)]`
- Giải thích dưới mỗi phần:
  R(h) = "Rủi ro của mô hình h"
  𝔼 = "Trung bình trên..."
  P = "...một phân phối cụ thể"
  L = "...của hàm mất mát"
- Ví dụ: nếu P = bệnh viện A, R(h) = tỉ lệ chẩn đoán sai trung bình tại viện A.
- Animate: scatter plot, mỗi điểm sáng khi được tính, R(h) cập nhật dần.

### AUDIO
"Risk, hay rủi ro, là thước đo cơ bản. Với một phân phối P cụ thể, Risk của mô hình h bằng kỳ vọng của hàm mất mát.

Nói đơn giản: R of h là xác suất mô hình mắc lỗi trung bình trên phân phối P. Nếu P là bệnh viện A, Risk là tỉ lệ chẩn đoán sai trung bình tại viện đó.

Nhưng ta có nhiều môi trường, nhiều phân phối. Câu hỏi là: khi có nhiều Risk khác nhau, ta gộp chúng lại bằng cách nào?"

---

## Scene R2 — Average Risk: Cách ERM Gộp
**~60 giây**

### VISUAL
- 3 thanh bar ngang: R_{e₁}=10%, R_{e₂}=15%, R_{e₃}=60%
  Màu GREEN_D, YELLOW_D, PURPLE
- Công thức ERM: `R_avg = (1/n) Σᵢ ℓᵢ = (1/m) Σ_e R_e`
- Animate: trung bình → R_avg = 28% [ORANGE]
- Hộp: "28% — nghe chấp nhận được?"
- Zoom vào R_{e₃} = 60% [RED, nhấp nháy]: "Nhưng nhóm này đang chịu 60%!"
- Text: "Average Risk che giấu thảm họa ở nhóm thiểu số"

### AUDIO
"ERM gộp risk bằng trung bình. Ba môi trường: risk 10, 15, và 60 phần trăm. Trung bình là 28 — nghe chấp nhận được.

Nhưng nhìn kỹ: môi trường thứ ba đang chịu 60 phần trăm lỗi. Trong y tế, đó có thể là một nhóm dân số đang bị chẩn đoán sai hơn một nửa.

Average Risk cho phép mô hình hy sinh nhóm thiểu số để giảm lỗi ở nhóm đa số. Đây chính xác là vấn đề của ERM.

Vậy thay vì trung bình, nếu ta nhìn vào trường hợp tệ nhất thì sao?"

---

## Scene R3 — Worst-Case Risk: Bảo vệ Nhóm Yếu Nhất
**~90 giây**

### VISUAL
- Giữ 3 thanh bar từ R2.
- TransformMatchingTex: `(1/m) Σ_e R_e` → `max_e R_e(h)`
- Chữ "max" xuất hiện GOLD, glow.
- Animate: thanh R_{e₃}=60% sáng lên, 2 thanh kia mờ đi.
- Text: "Worst-Case Risk = max_e R_e(h) = 60%"
- So sánh 2 mô hình:
  Model A: R_avg=28%, R_worst=60% [ORANGE/RED]
  Model B: R_avg=35%, R_worst=38% [ORANGE/GREEN]
- Câu hỏi: "Model nào deploy cho bệnh nhân thật?"
- Hộp GOLD: "Worst-Case Risk → bảo vệ nhóm bị tổn thương nhất"

### AUDIO
"Worst-Case Risk thay trung bình bằng max: tìm môi trường mà mô hình tệ nhất, và dùng đó làm thước đo.

So sánh hai mô hình. Model A có average risk 28 nhưng worst-case 60 phần trăm. Model B average 35 nhưng worst-case chỉ 38. Model nào bạn muốn deploy cho bệnh nhân thật?

Tại sao worst-case quan trọng? Bởi vì trong y tế, trong tài chính, trong luật pháp — bệnh nhân thiểu số, nhóm dân tộc ít, trường hợp hiếm — chính là những người bị tổn thương khi AI thất bại. Và họ xứng đáng được bảo vệ.

Nhưng worst-case chỉ là MỘT cách gộp risk. Thực tế có cả một họ các phương pháp."

---

## Scene R4 — Risk Aggregation Families
**~2 phút**

### VISUAL
- Bảng/heatmap 4 hàng xuất hiện lần lượt:

| Phương pháp | Công thức | Ý nghĩa |
|-------------|-----------|----------|
| Mean | `(1/m) Σ_e R_e` | ERM tối ưu cái này |
| Max | `max_e R_e` | Group DRO tối ưu cái này |
| CVaR | `E[R_e | R_e ≥ VaR_α]` | Tập trung vào đuôi phân phối |
| DRO | `sup_{P∈P} R_P(h)` | Robust với mọi phân phối |

- Mỗi hàng sáng lên khi được giải thích. Cột phải: link đến thuật toán.
- Hộp insight GOLD: "Các thuật toán khác nhau chỉ khác nhau ở cách gộp rủi ro"
- Mũi tên: Mean → Max → CVaR → DRO (mức độ bảo thủ tăng dần).

### AUDIO
"Đây là một trong những insight quan trọng nhất của tutorial: các thuật toán robust khác nhau thực chất chỉ khác nhau ở cách gộp rủi ro.

Mean — trung bình bình thường. ERM tối ưu cái này. Nhanh, đơn giản, nhưng hy sinh thiểu số.

Max — worst-case. Group DRO tối ưu cái này. Bảo vệ nhóm yếu nhất, nhưng có thể quá bi quan.

CVaR — Conditional Value at Risk. Không cực đoan như max, nhưng tập trung vào đuôi phân phối — những trường hợp tệ nhất, không phải tệ nhất tuyệt đối.

Distributionally Robust — bảo vệ trước mọi phân phối trong một tập hợp. Mạnh nhất về lý thuyết, nhưng tập hợp phải được chọn cẩn thận.

Khi bạn chọn một thuật toán robust, thực chất bạn đang chọn cách gộp risk. Hiểu điều này giúp bạn không bị lạc trong rừng thuật toán.

Bây giờ ta đã có ngôn ngữ toán học. Câu hỏi tiếp theo: tại sao ERM — tối ưu mean risk — lại chọn spurious features? Có phải chỉ vì thống kê, hay còn lý do sâu hơn?"
