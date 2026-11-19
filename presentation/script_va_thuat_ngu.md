# Lời thoại seminar DS111

13 slide, 13 phút trình bày và 2 phút hỏi đáp. Phần I gồm phân phối, skewness và ngoại lệ. Phần II gồm các thước đo và cơ sở tối ưu, rồi kiểm chứng bằng thực nghiệm.

Công thức, thuật ngữ và phụ lục dùng để ôn tập. Thời lượng dành cho lời thoại chính.

## 1. Nên điền 23 hay 34? (00:00–00:45)

**Mục tiêu**

Giải thích nội dung nên điền 23 hay 34? trong lựa chọn giá trị điền.

**Chỉ hình**

Dãy tuổi và ba câu hỏi xuyên suốt.

**Lời thoại**

Xin chào thầy và tất cả các bạn đến với mini seminar hôm nay. Mình có cột tuổi gồm 20, 22, 23, 25, 80 và một ô thiếu. Theo các bạn, nên điền 23 là Median hay 34 là Mean? [Dừng hai giây.]

Hôm nay mình tìm hiểu các thước đo xu hướng trung tâm để điền khuyết. Bài trả lời ba câu hỏi. Vì sao giá trị đại diện có thể ước lượng ô thiếu? Khi nào thay thế hợp lý? Và nó làm dữ liệu sai lệch ra sao? Trước hết, ta cần hiểu phân phối và cách thống kê mô tả nó.

**Thuật ngữ để chuẩn bị**

- **NaN** là dấu thiếu thường gặp ở cột số.
- **Imputation — điền khuyết** thay ô thiếu bằng một ước lượng.
- **Ground truth** là giá trị gốc được giữ riêng để đối chiếu sau khi che.

**Chuyển tiếp**

Tiếp theo là phân phối dữ liệu.

## 2. Phân phối dữ liệu (00:45–02:00)

**Mục tiêu**

Giải thích nội dung phân phối dữ liệu trong lựa chọn giá trị điền.

**Chỉ hình**

Normal, Gamma và Gamma phản chiếu với ba mốc tâm.

**Công thức và lưu ý để chuẩn bị**

Đối xứng minh họa có $\mathrm{Mean}\approx\mathrm{Median}\approx\mathrm{Mode}$ trên mẫu.

Lệch phải điển hình có $\mathrm{Mode}<\mathrm{Median}<\mathrm{Mean}$.

Lệch trái điển hình có $\mathrm{Mean}<\mathrm{Median}<\mathrm{Mode}$.

Các quan hệ này gắn với dạng phân phối cụ thể. Đối xứng riêng nó chưa bảo đảm Mean tồn tại, chẳng hạn Cauchy.

**Lời thoại**

Hình thứ nhất dùng phân phối chuẩn đối xứng một đỉnh. Ở mô hình này, Mean, Median và Mode cùng ở tâm. Trên mẫu hữu hạn, chúng thường chỉ gần nhau. Đối xứng còn gặp ở phân phối tam giác và nhiều dạng khác.

Hình thứ hai là Gamma lệch phải, đuôi kéo về phía các giá trị lớn. Thu nhập hoặc giá nhà có thể có dạng như vậy. Giá trị lớn đóng góp mạnh vào tổng, kéo Mean sang phải. Trong ví dụ này, Mode nhỏ hơn Median, nhỏ hơn Mean.

Hình thứ ba là Gamma phản chiếu có đuôi trái. Ta có thể liên tưởng đến bài kiểm tra dễ, nhiều điểm cao và ít điểm rất thấp. Mean bị kéo xuống, nằm phía trái Median. Các thứ tự này là ví dụ thường gặp. Với dữ liệu thực, mình vẫn xem hình dạng, số đỉnh và các điểm ở đuôi trước khi lựa chọn.

**Thuật ngữ để chuẩn bị**

- **Phân phối** mô tả vị trí và mức phổ biến của các giá trị.
- **Đối xứng** nghĩa là hai phía quanh tâm có cùng hình dạng. **Lệch phải/trái** nói về phía đuôi kéo dài.
- **Normal** là phân phối chuẩn. **Gamma** là họ phân phối trên miền dương dùng trong hình lệch phải.
- **Mật độ** có diện tích bằng 1. Xác suất của một khoảng bằng diện tích trên khoảng ấy.

**Chuyển tiếp**

Tiếp theo là skewness và ngoại lệ.

## 3. Skewness và ngoại lệ (02:00–03:00)

**Mục tiêu**

Giải thích nội dung skewness và ngoại lệ trong lựa chọn giá trị điền.

**Chỉ hình**

Bảng dấu skewness, hàng rào và boxplot absences.

**Công thức và lưu ý để chuẩn bị**

$IQR=Q_3-Q_1$, hàng rào $[Q_1-1.5IQR,\ Q_3+1.5IQR]$.

Râu boxplot dừng tại quan sát xa nhất còn trong hàng rào. Một dạng skewness là $g_1=m_3/m_2^{3/2}$, với $m_k=\sum_i(x_i-\bar{x})^k/n$. pandas dùng hệ số Fisher–Pearson hiệu chỉnh cỡ mẫu.

**Lời thoại**

Skewness đo bất đối xứng theo moment bậc ba. Dương thường gợi ý đuôi phải, âm thường gợi ý đuôi trái. Gần 0 cần xem hình vì các thành phần moment có thể bù nhau. Mình kết hợp histogram, boxplot và ý nghĩa biến thay vì đặt một ngưỡng chung.

Outlier là điểm khác biệt đáng kể so với cấu trúc thường gặp. Một cách gắn cờ dùng IQR bằng Q3 trừ Q1, rồi xét điểm ngoài hai hàng rào trên slide.

Ở demo số buổi vắng, Q1 bằng 0, Q3 bằng 6, nên IQR bằng 6. Hai hàng rào là âm 9 và 15, có 18 điểm lớn hơn 15 bị gắn cờ. Tụi mình giữ các điểm này để phân tích và kiểm tra nguồn gốc.

**Thuật ngữ để chuẩn bị**

- **Skewness** là hệ số bất đối xứng theo moment bậc ba chuẩn hóa.
- **Outlier** là điểm khác biệt đáng kể, cần xét nguồn gốc và cấu trúc dữ liệu.
- **Q1, Q3** là phân vị 25% và 75%. **IQR** bằng $Q3-Q1$.
- **Hàng rào** $[Q1-1{,}5IQR,Q3+1{,}5IQR]$ dùng gắn cờ. Râu boxplot dừng tại điểm xa nhất còn trong hàng rào.

**Chuyển tiếp**

Tiếp theo là mean — trung bình cộng.

## 4. Mean — Trung bình cộng (03:00–03:50)

**Mục tiêu**

Giải thích nội dung mean — trung bình cộng trong lựa chọn giá trị điền.

**Chỉ hình**

Công thức Mean và ví dụ đổi 80 thành 800.

**Công thức và lưu ý để chuẩn bị**

Với $X=\{x_1,\ldots,x_n\}$,
\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i.
\]
Một quan sát tăng $\Delta$ làm Mean tăng $\Delta/n$.

**Lời thoại**

Với n giá trị định lượng quan sát hợp lệ, Mean là tổng chia cho n. Nó dùng độ lớn của tất cả quan sát nên phản ánh mức trung bình của mẫu.

Năm tuổi đang có tổng là 170, chia 5 được 34. Nếu chỉ đổi 80 thành 800, Mean tăng lên 178. Một điểm thay đổi rất lớn có thể kéo Mean đi xa phần đông quan sát.

Tổng quát, một giá trị tăng delta thì Mean tăng delta chia n. Đây là lý do cần xem đuôi và các điểm cực đoan khi dùng Mean. Tuổi 80 vẫn có thể là quan sát hợp lệ.

**Thuật ngữ để chuẩn bị**

- **Mean** là trung bình cộng trên các giá trị quan sát hợp lệ.
- **$n$** là số giá trị có mặt, thay vì tổng số hàng gồm cả ô thiếu.
- **Độ nhạy với ngoại lệ** thể hiện qua việc thay một giá trị thêm $\Delta$ làm Mean đổi $\Delta/n$.

**Chuyển tiếp**

Tiếp theo là median — trung vị.

## 5. Median — Trung vị (03:50–04:40)

**Mục tiêu**

Giải thích nội dung median — trung vị trong lựa chọn giá trị điền.

**Chỉ hình**

Công thức n lẻ, n chẵn và hai ví dụ.

**Công thức và lưu ý để chuẩn bị**

Sau khi sắp xếp $x_{(1)}\le\ldots\le x_{(n)}$,
\[
\tilde{x}=\begin{cases}
x_{((n+1)/2)}, & n\text{ lẻ},\\
(x_{(n/2)}+x_{(n/2+1)})/2, & n\text{ chẵn}.
\end{cases}
\]
Trên slide, $x[k]$ là giá trị ở vị trí k sau khi sắp xếp.

**Lời thoại**

Để tính Median, sắp xếp tăng dần. Nếu n lẻ, lấy giá trị ở vị trí n cộng 1 rồi chia 2. Với n chẵn và dữ liệu định lượng, lấy trung bình hai số giữa.

Năm tuổi cho Median bằng 23. Nếu chỉ có 20, 22, 23, 25, Median bằng 22,5. Đổi 80 thành 800 vẫn giữ vị trí giữa của mẫu năm tuổi là 23.

Đó là tính robust, tức bền hơn Mean trước một vài điểm cực đoan. Median mô tả vị trí theo thứ hạng, còn chất lượng điền vẫn phụ thuộc mục tiêu và cơ chế thiếu.

**Thuật ngữ để chuẩn bị**

- **Median** là vị trí giữa theo thứ hạng sau khi sắp xếp.
- **Robust** nghĩa là ít bị ảnh hưởng bởi một số thay đổi cực đoan.
- **Mẫu chẵn** có hai vị trí giữa. Trung bình hai giá trị này là quy ước cho dữ liệu định lượng.

**Chuyển tiếp**

Tiếp theo là mode — mốt.

## 6. Mode — Mốt (04:40–05:30)

**Mục tiêu**

Giải thích nội dung mode — mốt trong lựa chọn giá trị điền.

**Chỉ hình**

Công thức Count, ví dụ một Mode và hai Mode.

**Công thức và lưu ý để chuẩn bị**

\[
\operatorname{Modes}(X)=\operatorname*{arg\,max}_v\operatorname{Count}(v).
\]
Một Mode là một phần tử của tập nghiệm. Nhãn được mã hóa bằng số vẫn cần xem thang đo trước khi lấy trung bình.

**Lời thoại**

Mode là giá trị xuất hiện nhiều nhất. Mình đếm tần suất rồi chọn giá trị có số đếm cao nhất. Nó hữu ích với nhãn như nhóm máu, sản phẩm, chuyên ngành hoặc người giám hộ.

Với Size trên hình, M xuất hiện ba lần nên là Mode. Dãy 2, 2, 3, 8, 8 có hai Mode 2 và 8. Mean bằng 4,6, Median bằng 3. Khi buộc chọn một Mode, SimpleImputer chọn giá trị nhỏ nhất, tức là 2.

Nếu mọi giá trị chỉ xuất hiện một lần, phép đếm chưa cho Mode duy nhất. Với biến liên tục, cần phân biệt đếm trùng với ước lượng đỉnh mật độ.

**Thuật ngữ để chuẩn bị**

- **Mode** là giá trị có tần suất cao nhất.
- **Đa mốt** có nhiều giá trị đồng tần suất cực đại.
- **Mode duy nhất** cần một giá trị có tần suất cao hơn mọi giá trị khác.
- **Nhãn danh nghĩa** có mã số nhưng khoảng cách giữa các mã cần cơ sở riêng trước khi tính trung bình.

**Chuyển tiếp**

Tiếp theo là vì sao dùng các thống kê để điền khuyết?.

## 7. Vì sao dùng các thống kê để điền khuyết? (05:30–06:45)

**Mục tiêu**

Giải thích nội dung vì sao dùng các thống kê để điền khuyết? trong lựa chọn giá trị điền.

**Chỉ hình**

Bảng ba loại mất mát và ba công thức argmin.

**Công thức và lưu ý để chuẩn bị**

\[
\bar{x}=\operatorname*{arg\,min}_a\sum_i(x_i-a)^2,\qquad
\tilde{x}\in\operatorname*{arg\,min}_a\sum_i|x_i-a|,
\]
\[
x_{\mathrm{mode}}\in\operatorname*{arg\,min}_a\sum_i\mathbf{1}(x_i\ne a).
\]
Mean có thể chứng minh bằng $\sum_i(x_i-a)^2=\sum_i(x_i-\bar{x})^2+n(a-\bar{x})^2$.

Mode có thể chứng minh bằng $\sum_i\mathbf{1}(x_i\ne a)=n-\operatorname{Count}(a)$. Chi tiết chứng minh trong tài liệu lý thuyết.

**Lời thoại**

Khi dự đoán bằng một hằng số cho mọi ô thiếu, mình cần xác định mức phạt khi sai. Nếu phạt bằng bình phương, Mean làm tổng mức phạt nhỏ nhất. Nếu dùng trị tuyệt đối, Median là một nghiệm tối ưu. Nếu đếm nhãn đúng hoặc sai, Mode giảm số lần sai.

Argmin nghĩa là tìm a làm biểu thức phía sau nhỏ nhất. Với Median và Mode, ký hiệu thuộc cho phép nhiều nghiệm. Chẳng hạn ở mẫu chẵn, cả khoảng giữa hai số giữa đều tối ưu tổng sai số tuyệt đối.

Vì vậy lựa chọn còn tùy cách đánh giá. MSE và RMSE cùng có lợi thế lý thuyết cho Mean trong phạm vi dự đoán hằng số. MAE tương ứng với Median, Accuracy tương ứng với Mode khi chi phí sai giữa các lớp bằng nhau. Để dùng cho ô chưa biết, cần kiểm tra phân phối mà ô ấy đến từ.

**Thuật ngữ để chuẩn bị**

- **Mean** là $\bar{x}=\sum_i x_i/n$.
- **Median** là giá trị giữa theo thứ hạng. Với mẫu số chẵn, trung bình hai số giữa là một quy ước. Mọi số giữa hai giá trị ấy đều tối ưu tổng sai số tuyệt đối.
- **Mode** là giá trị có tần suất cực đại. Nhiều Mode có thể đồng hạng.
- **Hàm mất mát** quy định mức phạt khi dự đoán sai. **MSE** là trung bình bình phương sai số. **MAE** là trung bình trị tuyệt đối. **RMSE** bằng căn MSE.
- **Mất mát 0–1** phạt 0 nếu nhãn đúng, 1 nếu nhãn sai.
- **Nhãn thứ bậc** như S < M < L có thứ tự. Median theo hạng cần quy tắc rõ, còn Mean của mã số tùy ý cần cơ sở về khoảng cách.
- **Quy tắc hòa** của SimpleImputer most_frequent chọn giá trị nhỏ nhất trong các Mode.

**Chuyển tiếp**

Tiếp theo là từ phần quan sát đến ô bị thiếu.

## 8. Từ phần quan sát đến ô bị thiếu (06:45–07:35)

**Mục tiêu**

Giải thích nội dung từ phần quan sát đến ô bị thiếu trong lựa chọn giá trị điền.

**Chỉ hình**

Hai đường sai số tuổi và giả định đại diện.

**Lời thoại**

Hai đường này chấm các giá trị c trên năm tuổi đã biết. MAE nhỏ nhất tại 23, RMSE nhỏ nhất tại 34. Tuổi thật ở NaN vẫn chưa biết.

Muốn dùng thống kê cho ô thiếu, phần quan sát phải đại diện phù hợp cho phần bị thiếu hoặc nhóm tương ứng. MCAR là thiếu độc lập với giá trị, thuận lợi cho tính đại diện theo thiết kế.

Nếu thiếu liên quan biến đã quan sát, cần xem phân phối có điều kiện. Nếu còn liên quan phần chưa quan sát, cần thêm giả định. Phân phối, cơ chế thiếu và mục tiêu sai số cùng tham gia quyết định.

**Thuật ngữ để chuẩn bị**

- **Dự đoán hằng số** dùng cùng một số cho mọi ô thiếu trong cột.
- **Phân phối quan sát** mô tả các giá trị đã ghi nhận và tần suất của chúng.
- **Tính đại diện** nghĩa là phần quan sát phù hợp với đối tượng cần dự đoán theo các đặc điểm đang dùng.
- **Bất định** là mức chưa biết về giá trị thật. Một con số dự đoán chưa biểu diễn đầy đủ mức này.
- **Robust — bền vững** mô tả mức ít nhạy của thống kê với một số thay đổi cực đoan.

**Chuyển tiếp**

Tiếp theo là kiểm chứng trên student performance.

## 9. Kiểm chứng trên Student Performance (07:35–08:45)

**Mục tiêu**

Giải thích nội dung kiểm chứng trên student performance trong lựa chọn giá trị điền.

**Chỉ hình**

Histogram, boxplot và thiết kế train/test.

**Lời thoại**

Mình dùng 649 dòng môn tiếng Bồ Đào Nha trong Student Performance của UCI. Bốn cột là G1, absences, guardian và G3. Trường được giữ đầy đủ để thử theo nhóm.

Trong demo, G1 có Mean 11,35, Median 11 và skewness 0,01. Absences có Mean 3,71, Median 2, skewness 2,08. Histogram và boxplot cho thấy vùng trung tâm G1 khá cân đối, số buổi vắng có đuôi phải.

Bản gốc đầy đủ nên mình giữ giá trị thật rồi che thử. Benchmark chia 486 dòng train, 163 dòng test trước khi che. Chỉ học thống kê từ train, áp lên test và chấm ô test bị che. Các phương pháp dùng chung mặt nạ, lặp 12 lần tại mỗi mức 5%, 15%, 30%.

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

Tiếp theo là cùng dữ liệu, khác mục tiêu sai số.

## 10. Cùng dữ liệu, khác mục tiêu sai số (08:45–10:00)

**Mục tiêu**

Giải thích nội dung cùng dữ liệu, khác mục tiêu sai số trong lựa chọn giá trị điền.

**Chỉ hình**

Hai nhóm cột sai số và số lần thắng theo cặp.

**Lời thoại**

Với absences ở mức 15%, Median có MAE 2,52 buổi, thấp hơn 2,83 của Mean. Nhưng Mean có RMSE 3,69, thấp hơn 3,86 của Median.

Median gần vùng phổ biến, phù hợp với sai số tuyệt đối. Trong RMSE, sai số lớn bị bình phương. Mean dịch về phía đuôi có thể giảm một phần lỗi ở ô có số buổi vắng cao. Kết quả test này phù hợp với cách giải thích theo tổn thất.

Theo từng mặt nạ, Median có MAE thấp hơn 10 trong 12 lần, có một lần hòa. Mean có RMSE thấp hơn 11 lần. Với guardian, Mode chọn mother, Accuracy trung bình 68,87%. Mình đọc đúng metric, độ lớn cải thiện và phạm vi thực nghiệm.

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

Tiếp theo là giá trị điền làm đổi phân phối.

## 11. Giá trị điền làm đổi phân phối (10:00–11:00)

**Mục tiêu**

Giải thích nội dung giá trị điền làm đổi phân phối trong lựa chọn giá trị điền.

**Chỉ hình**

Histogram trước/sau và tỷ trọng mother.

**Công thức và lưu ý để chuẩn bị**

Với $n$ quan sát và $m$ ô điền Mean quan sát, $s^2_{sau}=s^2_{quan\ sát}(n-1)/(n+m-1)$. Một lần che có thể có diễn biến tương quan khác xu hướng trung bình.

**Lời thoại**

Điền Median làm tần suất ở 2 buổi vắng tăng. Điền Mean thêm cụm tại khoảng 3,71. Các ô được điền mất sự khác nhau vốn có.

Điền Mean của phần quan sát giữ nguyên Mean. Các ô thêm vào có độ lệch bằng 0, tổng bình phương độ lệch giữ nguyên nhưng mẫu số phương sai tăng. SD absences giảm từ 4,66 xuống 4,31.

Với guardian, tỷ trọng mother tăng từ 70,3% lên 74,6%. Các ô father và other bị che nhận sai nhãn. Quan hệ giữa biến cũng có thể đổi. Qua 300 mặt nạ 15%, tương quan G3–GP sau điền Mean trung bình là 0,264, so với 0,284 của bản đầy đủ.

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

Tiếp theo là khi một giá trị chung chưa đủ.

## 12. Khi một giá trị chung chưa đủ (11:00–12:00)

**Mục tiêu**

Giải thích nội dung khi một giá trị chung chưa đủ trong lựa chọn giá trị điền.

**Chỉ hình**

G3 theo trường, bảng test và nhóm điểm 0.

**Lời thoại**

Nếu biết trường, mình có thể học Median G3 riêng từng trường trên train. Ở 15%, MAE từ 2,42 xuống 2,35, nhưng RMSE từ 3,17 lên 3,19. Lợi ích còn tùy mục tiêu sai số.

EDA thấy 15 dòng G3 bằng 0, gồm 14 dòng MS. UCI ghi miền điểm 0–20 nên mình giữ chúng. Thử loại rồi chia lại cho MAE Median chung 2,193 và theo trường 2,197. Kết quả nhạy với thành phần mẫu.

Cách lọc cũng đổi tập đối tượng và lần chia, nên cần tìm hiểu thêm trước khi gán nguyên nhân. Dùng theo nhóm cần cột nhóm có sẵn, đủ quan sát và thống kê dự phòng.

**Thuật ngữ để chuẩn bị**

- **Dự đoán có điều kiện** dùng thêm thông tin như trường của học sinh.
- **Group-wise imputation** học thống kê riêng cho từng nhóm trên train.
- **Fallback** là thống kê dự phòng khi nhóm chưa gặp hoặc thiếu quan sát. Project dùng Median train toàn cục cho nhóm dưới 20 quan sát.
- **Sensitivity analysis — phân tích độ nhạy** đổi một điều kiện rồi xem kết quả thay đổi thế nào.
- **Điểm G3 bằng 0** thuộc miền điểm UCI công bố. Chưa có hồ sơ xác nhận từng dòng là bỏ thi, nghỉ học hay mã thiếu.
- **Thay đổi tập đối tượng** xảy ra khi loại các dòng G3 bằng 0. Chia lại và tạo mặt nạ trên mẫu mới cũng thay đổi dữ liệu benchmark.

**Chuyển tiếp**

Tiếp theo là trở lại ô tuổi bị thiếu.

## 13. Trở lại ô tuổi bị thiếu (12:00–13:00)

**Mục tiêu**

Giải thích nội dung trở lại ô tuổi bị thiếu trong lựa chọn giá trị điền.

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

Dành hai phút còn lại cho hỏi đáp.

## Hỏi đáp (13:00–15:00)

Mở [lý thuyết đầy đủ](ly_thuyet.md), [script có thuật ngữ](script_va_thuat_ngu.md) và [câu hỏi phản biện](questions_answers.md).

## Phụ lục lý thuyết đầy đủ

### Phân phối dữ liệu và thước đo xu hướng trung tâm

Tài liệu học sâu đi kèm seminar. Phần I giải thích cách đọc phân phối. Phần II trình bày đầy đủ định nghĩa và cơ sở toán học dùng Mean, Median, Mode làm giá trị điền. Những phần chứng minh chi tiết dùng để chuẩn bị hỏi đáp.

#### I. Phân phối dữ liệu (Data Distribution)

Phân phối mô tả các giá trị xuất hiện ở đâu và phổ biến đến mức nào. Khi dùng một thống kê để điền cả cột, cần hiểu thống kê đó đại diện cho vùng nào của phân phối.

##### 1. Phân phối đối xứng (Symmetric Distribution)

Hai phía quanh tâm có hình dạng đối xứng. Với phân phối đối xứng, một đỉnh duy nhất tại tâm, Mean tồn tại và Median xác định tại tâm, ta có ba tâm trùng nhau ở mức tổng thể. Trong một mẫu hữu hạn, thường thấy

\[
\operatorname{Mean}\approx\operatorname{Median}\approx\operatorname{Mode}.
\]

Mean là lựa chọn đáng thử nếu dữ liệu định lượng, phần quan sát đại diện phù hợp, ít điểm cực đoan nghiêm trọng và mục tiêu liên quan sai số bình phương. Phân phối đối xứng còn có thể là tam giác hoặc nhiều dạng khác. Đối xứng riêng nó chưa bảo đảm Mean tồn tại, chẳng hạn với Cauchy. [NIST, Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm)

##### 2. Phân phối lệch phải (Right-skewed Distribution)

Đuôi kéo về phía các giá trị lớn. Thu nhập, giá nhà hoặc chi phí y tế có thể xuất hiện dạng này tùy mẫu và phạm vi khảo sát. Trong dạng một đỉnh điển hình được minh họa bằng Gamma, thường thấy

\[
\operatorname{Mode}<\operatorname{Median}<\operatorname{Mean}.
\]

Mean dùng độ lớn của mọi điểm nên một số giá trị rất lớn có thể kéo nó về đuôi. Median dựa trên thứ hạng nên thường gần vùng phổ biến hơn.

##### 3. Phân phối lệch trái (Left-skewed Distribution)

Đuôi kéo về phía các giá trị nhỏ. Một bài kiểm tra dễ có nhiều điểm cao và một số ít điểm rất thấp có thể cho hình dạng này. Với ví dụ Gamma phản chiếu,

\[
\operatorname{Mean}<\operatorname{Median}<\operatorname{Mode}.
\]

Các giá trị nhỏ ở đuôi có thể kéo Mean xuống. Ba thứ tự trên là quan hệ của các dạng minh họa thường gặp. Một đỉnh tự nó chưa bảo đảm thứ tự ấy cho mọi phân phối.

##### 4. Skewness và Outliers

**Skewness** là hệ số bất đối xứng. Một dạng Fisher–Pearson dùng moment bậc ba chuẩn hóa,

\[
g_1=\frac{\frac{1}{n}\sum_i(x_i-\bar{x})^3}
{\left(\frac{1}{n}\sum_i(x_i-\bar{x})^2\right)^{3/2}}.
\]

pandas `skew()` dùng hệ số đã hiệu chỉnh theo cỡ mẫu. Công thức trên cần độ phân tán khác 0.

| Skewness | Cách đọc và kiểm tra |
|---|---|
| Gần 0 | Ít bất đối xứng theo moment bậc ba. Xem histogram để kiểm tra hình dạng, nhiều đỉnh và đuôi |
| Dương | Thường có xu hướng lệch phải |
| Âm | Thường có xu hướng lệch trái |

Skewness gần 0 chưa đủ suy ra đối xứng hoặc chuẩn. Các thành phần của moment có thể bù nhau. Chọn phương pháp cần kết hợp histogram, boxplot, miền giá trị và cách thu thập dữ liệu. Ngưỡng skewness phù hợp phụ thuộc bối cảnh. [NIST, Skewness and Kurtosis](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm)

**Outlier** là quan sát khác biệt đáng kể so với cấu trúc thường gặp. Một cách gắn cờ dùng khoảng tứ phân vị,

\[
IQR=Q_3-Q_1.
\]

Điểm ngoài hàng rào

\[
[Q_1-1.5IQR,\ Q_3+1.5IQR]
\]

được đánh dấu để kiểm tra. Trong demo absences, Q1 = 0, Q3 = 6 và IQR = 6. Hai hàng rào là −9 và 15 buổi, có 18 điểm lớn hơn 15 bị gắn cờ. Giá trị vắng 0 buổi được giữ như quan sát hợp lệ.

Hàng rào gắn cờ ứng viên ngoại lệ. Cần kiểm tra nguyên nhân và ảnh hưởng trước khi sửa hoặc xóa. Râu boxplot thường dừng ở quan sát xa nhất còn nằm trong hàng rào, nên vị trí râu có thể khác vị trí hàng rào. [NIST, Detection of Outliers](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm)

#### II. Thước đo xu hướng trung tâm (Measures of Central Tendency)

##### 1. Mean — trung bình cộng

Với $n$ giá trị định lượng quan sát hợp lệ $X=\{x_1,\ldots,x_n\}$,

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i.
\]

Mean dùng độ lớn của toàn bộ giá trị. Nếu một quan sát tăng thêm $\Delta$, Mean tăng thêm $\Delta/n$, nên dễ bị ảnh hưởng bởi điểm cực đoan.

Với mẫu tuổi [20, 22, 23, 25, 80], Mean = 170/5 = 34. Nếu đổi 80 thành 800, Mean thành 890/5 = 178. Việc Mean thay đổi mạnh phản ánh độ nhạy của phép tổng. Tuổi 80 vẫn có thể là dữ liệu hợp lệ.

##### 2. Median — trung vị

Sắp xếp tăng dần thành $x_{(1)}\le\ldots\le x_{(n)}$. Với biến định lượng,

\[
\tilde{x}=
\begin{cases}
x_{((n+1)/2)}, & n\text{ lẻ},\\
\frac{x_{(n/2)}+x_{(n/2+1)}}{2}, & n\text{ chẵn}.
\end{cases}
\]

Với mẫu tuổi năm số, Median là số thứ ba, bằng 23. Với [20, 22, 23, 25], Median = (22 + 23)/2 = 22,5.

Median có tính **robust**, tức ít nhạy hơn với một vài điểm cực đoan. Đổi 80 thành 800 giữ Median bằng 23 vì hai giá trị đều đứng cuối và thứ hạng ở giữa giữ nguyên. Median vẫn phụ thuộc vào thành phần mẫu và cơ chế thiếu.

##### 3. Mode — mốt

Tập các giá trị có tần suất cực đại được viết

\[
\operatorname{Modes}(X)=\operatorname*{arg\,max}_v\operatorname{Count}(v).
\]

Nếu nghiệm duy nhất, gọi giá trị ấy là Mode. Mode phù hợp với nhãn loại như nhóm máu, loại sản phẩm, chuyên ngành hoặc người giám hộ.

- [M, M, L, S, M] có Mode M, xuất hiện ba lần.
- [2, 2, 3, 8, 8] có hai Mode 2 và 8. Mean bằng 4,6 và Median bằng 3.
- Nếu mọi giá trị xuất hiện một lần, phép đếm chưa cho một Mode duy nhất. Với biến liên tục, đỉnh mật độ hoặc khoảng histogram phổ biến là cách mô tả khác, phụ thuộc lựa chọn ước lượng.

Cần công bố cách phân xử khi hòa. `SimpleImputer(strategy="most_frequent")` chọn giá trị nhỏ nhất trong các giá trị đồng mốt. Mã số của nhãn danh nghĩa vẫn cần được xem là nhãn, thay vì tự động lấy trung bình. [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)

##### 4. Vì sao ba thống kê dùng được để điền khuyết?

Khi chỉ dự đoán cùng một hằng số $a$ cho cột, cần xác định mức phạt cho sai số. Ba thống kê giải ba bài toán tối ưu khác nhau.

| Thước đo | Tiêu chí | Ý nghĩa |
|---|---|---|
| Mean | Sai số bình phương | Giảm tổng bình phương độ lệch |
| Median | Sai số tuyệt đối | Giảm tổng khoảng cách tuyệt đối |
| Mode | Sai số nhãn 0–1 | Giảm số lần đoán sai với dự đoán cố định |

**Mean tối thiểu hóa tổng sai số bình phương.**

\[
\bar{x}=\operatorname*{arg\,min}_{a\in\mathbb R}\sum_i(x_i-a)^2.
\]

Có thể chứng minh bằng

\[
\sum_i(x_i-a)^2=\sum_i(x_i-\bar{x})^2+n(a-\bar{x})^2.
\]

Vế đầu độc lập với $a$, vế sau nhỏ nhất khi $a=\bar{x}$. Chia cho $n$ hoặc lấy căn sau khi chia đều giữ nguyên điểm tối ưu, nên kết quả áp dụng cho MSE và RMSE.

**Median tối thiểu hóa tổng sai số tuyệt đối.**

\[
\tilde{x}\in\operatorname*{arg\,min}_{a\in\mathbb R}\sum_i|x_i-a|.
\]

Dịch $a$ sang phải làm khoảng cách với điểm bên trái tăng và với điểm bên phải giảm. Tổng nhỏ nhất tại vị trí cân bằng số điểm hai phía theo nghĩa trung vị. Với $n$ chẵn, cả khoảng giữa hai số giữa đều là nghiệm. Trung bình hai số giữa là một lựa chọn, vì vậy công thức dùng ký hiệu thuộc tập nghiệm.

**Mode tối thiểu hóa số lần đoán sai.**

\[
x_{\mathrm{mode}}\in\operatorname*{arg\,min}_a\sum_i\mathbf{1}(x_i\ne a).
\]

Vì $\sum_i\mathbf{1}(x_i\ne a)=n-\operatorname{Count}(a)$, chọn nhãn xuất hiện nhiều nhất làm số lần sai nhỏ nhất. Có thể có nhiều nghiệm đồng hạng.

##### 5. Từ tối ưu trên mẫu đến ước lượng giá trị bị thiếu

Các kết quả trên chứng minh tối ưu trong phạm vi **một dự đoán hằng số trên tập dùng để tối ưu**. Khi dùng cho ô thiếu, Mean/Median/Mode từ phần quan sát là ước lượng cho các đại lượng tương ứng của phân phối cần dự đoán.

Cần giả định phần quan sát đủ đại diện cho phần thiếu hoặc nhóm đang xét. MCAR là điều kiện thuận lợi theo cơ chế che. Với các quan hệ có điều kiện, có thể cần thống kê theo nhóm hoặc phương pháp dùng thêm biến. Tối ưu trên train chưa bảo đảm thứ hạng trên mọi test.

Ở mẫu tuổi, MAE trên năm số đã quan sát nhỏ nhất tại 23 và RMSE nhỏ nhất tại 34. Tuổi thật ở ô NaN vẫn chưa biết. Trên absences của Student Performance, benchmark MCAR 15% cho MAE Median = 2,52 và Mean = 2,83, nhưng RMSE Mean = 3,69 và Median = 3,86. Các kết quả này minh họa vai trò của hàm mất mát khi lựa chọn phương pháp.

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
