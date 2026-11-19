# Lời thoại seminar DS111

9 slide, 13 phút trình bày và 2 phút hỏi đáp. Ba câu hỏi xuyên suốt bài là vì sao có thể dùng giá trị đại diện để ước lượng ô thiếu, khi nào cách thay thế hợp lý, và nó làm biến dạng dữ liệu thế nào.

Các phần thuật ngữ và phụ lục dùng để ôn tập, ngoài lời thoại 13 phút.

## 1. Nên điền 23 hay 34? (00:00–01:00)

**Mục tiêu**

Đặt câu hỏi nghiên cứu từ ví dụ tuổi.

**Chỉ hình**

Trỏ dãy tuổi, dừng ở NaN, rồi đọc ba câu hỏi.

**Lời thoại**

Xin chào thầy và tất cả các bạn đến với mini seminar hôm nay. Đầu tiên, mình có một cột tuổi gồm 20, 22, 23, 25, 80 và một ô bị thiếu. Theo các bạn, mình nên điền 23 là Median hay 34 là Mean? [Dừng hai giây.]

Hôm nay chúng ta cùng tìm hiểu việc vận dụng các thước đo xu hướng trung tâm để điền khuyết dữ liệu. Các bạn có thể đã gặp quy tắc chọn Mean, Median hoặc Mode. Trong bài này, tụi mình sẽ đi sâu vào cơ sở của các lựa chọn đó.

Câu hỏi xuyên suốt là vì sao một giá trị đại diện cho phân phối có thể dùng để ước lượng ô thiếu, khi nào cách thay thế ấy hợp lý, và nó làm dữ liệu sai lệch ra sao. Cuối bài, chúng ta sẽ quay lại lựa chọn 23 hay 34 với một cách lập luận đầy đủ hơn.

**Thuật ngữ để chuẩn bị**

- **NaN** là dấu thiếu thường gặp ở cột số.
- **Imputation — điền khuyết** thay ô thiếu bằng một ước lượng.
- **Ground truth** là giá trị gốc được giữ riêng để đối chiếu sau khi che.

**Chuyển tiếp**

Trước tiên, ta đang dự đoán điều gì khi lấy một giá trị chung để điền?

## 2. Giá trị đại diện là một dự đoán chung (01:00–02:30)

**Mục tiêu**

Giải thích từ phân phối quan sát đến dự đoán bằng một hằng số.

**Chỉ hình**

Hai đường sai số khi thay đổi giá trị dự đoán c, tính trên năm tuổi đã biết.

**Lời thoại**

Khi một ô tuổi bị thiếu, mình chưa biết người đó có đặc điểm gì khác. Nếu chỉ dùng cột tuổi và quyết định điền cùng một số, bài toán trở thành chọn một giá trị dự đoán chung.

Ta có thể dùng năm tuổi quan sát như một mô tả đơn giản về phân phối mà tuổi bị thiếu có thể đến từ. Nhưng bước này cần một giả định, đó là những người đã có tuổi phải đủ đại diện cho người bị thiếu tuổi. Nếu chỉ người cao tuổi bỏ trống, việc dùng phần quan sát sẽ có vấn đề.

Để thấy cách chọn giá trị chung, mình thử nhiều số c rồi chấm c với từng tuổi đã quan sát. Hình bên trái tính sai số tuyệt đối trung bình, nhỏ nhất tại 23. Hình bên phải tính căn của sai số bình phương trung bình, nhỏ nhất tại 34. Cả hai dùng cùng năm tuổi, nhưng đặt trọng số khác nhau cho sai số lớn.

Đường cong này tính trên phần đã biết. Tuổi thật ở ô NaN vẫn chưa biết. Giá trị đại diện cung cấp một dự đoán có cơ sở khi giả định về phần quan sát phù hợp, và chất lượng dự đoán còn phụ thuộc cách mình đo sai số.

**Thuật ngữ để chuẩn bị**

- **Dự đoán hằng số** dùng cùng một số cho mọi ô thiếu trong cột.
- **Phân phối quan sát** mô tả các giá trị đã ghi nhận và tần suất của chúng.
- **Tính đại diện** nghĩa là phần quan sát phù hợp với đối tượng cần dự đoán theo các đặc điểm đang dùng.
- **Bất định** là mức chưa biết về giá trị thật. Một con số dự đoán chưa biểu diễn đầy đủ mức này.
- **Robust — bền vững** mô tả mức ít nhạy của thống kê với một số thay đổi cực đoan.

**Chuyển tiếp**

Ba thước đo trung tâm tương ứng với ba mục tiêu dự đoán nào?

## 3. Mean, Median và Mode theo mục tiêu sai số (02:30–04:00)

**Mục tiêu**

Đặt các thống kê trong bài toán tối ưu dự đoán hằng số.

**Chỉ hình**

Bảng mục tiêu, thống kê và phạm vi áp dụng.

**Lời thoại**

Với biến định lượng, nếu phạt sai số bằng bình phương, Mean làm tổng mức phạt nhỏ nhất trên tập đang xét. Công thức là tổng các giá trị quan sát chia cho số quan sát. RMSE lấy căn sau khi tính trung bình bình phương, nên lựa chọn tối ưu vẫn là Mean.

Nếu phạt theo trị tuyệt đối, Median là giá trị tối ưu. Median dùng vị trí giữa sau khi sắp xếp. Vì dựa vào thứ hạng, nó ít nhạy hơn với việc đổi 80 thành 800 trong ví dụ tuổi. Khi có số phần tử chẵn, quy ước thông dụng lấy trung bình hai số giữa.

Với nhãn loại như người giám hộ, ta muốn đoán đúng nhiều ô nhất. Khi chi phí sai giữa các lớp bằng nhau, nhãn phổ biến nhất là lựa chọn chung hợp lý. Đó là Mode. Ví dụ Size có M, M, L, S, thiếu, M thì Mode bằng M.

Các kết quả tối ưu áp dụng cho một dự đoán cố định trên phân phối hoặc tập dùng để tối ưu. Trong thực nghiệm, mình học thống kê từ train rồi kiểm chứng trên test. Mode còn có thể hòa, chẳng hạn 2 và 8 đều xuất hiện hai lần trong dãy 2, 2, 3, 8, 8. Quy tắc của SimpleImputer là chọn giá trị nhỏ nhất trong các Mode.

**Thuật ngữ để chuẩn bị**

- **Mean** là $\bar{x}=\sum_i x_i/n$.
- **Median** là giá trị giữa theo thứ hạng. Với mẫu số chẵn, trung bình hai số giữa là một quy ước. Mọi số giữa hai giá trị ấy đều tối ưu tổng sai số tuyệt đối.
- **Mode** là giá trị có tần suất cực đại. Nhiều Mode có thể đồng hạng.
- **Hàm mất mát** quy định mức phạt khi dự đoán sai. **MSE** là trung bình bình phương sai số. **MAE** là trung bình trị tuyệt đối. **RMSE** bằng căn MSE.
- **Mất mát 0–1** phạt 0 nếu nhãn đúng, 1 nếu nhãn sai.
- **Nhãn thứ bậc** như S < M < L có thứ tự. Median theo hạng cần quy tắc rõ, còn Mean của mã số tùy ý cần cơ sở về khoảng cách.
- **Quy tắc hòa** của SimpleImputer most_frequent chọn giá trị nhỏ nhất trong các Mode.

**Chuyển tiếp**

Điều kiện nào giúp thống kê học từ phần quan sát áp dụng được cho ô thiếu?

## 4. Khi nào phần quan sát đủ đại diện? (04:00–05:30)

**Mục tiêu**

Nối hình dạng phân phối, cơ chế thiếu và thông tin sử dụng.

**Chỉ hình**

Ba phân phối lý thuyết và điều kiện áp dụng.

**Lời thoại**

Mean dùng độ lớn của mọi giá trị nên các điểm ở đuôi có thể kéo nó đi xa. Median dùng thứ hạng nên thường gần cụm phổ biến hơn khi đuôi dài. Trong ba ví dụ trên hình, Normal có ba tâm trùng nhau, Gamma có đuôi phải và Mean lớn hơn Median, còn Gamma phản chiếu có đuôi trái. Skewness thường dương ở đuôi phải và âm ở đuôi trái. Ta đọc cùng histogram và boxplot để thấy cấu trúc thực tế.

Hình dạng cho biết giá trị nào đại diện cho phần mình nhìn thấy. Muốn dùng nó cho ô thiếu, phải xét cách phát sinh thiếu. MCAR là xác suất thiếu độc lập với các giá trị dữ liệu. Cơ chế này cho phép phần còn lại đại diện theo thiết kế, dù mẫu hữu hạn vẫn dao động.

Nếu khả năng thiếu phụ thuộc đặc điểm đã quan sát, ta cần xem có nên điều kiện hóa theo các đặc điểm đó. Nếu còn phụ thuộc chính phần chưa quan sát, ước lượng đòi hỏi thêm giả định. Tỷ lệ thiếu tự nó chưa xác định được cơ chế.

Cuối cùng là ý nghĩa biến. Số 0 có thể hợp lệ. Nhãn mã hóa bằng số vẫn cần xem thang đo trước khi cộng hoặc lấy trung bình. Một thống kê chung cũng có thể bỏ qua khác biệt giữa các nhóm.

**Thuật ngữ để chuẩn bị**

- **MCAR** có xác suất thiếu độc lập với các giá trị dữ liệu.
- **MAR** nghĩa là sau khi xét phần quan sát, xác suất thiếu không còn phụ thuộc phần chưa quan sát.
- **MNAR** nghĩa là phần chưa quan sát vẫn liên quan xác suất thiếu sau khi xét phần quan sát.
- **Histogram** biểu diễn tần suất theo khoảng.
- **Hàm mật độ** có tổng diện tích bằng 1, xác suất khoảng bằng diện tích trên khoảng ấy.
- **Skewness** là hệ số bất đối xứng. Dương thường đi với đuôi phải, âm với đuôi trái. Giá trị gần 0 cần đọc cùng hình.
- **Moment bậc ba** dùng $(x_i-\bar{x})^3$, tăng ảnh hưởng của điểm xa tâm và giữ dấu trái/phải.
- **Q1, Q3** là phân vị 25% và 75%. **IQR** bằng $Q3-Q1$.
- **Boxplot** có hộp Q1–Q3, vạch Median và râu. Điểm ngoài hàng rào $Q1-1{,}5IQR$ và $Q3+1{,}5IQR$ được gắn cờ.
- **Ngoại lệ** cần kiểm tra nguồn gốc và có thể là quan sát hợp lệ.
- **Đa mốt trong mẫu** và **nhiều đỉnh trên mật độ** có cách xác định khác nhau.

**Chuyển tiếp**

Tụi mình kiểm chứng các lập luận này trên dữ liệu học sinh thực tế.

## 5. Kiểm chứng trên Student Performance (05:30–07:15)

**Mục tiêu**

Trình bày EDA và cách đánh giá bằng giá trị gốc được giữ riêng.

**Chỉ hình**

Histogram và boxplot của G1, absences, rồi quy trình train/test.

**Lời thoại**

Student Performance của UCI có 649 dòng môn tiếng Bồ Đào Nha, thu thập tại hai trường GP và MS. Tụi mình dùng G1 là điểm kỳ đầu, absences là số buổi vắng, guardian là người giám hộ và G3 là điểm cuối kỳ. Cột school được giữ đầy đủ để thử theo nhóm.

Bản gốc đầy đủ nên mình giữ giá trị thật rồi chủ động che ô. Trên hình là demo ở mức che danh nghĩa 15%. Riêng absences có 94 trên 649 ô bị che, tương đương 14,48%. Phần trăm thực tế dao động vì mỗi ô có một phép thử ngẫu nhiên.

G1 có Mean khoảng 11,35, Median 11 và skewness 0,01. Vùng trung tâm khá cân đối nhưng boxplot vẫn gắn cờ 14 điểm. Absences có Mean khoảng 3,71, Median 2 và skewness 2,08. Đuôi phải dài và có 18 điểm bị gắn cờ. Ta giữ cả các số buổi vắng cao và số 0 để phân tích.

Để chấm sai số, chia 486 dòng train và 163 dòng test trước, sau đó mới che riêng hai tập. Bộ điền chỉ học trên train đã che rồi áp lên test. Chỉ các ô test bị che được so với giá trị gốc. Các phương pháp dùng cùng mặt nạ, lặp 12 lần tại mỗi mức 5%, 15% và 30%. Cách này giúp câu hỏi “điền tốt đến đâu” có phép đo cụ thể.

**Thuật ngữ để chuẩn bị**

- **UCI** là kho dữ liệu công bố Student Performance.
- **G1, G2, G3** là điểm ba giai đoạn, theo thang 0–20. absences là số buổi vắng, guardian là người giám hộ, school là mã trường.
- **EDA** là phân tích khám phá qua thống kê và biểu đồ.
- **Train/test split** chia hàng thành tập học thống kê và tập đánh giá.
- **Mask — mặt nạ** là bảng True/False. True đánh dấu ô được che.
- **Che Bernoulli** thử che từng ô theo xác suất cố định. Tỷ lệ thực tế dao động quanh mức danh nghĩa.
- **Seed** xác định trạng thái khởi tạo bộ sinh số giả ngẫu nhiên để tái lập.
- **fit** học thống kê. **transform** dùng thống kê đã học để điền dữ liệu.
- **Leakage** là thông tin test tham gia học thống kê hoặc chọn phương pháp.
- **None, pd.NA, NaN** là những biểu diễn thiếu được pandas nhận diện trong kiểu cột phù hợp. **isna().sum()** đếm ô thiếu, **isna().mean()** tính tỷ lệ.
- **Benchmark** là thiết kế đánh giá cố định để so các phương pháp.

**Chuyển tiếp**

Kết quả có đúng với cách giải thích theo hàm mất mát không?

## 6. Cùng dữ liệu, khác mục tiêu sai số (07:15–09:00)

**Mục tiêu**

Dùng kết quả test để kiểm chứng lựa chọn thống kê.

**Chỉ hình**

Hai nhóm cột MAE/RMSE của absences và số lần thắng theo cặp.

**Lời thoại**

Ở mức che 15%, trên cột absences, Median có MAE 2,52 buổi, thấp hơn 2,83 của Mean. Khi đổi sang RMSE, Mean đạt 3,69, thấp hơn 3,86 của Median.

Vì sao thứ hạng đổi? Median gần vùng phổ biến của số buổi vắng, giúp giảm sai số tuyệt đối trung bình. Trong RMSE, các ô thật có số buổi vắng cao đóng góp lớn vì sai số bị bình phương. Mean dịch về đuôi phải nên có thể giảm một phần các lỗi lớn đó. Đây là kết quả test của mẫu này, phù hợp với lập luận về hai mục tiêu.

Ta cũng kiểm tra theo từng mặt nạ. Median có MAE thấp hơn ở 10 trên 12 lần, có một lần hòa. Mean có RMSE thấp hơn ở 11 trên 12 lần. Với G1, Mean có RMSE thấp hơn cả 12 lần nhưng chênh lệch trung bình chỉ khoảng 0,08 điểm. Cần đọc cả hướng và độ lớn cải thiện.

Với guardian, Mode chọn mother và Accuracy trung bình khoảng 68,87%. Con số đó bằng tỷ lệ mother thật trong các ô test che, vì mọi ô nhận cùng nhãn. Điểm trung bình và SD qua mặt nạ được lưu trong notebook.

Phân phối giúp hiểu vì sao các giá trị điền khác nhau, còn mục tiêu sai số quyết định mình đánh giá lựa chọn ấy theo tiêu chí nào.

**Thuật ngữ để chuẩn bị**

- **MAE** bằng $\sum_i|\hat{x}_i-x_i|/k$, **RMSE** bằng $\sqrt{\sum_i(\hat{x}_i-x_i)^2/k}$ trên $k$ ô test che.
- **Accuracy** là tỷ lệ ô nhãn điền đúng.
- **So sánh theo cặp** lấy hiệu hai điểm của cùng mặt nạ, tận dụng việc gặp cùng các ô khó/dễ.
- **SD qua mặt nạ** đo dao động giữa 12 lần che trên cùng dữ liệu và lần chia.
- **Điểm phần trăm** là đơn vị của chênh lệch tỷ lệ trên thang phần trăm.
- **Ý nghĩa thực tiễn** cần xét độ lớn cải thiện và mục tiêu sử dụng.
- **Wilcoxon dấu-hạng** dùng dấu và thứ hạng độ lớn của các hiệu. Cần xét giả định đối xứng của phân phối hiệu, tính độc lập của các cặp và xử lý hòa.
- **p-value** là xác suất thu được thống kê ít nhất cực đoan như kết quả đã thấy dưới giả thuyết không và giả định kiểm định.
- **Kiểm định nhiều lần** cần xác định trước họ so sánh và có thể cần hiệu chỉnh như Holm. Slide chính dùng độ lớn hiệu và số lần thắng để mô tả.

**Chuyển tiếp**

Một phương pháp có sai số chấp nhận được sẽ làm dữ liệu sau điền thay đổi ra sao?

## 7. Giá trị điền làm đổi phân phối (09:00–10:30)

**Mục tiêu**

Đánh giá tác động của việc thay các giá trị khác nhau bằng một hằng số.

**Chỉ hình**

Histogram trước/sau bên trái, tỷ trọng nhãn mẹ bên phải và SD.

**Lời thoại**

Trong hình absences, điền Median làm cột ở 2 buổi tăng lên. Điền Mean tạo thêm tần suất tại khoảng 3,71 buổi. Tất cả các ô thiếu cùng nhận một số, trong khi các giá trị thật bị che vốn khác nhau.

Khi điền bằng Mean của chính phần quan sát, Mean giữ nguyên. Tổng bình phương độ lệch quanh Mean cũng giữ nguyên vì các ô thêm vào có độ lệch bằng 0, còn mẫu số của phương sai tăng. Trong demo, SD absences giảm từ 4,66 xuống 4,31. Công thức phương sai mẫu được ghi trong phần tra cứu.

Biến loại cũng thay đổi. Tỷ trọng mother trong phần có mặt là 70,3%, sau điền Mode tăng thành 74,6%. Các ô father và other bị che đều được điền sai, dù Accuracy chung gần 69%. Nếu mục tiêu là phân tích cơ cấu người giám hộ, thay đổi này đáng quan tâm.

Quan hệ giữa biến cũng có thể bị ảnh hưởng. Lặp 300 mặt nạ MCAR 15%, tương quan G3 với chỉ báo trường GP trung bình sau điền Mean khoảng 0,264, so với 0,284 trên bản đầy đủ. Một lần che riêng có thể cho diễn biến khác. Vì thế mình xem cả sai số từng ô, hình dạng và quan hệ sau điền.

**Thuật ngữ để chuẩn bị**

- **Phương sai mẫu** bằng $s^2=\sum_i(x_i-\bar{x})^2/(n-1)$. **SD** bằng $\sqrt{s^2}$.
- **Co phương sai khi điền Mean** có $s^2_{sau}=s^2_{quan\ sát}(n-1)/(n+m-1)$ nếu điền Mean của chính $n$ ô quan sát vào $m$ ô thiếu.
- **Đỉnh nhân tạo** là tần suất tăng tại giá trị điền do nhiều ô nhận cùng một số.
- **Tương quan Pearson** đo quan hệ tuyến tính, nằm trong [−1, 1]. Chỉ báo GP bằng 1 nếu học GP, bằng 0 nếu MS.
- **Co tương quan dưới MCAR** có xấp xỉ $r_{sau}\approx r_{đầy\ đủ}\sqrt{1-q}$ khi một biến bị che xác suất $q$, biến còn lại đầy đủ và dùng Mean để điền. Một lần che hữu hạn có thể khác xu hướng trung bình.
- **Lớp đa số và lớp hiếm** có tần suất cao hoặc thấp hơn.
- **Recall lớp k** là tỷ lệ điền đúng trong các ô thật thuộc lớp k. Điền toàn mother cho recall father/other bằng 0 ở phần che có lớp đó.
- **Macro-F1** là trung bình F1 các lớp, trọng số bằng nhau. F1 kết hợp precision và recall.
- **Baseline lấy mẫu nhãn** có Accuracy kỳ vọng $\sum_k p_k^2$ khi nhãn thật và nhãn lấy mẫu độc lập, cùng phân phối. Giá trị lý thuyết theo tỷ lệ đầy đủ guardian khoảng 55,11%. Benchmark phải học xác suất dự đoán từ train.

**Chuyển tiếp**

Dùng thống kê theo nhóm có giải quyết được giới hạn của một giá trị toàn cục không?

## 8. Khi một giá trị chung chưa đủ (10:30–12:00)

**Mục tiêu**

Minh họa dự đoán có điều kiện và giới hạn của việc dựa vào nhóm.

**Chỉ hình**

Histogram G3 theo trường từ demo và bảng sai số trên test.

**Lời thoại**

Nếu biết trường của học sinh, mình có thể học Median G3 riêng cho GP và MS từ train. Đây là cách dùng thêm thông tin để dự đoán có điều kiện. Hai phân phối quan sát có chồng lấn và khác nhau ở một số vùng. Các mốc trong hình tính từ chính demo.

Trong benchmark 15%, MAE Median chung khoảng 2,42 điểm và theo trường khoảng 2,35. RMSE lần lượt khoảng 3,17 và 3,19. Mức cải thiện MAE khá nhỏ, còn RMSE hơi tăng. Dùng thêm thông tin nhóm vẫn cần kiểm chứng.

EDA còn cho thấy 15 dòng G3 bằng 0, trong đó 14 thuộc MS. UCI quy định điểm trong khoảng 0 đến 20 nên tụi mình giữ các dòng này. Nếu loại chúng trước khi chia lại, MAE Median chung khoảng 2,193 và theo trường khoảng 2,197. Kết quả nhạy với thành phần mẫu. Phân tích đó cũng thay đổi tập đối tượng và lần chia, nên cần tìm hiểu thêm trước khi gán nguyên nhân.

Nhóm phải có sẵn lúc điền và đủ quan sát. Mã dùng Median train toàn cục làm dự phòng cho nhóm chưa gặp hoặc có dưới 20 quan sát. Khi cấu trúc phức tạp hơn, có thể thử phương pháp dùng nhiều biến và đánh giá lại.

**Thuật ngữ để chuẩn bị**

- **Dự đoán có điều kiện** dùng thêm thông tin như trường của học sinh.
- **Group-wise imputation** học thống kê riêng cho từng nhóm trên train.
- **Fallback** là thống kê dự phòng khi nhóm chưa gặp hoặc thiếu quan sát. Project dùng Median train toàn cục cho nhóm dưới 20 quan sát.
- **Sensitivity analysis — phân tích độ nhạy** đổi một điều kiện rồi xem kết quả thay đổi thế nào.
- **Điểm G3 bằng 0** thuộc miền điểm UCI công bố. Chưa có hồ sơ xác nhận từng dòng là bỏ thi, nghỉ học hay mã thiếu.
- **Thay đổi tập đối tượng** xảy ra khi loại các dòng G3 bằng 0. Chia lại và tạo mặt nạ trên mẫu mới cũng thay đổi dữ liệu benchmark.

**Chuyển tiếp**

Quay lại ô tuổi bị thiếu, bây giờ chúng ta trả lời đầy đủ hơn.

## 9. Trở lại ô tuổi bị thiếu (12:00–13:00)

**Mục tiêu**

Trả lời trực tiếp ba vế câu hỏi mở đầu.

**Chỉ hình**

Ba câu trả lời và lựa chọn 23 hay 34.

**Lời thoại**

Vì sao dùng được một giá trị đại diện? Khi chỉ dự đoán bằng một hằng số, ta chọn giá trị làm nhỏ nhất tổn thất trên phân phối phù hợp. Mean, Median và Mode tương ứng với các mục tiêu khác nhau.

Khi nào hợp lý? Khi kiểu biến, mục tiêu sai số và giả định về phần quan sát phù hợp với phần thiếu. Nếu có thông tin nhóm hữu ích thì kiểm chứng cách dùng thông tin ấy.

Nó làm sai lệch dữ liệu thế nào? Điền hằng số làm mất biến thiên ở các ô điền, tăng tần suất tại một điểm hoặc một nhãn và có thể đổi tương quan.

Ở ví dụ tuổi, 23 phù hợp khi tối ưu sai số tuyệt đối trên phân phối quan sát, còn 34 phù hợp với sai số bình phương. Tuổi thật bị thiếu vẫn chưa biết. Lựa chọn có cơ sở cần đi cùng kiểm chứng và giới hạn. Mình cảm ơn thầy và các bạn.

**Thuật ngữ để chuẩn bị**

- **Ước lượng điểm** trả về một giá trị đại diện.
- **KNN imputation** dựa vào các hàng gần nhau theo khoảng cách, cần xem thang đo.
- **MICE** dùng các mô hình điều kiện theo chuỗi để tạo nhiều bộ điền, phản ánh độ bất định theo giả định.
- **IterativeImputer** mặc định tạo một bộ điền. Multiple imputation cần thêm lấy mẫu, nhiều lần chạy và gộp kết quả phù hợp.
- **Giới hạn khái quát hóa** gồm một môn học, một mẫu, một lần chia train/test và MCAR.

**Chuyển tiếp**

Mời thầy và các bạn đặt câu hỏi trong hai phút còn lại.

## Hỏi đáp (13:00–15:00)

Mở [câu hỏi phản biện](questions_answers.md), [script có thuật ngữ](script_va_thuat_ngu.md) và [nguồn tham khảo](references.md).


## Phụ lục tra cứu mã và công cụ

Phần này dùng để ôn tập và trả lời câu hỏi về cách chạy thực nghiệm.

| Công cụ | Vai trò |
|---|---|
| Python | Ngôn ngữ chạy chương trình |
| pandas | Đọc CSV, xử lý bảng và tính thống kê |
| NumPy | Tính toán mảng và sinh số giả ngẫu nhiên |
| scikit-learn | Bộ điền SimpleImputer và hàm chia train/test |
| SciPy | Phân phối lý thuyết và phép kiểm định trong phân tích bổ sung |
| matplotlib | Vẽ biểu đồ |
| unittest | Kiểm thử các hành vi của mã |
| Jupyter | Môi trường mở notebook và xem kết quả |

### Chuẩn bị dữ liệu

| Code | Giải thích |
|---|---|
| `pd.read_csv(source, sep=";", usecols=[...])` | Đọc những cột cần dùng từ CSV gốc có dấu phân tách chấm phẩy |
| `np.random.default_rng(SEED)` | Khởi tạo bộ sinh số để tái lập lần che |
| `rng.random((n_rows, n_cols)) < rate` | Sinh số trong [0, 1) cho mỗi ô, che nếu số đó nhỏ hơn xác suất đã đặt |
| `DataFrame.mask(mask)` | Thay các vị trí True bằng giá trị thiếu |
| `mask.reindex(columns=complete.columns, fill_value=False)` | Căn mặt nạ theo đúng cột, giữ school ngoài danh sách che |

### Học thống kê và chấm điểm

| Code | Giải thích |
|---|---|
| `train_test_split(..., test_size=0.25, random_state=42)` | Chia ngẫu nhiên theo hàng với cùng lần chia khi chạy lại |
| `np.random.SeedSequence(seed).spawn(2)` | Tạo hai seed con cho luồng che train và test |
| `train[[variable]]` | Giữ biến dưới dạng bảng hai chiều mà scikit-learn cần |
| `SimpleImputer(...).fit(...)` | Tính thống kê thay thế từ phần quan sát trong dữ liệu fit |
| `imputer.statistics_[0]` | Lấy giá trị điền đã học cho cột đầu tiên |
| `imputer.transform(...).ravel()` | Điền dữ liệu rồi duỗi mảng một cột thành mảng một chiều |
| `column.astype(object).where(column.notna(), np.nan)` | Chuẩn hóa đầu vào cột chữ và dấu thiếu cho cấu hình bộ điền hiện tại |
| `truth.loc[mask]` | Chọn giá trị gốc tại những ô đã che |
| `error.abs().mean()` | Tính MAE |
| `np.sqrt(error.pow(2).mean())` | Tính RMSE |
| `groupby(GROUP)[variable].agg(["count", "median"])` | Đếm giá trị có mặt và tính Median theo trường từ train |
| `test[GROUP].map(usable).fillna(fallback)` | Gán Median trường, dùng dự phòng khi trường chưa có thống kê đủ quan sát |
| `raise ValueError(...)` khi cột train toàn thiếu | Báo rằng không có quan sát để ước lượng thống kê |

### Vẽ hình và phân tích bổ sung

| Code | Giải thích |
|---|---|
| `matplotlib.use("Agg")` | Vẽ ra file bằng backend không cần cửa sổ đồ họa |
| `plt.subplots(..., layout="constrained")` | Tạo các ô biểu đồ và hỗ trợ căn khoảng trống |
| `hist(..., weights=np.full(len(values), 100 / len(values)))` | Mỗi quan sát đóng góp cùng tỷ trọng để trục dọc biểu diễn phần trăm |
| `boxplot(..., orientation="horizontal")` | Vẽ boxplot nằm ngang |
| `ax.axvline(...)` | Kẻ mốc dọc, dùng cho Mean và Median |
| `ax.fill_between(...)` | Tô diện tích dưới đường mật độ |
| `ax.stairs(...)` | Vẽ tỷ trọng histogram thành đường bậc thang |
| `ax.bar(..., yerr=std, capsize=4)` | Vẽ cột kèm thanh sai số bằng SD đã tính |
| `ax.bar_label(...)` | Ghi số lên cột |
| `savefig(..., dpi=240, bbox_inches="tight")` | Xuất hình độ phân giải cao và cắt viền thừa |
| `pivot(index="mask_seed", columns="method", values="value")` | Ghép điểm theo từng seed để lấy hiệu hai phương pháp khi phân tích bổ sung |
| `wilcoxon(differences)` | Tính kiểm định dấu-hạng, cần kiểm tra giả định, hiệu bằng 0 và giá trị hòa |

### Nguồn chuẩn bị thuật ngữ

- Ý nghĩa biến điểm, guardian và school theo dữ liệu UCI. [Student Performance](https://archive.ics.uci.edu/dataset/320/student-performance)
- Hệ số Fisher–Pearson và cách đọc bất đối xứng. [NIST về skewness](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm)
- Chiến lược và quy tắc chọn Mode của bộ điền. [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
- Giả thuyết kiểm định và xử lý hiệu bằng 0, giá trị hòa. [SciPy về Wilcoxon](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html)
- Điền đa biến và điền nhiều lần. [scikit-learn về imputation](https://scikit-learn.org/stable/modules/impute.html#multiple-vs-single-imputation)
