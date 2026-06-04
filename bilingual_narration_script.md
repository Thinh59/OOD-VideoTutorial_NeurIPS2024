# Bilingual Narration Script (Kịch Bản Song Ngữ Anh - Việt)

This document contains the complete, scene-by-scene narration script in both English and Vietnamese for the 31 scenes of the educational video tutorial on Out-of-Distribution (OOD) Generalization.

---

## Table of Contents
1. [Module 0: Hook & Roadmap](#module-0-hook--roadmap)
2. [Module 1: ERM & Shortcuts](#module-1-erm--shortcuts)
3. [Module 2: Group Structure & Metrics](#module-2-group-structure--metrics)
4. [Module 3: Causality & SCM](#module-3-causality--scm)
5. [Module 4: Importance Weighting & IRM](#module-4-importance-weighting--irm)
6. [Module 5: Group DRO & NuRD](#module-5-group-dro--nurd)
7. [Module 6: Semantic Corruption & JTT](#module-6-semantic-corruption--jtt)
8. [Module 7: Foundation Models & AI Fixing AI](#module-7-foundation-models--ai-fixing-ai)
9. [Module 8: Benchmarks & Reality Checks](#module-8-benchmarks--reality-checks)
10. [Module 9: Journey Summary & Conclusion](#module-9-journey-summary--conclusion)

---

## Module 0: Hook & Roadmap

### Scene 0.1 — Opening Clinical Notes (Mở Đầu: Hồ Sơ Lâm Sàng)
*   **English**: 
    "Let us begin with a real-world example. An AI system is trained to predict diseases from electronic health records. At Hospital A, it reaches an impressive ninety-five percent accuracy. But when we transfer the same model to Hospital B, the accuracy drops to seventy-two percent. What happened? A closer look at the training data reveals the truth. At Hospital A, one specific doctor had a habit: he wrote the word man for diabetes patients, and the word gentleman for arthritis patients. Two synonyms, yet the AI exploited this stylistic habit as a shortcut. In Hospital B, the new doctors did not share this habit. The shortcut disappeared, and the model collapsed. This is the core issue of this tutorial. The model did not fail because of a lack of parameters or data. It failed because it learned the wrong signal."
*   **Tiếng Việt**:
    "Hãy bắt đầu với một ví dụ thực tế. Một AI được huấn luyện để dự đoán bệnh từ hồ sơ bệnh án điện tử. Tại Bệnh viện A, nó đạt 95 phần trăm — ấn tượng. Nhưng khi chuyển sang Bệnh viện B, accuracy rớt xuống 72 phần trăm. Điều gì đã xảy ra? Nhìn kỹ vào dữ liệu huấn luyện. Tại Viện A, một bác sĩ cụ thể có thói quen: ông ta viết 'man' khi ghi hồ sơ bệnh nhân tiểu đường, và 'gentleman' khi ghi bệnh nhân viêm khớp. Hai từ đồng nghĩa — nhưng AI đã học được sự phân biệt này và dùng nó như một đường tắt. Khi sang Viện B, bác sĩ mới không có thói quen đó. Shortcut biến mất. Mô hình sụp đổ. Đây chính là vấn đề trọng tâm của tutorial này. Không phải AI thiếu dữ liệu hay thiếu tham số. Mà là AI đang học sai thứ."

### Scene 0.2 — Road Map (Lộ Trình)
*   **English**:
    "In this video, we will walk through eight key stops. We begin with the intuition behind shortcut learning, move to the mathematical formalization of out-of-distribution generalization, define risk aggregation families, analyze the causal structure of spurious correlations, explore robust methods from reweighting to IRM and DRO, evaluate their real-world performance on benchmarks, examine how foundation models change the landscape, and finally, discuss how we can leverage large models to correct robustness failures. Let us begin."
*   **Tiếng Việt**:
    "Trong video này chúng ta sẽ đi qua tám chặng. Bắt đầu bằng trực giác về vấn đề, sau đó hình thức hóa bằng toán học, định nghĩa risk và cách đo lường robustness, nhìn qua lăng kính nhân quả, khám phá các phương pháp giải quyết từ reweighting đến IRM và DRO, đánh giá thực tế qua benchmark, rồi xem foundation models thay đổi bài toán như thế nào. Và cuối cùng, liệu AI có thể tự sửa lỗi của chính mình. Đi thôi."

---

## Module 1: ERM & Shortcuts

### Scene 1.1 — ERM and the Accuracy Illusion (ERM và Ảo Ảnh Accuracy Cao)
*   **English**:
    "Let us start with a classic example. You are building an AI classifier to distinguish between penguins and camels. In the training dataset, penguins are always photographed on snow, and camels are always photographed on sand. In this two-dimensional feature space, the classes are perfectly separable. The model easily draws a decision boundary and achieves ninety-eight percent training accuracy. But look closely at what this decision boundary is doing. It aligns with the horizontal axis, the background color. It ignores the vertical axis, the actual animal shape. When we place a penguin on sand, the model predicts camel without hesitation. The prediction is wrong. To understand why, we must look at the heart of modern machine learning."
*   **Tiếng Việt**:
    "Hãy bắt đầu bằng ví dụ kinh điển trong tutorial. Bạn xây dựng AI phân loại chim cánh cụt và lạc đà. Tập dữ liệu huấn luyện: chim cánh cụt luôn đứng trên tuyết trắng, lạc đà luôn đứng trên cát vàng. Trong không gian đặc trưng hai chiều, dữ liệu chia thành hai cụm tách biệt hoàn hảo. Thuật toán học và vẽ được một đường phân loại. Accuracy 98 phần trăm. Tuyệt vời. Nhưng chú ý kỹ đường này đang làm gì. Nó đi theo trục ngang — đọc màu nền. Không phải trục dọc — hình dáng con vật. Khi một chú chim cánh cụt bị đặt trên cát vàng, đường phân loại không ngần ngại: đây là lạc đà. Sai hoàn toàn. Để hiểu tại sao, chúng ta cần nhìn vào trái tim của mọi thuật toán học máy hiện đại."

### Scene 1.2 — Why ERM Is Lazy (Giải Phẫu ERM: Tại Sao Nó Lười?)
*   **English**:
    "Empirical Risk Minimization, or ERM, is the standard machine learning framework. The objective is simple: find a set of parameters theta that minimizes the average loss on the training distribution. However, ERM has a single goal: to drop the training loss as quickly as possible. It is indifferent to whether the loss drops due to semantic understanding or simple shortcuts. From the perspective of gradient descent, there are two paths: analyze complex morphology, which is hard, or count background pixels, which is easy. Gradient descent always follows the path of the steepest descent. It chooses the background shortcut first, not because it is correct, but because it is the fastest way to minimize the loss. We call these unstable background features spurious features. They appear useful in the training data, but they are merely artifacts of the environment. So how do we mathematically distinguish between stable, causal signals and brittle, spurious features?"
*   **Tiếng Việt**:
    "ERM, Empirical Risk Minimization, là thuật toán học máy tiêu chuẩn. Ý tưởng đơn giản: tìm bộ tham số theta để minimize sai số trung bình trên tập train. Nhưng chú ý: ERM chỉ có một mục tiêu duy nhất — giảm Loss. Nó không biết, không quan tâm, liệu sự giảm đó đến từ hiểu thật sự hay từ đường tắt. Hãy hình dung từ góc nhìn Gradient Descent. Có hai con đường: phân tích hình thái học — tốn nhiều bước, khó học. Hoặc đếm pixel nền — một phép tính đơn giản. Gradient Descent luôn chọn con đường hai. Không phải vì nó xấu xa, mà vì đó là chiều gradient giảm nhanh nhất. Chúng ta gọi những đặc trưng như màu nền đó là Spurious Features — đặc trưng ảo. Chúng trông giống tín hiệu hữu ích trong train data, nhưng chỉ là sự trùng hợp của ngữ cảnh. Và câu hỏi tự nhiên tiếp theo là: làm sao ta phân biệt chính xác giữa đặc trưng thật và đặc trưng ảo?"

### Scene 1.3 — What Is a Spurious Feature? (Spurious Feature: Chính Xác Là Gì?)
*   **English**:
    "What exactly is a spurious feature? Let us think about the data generating process. A photographer wants to take a picture of a penguin, so they travel to the Arctic. The penguin is the cause, and the snowy background is the effect. The causal arrow points from the label to the background. But the AI reads this arrow in reverse: it sees the background and infers the penguin. This is anti-causal prediction. When the environment changes, such as a penguin standing on a beach, this correlation shatters. Yet, the true causal relationship remains: a penguin still looks like a penguin regardless of its background. Causal features are invariant across environments. Spurious features are brittle and bound to specific contexts. To resolve this, we need a formal mathematical language."
*   **Tiếng Việt**:
    "Vậy spurious feature là gì, chính xác? Hãy nghĩ về chuỗi sự kiện tạo ra dữ liệu. Nhiếp ảnh gia muốn chụp chim cánh cụt, họ đến Bắc Cực. Con chim là nguyên nhân, nền tuyết trắng là kết quả. Mũi tên nhân quả đi từ nhãn sang nền. Nhưng AI đang đọc ngược lại: thấy nền trắng, kết luận chim cánh cụt. Đây là dự đoán ngược chiều nhân quả. Khi môi trường thay đổi — chim cánh cụt xuất hiện ở sa mạc — tương quan đó tan biến. Nhưng mối quan hệ nhân quả thật vẫn còn: chim cánh cụt có hình dáng chim cánh cụt dù đứng ở đâu. Causal features ổn định qua mọi môi trường. Spurious features chỉ tồn tại ở một hoàn cảnh cụ thể. Nhưng cho đến giờ, tất cả những gì ta nói vẫn là trực giác. Để thực sự giải quyết vấn đề, ta cần một ngôn ngữ toán học chính xác."

### Scene 1.4 — Geometry and Inductive Bias (Mô Hình Toán Học & Simplicity Bias)
*   **English**:
    "To understand why gradient descent consistently prefers shortcuts, we look at the simplicity bias. In our generative model, the input x is a combination of the causal feature phi-star, the spurious feature psi-star modulated by the environment z, and noise. The majority group, where the environment matches the label, accounts for ninety-five percent of the training data. The minority group, where they mismatch, accounts for only five percent. For ERM, this five percent is virtually invisible. The average loss is dominated by the majority group, allowing the model to achieve high accuracy by learning the shortcut. Geometrically, the max-margin boundary is pulled toward the majority geometry, leaving the minority groups with insufficient margin. The invariant feature is present, but underused. This is not a software bug; it is a fundamental property of gradient-based optimization. To fix it, we must intervene."
*   **Tiếng Việt**:
    "Để hiểu tại sao gradient descent luôn chọn shortcut, ta cần một mô hình toán học chính xác cho dữ liệu và hiện tượng simplicity bias. Trong mô hình sinh của chúng ta, đầu vào x là tổ hợp của đặc trưng nhân quả phi-star, đặc trưng ảo psi-star đi kèm môi trường z, và nhiễu. Nhóm đa số chiếm 95% dữ liệu huấn luyện, nơi môi trường khớp với nhãn. Nhóm thiểu số chiếm 5%. Với ERM, nhóm thiểu số 5% này gần như vô hình. Loss trung bình bị thống trị bởi nhóm đa số, cho phép mô hình đạt accuracy cao bằng cách học shortcut. Về mặt hình học, ranh giới max-margin bị kéo về phía nhóm đa số, khiến nhóm thiểu số không đủ margin bảo vệ. Đặc trưng bất biến có tồn tại nhưng bị bỏ qua. Đây không phải lỗi code, mà là đặc tính cơ bản của tối ưu hóa gradient. Để khắc phục, chúng ta phải can thiệp."

---

## Module 2: Group Structure & Metrics

### Scene 2.1 — Group Structure (Cấu Trúc Nhóm)
*   **English**:
    "To measure this failure, we split the training distribution into groups defined by the cross-product of the label Y and the spurious attribute Z. This yields four groups. The majority groups, like cows on grass and camels on sand, are large. The minority groups, like cows on sand and camels on grass, are small. Standard ERM averages the risk across all groups. Because the majority dominates, the average risk remains low even if the model performs terribly on the minority. The model sacrifices the minority groups to minimize the average loss. This average hides the failure."
*   **Tiếng Việt**:
    "Để đo lường thất bại này, ta chia phân phối huấn luyện thành các nhóm dựa trên tích đề-các của nhãn Y và thuộc tính ảo Z. Điều này tạo ra bốn nhóm. Nhóm đa số (như bò trên cỏ, lạc đà trên cát) rất lớn. Nhóm thiểu số (như bò trên cát, lạc đà trên cỏ) rất nhỏ. ERM tiêu chuẩn lấy trung bình rủi ro trên mọi nhóm. Vì đa số áp đảo, rủi ro trung bình vẫn thấp ngay cả khi mô hình dự đoán tệ hại trên nhóm thiểu số. Mô hình sẵn sàng hy sinh nhóm thiểu số để giảm thiểu loss trung bình. Giá trị trung bình này che giấu đi sự thất bại."

### Scene 2.2 — Worst-Group Accuracy (Độ Chính Xác Trên Nhóm Tệ Nhất)
*   **English**:
    "To expose this failure, we define worst-group accuracy: the lowest accuracy among all defined groups. If we compare ERM with a robust algorithm, ERM might achieve a higher average accuracy of eighty-two percent but a worst-group accuracy of only eighteen percent. The robust model might achieve seventy-six percent average accuracy but maintain a seventy-two percent worst-group accuracy. In high-stakes domains like medicine or law, the worst-group accuracy represents the deployment risk. A model that is almost always wrong on a minority group is unsafe for clinical use."
*   **Tiếng Việt**:
    "Để vạch trần thất bại này, ta định nghĩa worst-group accuracy: độ chính xác thấp nhất trong tất cả các nhóm được xác định. Nếu ta so sánh ERM với một thuật toán robust, ERM có thể đạt trung bình 82% nhưng worst-group chỉ có 18%. Mô hình robust đạt trung bình 76% nhưng giữ được worst-group là 72%. Trong các lĩnh vực rủi ro cao như y tế hay luật pháp, worst-group accuracy đại diện cho rủi ro triển khai thực tế. Một mô hình gần như luôn sai trên nhóm thiểu số là không an toàn để sử dụng."

### Scene 2.3 — Distribution Shift Types (Các Loại Dịch Chuyển Phân Phối)
*   **English**:
    "Not all distribution shifts are the same. Covariate shift changes the input distribution P of X while keeping the label conditional P of Y given X constant. Label shift changes the class proportions P of Y. Spurious shift, however, alters the relationship between the shortcut and the label. The correlation that held during training flips or disappears. This is the most challenging shift because the model's reliance on the shortcut actively leads it astray when the correlation breaks."
*   **Tiếng Việt**:
    "Không phải mọi phân phối lệch (distribution shift) đều giống nhau. Covariate shift làm thay đổi phân phối đầu vào P(X) nhưng giữ nguyên xác suất có điều kiện P(Y|X). Label shift làm thay đổi tỷ lệ các lớp P(Y). Tuy nhiên, spurious shift thay đổi hoàn toàn mối quan hệ giữa shortcut và nhãn. Sự tương quan từng tồn tại trong lúc huấn luyện bị đảo ngược hoặc biến mất. Đây là loại shift thách thức nhất vì việc mô hình dựa vào shortcut sẽ dẫn đến sai lầm nghiêm trọng khi tương quan bị gãy."

---

## Module 3: Causality & SCM

### Scene 3.1 — Structural Causal Model (Mô Hình Nhân Quả Cấu Trúc - SCM)
*   **English**:
    "Let us build a Structural Causal Model. The label Y is the root cause. It determines the causal features, X-core. This is the stable, invariant path. The environment E is an external variable. E determines the background, X-spurious. Because the photographer's location correlates with the animal, Y and E are correlated in the training data, creating a link between Y and X-spurious. An ERM model exploits this link, predicting Y from X-spurious. This is anti-causal prediction. But when E changes, the correlation between Y and X-spurious breaks. Only the relationship between X-core and Y remains constant."
*   **Tiếng Việt**:
    "Hãy xây dựng Structural Causal Model cho bài toán này. Bắt đầu từ Y — nhãn. Con vật là penguin hay camel. Y quyết định đặc trưng vật lý: X_core. Bốn chân hay hai chân, lưng thẳng hay lưng bướu. Đây là mũi tên nhân quả thật. Nhưng màu nền đến từ đâu? Khi nhiếp ảnh gia chụp penguin, họ đến Bắc Cực. Đây là quyết định của môi trường E. Môi trường E tạo ra X_spur — màu nền trắng. Không phải penguin trực tiếp chọn màu nền. Tuy nhiên vì trong train data penguin đi với E là Bắc Cực, có tương quan giữa Y và X_spur. AI nhìn thấy tương quan này và học nó. Đây là bẫy: AI đang dự đoán ngược chiều nhân quả — từ hệ quả suy ra nguyên nhân. Khi E thay đổi — penguin ở sa mạc — tương quan đó biến mất. Chỉ mũi tên X_core đến Y là không bao giờ thay đổi."

### Scene 3.2 — Shift Breaks Shortcut (Môi Trường Thay Đổi, Liên Kết Ảo Vỡ Tan)
*   **English**:
    "When the environment shifts, from Arctic to beach to desert, the link between the label Y and the spurious feature X-spurious is fractured. The background changes, and the model's shortcut predictions fail. But the causal features are invariant. A penguin retains its shape in every environment. Causal features are stable. Spurious features are brittle. The challenge is to design algorithms that force the model to rely only on invariant features."
*   **Tiếng Việt**:
    "Hãy xem điều gì xảy ra khi môi trường thay đổi. E bằng đồng cỏ: mối liên hệ giữa Y và X_spur tồn tại — penguin đi với nền trắng. E bằng bãi biển: mối liên hệ đó lung lay. E bằng sa mạc: biến mất hoàn toàn. Nhưng mũi tên từ X_core đến Y không bao giờ thay đổi. Dù ở đồng cỏ, bãi biển, hay sa mạc — penguin vẫn có hình dáng penguin. SCM cho ta thấy rõ: spurious features là hệ quả của môi trường, không phải nguyên nhân của nhãn. Khi môi trường thay đổi, chúng thay đổi theo. Causal features thì không. Câu hỏi là: làm thế nào buộc mô hình chỉ học X_core? Chính vì bài toán có cấu trúc nhân quả rõ ràng như vậy, ta có nhiều hướng tiếp cận. Và hướng đầu tiên — đơn giản nhất — là reweighting."

---

## Module 4: Importance Weighting & IRM

### Scene 4.0 — Importance Weighting and Interpolation (Reweighting & Hiện Tượng Interpolation)
*   **English**:
    "The simplest way to balance the groups is importance weighting, where rare groups are upweighted in the loss function. In the oracle setting, the weight for each example is proportional to the inverse probability of the spurious attribute given the label. However, in deep neural networks, we face the challenge of interpolation. Modern networks have enough parameters to fit all training data perfectly, reaching zero training loss. When the training loss is zero, the gradients for all examples are zero. Multiplying a zero gradient by a large weight still yields zero. Importance weighting loses its effect in the over-parameterized regime. The model simply memorizes the minority exceptions while continuing to use the shortcut for the rest of the data. We must intervene in the learning objective itself."
*   **Tiếng Việt**:
    "Ý tưởng đơn giản nhất để chống shortcut: thay vì để mọi điểm dữ liệu đóng góp bằng nhau vào loss, ta gán trọng số lớn hơn cho nhóm thiểu số. Công thức thay đổi từ trung bình đều sang trung bình có trọng số: L bằng tổng wᵢ nhân ℓᵢ. Nếu minority chỉ chiếm 5 phần trăm nhưng ta gán trọng số 10 lần lớn hơn, chúng chiếm 50 phần trăm contribution vào loss. Model bây giờ phải quan tâm đến nhóm đó. Nhưng trong neural networks lớn có hiện tượng interpolation: mạng đủ capacity để fit HOÀN HẢO mọi điểm training, kể cả minority. Khi loss bằng 0, gradient bằng 0. Trọng số wᵢ lớn nhân với gradient bằng 0 vẫn bằng 0. Reweighting hoàn toàn mất tác dụng. Mô hình vẫn học shortcut rồi dùng capacity dư để học vẹt minority. Ta cần can thiệp sâu hơn."

### Scene 4.1 — IRM Idea (IRM: Trực Giác Cốt Lõi)
*   **English**:
    "Invariant Risk Minimization, or IRM, approaches this by seeking a representation where the optimal classifier is identical across all environments. If a representation relies on spurious features, the optimal classifier must change between environments to adapt to the shifting correlations. If we can find a representation Phi where a single linear classifier w is simultaneously optimal in all environments, then Phi must have discarded the spurious features, retaining only the invariant causal signals."
*   **Tiếng Việt**:
    "Chúng ta vừa thấy reweighting thất bại với mạng lớn. IRM — Invariant Risk Minimization — tiếp cận từ một góc độ hoàn toàn khác. Hãy nhìn vào ba môi trường. Dữ liệu phân phối khác nhau — màu nền khác, ngữ cảnh khác. Nhưng ranh giới quyết định đúng — đường phân chia penguin và camel theo hình dáng thật — giống hệt nhau trong cả ba. Tại sao? Vì hình dáng con vật không thay đổi theo môi trường. Đây là causal feature. IRM đặt ra một yêu cầu thanh lịch: tìm cách biểu diễn dữ liệu Phi, sao cho cùng một bộ phân loại tuyến tính w sẽ tối ưu ở tất cả các môi trường đồng thời. Nếu tồn tại Phi như vậy, Phi phải đã loại bỏ hết spurious features. Phi chỉ giữ lại causal features, vốn bất biến. Nhưng viết thành toán học như thế nào?"

### Scene 4.2 — IRM Formula (Công Thức Tối Ưu Hóa Của IRM)
*   **English**:
    "IRM translates this into a bi-level optimization problem. We minimize the risk across all environments, subject to the constraint that the classifier w is optimal in each environment individually. This constraint ensures that the model does not exploit shortcuts that are useful in one environment but harmful in another. However, this bi-level optimization is NP-hard and cannot be solved directly with gradient descent. We need a practical approximation."
*   **Tiếng Việt**:
    "IRM viết bài toán tối ưu bi-level: minimize tổng risk trên mọi môi trường, với ràng buộc rằng w phải là classifier tối ưu cho từng môi trường riêng lẻ. Tại sao ràng buộc này quan trọng? Nếu w tối ưu ở environment e₁ nhưng không tối ưu ở e₂, nghĩa là Phi đang dùng một đặc trưng hữu ích ở e₁ nhưng hại ở e₂ — tức là spurious feature. Ràng buộc này bảo đảm Phi trích xuất đặc trưng đủ bất biến để một w duy nhất làm việc được ở tất cả nơi. Vấn đề: bài toán này là NP-Hard. Không giải trực tiếp bằng Gradient Descent. Chúng ta cần một xấp xỉ."

### Scene 4.3 — IRM Gradients (IRMv1: Ràng Buộc Gradient Penalty)
*   **English**:
    "IRMv1 approximates the bi-level constraint using a gradient penalty. If the classifier w is optimal in environment e, the gradient of the loss with respect to w at that point must be zero. We add a penalty term that measures the squared norm of the gradient at a dummy classifier w equals one. A large gradient penalty indicates that the representation is relying on shortcuts, causing disagreement between environments. As we increase the penalty weight lambda, the optimizer is forced to find a representation where the gradients from all environments agree and approach zero. This drives spurious features out of the representation."
*   **Tiếng Việt**:
    "Trick toán học của IRMv1: nếu w bằng 1.0 là minimum của hàm loss, thì gradient của hàm loss tại w bằng 1.0 phải bằng 0. Vậy thay vì ràng buộc cứng, ta thay bằng penalty mềm: phạt khi gradient lớn. Gradient lớn tại w=1.0 nghĩa là w chưa phải minimum ở environment đó, Phi đang dùng shortcut. Gradient nhỏ nghĩa là Phi đã học đặc trưng bất biến. Khi lambda tăng, optimizer bị ép phải tìm Phi sao cho mọi môi trường đồng thuận. Spurious features bị loại vì chúng là nguyên nhân của sự bất đồng."

### Scene 4.4 — IRM Limits (Giới Hạn Của IRM Trong Thực Tế)
*   **English**:
    "While theoretically elegant, IRM faces significant practical limitations. First, it requires multiple, clearly defined training environments to detect disagreement. If the training environments are not diverse, the penalty cannot identify the shortcut. Second, the gradient penalty is highly sensitive to hyperparameters and optimization settings, making training unstable. Third, in many datasets, the ERM baseline is competitive with or outperforms IRM. IRM is strong in theory, but fragile in practice."
*   **Tiếng Việt**:
    "Chính vì những đặc điểm trên, IRM nghe rất thanh lịch về lý thuyết. Nhưng thực tế khắc nghiệt hơn nhiều. Ba trường hợp IRM thất bại: Một là invariant feature giả, khi spurious feature tình cờ bất biến qua tất cả environments huấn luyện. Hai là environments không đủ đa dạng để tạo bất đồng gradient. Ba là shortcut tồn tại ở mọi environment (như bias về chủng tộc/giới tính). Nhiều nghiên cứu thực nghiệm cho thấy ERM được tuning tốt đôi khi còn vượt trội IRMv1 trên benchmark thực tế. IRM mạnh về lý thuyết, nhưng fragile trong thực hành."

---

## Module 5: Group DRO & NuRD

### Scene 4.5 — NuRD (Phương Pháp NuRD)
*   **English**:
    "Because Invariant Risk Minimization faces practical challenges when environments lack diversity, Nuisance-Randomized Distillation, or NuRD, approaches the problem from a different angle. Instead of searching for invariance across environments, NuRD directly filters out the nuisance features from the representation. The core condition of NuRD is that the label Y must be independent of the nuisance attribute Z, conditioned on the representation Phi of X. In simple terms, once we extract the representation Phi of X, it should contain no residual information about the nuisance attribute Z that could be exploited by a classifier. If this condition holds, any model trained on Phi of X is mathematically prevented from using Z as a shortcut. But how do we identify the nuisance attribute Z in practice?"
*   **Tiếng Việt**:
    "Vì IRM gặp khó khăn thực tế khi thiếu môi trường đa dạng, Nuisance-Randomized Distillation (NuRD) tiếp cận từ hướng khác. Thay vì tìm sự bất biến giữa các môi trường, NuRD trực tiếp lọc bỏ các đặc trưng gây nhiễu (nuisance features) ra khỏi representation. Điều kiện cốt lõi của NuRD là nhãn Y phải độc lập với thuộc tính nhiễu Z khi đã biết representation Phi(X). Nói cách khác, khi trích xuất Phi(X), nó không được chứa thông tin dư thừa nào về Z để bộ phân loại có thể lợi dụng làm shortcut. Nếu điều này được thỏa mãn, mô hình được ngăn chặn về mặt toán học khỏi việc dùng Z làm shortcut. Nhưng làm sao xác định Z trong thực tế?"

### Scene 5.1 — Group DRO (Phương Pháp Group DRO)
*   **English**:
    "Group Distributionally Robust Optimization, or Group DRO, modifies the ERM objective with a single operator: max. Standard ERM minimizes the average loss. Since minority groups have small weights, they contribute very little to the average and are effectively ignored. Group DRO reframes this as a minimax game: minimize over the model parameters, maximize over the groups. The inner maximization identifies the group currently experiencing the highest risk, the worst-group. The outer minimization updates the model parameters specifically to reduce the risk of this worst group. As training progresses, the weights dynamically shift: whichever group performs worst is upweighted, forcing the model to focus on it. The model is prevented from sacrificing any single group to improve the average."
*   **Tiếng Việt**:
    "Group DRO thay đổi mục tiêu ERM bằng một toán tử duy nhất: max. ERM tiêu chuẩn tối ưu sai số trung bình. Vì nhóm thiểu số có trọng số nhỏ, đóng góp của chúng vào trung bình rất ít và bị ngó lơ. Group DRO thiết lập bài toán minimax: minimize tham số mô hình, maximize trên các nhóm. Bước max bên trong tìm ra nhóm đang có sai số cao nhất (worst-group). Bước min bên ngoài cập nhật mô hình để giảm thiểu sai số của nhóm này. Trọng số các nhóm thay đổi động trong quá trình train: nhóm nào tệ nhất sẽ được tăng trọng số, buộc mô hình phải tập trung vào nó, không cho phép hy sinh nhóm nào."

---

## Module 6: Semantic Corruption & JTT

### Scene 6.0 — Semantic Corruptions (Phát Hiện Nuisance Bằng Semantic Corruption)
*   **English**:
    "To filter out a nuisance feature, we must first detect it. We do this using a technique called Semantic Corruption. The intuition is straightforward: if we destroy the semantic meaning of the input while preserving the spurious shortcut, and the model still predicts successfully, it is relying on the shortcut. In natural language processing, we shuffle the word order. The semantic meaning is lost, but the word frequencies and n-gram statistics remain. If a sentiment classifier maintains eighty percent accuracy on this shuffled text, it is merely counting words, not understanding sentiment. In computer vision, we apply random patch masking. If a medical classifier still detects a disease after the diagnostic region is masked, it is likely reading scanner artifacts or hospital-specific markers. Semantic corruption exposes the specific shortcuts our models are exploiting."
*   **Tiếng Việt**:
    "Để lọc bỏ đặc trưng nhiễu, trước tiên ta phải phát hiện nó qua Semantic Corruption. Ý tưởng rất trực quan: nếu ta phá hủy ngữ nghĩa của đầu vào nhưng giữ nguyên shortcut ảo, mà mô hình vẫn dự đoán đúng, thì nó đang phụ thuộc vào shortcut. Trong xử lý ngôn ngữ tự nhiên, ta xáo trộn thứ tự từ. Ngữ nghĩa mất đi nhưng tần suất từ và thống kê n-gram vẫn còn. Nếu bộ phân loại cảm xúc vẫn đạt 80% accuracy trên văn bản xáo trộn này, nó chỉ đang đếm từ chứ không hiểu ngữ nghĩa. Trong thị giác máy tính, ta che ngẫu nhiên các mảng ảnh. Nếu AI y tế vẫn phát hiện bệnh khi vùng chẩn đoán bị che, nó đang đọc nhiễu máy quét thay vì dấu hiệu lâm sàng."

### Scene 6.1 — Just Train Twice (Thuật Toán JTT)
*   **English**:
    "Just Train Twice, or JTT, offers a simple and elegant solution: let a standard model identify its own weaknesses. In the first stage, we train a standard ERM model for only a few epochs, enough for it to capture easy shortcuts, but not long enough to memorize exceptions. We then identify the examples this model classifies incorrectly. Why do these mistakes matter? Because a quickly trained ERM model relies almost entirely on shortcuts. It correctly classifies majority examples where the shortcut aligns with the label. It misclassifies minority examples where the shortcut points in the wrong direction, such as a penguin on sand. These early mistakes are a natural proxy for the minority groups. In the second stage, we take these misclassified examples, upweight them by a factor of K equals twenty, and train a new model from scratch. On the Waterbirds benchmark, this simple two-stage process increases worst-group accuracy from thirty-two percent to seventy-one percent, without requiring a single manual group label. JTT leverages the model's own simplicity bias to identify what it needs to correct."
*   **Tiếng Việt**:
    "Just Train Twice (JTT) đề xuất giải pháp đơn giản: để mô hình tiêu chuẩn tự phát hiện điểm yếu của nó. Ở giai đoạn một, ta train ERM trong vài epoch — đủ để nó học các shortcut dễ nhưng chưa kịp nhớ vẹt các ngoại lệ. Ta lọc ra các ví dụ bị phân loại sai. Vì sao các lỗi này quan trọng? Vì một ERM train nhanh chỉ dựa vào shortcut. Nó đoán đúng các mẫu đa số (nơi shortcut khớp nhãn) và đoán sai các mẫu thiểu số (nơi shortcut đi ngược nhãn, như cánh cụt trên cát). Các lỗi ban đầu này chính là đại diện cho nhóm thiểu số. Ở giai đoạn hai, ta lấy các mẫu đoán sai này, nhân trọng số lên K=20 lần, và train một mô hình mới từ đầu. JTT tăng worst-group accuracy trên Waterbirds từ 32% lên 71% mà không cần nhãn nhóm thủ công nào."

---

## Module 7: Foundation Models & AI Fixing AI

### Scene 7.0 — The Promise of Scale: Accuracy on the Line (Lời Hứa Từ Quy Mô)
*   **English**:
    "Between twenty-twenty-one and twenty-twenty-two, researchers observed a compelling phenomenon known as Accuracy on the Line. When plotting the in-distribution accuracy of various models against their out-of-distribution accuracy, the points fall along a straight line. Models that perform better on the training distribution also perform better on shifted test distributions. Under the scaling laws of deep learning, larger models trained on more data yield higher in-distribution accuracy. If the linear relationship holds, scaling models should automatically resolve the OOD generalization problem. This was verified across thirty-six distinct datasets, suggesting that robustness might simply emerge with scale. However, as is often the case in machine learning, the reality is more nuanced."
*   **Tiếng Việt**:
    "Từ năm 2021 đến 2022, các nhà nghiên cứu đã quan sát thấy một hiện tượng hấp dẫn gọi là 'Accuracy on the Line'. Khi vẽ biểu đồ biểu diễn accuracy in-distribution của nhiều mô hình khác nhau đối chiếu với accuracy out-of-distribution của chúng, các điểm rơi vào một đường thẳng. Các mô hình hoạt động tốt hơn trên phân phối huấn luyện cũng hoạt động tốt hơn trên phân phối dịch chuyển. Theo các định luật mở rộng (scaling laws) của deep learning, mô hình lớn hơn được huấn luyện trên nhiều dữ liệu hơn mang lại hiệu suất in-distribution tốt hơn. Nếu mối quan hệ tuyến tính này giữ vững, việc scale mô hình lên sẽ tự động giải quyết bài toán OOD. Hiện tượng này đã được kiểm chứng trên 36 bộ dữ liệu khác nhau, gợi ý rằng robustness sẽ tự động sinh ra khi mô hình đủ lớn. Tuy nhiên thực tế lại phức tạp hơn."

### Scene 7.1 — Scale Does Not Solve It (Quy Mô Không Giải Quyết Được Tất Cả)
*   **English**:
    "If we look at worst-group accuracy, the metric that matters most for safety, scaling tells a very different story. As model size increases under standard ERM, worst-group accuracy plateaus. Scaling improves average performance, but does not eliminate spurious correlations. In fact, larger models possess the capacity to learn and memorize more complex, subtle shortcuts. These are not simple background colors; they are high-dimensional, cross-modal patterns that are difficult to detect. Accuracy on the Line holds for simple, uniform distribution shifts like ImageNet-Vtwo. But for spurious correlation shifts, scale alone is not enough. However, contrastive vision-language models like CLIP exhibit unique properties."
*   **Tiếng Việt**:
    "Nếu nhìn vào worst-group accuracy — chỉ số quan trọng nhất cho sự an toàn — việc tăng kích thước mô hình (scaling) mang lại kết quả rất khác. Khi kích thước mô hình tăng dưới ERM tiêu chuẩn, worst-group accuracy đi ngang. Scaling cải thiện hiệu suất trung bình nhưng không loại bỏ được tương quan ảo. Thực tế, mô hình lớn hơn có dung lượng để học và nhớ các shortcut phức tạp, tinh vi hơn. Chúng không phải là màu nền đơn giản, mà là các mẫu đa chiều, xuyên phương thức rất khó phát hiện. Accuracy on the Line chỉ đúng với các dịch chuyển phân phối đơn giản như ImageNet-V2. Còn với spurious correlation, quy mô lớn là chưa đủ."

### Scene 7.2 — CLIP and Web Correlations (CLIP và Tương Quan Trên Web Dữ Liệu)
*   **English**:
    "CLIP represents a unique case study. It is trained on four hundred million image-text pairs from the web using contrastive learning, rather than standard supervised classification. CLIP's zero-shot performance on the Waterbirds benchmark is remarkable: it achieves seventy-five percent worst-group accuracy without ever being trained on the dataset. Standard ERM achieves only thirty-two percent. Because CLIP is exposed to diverse web data, it has seen penguins in many different contexts. The association between penguins and snow is not strong enough to dominate the representation. At first glance, this suggests that large-scale contrastive training resolves OOD shifts. However, CLIP still inherits biases from its training data. For example, the term doctor is strongly associated with male faces in web media, and CLIP learns this correlation. With four hundred million examples, the model treats this bias as a true pattern."
*   **Tiếng Việt**:
    "CLIP là một trường hợp nghiên cứu độc đáo. Nó được huấn luyện trên 400 triệu cặp ảnh-văn bản từ web bằng contrastive learning. Hiệu suất zero-shot của CLIP trên Waterbirds rất đáng kinh ngạc: đạt 75% worst-group accuracy dù chưa từng train trên tập này. ERM chỉ đạt 32%. Vì CLIP tiếp xúc với dữ liệu web đa dạng, nó đã thấy chim cánh cụt trong nhiều bối cảnh khác nhau. Sự liên kết giữa cánh cụt và tuyết không đủ mạnh để chiếm trị representation. Tuy nhiên, CLIP vẫn kế thừa các định kiến từ dữ liệu web. Ví dụ, từ 'doctor' liên kết mạnh với gương mặt nam giới trên truyền thông, và CLIP học được tương quan này như một quy luật thực sự."

### Scene 7.3 — ICL Shortcuts (Shortcut Trong In-Context Learning)
*   **English**:
    "In large language models, shortcuts can emerge dynamically within the prompt itself during in-context learning. Consider a prompt where all positive examples happen to contain the word movie. The model may learn a shortcut: the presence of movie implies a positive label. When evaluated on a negative review about food, the model predicts positive. This is where we observe Reverse Scaling. A thirteen-billion parameter model is more likely to exploit this shortcut than a two-point-seven-billion parameter model. Because larger models are highly capable of capturing patterns within the context window, they are also more sensitive to accidental correlations in the prompt. Scale is not a universal solution for robustness. In the context of in-context learning, scaling can worsen the problem. However, these same capabilities allow us to use large models to correct robustness failures. This leads to the paradigm of AI fixing AI."
*   **Tiếng Việt**:
    "Ở các mô hình ngôn ngữ lớn, các shortcut có thể xuất hiện động ngay trong chính prompt thông qua in-context learning. Hãy tưởng tượng một prompt nơi tất cả ví dụ tích cực đều chứa từ 'movie'. Mô hình có thể học một shortcut: sự xuất hiện của từ 'movie' nghĩa là nhãn tích cực. Khi gặp một review tiêu cực về đồ ăn, mô hình vẫn đoán là 'tích cực'. Đây là nơi ta quan sát thấy Reverse Scaling. Một mô hình 13 tỷ tham số dễ bị lừa bởi shortcut này hơn mô hình 2.7 tỷ. Vì mô hình lớn cực kỳ nhạy bén trong việc bắt các mẫu trong ngữ cảnh, chúng cũng dễ bị ảnh hưởng bởi tương quan ngẫu nhiên trong prompt. Scaling có thể làm trầm trọng thêm vấn đề trong ICL."

### Scene 7.4 — Reverse Scaling (Hiện Tượng Reverse Scaling)
*   **English**:
    "A closer examination of the relationship between ID and OOD accuracy across different shifts reveals that the linear relationship often breaks down. For some shifts, we observe a vertical trend: models with similar in-distribution performance vary widely in their out-of-distribution accuracy. For other shifts, we see a horizontal trend: OOD performance saturates, and further scaling of ID accuracy yields no improvement. Under complex spurious shifts, we find no correlation at all. Most surprisingly, we sometimes observe negative correlation, or reverse scaling: larger models perform worse on OOD test sets. Accuracy on the Line is a special case that occurs under simple, smooth shifts. It is not a general law of scaling."
*   **Tiếng Việt**:
    "Khi kiểm tra kỹ hơn mối quan hệ giữa ID và OOD accuracy qua các loại dịch chuyển khác nhau, mối quan hệ tuyến tính thường bị phá vỡ. Với một số dịch chuyển, ta thấy xu hướng thẳng đứng: các mô hình có ID accuracy tương tự lại có OOD accuracy rất khác nhau. Với dịch chuyển khác, ta thấy xu hướng nằm ngang: hiệu suất OOD bão hòa, và việc scale ID accuracy thêm không mang lại cải tiến. Dưới các spurious shift phức tạp, không hề có tương quan. Đáng ngạc nhiên nhất, đôi khi ta thấy tương quan âm (reverse scaling): mô hình lớn hơn lại chạy tệ hơn trên tập test OOD. Accuracy on the Line chỉ là trường hợp đặc biệt."

### Scene 7.5 — Prompting for Robustness (PfR: Dùng AI Để Dán Nhãn Nhóm)
*   **English**:
    "This is the concept of Prompting for Robustness, or PfR. Group DRO is highly effective but requires group labels for all training data. Annotating thousands of backgrounds manually is expensive. PfR resolves this by using a large Vision-Language Model to generate these labels automatically. We prompt the VLM to describe the background of each training image. The model provides accurate labels at minimal cost. We then train Group DRO using these automated annotations. On the Waterbirds benchmark, PfR achieves ninety-one point zero-five percent worst-group accuracy, matching the performance of Group DRO trained on manual labels, and tripling the ERM baseline. This represents a clean narrative loop: while scaling introduces shortcuts in CLIP, we can leverage the capabilities of large VLMs to automate the annotations needed to train robust models. We are using AI to fix AI."
*   **Tiếng Việt**:
    "Đây là khái niệm Prompting for Robustness (PfR). Group DRO rất hiệu quả nhưng cần nhãn nhóm cho toàn bộ data train. Việc dán nhãn thủ công hàng ngàn background rất tốn kém. PfR giải quyết điều này bằng cách dùng một Vision-Language Model lớn để tự động tạo các nhãn này. Ta prompt VLM mô tả nền của từng ảnh train. Mô hình cung cấp nhãn chính xác với chi phí cực thấp. Sau đó, ta train Group DRO với các nhãn tự động này. Trên Waterbirds, PfR đạt 91.05% worst-group accuracy, tương đương Group DRO dùng nhãn thủ công và gấp ba lần baseline ERM. Đây là một vòng lặp thú vị: dùng AI lớn để sửa lỗi cho AI nhỏ."

### Scene 7.6 — CATO (Phương Pháp Tăng Cường Dữ Liệu Nhân Quả CATO)
*   **English**:
    "PfR automates annotation. But we still face the challenge of data scarcity: minority groups are often too small to support effective training. CATO, or Causal Augmentation, addresses this by using language models and causal reasoning to generate synthetic counterfactual data. Using the SCM, we identify the spurious attribute, the background. CATO then prompts a generative model to synthesize counterfactual examples: placing a waterbird on land, or a landbird on water. By augmenting the training set with these synthetic counterfactuals, we balance the group distributions. The model trained on this augmented dataset is significantly more robust. CATO combines causal inference with generative AI, representing an active area of research. This completes our narrative arc: scale initially promises robustness, fails under complex shifts, introduces new shortcuts, and is ultimately leveraged to automate annotations and generate counterfactual data to train robust models."
*   **Tiếng Việt**:
    "PfR tự động hóa việc dán nhãn. Nhưng ta vẫn gặp thách thức về sự khan hiếm dữ liệu: các nhóm thiểu số thường quá nhỏ để huấn luyện hiệu quả. CATO (Causal Augmentation) giải quyết điều này bằng cách dùng mô hình ngôn ngữ và suy luận nhân quả để tạo ra dữ liệu phản thực tế (counterfactual data) nhân tạo. Dựa trên SCM, ta xác định thuộc tính ảo là background. CATO prompt mô hình tạo ảnh phản thực tế: đặt chim nước lên cạn, chim cạn xuống nước. Bằng cách tăng cường dữ liệu huấn luyện với các ảnh nhân tạo này, ta cân bằng phân phối nhóm. Mô hình được train trên dữ liệu tăng cường này robust hơn đáng kể."

---

## Module 8: Benchmarks & Reality Checks

### Scene 8.1 — Benchmarks (Bốn Đấu Trường Đánh Giá Robustness)
*   **English**:
    "To evaluate these robust algorithms, the machine learning community has established several standard benchmarks. First: Waterbirds. This is a synthetic dataset where the correlation between the bird type and the background is controlled. It provides a clean testbed to evaluate algorithms under structured shifts. Second: CelebA. This contains celebrity images. The task is to predict blonde hair, but because blonde hair is strongly correlated with female faces in the dataset, standard models learn that blonde equals female. Third: CivilComments. This is a text dataset for online toxicity detection. Here, mentions of specific demographic groups, such as religions or races, are highly correlated with toxic labels, leading models to flag benign sentences containing these words. Fourth: Camelyon17. A medical dataset for tumor detection. The shortcut here is the scanner model used at different hospitals. Instead of analyzing the tissue pathology, models learn to recognize the scanner signature of the training hospital."
*   **Tiếng Việt**:
    "Để đánh giá các thuật toán robust này, cộng đồng đã xây dựng một số benchmark chuẩn. Thứ nhất: Waterbirds, một tập dữ liệu tổng hợp nơi tương quan giữa chim và nền được kiểm soát. Thứ hai: CelebA, tập ảnh người nổi tiếng, dự đoán tóc vàng nhưng bị tương quan mạnh với giới tính nữ. Thứ ba: CivilComments, tập văn bản phát hiện độc hại trực tuyến, nơi các từ chỉ nhóm nhân khẩu học (tôn giáo, chủng tộc) bị tương quan với nhãn độc hại. Thứ tư: Camelyon17, tập dữ liệu y khoa phát hiện khối u, nơi shortcut là loại máy quét được dùng tại các bệnh viện khác nhau."

### Scene 8.2 — Model Selection Paradox (Nghịch Lý Lựa Chọn Mô Hình)
*   **English**:
    "This leads to a fundamental challenge in robust machine learning: the Model Selection Paradox. To deploy a robust model, we must select the best candidate from our training runs. This selection requires an out-of-distribution validation set. But if we have access to an OOD validation set, the most logical step is to include it in the training data to improve the model. Once we do, that data is no longer out-of-distribution. Selecting models based on in-distribution validation sets does not correlate well with OOD performance. This paradox remains one of the most critical open problems in the field. Given these limitations, how do we approach OOD generalization in practice? And do Foundation Models change this landscape?"
*   **Tiếng Việt**:
    "Điều này dẫn đến một thách thức cơ bản trong học máy robust: Nghịch lý lựa chọn mô hình (Model Selection Paradox). Để triển khai một mô hình robust, ta phải chọn ứng viên tốt nhất từ quá trình train. Việc lựa chọn này yêu cầu một tập validation OOD. Nhưng nếu ta có quyền truy cập vào tập validation OOD, bước hợp lý nhất là đưa nó luôn vào dữ liệu train để cải thiện mô hình. Khi ta làm thế, dữ liệu đó không còn là OOD nữa. Việc lựa chọn mô hình dựa trên tập validation in-distribution lại không tương quan tốt với hiệu suất OOD. Nghịch lý này vẫn là một vấn đề nghiên cứu mở chưa có lời giải đơn giản."

### Scene 8.3 — Best Practices (Bài Học & Lời Khuyên Thực Tế)
*   **English**:
    "The practical checklist is simple. Identify the shift type. Report worst-group accuracy. Tune ERM carefully. Use Group DRO when group labels exist. Use JTT or clustering when they do not. For foundation models, try the last layer first. And whenever possible, collect more diverse data. With this framework in place, we can address the latest shift in the machine learning landscape: how do foundation models change the nature of shortcut learning?"
*   **Tiếng Việt**:
    "Danh sách kiểm tra thực tế rất đơn giản. Xác định loại dịch chuyển. Luôn báo cáo worst-group accuracy. Tối ưu ERM thật kỹ trước. Sử dụng Group DRO khi có nhãn nhóm. Sử dụng JTT hoặc phân cụm khi không có nhãn. Đối với foundation models, hãy thử huấn luyện lại lớp cuối cùng (last-layer retraining) trước. Và bất cứ khi nào có thể, hãy thu thập dữ liệu đa dạng hơn. Với khung làm việc này, chúng ta có thể giải quyết các thách thức mới trong thực tế."

---

## Module 9: Journey Summary & Conclusion

### Scene 9.1 — Journey Summary (Tóm Tắt Hành Trình)
*   **English**:
    "We have traveled a long path. We began with a simple question: why do models learn shortcuts? We saw that ERM minimizes average loss, which can sacrifice minority groups to favor the majority. We formalized this: OOD generalization requires performance to hold when distributions shift. We saw that robust algorithms are defined by their choice of risk aggregation, whether mean, max, CVaR, or DRO. Simplicity bias explains why gradient descent prefers shortcuts: simple features present larger gradients at initialization. Causal models clarify this structure: spurious features are environmental effects, while causal features are invariant properties of the object. We examined five methods: Reweighting, IRM, NuRD, Group DRO, and JTT. Each represents a solution under specific mathematical assumptions. Finally, we evaluated these on benchmarks, discussed the model selection paradox, and saw how foundation models fail and are then leveraged to improve robustness. This leads to a single concept: Stability. Robust AI is not about predicting perfectly in every new environment. It is about identifying the core causal features and relying on them consistently, regardless of context."
*   **Tiếng Việt**:
    "Chúng ta đã đi một chặng đường dài. Bắt đầu từ câu hỏi tại sao mô hình học shortcut. Ta thấy ERM tối thiểu hóa loss trung bình và có thể hy sinh nhóm thiểu số. Ta đã hình thức hóa điều này: OOD generalization đòi hỏi hiệu suất giữ vững khi phân phối dịch chuyển. Các thuật toán robust khác nhau thực chất chỉ khác ở cách gộp rủi ro: mean, max, CVaR, hay DRO. Simplicity bias giải thích vì sao gradient descent thích shortcut: đặc trưng đơn giản cho gradient lớn hơn ở điểm khởi tạo. Mô hình nhân quả làm rõ cấu trúc này: spurious features là hệ quả của môi trường, causal features là đặc tính bất biến. Chúng ta đã đi qua năm phương pháp chính: Reweighting, IRM, NuRD, Group DRO, và JTT. Cuối cùng, ta đánh giá trên benchmark, đối mặt với nghịch lý lựa chọn mô hình, và xem foundation models thất bại rồi được tận dụng để sửa lỗi như thế nào. Tất cả dẫn đến một khái niệm duy nhất: Sự ổn định (Stability). AI robust không phải là dự đoán đúng trong mọi môi trường mới, mà là xác định và dựa vào các đặc trưng nhân quả cốt lõi một cách nhất quán, bất kể ngữ cảnh."

### Scene 9.2 — Open Problems and Credits (Đóng Góp & Hướng Đi Mở)
*   **English**:
    "The tutorial concludes with three open research directions: developing OOD theory for foundation models, resolving model selection without OOD validation sets, and addressing robustness in multimodal and agentic systems. This is the next frontier. Thank you for watching. The link to the original tutorial, slides, and Manim source code are in the description below."
*   **Tiếng Việt**:
    "Tutorial kết thúc với ba hướng nghiên cứu mở: phát triển lý thuyết OOD cho foundation models, giải quyết nghịch lý chọn mô hình mà không cần validation OOD, và giải quyết độ robust trong hệ thống đa phương thức và tự trị (multimodal & agentic). Đây là những ranh giới tiếp theo. Cảm ơn các bạn đã theo dõi. Link đến bài giảng gốc, slide, và mã nguồn Manim được để dưới phần mô tả."
