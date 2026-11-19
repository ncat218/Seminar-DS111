# Lời thoại seminar DS111

13 slide, 13 phút trình bày và 2 phút hỏi đáp. Phần I gồm phân phối, skewness và ngoại lệ. Phần II gồm các thước đo và cơ sở tối ưu, rồi kiểm chứng bằng thực nghiệm.

## 1. Nên điền 23 hay 34? (00:00–00:45)

**Mục tiêu**

Giải thích nội dung nên điền 23 hay 34? trong lựa chọn giá trị điền.

**Chỉ hình**

Dãy tuổi và ba câu hỏi xuyên suốt.

**Lời thoại**

Xin chào thầy và tất cả các bạn đến với mini seminar hôm nay. Mình có cột tuổi gồm 20, 22, 23, 25, 80 và một ô thiếu. Theo các bạn, nên điền 23 là Median hay 34 là Mean? [Dừng hai giây.]

Hôm nay mình tìm hiểu các thước đo xu hướng trung tâm để điền khuyết. Bài trả lời ba câu hỏi. Vì sao giá trị đại diện có thể ước lượng ô thiếu? Khi nào thay thế hợp lý? Và nó làm dữ liệu sai lệch ra sao? Trước hết, ta cần hiểu phân phối và cách thống kê mô tả nó.

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

**Chuyển tiếp**

Dành hai phút còn lại cho hỏi đáp.

## Hỏi đáp (13:00–15:00)

Mở [lý thuyết đầy đủ](ly_thuyet.md), [script có thuật ngữ](script_va_thuat_ngu.md) và [câu hỏi phản biện](questions_answers.md).
