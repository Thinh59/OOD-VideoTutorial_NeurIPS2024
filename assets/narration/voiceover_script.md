## Scene 0.1 - Opening: Bệnh án của Bác sĩ

Hãy bắt đầu với một ví dụ thực tế. Một AI được huấn luyện để dự đoán bệnh từ hồ sơ bệnh án điện tử. Tại Bệnh viện A, nó đạt 95% - ấn tượng.

Nhưng khi chuyển sang Bệnh viện B, accuracy rớt xuống 72%.

Điều gì đã xảy ra? Nhìn kỹ vào dữ liệu huấn luyện. Tại Viện A, một bác sĩ cụ thể có thói quen: ông ta viết 'man' khi ghi hồ sơ bệnh nhân tiểu đường, và 'gentleman' khi ghi bệnh nhân viêm khớp. Hai từ đồng nghĩa - nhưng AI đã học được sự phân biệt này và dùng nó như một đường tắt.

Khi sang Viện B, bác sĩ mới không có thói quen đó. Shortcut biến mất. Mô hình sụp đổ.

Đây chính là vấn đề trọng tâm của tutorial này. Không phải AI thiếu dữ liệu hay thiếu tham số. Mà là AI đang học sai thứ.

## Scene 0.2 - Road Map

Trong video này chúng ta sẽ đi qua sáu chặng. Bắt đầu bằng câu hỏi tại sao AI học những đường tắt, sau đó nhìn vấn đề qua lăng kính nhân quả, khám phá ba phương pháp giải quyết, rồi xem chúng hoạt động ra sao trong thời đại của các mô hình khổng lồ như GPT và CLIP. Đi thôi.

## Scene 1.1 - ERM và Ảo ảnh Accuracy Cao

Hãy bắt đầu bằng ví dụ kinh điển trong tutorial. Bạn xây dựng AI phân loại chim cánh cụt và lạc đà.

Tập dữ liệu huấn luyện: chim cánh cụt luôn đứng trên tuyết trắng, lạc đà luôn đứng trên cát vàng. Trong không gian đặc trưng hai chiều, trục ngang là màu nền, trục dọc là hình dáng, dữ liệu chia thành hai cụm tách biệt hoàn hảo.

Thuật toán học và vẽ được một đường phân loại. Accuracy 98%. Tuyệt vời.

Nhưng chú ý kỹ đường này đang làm gì. Nó đi theo trục ngang, đọc màu nền. Không phải trục dọc, không dựa vào hình dáng thực của con vật.

Khi một chú chim cánh cụt bị đặt trên cát vàng, đường phân loại không ngần ngại: đây là lạc đà. Sai hoàn toàn.

Điều gì đã xảy ra? Để hiểu, chúng ta cần nhìn vào trái tim của mọi thuật toán học máy hiện đại.

## Scene 1.2 - Giải phẫu ERM: Tại sao nó lười?

ERM, Empirical Risk Minimization, là thuật toán học máy tiêu chuẩn. Ý tưởng rất đơn giản: tìm bộ tham số theta để minimize sai số trung bình trên tập train.

Nhưng chú ý điều này: ERM chỉ có một mục tiêu duy nhất, giảm con số Loss xuống. Nó không biết, không quan tâm, liệu sự giảm đó đến từ hiểu thật sự hay từ đường tắt.

Hãy hình dung từ góc nhìn của Gradient Descent. Có hai con đường để dự đoán đúng nhãn chim cánh cụt: con đường thứ nhất, phân tích cấu trúc hình thái học, nhận dạng dáng đứng đặc trưng và tỉ lệ thân mình, tốn nhiều bước gradient, khó học. Con đường thứ hai, đếm xem nền nhiều pixel trắng hay vàng hơn, một phép tính đơn giản.

Gradient Descent sẽ chọn con đường nào? Luôn luôn là con đường hai. Không phải vì nó thông minh xấu xa, mà đơn giản vì đó là chiều gradient giảm nhanh nhất.

Chúng ta gọi những đặc trưng như màu nền đó là Spurious Features, đặc trưng ảo. Chúng trông giống tín hiệu hữu ích trong train data, nhưng thực ra chỉ là sự trùng hợp ngẫu nhiên của ngữ cảnh. Và đây không phải lỗi của thuật toán. ERM đang làm đúng những gì được yêu cầu. Vấn đề nằm ở cách chúng ta định nghĩa mục tiêu học.

## Scene 1.3 - Spurious Feature: Chính xác là gì?



## Scene 1.3A — Hình thức hóa: X, Y và E

"Trước khi đi sâu vào các giải pháp... ta cần phải 'toán học hóa' trực giác này." [pause 0.5s]
"Trong học máy... mọi thứ bắt đầu bằng biến X..." [pause 0.3s]
"...đây là đầu vào mà mô hình nhìn thấy... như một tờ bệnh án hay một bức ảnh." [pause 0.5s]
"Đích đến của chúng ta là biến Y... nhãn cần dự đoán." [pause 0.8s]
"Nhưng... còn một biến số thứ ba thường bị bỏ quên." [pause 0.5s]
"Đó là E — Môi trường." [pause 0.8s]
"E đại diện cho ngữ cảnh tạo ra dữ liệu." [pause 0.3s]
"Bệnh viện A là một môi trường. Bệnh viện B là một môi trường khác." [pause 0.5s]
"Môi trường chính là thứ chi phối mối quan hệ giữa X và Y."

## Scene 1.3B — Sự đứt gãy của Học máy (OOD Definition)

"Trong học máy tiêu chuẩn... chúng ta luôn dựa vào một giả định ngầm." [pause 0.5s]
"Đó là dữ liệu huấn luyện... và dữ liệu kiểm thử... được rút ra từ cùng một phân phối xác suất." [pause 0.3s]
"P-train... bằng với P-test." [pause 1.0s]
"Nhưng bài toán Out-of-Distribution... hay OOD... đập vỡ hoàn toàn giả định này." [pause 0.8s]
"Trong thực tế... P-train không bao giờ bằng P-test." [pause 0.5s]
"Dữ liệu huấn luyện đến từ môi trường e-1... với những quy luật và định kiến riêng." [pause 0.5s]
"Còn khi triển khai thực tế... mô hình lại đối mặt với môi trường e-2." [pause 0.8s]
"Hai môi trường này... tạo ra hai phân phối hoàn toàn khác biệt."

## Scene 1.3C — Tập hợp Phân phối (Distribution Set)

"Thay vì một phân phối... chúng ta làm việc với một tập hợp các phân phối." [pause 0.5s]
"Huấn luyện trên một vài môi trường... và hy vọng mô hình ổn định trên một môi trường hoàn toàn mới." [pause 0.8s]
"Đó chính là chìa khóa... sự ổn định."
Vậy spurious feature là gì, chính xác?

Hãy nghĩ về chuỗi sự kiện tạo ra dữ liệu. Nhiếp ảnh gia muốn chụp chim cánh cụt, họ đến Bắc Cực. Con chim là nguyên nhân, nền tuyết trắng là kết quả. Mũi tên nhân quả đi từ nhãn sang nền.

Nhưng AI đang đọc ngược lại: thấy nền trắng, kết luận đây là chim cánh cụt. Đây là Anti-causal Prediction, dự đoán ngược chiều nhân quả.

Vấn đề: tương quan ngược chiều này chỉ tồn tại trong một môi trường cụ thể. Khi môi trường thay đổi, chim cánh cụt xuất hiện ở sa mạc, tương quan đó tan biến. Nhưng mối quan hệ nhân quả thật, chim cánh cụt có hình dáng của chim cánh cụt dù đứng ở đâu, vẫn còn đó.

Đây chính là sự khác biệt cốt lõi: Causal features ổn định qua mọi môi trường. Spurious features chỉ tồn tại ở một hoàn cảnh cụ thể.

## Scene 2.1 - Cấu trúc dữ liệu theo Group

Để nói chính xác về vấn đề này, chúng ta cần một ngôn ngữ toán học. Tutorial NeurIPS 2024 đề xuất nhìn dữ liệu qua lăng kính nhóm, Group.

Mỗi nhóm được định nghĩa bởi sự kết hợp của nhãn Y và đặc trưng ảo. Trong bài toán bò và lạc đà: bốn nhóm. Bò trên cỏ. Bò trên cát. Lạc đà trên cỏ. Lạc đà trên cát.

Trong thực tế, 90% dữ liệu là hai nhóm tự nhiên. Chỉ 10% là hai nhóm nghịch nhĩ. ERM tối ưu trung bình có trọng số, tự động ưu tiên 90% đó. Accuracy tổng thể 92%, nghe hay. Nhưng với nhóm bò trên cát? 18%.

Chính vì vậy, chúng ta cần một chỉ số đánh giá mới.

## Scene 2.2 - Worst-Group Accuracy: Thước đo thực sự

Nhìn vào hai mô hình. Model A có average accuracy 82%, trông hay hơn Model B với 76%. Theo ERM: chọn A.

Nhưng nhìn kỹ hơn. Model A hoàn toàn thất bại ở hai nhóm thiểu số, chỉ 18 và 21%. Trong thực tế điều này nghĩa là những bệnh nhân không theo khuôn sẽ bị chẩn đoán sai gần như hoàn toàn.

Model B có average thấp hơn, nhưng các nhóm đều được đối xử công bằng.

Worst-Group Accuracy là chỉ số chúng ta thực sự cần quan tâm khi deploy AI vào thế giới thực. Và bây giờ, để hiểu sâu hơn tại sao ERM thất bại, chúng ta cần đi vào cấu trúc nhân quả của dữ liệu.

## Scene 2.3 - Ba loại Distribution Shift

Không phải mọi distribution shift đều giống nhau. Tutorial phân loại ba dạng chính.

Thứ nhất: Covariate Shift. Phân phối đầu vào X thay đổi, nhưng mối quan hệ Y cho X vẫn nguyên. Khó nhưng giải quyết được.

Thứ hai: Label Shift. Tần suất của các class thay đổi. Ít nguy hiểm hơn.

Thứ ba, và nguy hiểm nhất: Spurious Shift. Mối quan hệ giữa đặc trưng ảo và nhãn bị đảo ngược hoàn toàn. Nếu trước đây bò thường ở đồng cỏ, nay tất cả bò đều ở sa mạc, mô hình dùng màu nền sẽ sai 100%. Đây chính là loại shift mà cả phần tutorial này tập trung vào.

## Scene 3.1 - Structural Causal Model: Xây từng mũi tên

Hãy xây dựng một mô hình nhân quả cho bài toán này, Structural Causal Model, hay SCM.

Bắt đầu từ những gì chúng ta biết chắc. Con vật Y là bò hay lạc đà. Điều này quyết định hình dáng thể chất: bốn chân, sừng, tỉ lệ thân mình. Đây là X_core, đặc trưng cốt lõi. Mũi tên nhân quả từ X_core đến Y.

Nhưng còn màu nền thì sao? Khi nhiếp ảnh gia đi chụp bò, họ đến đồng cỏ. Đây là quyết định của môi trường E. Môi trường tạo ra X_spur, màu nền xanh. Không phải bò trực tiếp quyết định màu nền.

Tuy nhiên, vì trong train data bò thường đi với E bằng đồng cỏ, có sự tương quan giữa Y và X_spur. AI nhìn thấy tương quan này và học nó. Đây chính là bẫy. AI đang học ngược chiều nhân quả. Khi E thay đổi, tương quan đó biến mất. Chỉ có mũi tên nhân quả thật từ X_core đến Y là không đổi.

## Scene 3.2 - Distribution Shift phá vỡ liên kết ảo



## Scene 3.3 — Bài test tối thượng

"Đây là bài kiểm tra sự thật." [pause 0.5s]
"Trong môi trường huấn luyện... cả mô hình nhân quả và mô hình đường tắt đều dự đoán đúng." [pause 0.8s]
"Nhưng khi triển khai thực tế... chỉ có mô hình nhân quả mới sống sót qua sự thay đổi môi trường." [pause 0.8s]
"Đó là cái giá của việc học thuộc lòng."
Hãy xem điều gì xảy ra khi môi trường thay đổi.

E bằng đồng cỏ: mối liên hệ giữa Y và X_spur tồn tại. AI hoạt động tốt.
E bằng bãi biển: mối liên hệ đó lung lay.
E bằng tuyết: hoàn toàn biến mất.

Nhưng mũi tên từ X_core đến Y, hình dáng con vật quyết định nhãn, không bao giờ thay đổi. Dù ở đồng cỏ, bãi biển, hay sa mạc, bò vẫn có bốn chân và hai sừng.

Và câu hỏi đặt ra bây giờ là: làm thế nào để buộc AI chỉ học những thứ bất biến này?

## Scene 4.1 - IRM: Ý tưởng bất biến



## Scene 4.1A — Nguyên lý Bất biến

"Nguyên lý Invariance... hay sự bất biến... phát biểu rằng:" [pause 0.5s]
"Để tìm được đặc trưng bền vững... chúng ta phải tìm một không gian biểu diễn..." [pause 0.3s]
"...nơi mà bộ phân loại tối ưu là hoàn toàn giống nhau... trên mọi môi trường." [pause 0.8s]
"Mục tiêu là học một bộ dự đoán bất biến."

## Scene 4.1B — Hình học của sự Bất biến

"Hãy nhìn cách không gian bất biến hoạt động." [pause 0.5s]
"Hai môi trường bị méo mó... đi qua bộ trích xuất đặc trưng..." [pause 0.3s]
"...và được biến đổi thành một không gian chung." [pause 0.5s]
"Tại đây... một đường ranh giới duy nhất có thể phân loại đúng cho tất cả."
Bây giờ hãy đặt câu hỏi khác: điều gì sẽ xảy ra nếu chúng ta không gộp tất cả dữ liệu từ mọi môi trường lại rồi chạy ERM, mà thay vào đó nhìn các môi trường riêng lẻ?

IRM, Invariant Risk Minimization, đặt ra một yêu cầu rất thú vị: tìm một cách biểu diễn dữ liệu, gọi là Phi, sao cho cùng một bộ phân loại tuyến tính w sẽ tối ưu ở tất cả các môi trường đồng thời.

Nếu tồn tại một Phi như vậy, thì Phi phải loại bỏ hết spurious features vì chúng không nhất quán giữa các môi trường. Phi chỉ giữ lại đặc trưng causal, vốn bất biến. Nghe thanh lịch. Nhưng làm thế nào để tối ưu hóa điều này?

## Scene 4.2 - Công thức IRM: Từ ràng buộc cứng đến Gradient Penalty

IRM viết bài toán tối ưu bi-level: minimize tổng risk trên mọi môi trường, với ràng buộc rằng w phải là classifier tối ưu cho từng môi trường riêng lẻ. Ràng buộc này bảo đảm Phi trích xuất đặc trưng đủ bất biến để một w duy nhất làm việc được ở tất cả nơi.

Vấn đề: bài toán này là NP-Hard. Không giải trực tiếp bằng Gradient Descent được.

Đây là nơi một trick toán học đẹp xuất hiện. Nếu w bằng 1.0 là minimum của hàm loss, thì gradient của hàm loss tại w bằng 1.0 phải bằng 0. Đó là định nghĩa của minimum. Vậy thay vì ràng buộc cứng, ta đo mức độ vi phạm bằng độ lớn của gradient.

Gradient lớn tại w bằng 1.0 nghĩa là w chưa phải minimum, Phi đang dùng shortcut. Gradient nhỏ nghĩa là Phi đã học đặc trưng bất biến.

Đây là IRMv1. Khi lambda tăng, optimizer bị ép phải tìm Phi sao cho mọi môi trường đồng thuận. Spurious features bị loại vì chúng là nguyên nhân của sự bất đồng đó.

## Scene 4.3 - Trực quan: Gradient Vectors hội tụ

Hình dung trực quan. Nếu Phi đang dùng spurious feature, đặc trưng đó hữu ích ở một số môi trường nhưng hại ở môi trường khác. Mỗi môi trường muốn w dịch chuyển theo hướng khác nhau. Ba vector gradient chỉ về ba hướng khác nhau, bất đồng.

Khi penalty lambda tăng, optimizer bị phạt nếu các gradient còn phân kỳ. Nó buộc phải tìm Phi mà tất cả môi trường đồng thuận. Spurious features bị loại khỏi Phi vì chúng là nguyên nhân của sự bất đồng. Phần còn lại trong Phi chính là causal features.

## Scene 4.4 - Giới hạn của IRM

IRM có giới hạn lý thuyết quan trọng. Nó chỉ hoạt động khi các môi trường đủ đa dạng để expose sự không nhất quán của spurious features. Nếu chỉ có hai môi trường mà cả hai đều chứa cùng shortcut, IRM không có cách nào phát hiện.

Ngoài ra, IRMv1 rất nhạy với lựa chọn lambda và thường không ổn định khi training. Nhiều nghiên cứu cho thấy ERM được tuning tốt đôi khi còn vượt trội hơn. Vậy nếu không có đủ môi trường rõ ràng, chúng ta cần hướng tiếp cận khác.

## Scene 5.1 - Group DRO: Tối ưu hóa Worst-Case

Group DRO thay đổi mục tiêu tối ưu bằng một từ: max.

ERM minimize trung bình có trọng số của loss trên các nhóm. Nhóm nhỏ có trọng số nhỏ, tự động bị bỏ qua. DRO thay đổi luật chơi: nó tìm nhóm đang tệ nhất, worst-case group, và minimize loss của nhóm đó.

Hãy hình dung loss landscape như địa hình nhìn từ trên. ERM tìm thung lũng thấp nhất trung bình, lăn qua góc tối tăm nơi nhóm thiểu số đang vật lộn. DRO liên tục cập nhật trọng số: nhóm nào có loss cao thì upweight. Optimizer phải chú ý đến nhóm đó.

Group DRO rất mạnh khi có nhãn nhóm. Nhưng gán nhãn nhóm rất tốn kém trong thực tế. Và đây là lúc JTT xuất hiện.

## Scene 6.1 - JTT: Để ERM tự chỉ ra điểm yếu

JTT, Just Train Twice, có câu trả lời thanh lịch: hãy để ERM tự chỉ ra.

Bước 1: Train một mô hình ERM nhỏ trong vài epochs, đủ để nó học shortcuts, nhưng chưa memorize. Nhìn vào những điểm mà mô hình này dự đoán sai.

Tại sao những điểm bị sai lại quan trọng? Vì mô hình ERM học shortcuts ngay lập tức. Điểm nào thuộc nhóm đa số, shortcut hoạt động, dự đoán đúng. Điểm nào thuộc nhóm thiểu số, shortcut chỉ sai hướng, dự đoán sai. Các điểm bị sai chính xác là những điểm mà shortcut không giúp ích được.

Bước 2: Gom những điểm sai đó lại, nhân bản chúng lên K lần, tạo dataset mới nơi thiểu số được đại diện đầy đủ. Train mô hình thứ hai trên dataset này.

Kết quả: Worst-group accuracy tăng từ 32% lên 71%, mà không cần một nhãn nhóm thủ công nào. ERM đã tự lộ ra điểm yếu của chính mình.

## Scene 7.1 - Scale không giải quyết được vấn đề

Câu hỏi tự nhiên: liệu chúng ta có cần lo về điều này khi các mô hình ngày càng to hơn? Phải chăng 100 tỉ tham số tự động giải quyết vấn đề?

Câu trả lời là không. Khi model size tăng nhưng vẫn train theo ERM, worst-group accuracy gần như không tăng sau một điểm nhất định. Scale giúp average accuracy, nhưng không giải quyết spurious correlations.

Thậm chí tệ hơn: mô hình lớn hơn có capacity lớn hơn để memorize spurious features tinh vi hơn. Scale amplifies, không fixes, vấn đề.

## Scene 7.2 - CLIP và Spurious Correlations từ Web

CLIP được train trên 400 triệu cặp ảnh và văn bản từ internet. Khả năng zero-shot đáng kinh ngạc. Nhưng internet phản ánh thế giới với tất cả bias của nó.

Khi văn bản bác sĩ xuất hiện trên web đi kèm ảnh người, phần lớn là nam. CLIP học tương quan đó. Nó không có lý do gì để nghĩ đây là spurious, vì với 400 triệu ví dụ, đây trông như một pattern thật.

Kết quả: các tác vụ downstream kế thừa bias từ CLIP. Medical diagnosis, hiring tools, hay content moderation xây trên CLIP đều mang theo spurious correlations đã được học ở quy mô khổng lồ. Scale consolidates spurious, không xóa nó.

## Scene 7.3 - In-Context Learning và Spurious Shortcuts trong LLMs

Trong thế giới Large Language Models, spurious shortcuts xuất hiện ở một nơi bất ngờ: ngay trong cái prompt mà bạn viết.

In-Context Learning, hay ICL, là khả năng LLM học từ một vài ví dụ được cung cấp trực tiếp trong prompt. Nhìn qua thì tuyệt vời. Nhưng slides của tutorial chỉ ra một vấn đề tinh vi.

Trong prompt này, tất cả ba ví dụ Positive đều chứa từ 'movie'. LLM không học được rằng câu văn tích cực thì nhãn là Positive. Nó học được điều đơn giản hơn: 'movie' xuất hiện trong prompt thì nhãn là Positive.

Khi gặp một câu không liên quan đến phim nhưng cũng là Positive, hay ngược lại, LLM sai. Đây là spurious correlation được tạo ra bởi chính người viết prompt, không phải bởi dữ liệu train.

Và đây là điểm đặc biệt nguy hiểm của ICL shortcuts: chúng vô hình. Bạn không thể kiểm tra 'model weights' vì shortcuts nằm trong ngữ cảnh, thay đổi theo từng lần gọi.

## Scene 7.4 - Reverse Scaling: Mô hình TO hơn = DỄ BỊ LỪA hơn

Đây là phát hiện gây sốc nhất trong phần Foundation Models của tutorial: Reverse Scaling.

Thông thường chúng ta kỳ vọng mô hình lớn hơn sẽ mạnh hơn, robust hơn với shortcuts. Nhưng với ICL spurious correlations, điều ngược lại xảy ra. Mô hình 13 tỉ tham số bị ảnh hưởng bởi shortcut 'movie' trong prompt nhiều hơn mô hình 2.7 tỉ tham số.

Tại sao? Vì mô hình lớn hơn rất giỏi trong việc đọc ngữ cảnh và nắm bắt pattern trong prompt. Đây chính là khả năng tạo nên ICL. Nhưng nó cũng có nghĩa là mô hình lớn hơn 'quá nhạy' với mọi pattern, kể cả pattern không liên quan đến task thực sự.

Scale không phải là thuốc chữa bách bệnh.

## Scene 7.5 - PfR: Dùng AI để chữa lỗi cho AI

Đây là giải pháp đột phá của năm 2024: PfR - Prompting for Robustness.

Vấn đề cốt lõi: Group DRO cần nhãn nhóm, tức là với mỗi ảnh chim, cần biết nền là nước hay đất. Gán nhãn thủ công cho hàng vạn ảnh rất tốn kém.

Giải pháp: dùng chính một mô hình lớn như GPT-4V để gán nhãn phông nền. Đưa từng ảnh vào VLM với prompt đơn giản: hãy mô tả nền của ảnh này. VLM trả về nhãn phông nền chính xác với chi phí gần như bằng không.

Sau đó kết hợp nhãn phông nền tự động này với nhãn bệnh nhân thủ công để chạy Group DRO.

Kết quả trên Waterbirds: Worst-group accuracy tăng từ 71% lên 91.05%. Không cần thêm dữ liệu train, không cần thay đổi thuật toán. Chỉ cần dùng AI lớn để gán nhãn cho AI nhỏ.

## Scene 7.6 - CATO: Counterfactual Data bằng LLM

PfR giải quyết vấn đề gán nhãn. Nhưng còn một vấn đề khác: ngay cả khi biết nhóm nào là thiểu số, số lượng mẫu vẫn quá ít để train hiệu quả.

CATO giải quyết điều này bằng cách dùng LLM và suy luận nhân quả để sinh ra dữ liệu counterfactual. Từ SCM đã xây dựng, ta biết spurious feature là phông nền. Vậy CATO yêu cầu LLM: hãy tưởng tượng waterbird này đứng trên đất thay vì nước. Mô tả lại ảnh đó.

LLM sinh ra các mô tả, hoặc thậm chí ảnh tổng hợp, của các trường hợp counterfactual. Dataset mới giờ cân bằng hơn nhiều.

Đây là hướng kết hợp giữa nhân quả và generative AI - một trong những xu hướng nghiên cứu nóng nhất của năm 2024.

## Scene 8.1 - Benchmarks và Sự thật phũ phàng

Để đánh giá khách quan, cộng đồng xây dựng các benchmark chuẩn. WILDS cung cấp dữ liệu thực từ y tế và khoa học, nơi distribution shift xảy ra tự nhiên. DomainBed tổng hợp nhiều dataset để kiểm chứng domain generalization.

Và đây là sự thật phũ phàng: nhìn vào kết quả thực nghiệm, không có phương pháp nào thống trị tuyệt đối. Tệ hơn: khi ERM được tuning cẩn thận, lựa chọn learning rate, weight decay và augmentation tốt, nó thường cạnh tranh được với các phương pháp phức tạp hơn nhiều.

Điều này không có nghĩa các phương pháp robust vô ích. Khi spurious correlation cực mạnh và có cấu trúc rõ ràng, chúng thực sự giúp ích. Nhưng bài học thực tiễn: đừng bỏ qua baseline trước khi bạn đã tuning nó thật kỹ.

## Scene 8.2 - Nghịch lý Model Selection

Một nghịch lý thực tiễn không có lời giải hoàn hảo. Giả sử bạn đã train ERM, IRM, và DRO. Bây giờ cần chọn model nào để deploy. Bạn cần một validation set OOD để đánh giá.

Nhưng nếu đã có validation set OOD, tại sao không dùng nó để train luôn? Và nếu dùng để train, nó không còn là OOD nữa.

Dùng ID validation set thường không tương quan tốt với OOD performance. Tutorial gọi đây là một trong những open problems quan trọng nhất của lĩnh vực.

## Scene 8.3 - Best Practices: Flowchart thực tiễn

Tutorial kết thúc với bảy best practices được đúc kết từ hàng trăm công trình nghiên cứu.

Một: hiểu rõ loại distribution shift trong bài toán của bạn trước khi chọn phương pháp. Hai: luôn report Worst-Group Accuracy, không chỉ average. Ba: tune ERM thật kỹ làm baseline trước. Bốn: nếu có group labels, Group DRO là lựa chọn mạnh nhất. Năm: nếu không, JTT hoặc clustering-based là điểm khởi đầu tốt. Sáu: với foundation models, thử Last Layer Retraining trước khi fine-tune toàn bộ. Và bảy, quan trọng nhất: thu thập thêm dữ liệu đa dạng môi trường. Data collection thường hiệu quả hơn mọi algorithmic fix.

## Scene 9.1 - Tổng hợp hành trình

Chúng ta đã đi một hành trình dài.

Bắt đầu từ một câu hỏi đơn giản: tại sao AI học những thứ sai? ERM và shortcut learning.

Rồi nhìn qua lăng kính nhân quả: spurious features tồn tại vì AI học tương quan thay vì nhân quả, và tương quan đó bị phá vỡ khi môi trường thay đổi.

Ba phương pháp, IRM, Group DRO, JTT, cố gắng buộc AI học causal features bằng những cách khác nhau: qua invariance của gradient, qua tối ưu worst-case, qua self-identification của thiểu số.

Và trong thời đại foundation models, vấn đề không biến mất. Nó chỉ thay đổi hình dạng và quy mô.

Tất cả dẫn về một từ: Stability. Một AI ổn định không phải là AI không bao giờ gặp phân phối mới. Mà là AI biết điều gì thực sự quan trọng, và giữ vững niềm tin đó dù hoàn cảnh thay đổi.

Đây là ranh giới tiếp theo.

## Scene 9.2 - Open Problems & Credits

Cảm ơn các bạn. Tutorial để lại ba cánh cửa mở: lý thuyết OOD cho foundation models, model selection không cần OOD validation, và OOD trong thế giới multimodal và agentic AI. Đây là biên giới tiếp theo của nghiên cứu. Link tutorial gốc, slides, và source code Manim đều có trong phần mô tả.