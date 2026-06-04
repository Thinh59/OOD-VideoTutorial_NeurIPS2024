# KỊCH BẢN MANIM — PHIÊN BẢN 3 (PATCH: BÁM SÁT SLIDES GỐC)
## Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability
### NeurIPS 2024 Tutorial — Makar, Puli, Wald

---

## YOUTUBE DESCRIPTION TEMPLATE (Bắt buộc theo yêu cầu thầy)

```
Nhóm: [Tên nhóm]
Thành viên:
1. Phan Huỳnh Châu Thịnh (Na) - MSSV: [...]
2. Mỹ Linh - MSSV: [...]
3. Hồng Thanh - MSSV: [...]
4. Trọng Hòa - MSSV: [...]

Thông tin môn học:
- Môn học: [Tên môn] — Khóa/Lớp: [...]
- GVLT: [Tên GVLT]
- Trợ giảng: [Tên TG]
- GVTH: [Tên GVTH]

Mã nguồn Manim (GitHub): [Link GitHub repo]

Thông tin Tutorial được chọn:
- Tên: Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability
- Link: https://neurips.cc/virtual/2024/tutorial/99523
- Hội nghị: NeurIPS 2024
- Tác giả: Maggie Makar, Aahlad Manas Puli, Yoav Wald
```

---

## THAY ĐỔI SO VỚI V2 (Patch theo feedback)

| Lỗi | Trước (Hallucination) | Sau (Bám slides gốc) |
|---|---|---|
| Scene 0.1 | COVID X-ray + chiều cao vai | "man" vs "gentleman" — Clinical Notes |
| Scene 1.1 | Bò trên cỏ / Lạc đà trên cát | **Chim cánh cụt trên tuyết** / Lạc đà trên cát |
| Scene 7.3 | NLI "No one" shortcut | **ICL "movie ~ positive"** shortcut |
| Scene 7.4 | Last Layer Retraining (không có trong slides) | **Reverse Scaling + PfR + CATO** |

Nội dung bổ sung mới: Scene 7.4 (Reverse Scaling), Scene 7.5 (PfR), Scene 7.6 (CATO)

---

## BẢNG MÀU & QUY ƯỚC (dùng nhất quán toàn video)

| Đối tượng | Màu Manim | Ghi chú |
|---|---|---|
| Nền | BLACK | #000000 |
| Đặc trưng Nhân quả (Core) | BLUE_D | Tất cả thứ có tính nhân quả |
| Đặc trưng Ảo (Spurious) | RED | Shortcuts, spurious links |
| Môi trường 1 / Group 1 | GREEN_D | e1 |
| Môi trường 2 / Group 2 | YELLOW_D | e2 |
| Môi trường 3 / Group 3 | PURPLE | e3 |
| Công thức / Text | WHITE | — |
| Highlight toán học | GOLD | Nhấn mạnh key term |
| Cảnh báo / Điểm yếu | ORANGE | Penalty, warning |

## NGUYÊN TẮC 3BLUE1BROWN — BẮT BUỘC

1. **Câu hỏi trước, trả lời sau** — mỗi scene mở bằng một câu hỏi cụ thể, không giải thích ngay
2. **Geometry-first** — mọi khái niệm trừu tượng đều được hình học hóa trước khi viết công thức
3. **Xây dựng từng lớp** — không hiện toàn bộ hình cùng lúc; từng phần xuất hiện theo đúng nhịp lời đọc
4. **Aha moment rõ ràng** — mỗi scene phải có 1 khoảnh khắc "à ra vậy" được nhấn mạnh bằng animation
5. **Audio script viết đủ từng câu** — có thể đọc thẳng thành voiceover, không phải ghi chú tóm tắt
6. **Transition mượt** — ưu tiên TransformMatchingTex, FadeTransform, ReplacementTransform

---

---

# PHẦN 1 — VẤN ĐỀ: "Khi AI tự tin mà sai"

---

## Scene 0.1 — Opening: Bệnh án của Bác sĩ
**Thời lượng ước tính: ~90 giây**
*(Ví dụ trực tiếp từ Tutorial NeurIPS 2024 — Clinical Notes)*

### VISUAL — từng bước

**Bước 0.1a**
Màn hình đen. Chữ xuất hiện chậm từ giữa, WHITE, font lớn:

    Một AI được huấn luyện để dự đoán bệnh
    từ hồ sơ bệnh án điện tử.

**Bước 0.1b**
Vẽ 2 bệnh án dạng text trên màn hình (hộp chữ nhật WHITE viền mỏng):

Bệnh án 1:
    "89 yr old MAN, presenting with polyuria..."
    AI predict: → Diabetes (Tiểu đường)  ✓

Bệnh án 2:
    "70 yr old GENTLEMAN, joint pain, swelling..."
    AI predict: → Arthritis (Viêm khớp)  ✓

Thanh accuracy bên phải:
    Hospital A — Accuracy: ████████████ 95%  [GREEN]

**Bước 0.1c**
Camera pan sang phải. Bệnh viện B xuất hiện. Một bệnh án mới:

    "65 yr old MAN, joint pain, morning stiffness..."
    AI predict: → Diabetes  ✗

Thanh accuracy:
    Hospital B — Accuracy: ████░░░░░░░░ 72%  [RED]

Dấu "?" lớn GOLD nhấp nháy 3 lần.

**Bước 0.1d**
Zoom vào 2 bệnh án đầu. Highlight bằng hộp RED: các từ "MAN" và "GENTLEMAN". Mũi tên xuất hiện:

    "MAN"       ──────→  Diabetes
    "GENTLEMAN" ──────→  Arthritis

Text xuất hiện bên dưới:

    "AI không đọc chỉ số y khoa.
     Nó học thói quen viết của bác sĩ ở Viện A."

### AUDIO — Script đầy đủ

"Hãy bắt đầu với một ví dụ thực tế. Một AI được huấn luyện để dự đoán bệnh từ hồ sơ bệnh án điện tử. Tại Bệnh viện A, nó đạt 95% — ấn tượng.

Nhưng khi chuyển sang Bệnh viện B, accuracy rớt xuống 72%.

Điều gì đã xảy ra? Nhìn kỹ vào dữ liệu huấn luyện. Tại Viện A, một bác sĩ cụ thể có thói quen: ông ta viết 'man' khi ghi hồ sơ bệnh nhân tiểu đường, và 'gentleman' khi ghi bệnh nhân viêm khớp. Hai từ đồng nghĩa — nhưng AI đã học được sự phân biệt này và dùng nó như một đường tắt.

Khi sang Viện B, bác sĩ mới không có thói quen đó. Shortcut biến mất. Mô hình sụp đổ.

Đây chính là vấn đề trọng tâm của tutorial này. Không phải AI thiếu dữ liệu hay thiếu tham số. Mà là AI đang học sai thứ."

---

## Scene 0.2 — Road Map
**Thời lượng ước tính: ~40 giây**

### VISUAL — từng bước

**Bước 0.2a**
Màn hình xóa. Vẽ con đường nằm ngang từ trái sang phải (2 đường song song màu GRAY). Biển hiệu trái: "XUẤT PHÁT".

**Bước 0.2b**
Lần lượt xuất hiện 6 trạm dừng (Circle nodes), text nhỏ bên dưới mỗi node:

    [ERM & Shortcuts] → [Nhân quả] → [IRM] → [DRO & JTT] → [Foundation Models] → [Best Practices]
       ORANGE             BLUE_D     GREEN_D    YELLOW_D         PURPLE               GOLD

**Bước 0.2c**
Chấm nhỏ màu WHITE (xe) di chuyển từ XUẤT PHÁT, dừng ở node 1, node 1 sáng lên.

### AUDIO

"Trong video này chúng ta sẽ đi qua sáu chặng. Bắt đầu bằng câu hỏi tại sao AI học những đường tắt, sau đó nhìn vấn đề qua lăng kính nhân quả, khám phá ba phương pháp giải quyết, rồi xem chúng hoạt động ra sao trong thời đại của các mô hình khổng lồ như GPT và CLIP. Đi thôi."

---

## Scene 1.1 — ERM và Ảo ảnh Accuracy Cao
**Thời lượng ước tính: ~2 phút**
*(Ví dụ Penguins vs Camels — trực tiếp từ Slides Tutorial)*

### VISUAL — từng bước

**Bước 1.1a**
Vẽ không gian 2D trống. Trục x ngang: gradient màu từ TRẮNG TUYẾT sang VÀNG CÁT, label "màu nền". Trục y dọc: gradient từ mờ lên rõ, label "hình dáng con vật". Chưa có điểm nào.

**Bước 1.1b**
Animate 20 điểm xuất hiện lần lượt:
- 10 điểm BLUE_D (chim cánh cụt — Penguin): góc trên-trái (hình dáng đứng thẳng + nền trắng tuyết)
- 10 điểm YELLOW_D (lạc đà — Camel): góc dưới-phải (hình dáng lưng bướu + nền vàng cát)

Icon đơn giản: penguin = hình oval đứng nhỏ, camel = hình lưng cong.

**Bước 1.1c**
Đường phân loại WHITE nghiêng 45 độ trượt vào, chia đôi 2 cụm hoàn hảo. Text bên cạnh:

    Train Accuracy = 98%  ✓  [GREEN]

**Bước 1.1d**
Pause 1 giây. Camera zoom vào đường phân loại. Mũi tên đỏ chỉ ra đường đang đi theo trục x (màu nền), không theo trục y (hình dáng).

**Bước 1.1e**
Xuất hiện điểm BLUE_D mới ở góc dưới-phải (chim cánh cụt trên cát — vì bị mang ra sa mạc). Điểm nhấp nháy "?". Mô hình predict YELLOW_D (Camel). Dấu ✗ RED to xuất hiện.

**Bước 1.1f**
Đường phân loại đổi màu RED, pulsing 2 lần. Text:

    "Đường này đọc MÀU NỀN — không phải CON VẬT"

### AUDIO

"Hãy bắt đầu bằng ví dụ kinh điển trong tutorial. Bạn xây dựng AI phân loại chim cánh cụt và lạc đà.

Tập dữ liệu huấn luyện: chim cánh cụt luôn đứng trên tuyết trắng, lạc đà luôn đứng trên cát vàng. Trong không gian đặc trưng hai chiều, trục ngang là màu nền, trục dọc là hình dáng, dữ liệu chia thành hai cụm tách biệt hoàn hảo.

Thuật toán học và vẽ được một đường phân loại. Accuracy 98%. Tuyệt vời.

Nhưng chú ý kỹ đường này đang làm gì. Nó đi theo trục ngang, đọc màu nền. Không phải trục dọc, không dựa vào hình dáng thực của con vật.

Khi một chú chim cánh cụt bị đặt trên cát vàng, đường phân loại không ngần ngại: đây là lạc đà. Sai hoàn toàn.

Điều gì đã xảy ra? Để hiểu, chúng ta cần nhìn vào trái tim của mọi thuật toán học máy hiện đại."

---

## Scene 1.2 — Giải phẫu ERM: Tại sao nó lười?
**Thời lượng ước tính: ~2.5 phút**

### VISUAL — từng bước

**Bước 1.2a**
Màn hình xóa trắng. Viết công thức ERM từng phần theo nhịp lời đọc:

Phần 1 xuất hiện:

    min_θ

Text nhỏ bên dưới: "Tìm bộ tham số tốt nhất..."

Phần 2 thêm vào:

    𝔼_{(x,y)∼P_train}

Hộp ORANGE bao quanh P_train. Text: "...bằng cách nhìn vào train data..."

Phần 3 hoàn chỉnh:

    [ℓ(f_θ(x), y)]

Text: "...và giảm sai số trung bình."

**Bước 1.2b**
Camera zoom vào P_train. Phần còn lại mờ đi. Text to xuất hiện:

    "ERM chỉ thấy P_train. Không hơn. Không kém."

**Bước 1.2c**
Vẽ sơ đồ 2 con đường từ hộp INPUT (bên trái) đến hộp OUTPUT (bên phải):

Con đường 1 — BLUE_D, đường dày, không được chọn:
  Label: "Phân tích cấu trúc: dáng đứng, lưng thẳng/bướu, tỉ lệ thân..."
  Bên cạnh: đồng hồ cát + thanh progress dài nhiều bước

Con đường 2 — RED, nét đứt, ký hiệu ⚡, được chọn:
  Label: "Đếm pixel trắng (tuyết) hoặc vàng (cát)"
  Bên cạnh: tia chớp, 1 bước duy nhất

**Bước 1.2d**
Animate viên bi WHITE xuất phát từ INPUT. Tại ngã rẽ: dao động nhẹ 0.5 giây... rồi lao thẳng vào Con đường 2. Text nhỏ dưới viên bi:

    "Gradient Descent chọn con đường giảm Loss nhanh nhất"

**Bước 1.2e**
Con đường 2 sáng hơn, Con đường 1 mờ đi dần. Text lớn xuất hiện ở trung tâm:

    SPURIOUS FEATURE

Màu RED, viền GOLD.

### AUDIO

"ERM, Empirical Risk Minimization, là thuật toán học máy tiêu chuẩn. Ý tưởng rất đơn giản: tìm bộ tham số theta để minimize sai số trung bình trên tập train.

Nhưng chú ý điều này: ERM chỉ có một mục tiêu duy nhất, giảm con số Loss xuống. Nó không biết, không quan tâm, liệu sự giảm đó đến từ hiểu thật sự hay từ đường tắt.

Hãy hình dung từ góc nhìn của Gradient Descent. Có hai con đường để dự đoán đúng nhãn chim cánh cụt: con đường thứ nhất, phân tích cấu trúc hình thái học, nhận dạng dáng đứng đặc trưng và tỉ lệ thân mình, tốn nhiều bước gradient, khó học. Con đường thứ hai, đếm xem nền nhiều pixel trắng hay vàng hơn, một phép tính đơn giản.

Gradient Descent sẽ chọn con đường nào? Luôn luôn là con đường hai. Không phải vì nó thông minh xấu xa, mà đơn giản vì đó là chiều gradient giảm nhanh nhất.

Chúng ta gọi những đặc trưng như màu nền đó là Spurious Features, đặc trưng ảo. Chúng trông giống tín hiệu hữu ích trong train data, nhưng thực ra chỉ là sự trùng hợp ngẫu nhiên của ngữ cảnh. Và đây không phải lỗi của thuật toán. ERM đang làm đúng những gì được yêu cầu. Vấn đề nằm ở cách chúng ta định nghĩa mục tiêu học."

---

## Scene 1.3 — Spurious Feature: Chính xác là gì?
**Thời lượng ước tính: ~1.5 phút**

### VISUAL — từng bước

**Bước 1.3a**
Vẽ timeline đơn giản từ trái sang phải. Chuỗi sự kiện xuất hiện lần lượt:

    [Nhiếp ảnh gia muốn chụp CHIM CÁNH CỤT]
             ↓
    [Chọn địa điểm: Bắc Cực — Tuyết trắng]
             ↓
    [Ảnh: nền trắng + chim cánh cụt]

Mũi tên nhân quả BLUE_D đậm từ "PENGUIN (Y)" → "NỀN TRẮNG (X_spur)".

**Bước 1.3b**
Vẽ thêm mũi tên nét đứt RED ngược chiều:

    NỀN TRẮNG -----→ PENGUIN   [RED, dashed]

Label trên mũi tên: "AI đang học điều này". Label nhỏ bên cạnh: "Ngược chiều nhân quả!".

**Bước 1.3c**
Animate thay đổi môi trường: text "Môi trường: Bắc Cực" → "Môi trường: Sa mạc". Mũi tên đứt RED nhấp nháy 2 lần... rồi vỡ vụn thành các mảnh nhỏ bay ra xung quanh. Mũi tên BLUE_D vẫn đứng vững, sáng lên.

**Bước 1.3d**
Text lớn:

    Causal Features   =  INVARIANT  (bất biến)
    Spurious Features =  BRITTLE    (dễ vỡ)

### AUDIO

"Vậy spurious feature là gì, chính xác?

Hãy nghĩ về chuỗi sự kiện tạo ra dữ liệu. Nhiếp ảnh gia muốn chụp chim cánh cụt, họ đến Bắc Cực. Con chim là nguyên nhân, nền tuyết trắng là kết quả. Mũi tên nhân quả đi từ nhãn sang nền.

Nhưng AI đang đọc ngược lại: thấy nền trắng, kết luận đây là chim cánh cụt. Đây là Anti-causal Prediction, dự đoán ngược chiều nhân quả.

Vấn đề: tương quan ngược chiều này chỉ tồn tại trong một môi trường cụ thể. Khi môi trường thay đổi, chim cánh cụt xuất hiện ở sa mạc, tương quan đó tan biến. Nhưng mối quan hệ nhân quả thật, chim cánh cụt có hình dáng của chim cánh cụt dù đứng ở đâu, vẫn còn đó.

Đây chính là sự khác biệt cốt lõi: Causal features ổn định qua mọi môi trường. Spurious features chỉ tồn tại ở một hoàn cảnh cụ thể."

---

---

# PHẦN 2 — FRAMEWORK TOÁN HỌC: "Đặt tên cho vấn đề"

---

## Scene 2.1 — Cấu trúc dữ liệu theo Group
**Thời lượng ước tính: ~2 phút**

### VISUAL — từng bước

**Bước 2.1a**
Vẽ lưới 2×2. Kích thước mỗi ô tỉ lệ với phần trăm dữ liệu:

    ┌──────────────────────┬────────────────────┐
    │  (Bò, Cỏ)  45%      │  (Bò, Cát)  5%     │
    │  [GREEN_D, to]       │  [RED, nhỏ, ★]     │
    ├──────────────────────┼────────────────────┤
    │  (Lạc đà, Cỏ)  5%  │  (Lạc đà, Cát) 45% │
    │  [RED, nhỏ, ★]      │  [YELLOW_D, to]    │
    └──────────────────────┴────────────────────┘

Hai ô nhỏ (RED) nhấp nháy nhẹ.

**Bước 2.1b**
Mũi tên chỉ vào 2 ô nhỏ. Label:

    "Minority Groups — chỉ 10% tổng dữ liệu"

**Bước 2.1c**
Viên bi đại diện ERM lăn qua các ô, tự động ưu tiên ô lớn (trọng số tỉ lệ). Accuracy hiện lên:

    Overall:           92%   [GREEN]
    Group (Bò, Cát):   18%   [RED, nhấp nháy]

**Bước 2.1d**
Text xuất hiện:

    "Average accuracy che giấu thảm họa ở nhóm thiểu số"

### AUDIO

"Để nói chính xác về vấn đề này, chúng ta cần một ngôn ngữ toán học. Tutorial NeurIPS 2024 đề xuất nhìn dữ liệu qua lăng kính nhóm, Group.

Mỗi nhóm được định nghĩa bởi sự kết hợp của nhãn Y và đặc trưng ảo. Trong bài toán bò và lạc đà: bốn nhóm. Bò trên cỏ. Bò trên cát. Lạc đà trên cỏ. Lạc đà trên cát.

Trong thực tế, 90% dữ liệu là hai nhóm tự nhiên. Chỉ 10% là hai nhóm nghịch nhĩ. ERM tối ưu trung bình có trọng số, tự động ưu tiên 90% đó. Accuracy tổng thể 92%, nghe hay. Nhưng với nhóm bò trên cát? 18%.

Chính vì vậy, chúng ta cần một chỉ số đánh giá mới."

---

## Scene 2.2 — Worst-Group Accuracy: Thước đo thực sự
**Thời lượng ước tính: ~1.5 phút**

### VISUAL — từng bước

**Bước 2.2a**
Vẽ 2 mô hình song song, horizontal bar chart:

    MODEL A (ERM):
      Group (Bò, Cỏ):      ████████████████ 96%
      Group (Bò, Cát):     ████ 18%              ← RED
      Group (Lạc đà, Cỏ):  ████ 21%              ← RED
      Group (Lạc đà, Cát): ████████████████ 94%
      Average:             ██████████████░  82%  [GREEN ✓]

    MODEL B (Robust):
      Group (Bò, Cỏ):      ████████████░ 78%
      Group (Bò, Cát):     ████████████  75%
      Group (Lạc đà, Cỏ):  ████████████  72%
      Group (Lạc đà, Cát): ████████████░ 80%
      Average:             ████████████░  76%  [RED ✗]

**Bước 2.2b**
Highlight dòng worst-group bằng hộp viền:
- Model A: WORST = 18% [RED]
- Model B: WORST = 72% [GREEN]

**Bước 2.2c**
Câu hỏi lớn xuất hiện:

    "Model nào tốt hơn cho bệnh viện thật?"

Pause 2 giây. Rồi:

    "Worst-Group Accuracy = thước đo của sự công bằng thực sự"

### AUDIO

"Nhìn vào hai mô hình. Model A có average accuracy 82%, trông hay hơn Model B với 76%. Theo ERM: chọn A.

Nhưng nhìn kỹ hơn. Model A hoàn toàn thất bại ở hai nhóm thiểu số, chỉ 18 và 21%. Trong thực tế điều này nghĩa là những bệnh nhân không theo khuôn sẽ bị chẩn đoán sai gần như hoàn toàn.

Model B có average thấp hơn, nhưng các nhóm đều được đối xử công bằng.

Worst-Group Accuracy là chỉ số chúng ta thực sự cần quan tâm khi deploy AI vào thế giới thực. Và bây giờ, để hiểu sâu hơn tại sao ERM thất bại, chúng ta cần đi vào cấu trúc nhân quả của dữ liệu."

---

## Scene 2.3 — Ba loại Distribution Shift
**Thời lượng ước tính: ~2 phút**

### VISUAL — từng bước

**Bước 2.3a**
Vẽ 3 cặp bell curve cạnh nhau. Mỗi cặp: train = BLUE_D, test = GREEN_D. Label từng cặp:

Cặp 1 — Covariate Shift:
  Curve test dịch sang phải. Ranh giới quyết định giữ nguyên vị trí.
  Label: "P(Y|X) không đổi ✓ | P(X) thay đổi"

Cặp 2 — Label Shift:
  Curve không dịch nhưng chiều cao thay đổi (một class ít hơn trong test).
  Label: "P(X|Y) không đổi ✓ | P(Y) thay đổi"

Cặp 3 — Spurious Shift (gắn sao vàng):
  Spurious feature của train FLIP ngược trong test.
  Đường phân loại dựa vào spurious → hoàn toàn sai trong test.
  Label: "P(X_spur|Y) ĐẢO NGƯỢC ✗" — GOLD highlight

**Bước 2.3b**
Zoom vào Cặp 3. Text:

    "Tutorial NeurIPS 2024 tập trung vào loại này"

### AUDIO

"Không phải mọi distribution shift đều giống nhau. Tutorial phân loại ba dạng chính.

Thứ nhất: Covariate Shift. Phân phối đầu vào X thay đổi, nhưng mối quan hệ Y cho X vẫn nguyên. Khó nhưng giải quyết được.

Thứ hai: Label Shift. Tần suất của các class thay đổi. Ít nguy hiểm hơn.

Thứ ba, và nguy hiểm nhất: Spurious Shift. Mối quan hệ giữa đặc trưng ảo và nhãn bị đảo ngược hoàn toàn. Nếu trước đây bò thường ở đồng cỏ, nay tất cả bò đều ở sa mạc, mô hình dùng màu nền sẽ sai 100%. Đây chính là loại shift mà cả phần tutorial này tập trung vào."

---

---

# PHẦN 3 — GÓC NHÌN NHÂN QUẢ: "Tại sao, không chỉ là Như thế nào"

---

## Scene 3.1 — Structural Causal Model: Xây từng mũi tên
**Thời lượng ước tính: ~2.5 phút**

### VISUAL — từng bước

**Bước 3.1a**
Màn hình đen. Node tròn GOLD ở trung tâm:

    Y  (Nhãn: Bò / Lạc đà)

Câu hỏi nhỏ phía dưới: "Y ảnh hưởng đến gì?"

**Bước 3.1b**
Node BLUE_D xuất hiện bên trái: "X_core (Hình dáng con vật)". Mũi tên굵 BLUE_D:

    X_core ──────────────→ Y
    "Nhân quả thực sự"

**Bước 3.1c**
Node ORANGE xuất hiện góc trên: "E (Môi trường)". Câu hỏi nhỏ: "Màu nền đến từ đâu?" Mũi tên ORANGE từ E → X_spur (node RED bên phải):

    E (Môi trường)
         |
         ↓
    X_spur (Màu nền)   "Môi trường quyết định ngữ cảnh"

**Bước 3.1d**
Mũi tên RED từ Y → X_spur. Giải thích nhỏ bên cạnh:

    "Vì Y=bò → người chụp chọn E=đồng cỏ → X_spur=nền xanh"

**Bước 3.1e**
Toàn bộ SCM hiện ra:

         E (Môi trường)
        ↙              ↘
    X_core ──→ Y ──→ X_spur
    [BLUE_D]  [GOLD]  [RED]

Mũi tên đứt RED vẽ từ X_spur ngược về Y, label "AI đang học điều này ←", kèm ký hiệu gạch chéo.

### AUDIO

"Hãy xây dựng một mô hình nhân quả cho bài toán này, Structural Causal Model, hay SCM.

Bắt đầu từ những gì chúng ta biết chắc. Con vật Y là bò hay lạc đà. Điều này quyết định hình dáng thể chất: bốn chân, sừng, tỉ lệ thân mình. Đây là X_core, đặc trưng cốt lõi. Mũi tên nhân quả từ X_core đến Y.

Nhưng còn màu nền thì sao? Khi nhiếp ảnh gia đi chụp bò, họ đến đồng cỏ. Đây là quyết định của môi trường E. Môi trường tạo ra X_spur, màu nền xanh. Không phải bò trực tiếp quyết định màu nền.

Tuy nhiên, vì trong train data bò thường đi với E bằng đồng cỏ, có sự tương quan giữa Y và X_spur. AI nhìn thấy tương quan này và học nó. Đây chính là bẫy. AI đang học ngược chiều nhân quả. Khi E thay đổi, tương quan đó biến mất. Chỉ có mũi tên nhân quả thật từ X_core đến Y là không đổi."

---

## Scene 3.2 — Distribution Shift phá vỡ liên kết ảo
**Thời lượng ước tính: ~1.5 phút**

### VISUAL — từng bước

**Bước 3.2a**
Giữ nguyên SCM từ Scene 3.1. Node E sáng lên. Text thay đổi ba lần với animation FadeTransform:

    E: "Đồng cỏ"  →  E: "Bãi biển"  →  E: "Tuyết"

**Bước 3.2b**
Mỗi lần E thay đổi: mũi tên Y → X_spur nhấp nháy RED, sau đó bẻ gãy (fracture: các đoạn nhỏ fly out). Sau 3 lần: mũi tên biến mất hoàn toàn.

**Bước 3.2c**
Chỉ còn lại:

    X_core ──→ Y
    [BLUE_D sáng lên mạnh, glow effect]
    "Bền vững qua mọi môi trường"

**Bước 3.2d**
Text lớn:

    Causal Features  = INVARIANT
    Spurious Features = BRITTLE

### AUDIO

"Hãy xem điều gì xảy ra khi môi trường thay đổi.

E bằng đồng cỏ: mối liên hệ giữa Y và X_spur tồn tại. AI hoạt động tốt.
E bằng bãi biển: mối liên hệ đó lung lay.
E bằng tuyết: hoàn toàn biến mất.

Nhưng mũi tên từ X_core đến Y, hình dáng con vật quyết định nhãn, không bao giờ thay đổi. Dù ở đồng cỏ, bãi biển, hay sa mạc, bò vẫn có bốn chân và hai sừng.

Và câu hỏi đặt ra bây giờ là: làm thế nào để buộc AI chỉ học những thứ bất biến này?"

---

---

# PHẦN 4 — PHƯƠNG PHÁP: IRM, DRO, JTT

---

## Scene 4.1 — IRM: Ý tưởng bất biến
**Thời lượng ước tính: ~1.5 phút**

### VISUAL — từng bước

**Bước 4.1a**
Vẽ 3 không gian 2D cạnh nhau. Viền màu GREEN_D, YELLOW_D, PURPLE. Label: e1, e2, e3.

**Bước 4.1b**
Trong mỗi không gian: scatter plot với phân phối trông khác nhau (vị trí, mật độ điểm khác). Nhưng ranh giới quyết định tối ưu thật (BLUE_D) thì giống nhau trong cả ba.

**Bước 4.1c**
Câu hỏi xuất hiện ở trung tâm:

    "Liệu có tồn tại một biểu diễn Φ(x),
    sao cho một bộ phân loại w* sẽ tối ưu
    ở MỌI môi trường đồng thời?"

Pause 2 giây. Rồi:

    "→ Đây là ý tưởng cốt lõi của IRM"

**Bước 4.1d**
Vẽ kiến trúc mạng chia 2 phần:

    [Input x] → [Φ: Feature Extractor] → [w: Linear Classifier] → [Output]
                       BLUE_D                    GREEN_D

### AUDIO

"Bây giờ hãy đặt câu hỏi khác: điều gì sẽ xảy ra nếu chúng ta không gộp tất cả dữ liệu từ mọi môi trường lại rồi chạy ERM, mà thay vào đó nhìn các môi trường riêng lẻ?

IRM, Invariant Risk Minimization, đặt ra một yêu cầu rất thú vị: tìm một cách biểu diễn dữ liệu, gọi là Phi, sao cho cùng một bộ phân loại tuyến tính w sẽ tối ưu ở tất cả các môi trường đồng thời.

Nếu tồn tại một Phi như vậy, thì Phi phải loại bỏ hết spurious features vì chúng không nhất quán giữa các môi trường. Phi chỉ giữ lại đặc trưng causal, vốn bất biến. Nghe thanh lịch. Nhưng làm thế nào để tối ưu hóa điều này?"

---

## Scene 4.2 — Công thức IRM: Từ ràng buộc cứng đến Gradient Penalty
**Thời lượng ước tính: ~3 phút**

### VISUAL — từng bước

**Bước 4.2a**
Viết công thức bi-level optimization từng dòng:

    min_{Φ,w}  Σ_{e∈E}  R_e(w∘Φ)

    subject to  w ∈ argmin_{w̄} R_e(w̄∘Φ),  ∀e∈E

Hộp RED bao quanh constraint. Label: "NP-Hard — không giải trực tiếp được".

**Bước 4.2b**
Trực quan hóa ràng buộc: vẽ trục số w. Ba parabola Loss_e(w) với đáy ở các vị trí khác nhau (GREEN_D, YELLOW_D, PURPLE). Ràng buộc nói w=1.0 phải là đáy của tất cả. Minh họa vi phạm: các đáy ở w=0.8, w=1.3, w=1.1, không thể đồng thời thỏa mãn.

**Bước 4.2c**
Text xuất hiện:

    "Nếu w=1.0 là minimum của R_e(w∘Φ) thì:
     ∇_{w|w=1.0} R_e(w∘Φ) = 0
     
     → Gradient lớn = vi phạm bất biến
     → Đo vi phạm bằng độ lớn gradient!"

**Bước 4.2d**
TransformMatchingTex: constraint biến thành penalty term:

    min_{Φ,w}  Σ_e R_e(w∘Φ)  +  λ ‖∇_{w|w=1.0} R_e(w∘Φ)‖²
               ──────────────    ──────────────────────────────
               fit mọi môi trường   penalty vi phạm bất biến

Penalty term xuất hiện từ bên phải, màu ORANGE.

**Bước 4.2e**
ValueTracker animation: λ tăng từ 0 lên 10 trong 3 giây. Ba parabola dần dịch chuyển, đáy hội tụ về w=1.0.

### AUDIO

"IRM viết bài toán tối ưu bi-level: minimize tổng risk trên mọi môi trường, với ràng buộc rằng w phải là classifier tối ưu cho từng môi trường riêng lẻ. Ràng buộc này bảo đảm Phi trích xuất đặc trưng đủ bất biến để một w duy nhất làm việc được ở tất cả nơi.

Vấn đề: bài toán này là NP-Hard. Không giải trực tiếp bằng Gradient Descent được.

Đây là nơi một trick toán học đẹp xuất hiện. Nếu w bằng 1.0 là minimum của hàm loss, thì gradient của hàm loss tại w bằng 1.0 phải bằng 0. Đó là định nghĩa của minimum. Vậy thay vì ràng buộc cứng, ta đo mức độ vi phạm bằng độ lớn của gradient.

Gradient lớn tại w bằng 1.0 nghĩa là w chưa phải minimum, Phi đang dùng shortcut. Gradient nhỏ nghĩa là Phi đã học đặc trưng bất biến.

Đây là IRMv1. Khi lambda tăng, optimizer bị ép phải tìm Phi sao cho mọi môi trường đồng thuận. Spurious features bị loại vì chúng là nguyên nhân của sự bất đồng đó."

---

## Scene 4.3 — Trực quan: Gradient Vectors hội tụ
**Thời lượng ước tính: ~1.5 phút**

### VISUAL — từng bước

**Bước 4.3a**
Không gian tham số w (trục số). Ba parabola với đáy ở vị trí khác nhau.

**Bước 4.3b**
Tại điểm w=1.0: 3 vector gradient (mũi tên) chỉ về 3 hướng khác nhau (phân kỳ).

    "3 môi trường bất đồng → shortcut đang được dùng!"

**Bước 4.3c**
ValueTracker λ tăng dần. Ba vector gradient xoay từng bước về cùng hướng, nhỏ dần, tiến về 0. Animation mượt 3 giây.

    "Penalty ép đồng thuận → shortcut bị loại"

### AUDIO

"Hình dung trực quan. Nếu Phi đang dùng spurious feature, đặc trưng đó hữu ích ở một số môi trường nhưng hại ở môi trường khác. Mỗi môi trường muốn w dịch chuyển theo hướng khác nhau. Ba vector gradient chỉ về ba hướng khác nhau, bất đồng.

Khi penalty lambda tăng, optimizer bị phạt nếu các gradient còn phân kỳ. Nó buộc phải tìm Phi mà tất cả môi trường đồng thuận. Spurious features bị loại khỏi Phi vì chúng là nguyên nhân của sự bất đồng. Phần còn lại trong Phi chính là causal features."

---

## Scene 4.4 — Giới hạn của IRM
**Thời lượng ước tính: ~1 phút**

### VISUAL — từng bước

**Bước 4.4a**
Vẽ 2 môi trường giống nhau hoàn toàn (cùng spurious correlation). IRM không phát hiện được vì không có bất đồng.

**Bước 4.4b**
Hộp tóm tắt:

    ✓  IRM: nền tảng lý thuyết nhân quả vững chắc
    ✗  IRM: cần nhiều môi trường đủ đa dạng
    ✗  IRM: nhạy với lựa chọn λ, không ổn định khi train

### AUDIO

"IRM có giới hạn lý thuyết quan trọng. Nó chỉ hoạt động khi các môi trường đủ đa dạng để expose sự không nhất quán của spurious features. Nếu chỉ có hai môi trường mà cả hai đều chứa cùng shortcut, IRM không có cách nào phát hiện.

Ngoài ra, IRMv1 rất nhạy với lựa chọn lambda và thường không ổn định khi training. Nhiều nghiên cứu cho thấy ERM được tuning tốt đôi khi còn vượt trội hơn. Vậy nếu không có đủ môi trường rõ ràng, chúng ta cần hướng tiếp cận khác."

---

## Scene 5.1 — Group DRO: Tối ưu hóa Worst-Case
**Thời lượng ước tính: ~2.5 phút**

### VISUAL — từng bước

**Bước 5.1a**
Pie chart Waterbirds (4 mảnh, kích thước tỉ lệ):
- Waterbird + Water: 45% [BLUE_D]
- Landbird + Land: 45% [GREEN_D]
- Waterbird + Land: 5% [RED, nhấp nháy]
- Landbird + Water: 5% [RED, nhấp nháy]

Label: "Bộ dữ liệu Waterbirds — benchmark kinh điển"

**Bước 5.1b**
Viết công thức ERM, highlight phần trung bình:

    min_θ  Σ_g  p_g · 𝔼_g[ℓ]

Mũi tên chỉ vào p_g: khi p_g nhỏ thì nhóm bị bỏ qua.

**Bước 5.1c**
TransformMatchingTex: Σ_g p_g → max_g:

    min_θ  max_{g∈G}  𝔼_{(x,y)∼P_g} [ℓ(f_θ(x),y)]

Chữ max xuất hiện với GOLD highlight. Text: "Thay trung bình bằng worst-case".

**Bước 5.1d**
Loss surface 2D contour (nhìn từ trên xuống). ERM: viên bi tìm vùng thấp nhất. DRO: viên bi bị kéo về vùng nhóm thiểu số (worst group). Animate 2 viên bi chạy khác nhau.

**Bước 5.1e**
Pseudocode animation từng dòng:

    For each training step:
      1. Tính loss L_g cho mỗi group g
      2. Upweight group có L_g cao nhất
      3. Update θ theo trọng số mới

### AUDIO

"Group DRO thay đổi mục tiêu tối ưu bằng một từ: max.

ERM minimize trung bình có trọng số của loss trên các nhóm. Nhóm nhỏ có trọng số nhỏ, tự động bị bỏ qua. DRO thay đổi luật chơi: nó tìm nhóm đang tệ nhất, worst-case group, và minimize loss của nhóm đó.

Hãy hình dung loss landscape như địa hình nhìn từ trên. ERM tìm thung lũng thấp nhất trung bình, lăn qua góc tối tăm nơi nhóm thiểu số đang vật lộn. DRO liên tục cập nhật trọng số: nhóm nào có loss cao thì upweight. Optimizer phải chú ý đến nhóm đó.

Group DRO rất mạnh khi có nhãn nhóm. Nhưng gán nhãn nhóm rất tốn kém trong thực tế. Và đây là lúc JTT xuất hiện."

---

## Scene 6.1 — JTT: Để ERM tự chỉ ra điểm yếu
**Thời lượng ước tính: ~2.5 phút**

### VISUAL — từng bước

**Bước 6.1a**
Câu hỏi lớn:

    "Nếu không biết mỗi điểm thuộc nhóm nào...
    làm sao tìm được nhóm thiểu số?"

**Bước 6.1b**
Text xuất hiện: "Hãy để ERM tự chỉ ra."

Vẽ timeline 2 giai đoạn:

GIAI ĐOẠN 1 — ERM sơ bộ (5 epochs):
  - Thanh progress ngắn.
  - Kết quả: 2 rổ xuất hiện (animate điểm rơi vào):
    - Rổ GRAY (đúng): mờ. Label: "Dễ — shortcut hoạt động"
    - Rổ GOLD (sai): sáng, nhấp nháy. Label: "Khó — không có shortcut!"

**Bước 6.1c**
Lý giải trực quan tại sao các điểm bị sai = thiểu số:
- (Bò, Cỏ): shortcut "nền xanh = bò" đúng → rơi vào rổ GRAY
- (Bò, Cát): shortcut "nền vàng = lạc đà" sai → rơi vào rổ GOLD
Animate đường đi của mỗi loại điểm vào đúng rổ.

GIAI ĐOẠN 2 — Train mô hình robust:
  - Lấy rổ GOLD.
  - Nhân bản K=20 lần (animate copy, số lượng tăng, con số K=20 xuất hiện to).
  - Dataset mới: rổ GOLD chiếm tỉ lệ lớn hơn nhiều.
  - Train mô hình thứ 2.

**Bước 6.1d**
Kết quả:

    ERM:  Worst-Group = 32%  [RED]
    JTT:  Worst-Group = 71%  [GREEN]
          ← Không cần một nhãn nhóm nào!

### AUDIO

"JTT, Just Train Twice, có câu trả lời thanh lịch: hãy để ERM tự chỉ ra.

Bước 1: Train một mô hình ERM nhỏ trong vài epochs, đủ để nó học shortcuts, nhưng chưa memorize. Nhìn vào những điểm mà mô hình này dự đoán sai.

Tại sao những điểm bị sai lại quan trọng? Vì mô hình ERM học shortcuts ngay lập tức. Điểm nào thuộc nhóm đa số, shortcut hoạt động, dự đoán đúng. Điểm nào thuộc nhóm thiểu số, shortcut chỉ sai hướng, dự đoán sai. Các điểm bị sai chính xác là những điểm mà shortcut không giúp ích được.

Bước 2: Gom những điểm sai đó lại, nhân bản chúng lên K lần, tạo dataset mới nơi thiểu số được đại diện đầy đủ. Train mô hình thứ hai trên dataset này.

Kết quả: Worst-group accuracy tăng từ 32% lên 71%, mà không cần một nhãn nhóm thủ công nào. ERM đã tự lộ ra điểm yếu của chính mình."

---

---

# PHẦN 5 — FOUNDATION MODELS

---

## Scene 7.1 — Scale không giải quyết được vấn đề
**Thời lượng ước tính: ~2 phút**

### VISUAL — từng bước

**Bước 7.1a**
Đồ thị đường: trục x = Model Size log scale (10M → 1B → 100B), trục y = Worst-Group Accuracy. Hai đường:
- ERM (RED): tăng nhẹ rồi plateau ở ~55%
- DRO (BLUE_D): tăng đáng kể hơn, đạt ~75%

**Bước 7.1b**
Highlight vùng Large Models (>10B params). Icon robot/brain cho GPT-scale models nằm trên đường plateau ERM. Text:

    "Bigger ≠ More Robust"

**Bước 7.1c**
Animation: model lớn hơn → nhiều đường tắt nhỏ phức tạp hơn xuất hiện (RED, nhiều nhánh). Text:

    "Scale amplifies, not fixes, spurious correlations"

### AUDIO

"Câu hỏi tự nhiên: liệu chúng ta có cần lo về điều này khi các mô hình ngày càng to hơn? Phải chăng 100 tỉ tham số tự động giải quyết vấn đề?

Câu trả lời là không. Khi model size tăng nhưng vẫn train theo ERM, worst-group accuracy gần như không tăng sau một điểm nhất định. Scale giúp average accuracy, nhưng không giải quyết spurious correlations.

Thậm chí tệ hơn: mô hình lớn hơn có capacity lớn hơn để memorize spurious features tinh vi hơn. Scale amplifies, không fixes, vấn đề."

---

## Scene 7.2 — CLIP và Spurious Correlations từ Web
**Thời lượng ước tính: ~2 phút**

### VISUAL — từng bước

**Bước 7.2a**
Kiến trúc CLIP đơn giản:

    [Ảnh]  →  [Image Encoder]  ─┐
                                 ├─→  Cosine Similarity  →  Score
    [Text] →  [Text Encoder]   ─┘

Text nhỏ: "Train trên 400M cặp ảnh-văn bản từ internet"

**Bước 7.2b**
Ví dụ bias:
- Input: icon người mặc áo trắng. Text: "doctor" → score cao ✓
- Thay bằng icon phụ nữ mặc áo trắng → score thấp hơn đáng kể
- Histogram: phân phối score "doctor" theo gender, lệch rõ sang nam

**Bước 7.2c**
Bar chart: tần suất từ "doctor" trên web đi kèm ảnh nam >> đi kèm ảnh nữ. Đây là nguồn gốc của bias.

**Bước 7.2d**
Text:

    "Web data amplify bias xã hội
    CLIP không phân biệt causal từ spurious"

### AUDIO

"CLIP được train trên 400 triệu cặp ảnh và văn bản từ internet. Khả năng zero-shot đáng kinh ngạc. Nhưng internet phản ánh thế giới với tất cả bias của nó.

Khi văn bản bác sĩ xuất hiện trên web đi kèm ảnh người, phần lớn là nam. CLIP học tương quan đó. Nó không có lý do gì để nghĩ đây là spurious, vì với 400 triệu ví dụ, đây trông như một pattern thật.

Kết quả: các tác vụ downstream kế thừa bias từ CLIP. Medical diagnosis, hiring tools, hay content moderation xây trên CLIP đều mang theo spurious correlations đã được học ở quy mô khổng lồ. Scale consolidates spurious, không xóa nó."

---

## Scene 7.3 — In-Context Learning và Spurious Shortcuts trong LLMs
**Thời lượng ước tính: ~1.5 phút**
*(Ví dụ ICL "movie ~ positive" — trực tiếp từ Slides Tutorial)*

### VISUAL — từng bước

**Bước 7.3a**
Vẽ khung "prompt" điển hình của In-Context Learning (ICL) — dạng few-shot:

    Prompt gửi cho LLM:
    ┌────────────────────────────────────────┐
    │ "The movie was incredible!" → Positive │
    │ "Best movie of the year!"   → Positive │
    │ "I loved this movie!"       → Positive │
    │                                        │
    │ "The food was terrible."    → ???      │
    └────────────────────────────────────────┘

**Bước 7.3b**
LLM predict: "Positive" cho câu cuối. Dấu ✗ RED xuất hiện. Nhãn đúng là "Negative".

Zoom vào các ví dụ trên. Highlight màu ORANGE: từ "movie" xuất hiện trong tất cả 3 ví dụ Positive.

Text:

    Shortcut LLM học được:
    "movie" trong prompt → POSITIVE

**Bước 7.3c**
Vẽ biểu đồ minh họa: trong prompt train, từ "movie" xuất hiện 100% cùng nhãn Positive. LLM bị lừa bởi tương quan này.

Animate: khi prompt thay đổi (ví dụ mới về "movie" nhưng lần này là Negative), LLM vẫn predict Positive. Dấu ✗ RED to.

**Bước 7.3d**
Text kết luận:

    "LLMs học shortcuts TRONG CHÍNH CÁI PROMPT.
     In-Context Learning ≠ Robust Learning."

### AUDIO

"Trong thế giới Large Language Models, spurious shortcuts xuất hiện ở một nơi bất ngờ: ngay trong cái prompt mà bạn viết.

In-Context Learning, hay ICL, là khả năng LLM học từ một vài ví dụ được cung cấp trực tiếp trong prompt. Nhìn qua thì tuyệt vời. Nhưng slides của tutorial chỉ ra một vấn đề tinh vi.

Trong prompt này, tất cả ba ví dụ Positive đều chứa từ 'movie'. LLM không học được rằng câu văn tích cực thì nhãn là Positive. Nó học được điều đơn giản hơn: 'movie' xuất hiện trong prompt thì nhãn là Positive.

Khi gặp một câu không liên quan đến phim nhưng cũng là Positive, hay ngược lại, LLM sai. Đây là spurious correlation được tạo ra bởi chính người viết prompt, không phải bởi dữ liệu train.

Và đây là điểm đặc biệt nguy hiểm của ICL shortcuts: chúng vô hình. Bạn không thể kiểm tra 'model weights' vì shortcuts nằm trong ngữ cảnh, thay đổi theo từng lần gọi."

---

## Scene 7.4 — Reverse Scaling: Mô hình TO hơn = DỄ BỊ LỪA hơn
**Thời lượng ước tính: ~1.5 phút**
*(Phát hiện từ Tutorial NeurIPS 2024)*

### VISUAL — từng bước

**Bước 7.4a**
Đồ thị: trục x = Model Size (2.7B → 7B → 13B params), trục y = mức độ bị ảnh hưởng bởi spurious ICL shortcuts (% predictions bị shortcut chi phối). Vẽ đường:

    [2.7B] ──── [7B] ──── [13B]
     30%         52%        71%     [RED, đi lên]

Không phải đi xuống như kỳ vọng — mà đi LÊN.

**Bước 7.4b**
Animation nhấn mạnh: biểu tượng model lớn hơn (hộp to hơn) = bị thao túng bởi shortcut nhiều hơn.

Text lớn:

    "REVERSE SCALING"
    Mô hình lớn hơn → nhạy hơn với ICL shortcuts!

**Bước 7.4c**
Giải thích trực quan: LLM lớn hơn có capacity tốt hơn để "đọc ý định" người viết prompt → nhạy cảm hơn với pattern trong prompt → dễ bị lừa hơn bởi spurious correlations trong ngữ cảnh.

### AUDIO

"Đây là phát hiện gây sốc nhất trong phần Foundation Models của tutorial: Reverse Scaling.

Thông thường chúng ta kỳ vọng mô hình lớn hơn sẽ mạnh hơn, robust hơn với shortcuts. Nhưng với ICL spurious correlations, điều ngược lại xảy ra. Mô hình 13 tỉ tham số bị ảnh hưởng bởi shortcut 'movie' trong prompt nhiều hơn mô hình 2.7 tỉ tham số.

Tại sao? Vì mô hình lớn hơn rất giỏi trong việc đọc ngữ cảnh và nắm bắt pattern trong prompt. Đây chính là khả năng tạo nên ICL. Nhưng nó cũng có nghĩa là mô hình lớn hơn 'quá nhạy' với mọi pattern, kể cả pattern không liên quan đến task thực sự.

Scale không phải là thuốc chữa bách bệnh."

---

## Scene 7.5 — PfR: Dùng AI để chữa lỗi cho AI
**Thời lượng ước tính: ~2 phút**
*(Thuật toán PfR — Prompting for Robustness — từ Tutorial 2024)*

### VISUAL — từng bước

**Bước 7.5a**
Câu hỏi lớn:

    "Group DRO cần nhãn nhóm.
     JTT cần 2 vòng train.
     Còn với Foundation Models — có cách nào tự động hơn không?"

**Bước 7.5b**
Vẽ luồng PfR (3 khối nối nhau bằng mũi tên):

    Khối 1: [Hình ảnh Waterbirds] — hàng vạn ảnh chim
    Khối 2: [VLM / GPT-4V]
             Prompt: "Describe the background: water or land?"
    Khối 3: [Nhãn phông nền tự động] — "water", "land", "water"...

Animate: ảnh đi vào VLM, nhãn phông nền bắn ra.

**Bước 7.5c**
Mũi tên kết hợp:

    [Nhãn phông nền từ VLM]  +  [Nhãn bird type thủ công]
                    ↓
             [Group DRO]
                    ↓
     Worst-Group Accuracy: 71% → 91.05%  [GREEN, tăng vọt]

**Bước 7.5d**
Text nhãn kết quả:

    PfR = Prompting for Robustness
    "AI lớn gán nhãn cho AI nhỏ.
     Không tốn một đồng gán nhãn thủ công."

### AUDIO

"Đây là giải pháp đột phá của năm 2024: PfR — Prompting for Robustness.

Vấn đề cốt lõi: Group DRO cần nhãn nhóm, tức là với mỗi ảnh chim, cần biết nền là nước hay đất. Gán nhãn thủ công cho hàng vạn ảnh rất tốn kém.

Giải pháp: dùng chính một mô hình lớn như GPT-4V để gán nhãn phông nền. Đưa từng ảnh vào VLM với prompt đơn giản: hãy mô tả nền của ảnh này. VLM trả về nhãn phông nền chính xác với chi phí gần như bằng không.

Sau đó kết hợp nhãn phông nền tự động này với nhãn bệnh nhân thủ công để chạy Group DRO.

Kết quả trên Waterbirds: Worst-group accuracy tăng từ 71% lên 91.05%. Không cần thêm dữ liệu train, không cần thay đổi thuật toán. Chỉ cần dùng AI lớn để gán nhãn cho AI nhỏ."

---

## Scene 7.6 — CATO: Counterfactual Data bằng LLM
**Thời lượng ước tính: ~1.5 phút**
*(Thuật toán CATO — từ Tutorial 2024)*

### VISUAL — từng bước

**Bước 7.6a**
Câu hỏi:

    "Nếu không có đủ dữ liệu thiểu số để train...
     có thể TỰ SINH RA không?"

**Bước 7.6b**
Vẽ luồng CATO:

    Bước 1: Dùng LLM để phân tích dữ liệu
             → Nhận diện spurious features Z
             → "Nền nước" là spurious với "waterbird"

    Bước 2: LLM + Causal Reasoning
             → Sinh dữ liệu counterfactual:
             "Waterbird trên đất" (đảo ngược nền)
             "Landbird trên nước" (đảo ngược nền)

    Bước 3: Dataset mới = Original + Counterfactual
             → Train model robust hơn

**Bước 7.6c**
Animation: từ 2 nhóm nhỏ (5% mỗi loại), CATO sinh thêm dữ liệu counterfactual → 2 nhóm nhỏ giờ có đủ samples. Pie chart cân bằng lại.

**Bước 7.6d**
Text:

    CATO = Causal Augmentation + LLM
    "Tạo ra dữ liệu 'counterfactual' để cân bằng dataset"

### AUDIO

"PfR giải quyết vấn đề gán nhãn. Nhưng còn một vấn đề khác: ngay cả khi biết nhóm nào là thiểu số, số lượng mẫu vẫn quá ít để train hiệu quả.

CATO giải quyết điều này bằng cách dùng LLM và suy luận nhân quả để sinh ra dữ liệu counterfactual. Từ SCM đã xây dựng, ta biết spurious feature là phông nền. Vậy CATO yêu cầu LLM: hãy tưởng tượng waterbird này đứng trên đất thay vì nước. Mô tả lại ảnh đó.

LLM sinh ra các mô tả, hoặc thậm chí ảnh tổng hợp, của các trường hợp counterfactual. Dataset mới giờ cân bằng hơn nhiều.

Đây là hướng kết hợp giữa nhân quả và generative AI — một trong những xu hướng nghiên cứu nóng nhất của năm 2024."

---

---

# PHẦN 6 — BENCHMARKS & KẾT LUẬN

---

## Scene 8.1 — Benchmarks và Sự thật phũ phàng
**Thời lượng ước tính: ~2 phút**

### VISUAL — từng bước

**Bước 8.1a**
Gallery 4 benchmark (2×2 grid), mỗi ô có icon đơn giản + tên + Gap metric:

    [Waterbirds]          [CelebA]
    Icon: chim+cỏ         Icon: khuôn mặt
    Task: bird type       Task: hair color
    Spurious: background  Spurious: gender
    WG Gap: 50%           WG Gap: 40%

    [Camelyon17 WILDS]    [CivilComments WILDS]
    Icon: kính hiển vi    Icon: text bubble
    Task: tumor detect    Task: toxicity
    Spurious: hospital    Spurious: identity
    WG Gap: 30%           WG Gap: 35%

**Bước 8.1b**
Bar chart grouped: 5 phương pháp × 4 datasets:
- ERM (GRAY), IRM (BLUE_D), DRO (GREEN_D), JTT (YELLOW_D), CORAL (PURPLE)
- Không có phương pháp nào win tất cả. Kết quả đan xen.

**Bước 8.1c**
Highlight: ERM được tuned tốt bằng hoặc hơn các phương pháp phức tạp ở 2/4 datasets. Hộp ORANGE:

    "ERM + careful tuning ≈ state-of-the-art (sometimes!)"
    "Không có silver bullet"

### AUDIO

"Để đánh giá khách quan, cộng đồng xây dựng các benchmark chuẩn. WILDS cung cấp dữ liệu thực từ y tế và khoa học, nơi distribution shift xảy ra tự nhiên. DomainBed tổng hợp nhiều dataset để kiểm chứng domain generalization.

Và đây là sự thật phũ phàng: nhìn vào kết quả thực nghiệm, không có phương pháp nào thống trị tuyệt đối. Tệ hơn: khi ERM được tuning cẩn thận, lựa chọn learning rate, weight decay và augmentation tốt, nó thường cạnh tranh được với các phương pháp phức tạp hơn nhiều.

Điều này không có nghĩa các phương pháp robust vô ích. Khi spurious correlation cực mạnh và có cấu trúc rõ ràng, chúng thực sự giúp ích. Nhưng bài học thực tiễn: đừng bỏ qua baseline trước khi bạn đã tuning nó thật kỹ."

---

## Scene 8.2 — Nghịch lý Model Selection
**Thời lượng ước tính: ~1.5 phút**

### VISUAL — từng bước

**Bước 8.2a**
Vòng lặp luẩn quẩn (circular arrows, xoay không dừng):

    "Muốn chọn model OOD tốt nhất"
             ↓
    "Cần validation set OOD"
             ↓
    "Nếu có OOD val set →
    sao không train trực tiếp?"
             ↓
    "Đưa vào train → không còn là OOD nữa!"
             ↓ (quay lại đầu)

Text trung tâm vòng tròn: "Model Selection Paradox" [GOLD]

**Bước 8.2b**
Hai lựa chọn không hoàn hảo:

    Option A: Dùng ID validation → không đảm bảo OOD performance
    Option B: Giả định biết test distribution → không thực tế

**Bước 8.2c**
Text:

    "Open Problem — chưa có lời giải hoàn hảo"

### AUDIO

"Một nghịch lý thực tiễn không có lời giải hoàn hảo. Giả sử bạn đã train ERM, IRM, và DRO. Bây giờ cần chọn model nào để deploy. Bạn cần một validation set OOD để đánh giá.

Nhưng nếu đã có validation set OOD, tại sao không dùng nó để train luôn? Và nếu dùng để train, nó không còn là OOD nữa.

Dùng ID validation set thường không tương quan tốt với OOD performance. Tutorial gọi đây là một trong những open problems quan trọng nhất của lĩnh vực."

---

## Scene 8.3 — Best Practices: Flowchart thực tiễn
**Thời lượng ước tính: ~2 phút**

### VISUAL — từng bước

**Bước 8.3a**
Vẽ decision flowchart, từng nhánh sáng lên theo lời đọc:

    START
       ↓
    Xác định loại Distribution Shift
    (Covariate? Label? Spurious?)
       ↓
    Có Group Labels không?
      ├── CÓ  ──→  Group DRO
      └── KHÔNG ──→  JTT hoặc Clustering-based
       ↓
    Đang dùng Foundation Model?
      ├── CÓ  ──→  Last Layer Retraining trước
      └── KHÔNG ──→  Tune ERM thật kỹ làm baseline
       ↓
    Tăng diversity training data nếu có thể
       ↓
    Luôn report Worst-Group Accuracy

Cuối cùng toàn bộ cây sáng.

### AUDIO

"Tutorial kết thúc với bảy best practices được đúc kết từ hàng trăm công trình nghiên cứu.

Một: hiểu rõ loại distribution shift trong bài toán của bạn trước khi chọn phương pháp. Hai: luôn report Worst-Group Accuracy, không chỉ average. Ba: tune ERM thật kỹ làm baseline trước. Bốn: nếu có group labels, Group DRO là lựa chọn mạnh nhất. Năm: nếu không, JTT hoặc clustering-based là điểm khởi đầu tốt. Sáu: với foundation models, thử Last Layer Retraining trước khi fine-tune toàn bộ. Và bảy, quan trọng nhất: thu thập thêm dữ liệu đa dạng môi trường. Data collection thường hiệu quả hơn mọi algorithmic fix."

---

---

# PHẦN 7 — KẾT LUẬN

---

## Scene 9.1 — Tổng hợp hành trình
**Thời lượng ước tính: ~2 phút**

### VISUAL — từng bước

**Bước 9.1a**
Camera zoom lùi chậm. Hiện ra bản đồ khái niệm toàn bộ:

    [ERM & Shortcuts]          [Foundation Models]
           ↓                          ↓
    [SCM / Causality]    ←→    [Scale ≠ Robustness]
           ↓
    [IRM] ── [DRO] ── [JTT]
           ↓
    [Benchmarks & Best Practices]

Tất cả nối nhau bằng mũi tên nhẹ.

**Bước 9.1b**
Mọi thứ mờ dần. Chỉ còn 3 từ xuất hiện lần lượt từ trái sang phải:

    CORRELATION  →  CAUSATION  →  STABILITY
      [GRAY]         [BLUE_D]      [GOLD, glow]

**Bước 9.1c**
Chữ STABILITY to nhất, particle effect nhẹ xung quanh. Dưới cùng:

    "Đây là ranh giới tiếp theo của Trí tuệ Nhân tạo."

### AUDIO

"Chúng ta đã đi một hành trình dài.

Bắt đầu từ một câu hỏi đơn giản: tại sao AI học những thứ sai? ERM và shortcut learning.

Rồi nhìn qua lăng kính nhân quả: spurious features tồn tại vì AI học tương quan thay vì nhân quả, và tương quan đó bị phá vỡ khi môi trường thay đổi.

Ba phương pháp, IRM, Group DRO, JTT, cố gắng buộc AI học causal features bằng những cách khác nhau: qua invariance của gradient, qua tối ưu worst-case, qua self-identification của thiểu số.

Và trong thời đại foundation models, vấn đề không biến mất. Nó chỉ thay đổi hình dạng và quy mô.

Tất cả dẫn về một từ: Stability. Một AI ổn định không phải là AI không bao giờ gặp phân phối mới. Mà là AI biết điều gì thực sự quan trọng, và giữ vững niềm tin đó dù hoàn cảnh thay đổi.

Đây là ranh giới tiếp theo."

---

## Scene 9.2 — Open Problems & Credits
**Thời lượng ước tính: ~45 giây**

### VISUAL — từng bước

**Bước 9.2a**
Ba icon cánh cửa chưa mở (ánh sáng hé ra từ khe):

    1. "Lý thuyết OOD cho Foundation Models"
    2. "Model Selection không cần OOD validation"
    3. "OOD trong Multimodal & Agentic AI"

**Bước 9.2b**
Fade in credits trên nền đen. SCM nodes tiếp tục xoay chậm ở background:

    Based on:
    NeurIPS 2024 Tutorial
    "Out-of-Distribution Generalization: Shortcuts, Spuriousness & Stability"
    Maggie Makar  ·  Aahlad Manas Puli  ·  Yoav Wald

    Produced by:
    Phan Huỳnh Châu Thịnh (Na)  ·  Mỹ Linh  ·  Hồng Thanh  ·  Trọng Hòa
    [Tên môn học]  ·  HCMUS  ·  [Năm học]
    GitHub: [link repository Manim]

### AUDIO

"Cảm ơn các bạn. Tutorial để lại ba cánh cửa mở: lý thuyết OOD cho foundation models, model selection không cần OOD validation, và OOD trong thế giới multimodal và agentic AI. Đây là biên giới tiếp theo của nghiên cứu. Link tutorial gốc, slides, và source code Manim đều có trong phần mô tả."

---

---

# PHỤ LỤC KỸ THUẬT MANIM

---

## A. Mapping Scene → File Python

| File | Scenes | Ước tính |
|------|--------|----------|
| module0_hook.py | 0.1, 0.2 | ~3 phút |
| module1_erm.py | 1.1, 1.2, 1.3 | ~6 phút |
| module2_framework.py | 2.1, 2.2, 2.3 | ~6 phút |
| module3_causality.py | 3.1, 3.2 | ~4 phút |
| module4_irm.py | 4.1, 4.2, 4.3, 4.4 | ~8 phút |
| module5_dro.py | 5.1 | ~3 phút |
| module6_jtt.py | 6.1 | ~3 phút |
| module7_foundation.py | 7.1, 7.2, 7.3, 7.4, 7.5, 7.6 | ~10 phút |
| module8_benchmarks.py | 8.1, 8.2, 8.3 | ~6 phút |
| module9_outro.py | 9.1, 9.2 | ~3 phút |
| TỔNG | | ~52 phút |

Lưu ý: Tutorial gốc khoảng 3 tiếng. Video giải thích 45 đến 55 phút là hợp lý.

---

## B. Snippets Kỹ thuật quan trọng

```python
# COLORS — dùng nhất quán toàn dự án
CAUSAL_COLOR   = BLUE_D
SPURIOUS_COLOR = RED
ENV_COLORS     = [GREEN_D, YELLOW_D, PURPLE]
MATH_HL        = GOLD
ALERT_COLOR    = ORANGE

# MovingCameraScene — zoom và pan
class ModuleScene(MovingCameraScene):
    def construct(self):
        self.play(
            self.camera.frame.animate.move_to(target).set_width(6)
        )
        self.wait(1)
        self.play(
            self.camera.frame.animate.move_to(formula).set_width(14)
        )

# TransformMatchingTex — ERM sang DRO
erm = MathTex(
    r"\min_\theta", r"\sum_g", r"p_g \cdot \mathbb{E}_g[\ell]"
)
dro = MathTex(
    r"\min_\theta", r"\max_{g \in \mathcal{G}}", r"\mathbb{E}_g[\ell]"
)
self.play(TransformMatchingTex(erm, dro, run_time=2))

# ValueTracker — lambda animation cho IRM
lam = ValueTracker(0)
lambda_label = always_redraw(
    lambda: DecimalNumber(
        lam.get_value(), num_decimal_places=1, color=ORANGE
    ).next_to(penalty_bar, RIGHT)
)
self.add(lambda_label)
self.play(lam.animate.set_value(10), run_time=3, rate_func=smooth)

# Causal Graph nodes
Y_node     = Circle(radius=0.45, color=GOLD  ).set_fill(GOLD,   0.15)
X_core     = Circle(radius=0.45, color=BLUE_D).set_fill(BLUE_D, 0.15).shift(LEFT*3.5)
X_spur     = Circle(radius=0.45, color=RED   ).set_fill(RED,    0.15).shift(RIGHT*3.5)
E_node     = Circle(radius=0.35, color=ORANGE).set_fill(ORANGE, 0.15).shift(UP*2+RIGHT*3.5)

arrow_causal   = Arrow(X_core.get_right(), Y_node.get_left(),      color=BLUE_D, buff=0.1)
arrow_spurious = Arrow(Y_node.get_right(), X_spur.get_left(),      color=RED,    buff=0.1)
arrow_env      = Arrow(E_node.get_bottom(), X_spur.get_top(),      color=ORANGE, buff=0.1)

# Spurious arrow vỡ vụn khi E thay đổi
self.play(
    FadeOut(arrow_spurious),
    Flash(
        arrow_spurious.get_center(),
        color=RED, num_lines=10, line_length=0.3
    ),
    run_time=1.2
)

# Parabolas cho IRM visualization
axes = Axes(
    x_range=[-0.5, 2.5], y_range=[0, 4],
    x_length=6, y_length=4
)
shifts = [0.4, 1.0, 1.7]
for shift, color in zip(shifts, ENV_COLORS):
    curve = axes.plot(
        lambda x, s=shift: (x - s)**2,
        color=color, stroke_width=3
    )
    self.add(curve)

# JTT Buckets
wrong_bucket   = RoundedRectangle(
    height=2.5, width=2.2,
    corner_radius=0.2, color=GOLD
).shift(RIGHT*2)
correct_bucket = RoundedRectangle(
    height=2.5, width=2.2,
    corner_radius=0.2, color=GRAY
).shift(LEFT*2)

for dot in minority_dots:
    self.play(
        dot.animate.move_to(wrong_bucket.get_center()),
        run_time=0.25
    )
```

---

## C. Checklist Nộp Bài

### Nội dung — tránh bị trừ điểm
- [ ] Đủ 6 phần: ERM, Framework, Causality, Methods (IRM + DRO + JTT), Foundation Models, Benchmarks + Best Practices
- [ ] Công thức IRMv1 đúng: gradient penalty, không phải bi-level gốc
- [ ] Scene 0.1 dùng ví dụ "man" vs "gentleman" từ slides gốc (không phải COVID)
- [ ] Scene 1.1 dùng Chim cánh cụt / Lạc đà từ slides gốc (không phải Bò / Lạc đà)
- [ ] Scene 7.3 dùng ICL "movie ~ positive" từ slides gốc
- [ ] Scene 7.4 Reverse Scaling được đề cập
- [ ] Scene 7.5 PfR (Prompting for Robustness) được đề cập với số liệu 91.05%
- [ ] Scene 7.6 CATO được đề cập
- [ ] Worst-Group Accuracy được định nghĩa và so sánh rõ
- [ ] Model Selection Paradox được đề cập
- [ ] Best practices cuối video (flowchart)

### Kỹ thuật — đảm bảo chất lượng
- [ ] Render ít nhất 1080p: manim -pqh
- [ ] Voiceover rõ, tốc độ 130 đến 150 từ/phút, không tiếng ồn nền
- [ ] Màu sắc nhất quán theo bảng màu đã định nghĩa
- [ ] TransformMatchingTex dùng ít nhất tại Scene 4.2 (IRM) và Scene 5.1 (ERM sang DRO)
- [ ] MovingCameraScene dùng để zoom vào SCM và các công thức

### Điểm thưởng
- [ ] Phụ đề tiếng Việt SRT khớp voiceover: +10 điểm
- [ ] GitHub repo Manim source code public: +10 điểm
- [ ] Mô tả YouTube đầy đủ: MSSV tất cả thành viên, tên môn học và lớp, GVLT và TG và GVTH, GitHub link, tutorial link + NeurIPS 2024
