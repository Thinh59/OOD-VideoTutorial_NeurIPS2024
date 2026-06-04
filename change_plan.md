# 📋 KẾ HOẠCH CHỈNH SỬA KỊCH BẢN OOD — 10 VẤN ĐỀ

## Tổng quan

| Metric | Hiện tại | Mục tiêu |
|--------|----------|----------|
| Số từ | ~4,500 | ~15,000–18,000 |
| Coverage | ~40% | ~90–95% |
| Số scene | ~22 | ~45–50 |
| Thời lượng | ~50 phút | ~80–100 phút |

---

## CẤU TRÚC MỚI ĐỀ XUẤT

```
PART I  – VẤN ĐỀ (Scene 0.1 → 1.3)           ← GIỮ NGUYÊN
PART Ia – FORMALIZING (Scene F1→F4)            ← MỚI (VĐ1)
PART Ib – RISK AGGREGATION (Scene R1→R4)       ← MỚI (VĐ2)
PART II – FRAMEWORK TOÁN HỌC (2.1→2.3)        ← GIỮ + SỬA
PART IIa – GIẢ ĐỊNH TOÁN HỌC (1.4A→1.4C)     ← MỚI (VĐ3)
PART III – NHÂN QUẢ (3.1→3.2)                 ← GIỮ NGUYÊN
PART IV – REWEIGHTING (RW1→RW3)               ← MỚI (VĐ6)
PART V  – IRM (4.1→4.4 mở rộng + 4.5 Failure) ← SỬA + MỚI (VĐ4,5)
PART VI – NuRD (N1→N5)                        ← MỞ RỘNG (VĐ7)
PART VII – GROUP DRO (5.1 mở rộng)            ← SỬA (VĐ8)
PART VIII – JTT (6.1)                         ← GIỮ NGUYÊN
PART IX  – BENCHMARKS (B1→B5)                 ← MỞ RỘNG (VĐ9)
PART X   – FOUNDATION MODELS (7.1→7.6 mở rộng)← SỬA (VĐ10)
PART XI  – KẾT LUẬN (9.1→9.2)                ← GIỮ + CẬP NHẬT
```

---

## CHI TIẾT 10 VẤN ĐỀ

### VĐ1: THIẾU FORMALIZING THE PROBLEM
**Vị trí chèn:** Sau Scene 1.3, trước PHẦN 2
**Scenes mới:** 4 scenes

| Scene | Tiêu đề | Nội dung chính | Thời lượng |
|-------|---------|----------------|------------|
| F1 | From Clinical Example to Math | X=input, Y=label, E=environment. Ví dụ: X=bệnh án, Y=bệnh, E=bệnh viện | ~90s |
| F2 | OOD Generalization Definition | ID: (X,Y)∼P_train. OOD: (X,Y)∼P_test, P_train≠P_test | ~60s |
| F3 | Environment Distribution | e∈E, mỗi environment có P_e(X,Y) | ~60s |
| F4 | The Set of Possible Worlds | P = {p₁, p₂, p₃,...}. Muốn tốt trên cả họ phân phối | ~90s |

**Audio keywords:** formal definition, distribution, environment, robustness across distributions

---

### VĐ2: THIẾU RISK AGGREGATION
**Vị trí chèn:** Sau VĐ1 (F4), trước PHẦN 2
**Scenes mới:** 4 scenes

| Scene | Tiêu đề | Nội dung | Thời lượng |
|-------|---------|----------|------------|
| R1 | Expected Risk | R(h) = E[L(h(X),Y)] — định nghĩa risk cho 1 phân phối | ~60s |
| R2 | Average Risk (ERM) | (1/n)Σℓᵢ — ERM tối ưu cái này | ~60s |
| R3 | Worst-Case Risk | max_e R_e(h) — bệnh nhân thiểu số mới bị tổn thương | ~90s |
| R4 | Risk Aggregation Families | Heatmap: Mean, Max, CVaR, DRO. Insight: thuật toán chỉ khác nhau ở cách gộp rủi ro | ~90s |

**Audio keywords:** risk, aggregation, worst-case, CVaR, distributionally robust

---

### VĐ3: THIẾU GIẢ ĐỊNH TOÁN HỌC
**Vị trí chèn:** Sau Scene 2.3, trước PHẦN 3
**Scenes mới:** 3 scenes

| Scene | Tiêu đề | Nội dung | Thời lượng |
|-------|---------|----------|------------|
| 1.4A | Generative Model | x = yφ* + yzψ* + ξ. Giải thích từng thành phần | ~90s |
| 1.4B | Majority vs Minority | P(Z=Y)=0.95, P(Z≠Y)=0.05. Visual: pie chart | ~60s |
| 1.4C | Simplicity Bias | Tại sao GD chọn Z trước. Gradient theo spurious feature giảm nhanh hơn | ~90s |

**Audio keywords:** generative model, simplicity bias, gradient descent, majority/minority

---

### VĐ4: IRM QUÁ NÔNG
**Vị trí:** Mở rộng Scene 4.1–4.3 hiện tại
**Thay đổi:**

| Hành động | Chi tiết |
|-----------|----------|
| **Mở rộng 4.1** | Thêm: Φ(X) là representation, muốn ∃ w tối ưu ∀e. Xây dựng từ trực giác trước |
| **Mở rộng 4.2** | Tách rõ: (1) Bi-level objective đầy đủ → (2) Tại sao constraint khó → (3) Relaxation thành penalty → (4) IRMv1 formula |
| **Thêm Scene 4.2B** | Geometry của IRM: invariant representation trong feature space |
| **Giữ 4.3** | Gradient vectors hội tụ — giữ nguyên |

---

### VĐ5: THIẾU IRM FAILURE CASES
**Vị trí:** Mở rộng Scene 4.4
**Thay đổi:**

| Hành động | Chi tiết |
|-----------|----------|
| **Mở rộng 4.4** | Thêm 3 counterexamples cụ thể: (1) Invariant Feature giả, (2) Environment không đủ đa dạng, (3) Shortcut tồn tại ở mọi environment |
| **Thêm visual** | Mỗi counterexample = 1 SCM diagram nhỏ + dấu ✗ |
| **Thời lượng** | Từ ~1 phút → ~2.5 phút |

---

### VĐ6: THIẾU REWEIGHTING FAMILY
**Vị trí chèn:** Trước IRM (trước Scene 4.1)
**Scenes mới:** 3 scenes

| Scene | Tiêu đề | Nội dung | Thời lượng |
|-------|---------|----------|------------|
| RW1 | Reweighting Principle | L = Σwᵢℓᵢ. Tăng trọng số minority | ~90s |
| RW2 | Oracle Reweighting | Nếu biết P(Y|Z), weighting hoàn hảo | ~60s |
| RW3 | Why Reweighting Fails | Interpolation: mạng lớn → loss=0 → trọng số vô nghĩa | ~90s |

---

### VĐ7: NuRD MỞ RỘNG
**Vị trí:** Sau IRM, trước Group DRO
**Thay đổi:** Từ 0 scene riêng → 5 scenes

| Scene | Tiêu đề | Nội dung | Thời lượng |
|-------|---------|----------|------------|
| N1 | NuRD Core Idea | Y⊥Z|φ(X). Lọc nuisance khỏi representation | ~90s |
| N2 | Detecting Nuisance: Semantic Corruption | Masking, n-gram randomization | ~60s |
| N3 | Vision Masking | Che phần ảnh → model vẫn đoán đúng = shortcut | ~60s |
| N4 | Teacher-Student Distillation | Teacher trên corrupted data → Student học clean | ~90s |
| N5 | Mutual Information Intuition | min I(φ(X); Z) while keeping I(φ(X); Y) | ~60s |

---

### VĐ8: GROUP DRO THIẾU CÔNG THỨC
**Vị trí:** Mở rộng Scene 5.1
**Thay đổi:**

| Hành động | Chi tiết |
|-----------|----------|
| **Thêm công thức** | min_h max_g R_g(h) — inner maximization + outer minimization |
| **Thêm giải thích** | Inner: tìm nhóm tệ nhất. Outer: tối ưu cho nhóm đó |
| **Thêm limitations** | Oracle group labels cần thiết, practical limitations |
| **Thời lượng** | Từ ~2.5 phút → ~4 phút |

---

### VĐ9: THIẾU BENCHMARK CRISIS
**Vị trí:** Mở rộng PHẦN 6 (Scene 8.1–8.2)
**Thay đổi:** Từ 3 scenes → 5+ scenes

| Scene | Tiêu đề | Nội dung | Thời lượng |
|-------|---------|----------|------------|
| B1 | Benchmark Gallery | Waterbirds, CelebA, CivilComments, Camelyon17, WILDS — chi tiết từng cái | ~2 phút |
| B2 | Are Benchmarks Realistic? | Câu hỏi: benchmark có phản ánh thực tế? | ~90s |
| B3 | Benchmark Disagreement | Pearson correlation heatmap, không method nào win all | ~90s |
| B4 | Model Selection Problem | OOD validation paradox (giữ 8.2 hiện tại + mở rộng) | ~90s |
| B5 | The Real Lesson | Thuật toán không tệ, benchmark mới là vấn đề | ~60s |

---

### VĐ10: FOUNDATION MODELS THIẾU ARC
**Vị trí:** Mở rộng PHẦN 5 (Scene 7.1–7.6)
**Thay đổi:** Thêm arc narrative hoàn chỉnh

| Thay đổi | Chi tiết |
|----------|----------|
| **Thêm Scene 7.0** | "The Promise of Scale" — Accuracy on the Line, evidence across datasets |
| **Mở rộng 7.1** | Scale cứu OOD? → Evidence → Nhưng không hẳn |
| **Thêm Scene 7.1B** | "Broken Promises" — vertical/horizontal/no trend/negative correlation |
| **Mở rộng 7.4** | Label Noise + Reverse Scaling chi tiết hơn |
| **Narrative arc** | Scale hứa hẹn → Scale thất bại → Scale còn tệ hơn → Scale giúp gán nhãn → Dùng Scale sửa Scale |

---

## THỨ TỰ THỰC HIỆN

| Phase | Việc | Ảnh hưởng |
|-------|------|-----------|
| 1 | VĐ1 + VĐ2: Formalizing + Risk Aggregation | Đặt nền móng toán học |
| 2 | VĐ3: Mathematical Assumptions | Kết nối ERM → tại sao GD chọn shortcut |
| 3 | VĐ6: Reweighting Family | Cần trước IRM để có flow logic |
| 4 | VĐ4 + VĐ5: IRM mở rộng + Failure | Phần methods chính |
| 5 | VĐ7: NuRD mở rộng | Methods tiếp theo |
| 6 | VĐ8: Group DRO formulas | Methods cuối |
| 7 | VĐ9: Benchmark Crisis | Reality check |
| 8 | VĐ10: Foundation Models arc | Câu chuyện kết |

---

## TỔNG KẾT SCENES MỚI/SỬA

| Loại | Số lượng |
|------|----------|
| Scene **mới hoàn toàn** | ~22 scenes |
| Scene **mở rộng đáng kể** | ~8 scenes |
| Scene **giữ nguyên** | ~12 scenes |
| **Tổng** | ~42–45 scenes |

> [!IMPORTANT]
> Trước khi viết kịch bản chi tiết, cần xác nhận:
> 1. Bạn muốn bản **~8,000 từ (75% coverage)** hay **~15,000 từ (95% coverage)**?
> 2. Có muốn giữ nguyên format hiện tại (VISUAL + AUDIO riêng) hay đổi format?
> 3. Thứ tự scenes trong kịch bản có đúng như đề xuất trên không?
