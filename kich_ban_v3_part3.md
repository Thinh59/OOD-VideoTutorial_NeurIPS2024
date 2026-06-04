# KỊCH BẢN V3 — PART VII
## IRM: Invariant Risk Minimization (Đầy đủ + Failure Cases)

---

# PART VII — IRM: "Bất biến là chìa khóa"

---

## Scene 4.1 — IRM: Trực giác cốt lõi
**~2 phút**

### VISUAL
- 3 không gian 2D cạnh nhau, viền GREEN_D, YELLOW_D, PURPLE. Label: e₁, e₂, e₃.
- Trong mỗi không gian: scatter plot với phân phối trông KHÁC nhau.
  Nhưng ranh giới quyết định tối ưu thật (BLUE_D) thì GIỐNG nhau trong cả ba.
- Câu hỏi xuất hiện ở trung tâm:
  "Nếu môi trường thay đổi mà đường phân loại đúng vẫn giống nhau...
   thì đường đó phải dựa vào ĐẶC TRƯNG KHÔNG ĐỔI."
- Pause 2 giây. Text: "→ Đây là ý tưởng cốt lõi của IRM"
- Vẽ kiến trúc mạng chia 2 phần:
  `[Input x] → [Φ: Feature Extractor] → [w: Linear Classifier] → [Output]`
  BLUE_D (Φ), GREEN_D (w)
- Text: "Φ trích xuất đặc trưng. w phân loại. IRM ép Φ chỉ giữ causal features."

### AUDIO
"Chúng ta vừa thấy reweighting thất bại với mạng lớn. IRM — Invariant Risk Minimization — tiếp cận từ một góc độ hoàn toàn khác.

Hãy nhìn vào ba môi trường. Dữ liệu phân phối khác nhau — màu nền khác, ngữ cảnh khác. Nhưng ranh giới quyết định đúng — đường phân chia penguin và camel theo hình dáng thật — giống hệt nhau trong cả ba.

Tại sao? Vì hình dáng con vật không thay đổi theo môi trường. Đây là causal feature.

IRM đặt ra một yêu cầu thanh lịch: tìm cách biểu diễn dữ liệu Phi, sao cho cùng một bộ phân loại tuyến tính w sẽ tối ưu ở tất cả các môi trường đồng thời.

Nếu tồn tại Phi như vậy, Phi phải đã loại bỏ hết spurious features — vì chúng không nhất quán giữa các môi trường. Phi chỉ giữ lại causal features, vốn bất biến.

Nghe thanh lịch. Nhưng viết thành toán học như thế nào?"

---

## Scene 4.2 — IRM Objective: Bi-level Optimization
**~2 phút**

### VISUAL
- Công thức bi-level xuất hiện từng dòng:
  ```
  min_{Φ,w}  Σ_{e∈E}  R_e(w∘Φ)

  subject to  w ∈ argmin_{w̄} R_e(w̄∘Φ),  ∀e∈E
  ```
- Hộp RED bao constraint. Label: "Ràng buộc: w phải là minimum của MỌI environment"
- Giải thích dòng 1: "Minimize tổng risk trên mọi môi trường"
- Giải thích constraint: "w phải tối ưu riêng cho TỪNG môi trường — không chỉ tổng"
- Visualize constraint: 3 parabola Loss_e(w) với đáy ở vị trí khác nhau.
  Constraint nói: w=1.0 phải là đáy của CẢ BA. Nhưng đáy ở w=0.8, w=1.3, w=1.1 — không thể thỏa mãn cùng lúc.
- Hộp ORANGE: "NP-Hard — không giải trực tiếp bằng Gradient Descent"

### AUDIO
"IRM viết bài toán tối ưu bi-level: minimize tổng risk trên mọi môi trường, với ràng buộc rằng w phải là classifier tối ưu cho từng môi trường riêng lẻ.

Tại sao ràng buộc này quan trọng? Nếu w tối ưu ở environment e₁ nhưng không tối ưu ở e₂, nghĩa là Phi đang dùng một đặc trưng hữu ích ở e₁ nhưng hại ở e₂ — tức là spurious feature.

Ràng buộc này bảo đảm Phi trích xuất đặc trưng đủ bất biến để một w duy nhất làm việc được ở tất cả nơi.

Vấn đề: bài toán này là NP-Hard. Không giải trực tiếp bằng Gradient Descent. Hình dung: ba parabola với đáy ở ba vị trí khác nhau — không có w nào là đáy của cả ba cùng lúc.

Chúng ta cần một xấp xỉ. Và đây là nơi một trick toán học đẹp xuất hiện."

---

## Scene 4.2B — Từ Constraint đến Gradient Penalty
**~2 phút**

### VISUAL
- Nhắc lại: constraint cứng là `w ∈ argmin_{w̄} R_e(w̄∘Φ)`
- Text: "Nếu w=1.0 là minimum của R_e thì ∇_{w|w=1.0} R_e(w∘Φ) = 0"
  Đây là định nghĩa toán học của minimum.
- "→ Gradient lớn = w chưa phải minimum = vi phạm bất biến"
- "→ Đo vi phạm bằng độ lớn gradient!"
- TransformMatchingTex: constraint biến thành penalty:
  ```
  min_{Φ,w}  Σ_e R_e(w∘Φ)  +  λ·Σ_e ‖∇_{w|w=1.0} R_e(w∘Φ)‖²
             ──────────────    ──────────────────────────────────
             fit mọi môi trường    penalty vi phạm bất biến
  ```
- Penalty term xuất hiện từ bên phải, màu ORANGE.
- ValueTracker: λ tăng từ 0 → 10 trong 3 giây.
  Ba parabola dần dịch chuyển, đáy hội tụ về w=1.0.
- Text: "IRMv1 — phiên bản thực tế có thể train bằng Gradient Descent"

### AUDIO
"Trick toán học: nếu w bằng 1.0 là minimum của hàm loss, thì gradient của hàm loss tại w bằng 1.0 phải bằng 0. Đó là định nghĩa của minimum.

Vậy thay vì ràng buộc cứng — w phải là argmin — ta thay bằng penalty mềm: phạt khi gradient lớn.

Gradient lớn tại w=1.0 nghĩa là w chưa phải minimum ở environment đó, Phi đang dùng shortcut. Gradient nhỏ nghĩa là Phi đã học đặc trưng bất biến.

Đây là IRMv1. Khi lambda tăng, optimizer bị ép phải tìm Phi sao cho mọi môi trường đồng thuận. Spurious features bị loại vì chúng là nguyên nhân của sự bất đồng.

Nhưng có một điểm tinh tế: tại sao dùng w=1 cố định thay vì w tổng quát?"

---

## Scene 4.3 — Tại sao w=1? Geometry của IRMv1
**~90 giây**

### VISUAL
- Không gian đặc trưng Φ(x) 2D.
- Với w=1 scalar: classifier là hyperplane qua origin với hệ số do Φ quyết định.
- Giải thích: "w=1 không mất tính tổng quát — Φ có thể học scale"
- Vẽ 3 environment: mỗi environment có gradient vector tại điểm w=1.
  - Với spurious feature: gradient vectors chỉ về 3 hướng KHÁC nhau (phân kỳ)
  - Với causal feature: gradient vectors gần như cùng hướng (hội tụ)
- Animation: penalty ép gradient hội tụ → spurious bị đẩy ra khỏi Φ.
- Text: "Invariant representation = gradient đồng thuận qua mọi environment"

### AUDIO
"Tại sao chọn w bằng 1 cố định? Vì với classifier tuyến tính, w chỉ là scalar scale — Phi có thể học scale đó vào trong representation của mình. Nên w=1 không mất tính tổng quát, nhưng đơn giản hóa bài toán đáng kể.

Nhìn trực quan: với spurious feature, gradient tại w=1 trỏ về hướng khác nhau ở mỗi environment — vì spurious hữu ích ở environment này nhưng hại ở environment kia. Penalty phạt sự phân kỳ này.

Với causal feature, gradient gần như đồng hướng qua mọi environment. Penalty gần như bằng không. Phi được phép giữ causal feature.

Kết quả: Phi hội tụ về invariant representation — chỉ chứa những gì nhất quán qua mọi môi trường."

---

## Scene 4.4 — Gradient Vectors Hội tụ (Visualization)
**~90 giây**

### VISUAL
- Không gian tham số w (trục số). Ba parabola với đáy ở vị trí khác nhau.
- Tại điểm w=1.0: 3 vector gradient (mũi tên) chỉ về 3 hướng khác nhau (phân kỳ).
  Label: "3 môi trường bất đồng → shortcut đang được dùng!"
- ValueTracker λ tăng dần. Ba vector gradient xoay từng bước về cùng hướng, nhỏ dần, tiến về 0.
  Label: "Penalty ép đồng thuận → shortcut bị loại"
- Final state: cả 3 gradient ≈ 0. Ba parabola có đáy gần nhau.
  Text: "Phi đã học invariant features ✓"

### AUDIO
"Hình dung trực quan. Nếu Phi đang dùng spurious feature, đặc trưng đó hữu ích ở một số môi trường nhưng hại ở môi trường khác. Mỗi môi trường muốn w dịch chuyển theo hướng khác nhau. Ba vector gradient chỉ về ba hướng khác nhau — bất đồng.

Khi penalty lambda tăng, optimizer bị phạt nếu các gradient còn phân kỳ. Nó buộc phải tìm Phi mà tất cả môi trường đồng thuận. Spurious features bị loại khỏi Phi vì chúng là nguyên nhân của sự bất đồng.

Phần còn lại trong Phi — những chiều mà mọi environment đồng ý — chính là causal features."

---

## Scene 4.5 — IRM Failure Cases: Khi Bất biến Không Đủ
**~2.5 phút**

### VISUAL
- Tiêu đề lớn: "IRM is NOT a Silver Bullet" [ORANGE]
- 3 counterexample, mỗi cái có SCM diagram nhỏ + dấu ✗ RED:

**Counterexample 1: Invariant Feature giả**
- SCM: X_spur tình cờ bất biến qua tất cả environments trong tập train.
- Ví dụ: tất cả bệnh viện trong train đều có cùng thói quen viết "man/gentleman".
- Text: "Spurious feature bất biến trong train ≠ causal. IRM không phân biệt được."

**Counterexample 2: Environments không đủ đa dạng**
- 2 environment với cùng spurious correlation (P(Z=Y)=0.95 ở CẢ HAI).
- IRM không có bất đồng để detect → không loại được spurious.
- Text: "IRM cần diversity. Không đủ diversity → gradient penalty = 0 ở cả hai."

**Counterexample 3: Shortcut tồn tại ở mọi environment**
- SCM: spurious feature Z không phụ thuộc vào E — Z tồn tại ở mọi nơi.
- Ví dụ: race/gender bias trong ngôn ngữ — tồn tại ở mọi dataset.
- IRM không thể loại Z vì Z không "vi phạm" bất biến.

### AUDIO
"Chính vì những đặc điểm trên, IRM nghe rất thanh lịch về lý thuyết. Nhưng thực tế khắc nghiệt hơn nhiều.

Ba trường hợp IRM thất bại.

Thứ nhất: invariant feature giả. Nếu một spurious feature tình cờ bất biến qua tất cả environments trong tập train — ví dụ tất cả bệnh viện train đều có cùng thói quen ghi chép — IRM sẽ giữ spurious feature đó vì nó 'vượt qua' bài kiểm tra bất biến.

Thứ hai: environments không đủ đa dạng. IRM hoạt động bằng cách phát hiện BẤT ĐỒNG giữa environments. Nếu hai environments có cùng spurious correlation mạnh, gradient penalty ở cả hai đều nhỏ — IRM không phát hiện vấn đề.

Thứ ba: shortcut tồn tại ở mọi environment. Bias về race hay gender trong ngôn ngữ không phải là spurious correlation phụ thuộc environment — chúng xuất hiện ở mọi nơi. IRM không có cơ chế loại bỏ chúng.

Nhiều nghiên cứu thực nghiệm cho thấy ERM được tuning tốt đôi khi còn vượt trội IRMv1 trên benchmark thực tế. IRM mạnh về lý thuyết, nhưng fragile trong practice.

Vậy nếu không có đủ môi trường rõ ràng, hoặc shortcut không phải environment-dependent, ta cần hướng tiếp cận khác. Và đó là khi ta quay lại với cấu trúc nhóm — nhưng lần này với một công thức chặt chẽ hơn."

---

## Scene 4.6 — IRM trong Thực tế: Khi nào dùng?
**~60 giây**

### VISUAL
- Bảng tóm tắt:
  | Điều kiện | IRM phù hợp? |
  |-----------|--------------|
  | Có nhiều environments đa dạng | ✓ Tốt |
  | Spurious khác nhau rõ giữa environments | ✓ Tốt |
  | Chỉ 2 environments giống nhau | ✗ Yếu |
  | Spurious tồn tại mọi nơi | ✗ Yếu |
  | Neural network rất lớn | ✗ Yếu (interpolation) |
- Hộp GOLD: "IRM: nền tảng lý thuyết nhân quả vững, nhưng cần environments chất lượng cao"
- Arrow chỉ sang: "Nếu không có environments → NuRD hoặc Group DRO"

### AUDIO
"Tóm lại về IRM: nó hoạt động tốt khi bạn có nhiều environments đủ đa dạng và spurious correlation thay đổi đáng kể giữa các environments. Đây là setting lý tưởng nhất.

Nhưng trong nhiều bài toán thực tế — y tế, ngôn ngữ, khoa học — bạn không có luxury đó. Environments không đủ hoặc không đủ đa dạng.

Chính vì những thất bại này, cộng đồng đã phát triển hai hướng song song. Một là NuRD — tìm và loại bỏ nuisance features một cách trực tiếp. Hai là Group DRO — thay vì bất biến, tối ưu trực tiếp worst-case group. Ta sẽ đến cả hai."
