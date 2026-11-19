# Lời thoại seminar DS111

24 slide, khoảng 25 phút trình bày. Bản đầy đủ để giải thích sâu; [lộ trình 15 phút](lo_trinh_15phut.md) chọn 13 slide để nói trong 13 phút và dành 2 phút hỏi đáp.

## 1. Nên điền 23 hay 34? (00:00–01:00)

**Mục tiêu**

Giải thích nội dung nên điền 23 hay 34? trong lựa chọn giá trị điền.

**Chỉ hình**

Dãy tuổi và ba câu hỏi xuyên suốt.

**Lời thoại**

Xin chào thầy và tất cả các bạn đến với mini seminar hôm nay. Mình có cột tuổi gồm 20, 22, 23, 25, 80 và một ô thiếu. Theo các bạn, nên điền 23 là Median hay 34 là Mean? [Dừng hai giây.]

Hôm nay mình tìm hiểu các thước đo xu hướng trung tâm để điền khuyết. Bài trả lời ba câu hỏi. Vì sao giá trị đại diện có thể ước lượng ô thiếu? Khi nào thay thế hợp lý? Và nó làm dữ liệu sai lệch ra sao? Trước hết, ta cần hiểu phân phối và cách thống kê mô tả nó.

**Chuyển tiếp**

Tiếp theo là phân phối dữ liệu.

## 2. Phân phối dữ liệu (01:00–02:00)

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

## 4. Mean — Trung bình cộng (03:00–04:00)

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

## 5. Median — Trung vị (04:00–05:00)

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

## 6. Mode — Mốt (05:00–06:00)

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

## 7. Điền khuyết là ước lượng điều gì? (06:00–07:00)

**Mục tiêu**

Điền khuyết là ước lượng điều gì?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

$a^*\in\arg\min_a E[L(X,a)\mid M=0]$ là đích; $\hat a\in\arg\min_a\sum_{i:M_i=1}L(x_i,a)$ là ước lượng từ phần quan sát. Dưới MCAR, $F_{X\mid M=0}=F_{X\mid M=1}$. Nếu có thông tin nhóm, xét phân phối có điều kiện phù hợp.

**Lời thoại**

Khi một ô tuổi thiếu, tuổi thật của người đó chưa biết. Nếu chỉ cho phép điền một hằng số cho mọi người thiếu, ta cần định nghĩa thế nào là điền tốt. Ký hiệu L là mức phạt khi dùng a thay cho X. M bằng 1 nghĩa là quan sát được, M bằng 0 nghĩa là thiếu. Công thức đầu tiên chọn a để mức phạt trung bình trên phần thiếu nhỏ nhất.

Khó khăn là mình không biết X ở phần thiếu để tính mức phạt đó. Vì vậy mình học a từ những giá trị quan sát được, như công thức thứ hai. Bước chuyển này cần một giả định: phần quan sát phải cung cấp thông tin phù hợp về phần thiếu. Trong MCAR, hai phần có cùng phân phối theo cơ chế che, nhưng thống kê từ mẫu vẫn có sai số.

Vì vậy có hai câu hỏi riêng. Một là tối ưu theo loại sai số nào? Hai là mẫu đang quan sát có đại diện cho đối tượng bị thiếu hay không? Ba công thức tiếp theo trả lời câu hỏi thứ nhất.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 8. Vì sao Mean tối ưu sai số bình phương? (07:00–08:30)

**Mục tiêu**

Vì sao Mean tối ưu sai số bình phương?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

$E[(X-a)^2]=\operatorname{Var}(X)+(\mu-a)^2$. Trên mẫu: $f'(a)=2na-2\sum x_i$ và $f''(a)=2n>0$. Nghiệm là $\bar x$. RMSE là căn của MSE nên có cùng nghiệm trên cùng tập dự đoán.

**Lời thoại**

Bắt đầu với Mean. Mình gọi mu là trung bình của phân phối và giả sử moment bậc hai hữu hạn. Khi khai triển bình phương X trừ a, rồi lấy kỳ vọng, kết quả tách thành phương sai cộng với bình phương khoảng cách từ a đến mu. Số hạng chéo bằng 0 vì kỳ vọng của X trừ mu bằng 0.

Phương sai là một đặc điểm của phân phối, không đổi theo a. Phần mình điều khiển được là bình phương mu trừ a, nhỏ nhất bằng 0 khi a bằng mu. Do đó Mean là hằng số tốt nhất nếu đánh giá bằng sai số bình phương. Trên mẫu quan sát, lấy đạo hàm tổng bình phương sai số cũng cho a bằng tổng các giá trị chia n.

Nhưng hãy nhìn lại phần phương sai: ngay cả lựa chọn tối ưu vẫn để lại sai số. Điền 34 trong ví dụ tuổi có cơ sở theo tiêu chí bình phương trên phân phối quan sát; công thức không nói tuổi thật của người thiếu là 34. Phân biệt này rất quan trọng khi giải thích ý nghĩa của điền khuyết.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 9. Vì sao Median tối ưu sai số tuyệt đối? (08:30–10:00)

**Mục tiêu**

Vì sao Median tối ưu sai số tuyệt đối?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Ở vị trí không trùng quan sát, $g'(a)=\#\{x_i<a\}-\#\{x_i>a\}$. Median $m$ thỏa $P(X\le m)\ge1/2$ và $P(X\ge m)\ge1/2$. Nếu E|X| hữu hạn và phân phối liên tục thích hợp, đạo hàm rủi ro là $2F(a)-1$.

**Lời thoại**

Với Median, mức phạt là khoảng cách tuyệt đối. Hãy tưởng tượng đặt một điểm a trên trục số rồi cộng khoảng cách từ a đến mọi quan sát.

Khi dịch a sang phải một chút và không đi qua quan sát nào, mỗi điểm ở bên trái làm tổng khoảng cách tăng. Mỗi điểm bên phải làm tổng giảm. Nếu còn nhiều điểm bên phải hơn, dịch phải làm tổng nhỏ đi. Khi đến vùng cân bằng giữa hai phía, mình không thể giảm tổng bằng cách dịch tiếp theo một hướng. Đó là vùng trung vị.

Với số phần tử chẵn, mọi điểm giữa hai giá trị giữa đều có thể tối ưu; lấy trung bình hai số là quy ước. Với phân phối rời rạc có nhiều giá trị bằng nhau, mình dùng hai bất đẳng thức trên slide: ít nhất nửa khối xác suất ở mỗi phía tính cả điểm trung vị.

Đây cũng là lý do Median ít nhạy với độ lớn của một điểm cực đoan. Độ dốc phụ thuộc số điểm ở mỗi phía; Mean chịu thêm tác động của độ lớn khoảng cách vì bình phương sai số. Vì vậy Median thích hợp cho dự đoán hằng số dưới sai số tuyệt đối, với giả định đại diện phù hợp.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 10. Vì sao Mode tối ưu số lần đoán sai? (10:00–11:00)

**Mục tiêu**

Vì sao Mode tối ưu số lần đoán sai?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

$\sum_i\mathbf1(x_i\ne a)=n-\operatorname{Count}(a)$; $E[\mathbf1(X\ne a)]=1-P(X=a)$. Nhãn đồng tần suất cực đại cùng tối ưu. Dùng nhãn rời rạc và chi phí sai bằng nhau.

**Lời thoại**

Với biến loại, khoảng cách số học giữa hai nhãn thường không có ý nghĩa. Mình phạt 0 nếu nhãn điền đúng và phạt 1 nếu sai. Giả sử điền cùng nhãn a cho n quan sát: số lần sai bằng n trừ số lần nhãn a thực sự xuất hiện.

Muốn số sai nhỏ nhất, mình chọn nhãn có số đếm lớn nhất, chính là Mode. Trong ví dụ M, M, L, S, M, điền M thì sai hai lần. Điền L thì sai bốn lần. Với toàn bộ phân phối, xác suất sai bằng 1 trừ xác suất của nhãn được chọn.

Kết luận này dùng chi phí nhầm bằng nhau. Nếu bỏ sót một lớp hiếm gây thiệt hại lớn hơn, mình cần hàm chi phí khác. Accuracy cao khi luôn điền nhãn đa số cũng không có nghĩa đã phục hồi được các lớp hiếm. Chút nữa guardian sẽ cho thấy tần suất nhãn đa số còn tăng sau khi điền.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 11. Vì sao dùng các thống kê để điền khuyết? (11:00–12:00)

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

## 12. Từ phần quan sát đến ô bị thiếu (12:00–13:00)

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

## 13. Kiểm chứng trên Student Performance (13:00–14:00)

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

## 14. Hai mức đánh giá điền khuyết (14:00–15:00)

**Mục tiêu**

Hai mức đánh giá điền khuyết.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Với một mô hình tuyến tính cố định, khi riêng đặc trưng j được thay, $\Delta\hat y=\beta_j(\hat a_j-x_j)$. Đồng nhất thức này không mô tả đầy đủ việc huấn luyện lại.

**Lời thoại**

Sau phần toán, mình cần phân biệt hai thí nghiệm. Thí nghiệm một hỏi: mình điền ô bị che gần giá trị thật đến đâu? Khi đó chỉ chấm những ô test đã che, vì các ô còn nguyên không cần dự đoán.

Thí nghiệm hai hỏi: sau khi xử lý thiếu và huấn luyện, mô hình còn dự đoán điểm G3 tốt đến đâu? Khi đó giữ điểm thật G3 đầy đủ và chấm mọi học sinh test. Giá trị bị điền nằm ở các biến đầu vào.

Hai tiêu chí có liên quan nhưng không đồng nhất. Với một mô hình tuyến tính đã cố định, sai lệch ở đặc trưng j làm dự đoán đổi bằng hệ số beta j nhân sai lệch của đặc trưng đó. Đặc trưng có ảnh hưởng khác nhau sẽ truyền sai số khác nhau. Khi huấn luyện lại, chính các hệ số hoặc các nhánh của cây cũng có thể đổi. Vì vậy histogram và lỗi khôi phục ô chưa trả lời hết tác động đến mô hình.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 15. Cùng dữ liệu, khác mục tiêu sai số (15:00–16:00)

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

## 16. Giá trị điền làm đổi phân phối (16:00–17:00)

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

## 17. Bài toán huấn luyện dự đoán G3 (17:00–18:00)

**Mục tiêu**

Bài toán huấn luyện dự đoán G3.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Số: G1, G2, age, absences. Loại: guardian, school. Khi huấn luyện, G3 là y và không có trong X. Thí nghiệm khôi phục G3 là một thí nghiệm độc lập.

**Lời thoại**

Mình dùng cùng bộ UCI Student Performance môn tiếng Bồ Đào Nha. Đích là G3, điểm cuối kỳ từ 0 đến 20. Sáu đầu vào gồm G1, G2, tuổi, số buổi vắng, người giám hộ và trường học.

G3 được giữ đầy đủ và không nằm trong danh sách đầu vào. Mình che sáu đặc trưng bằng mặt nạ MCAR rồi so sánh ba cách điền cho biến số: Mean, Median và Mode. Cả ba cấu hình đều dùng Mode cho biến loại để giữ cùng cách xử lý phần đó. Các cột số ở đây là điểm hoặc số nguyên, nên Mode có ý nghĩa để làm phép so sánh.

G1 và G2 đã có trước G3 trong bối cảnh này. Bài toán là dự đoán điểm cuối kỳ sau khi có các điểm trước đó. Nếu muốn cảnh báo từ đầu năm, mình cần bỏ G1/G2 rồi chạy lại một bài toán khác. Cách đặt mốc thời gian quyết định dữ liệu nào được phép dùng.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 18. Pipeline huấn luyện và kiểm tra (18:00–19:00)

**Mục tiêu**

Pipeline huấn luyện và kiểm tra.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

$R^2=1-\sum(y_i-\hat y_i)^2/\sum(y_i-\bar y_\mathrm{test})^2$. Mean test chỉ ở định nghĩa metric, không dùng tạo dự đoán. Predict train mean dùng Mean y_train. [Pipeline chống rò rỉ](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage).

**Lời thoại**

Để so sánh công bằng, mình dùng năm lần chia ngẫu nhiên 75 phần trăm train và 25 phần trăm test. Mỗi lần chia có bốn mặt nạ cho từng mức thiếu 5, 15 và 30 phần trăm. Các phương pháp nhận đúng cùng hàng và mặt nạ tương ứng.

Ridge là hồi quy tuyến tính có phạt độ lớn hệ số; mình cố định alpha bằng 1 và chuẩn hóa các biến số sau khi điền. Random Forest lấy trung bình dự đoán của 100 cây, đặt tối thiểu ba mẫu ở một lá. Hai loại mô hình giúp xem tác động trong cách học tuyến tính và cách chia cây.

Mọi thống kê điền, mã hóa nhãn, chuẩn hóa và mô hình đều fit trên train. Test chỉ được transform và dự đoán. Tổng cộng có 360 pipeline train có thiếu và 10 mốc đầy đủ, tức 370 lần fit. Siêu tham số được cố định trước, không chọn bằng điểm test.

Mình báo MAE, RMSE và R bình phương trên G3 thật của toàn bộ 163 dòng test. Các lần chia có chồng lấn nên độ lệch chuẩn mô tả dao động thực nghiệm, không phải khoảng tin cậy từ 20 mẫu độc lập.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 19. Mô hình sau điền thay đổi thế nào? (19:00–20:00)

**Mục tiêu**

Mô hình sau điền thay đổi thế nào?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Bảng lấy tự động từ results/model_evaluation.csv và model_reference.csv. Đây là trung bình RMSE từng lần chạy; không gộp các lần chia chồng lấn thành một test độc lập.

**Lời thoại**

Đây là kết quả đã chạy, ở mức thiếu 15 phần trăm trong cả train và test. Mỗi số là trung bình của 20 tổ hợp chia và che.

Với Ridge, đầu vào đầy đủ cho RMSE khoảng 1,379 điểm. Sau khi có thiếu và điền Mean, RMSE lên 1,728; điền Median là 1,734 và Mode là 1,748. Với Random Forest, mốc đầy đủ là 1,359; ba cách điền lần lượt khoảng 1,614, 1,640 và 1,646.

Như vậy mô hình vẫn dự đoán được, nhưng mất thông tin đầu vào đã làm tăng sai số. Trong thiết kế này, khác biệt giữa ba cách điền nhỏ hơn mức giảm hiệu năng từ đầy đủ sang có thiếu. Mean cho RMSE thấp nhất trong ba cấu hình ở mức này, nhưng chưa phải chứng minh Mean luôn tốt hơn, và mình chưa xác lập ý nghĩa thống kê của chênh lệch.

Trước đó Median có MAE thấp hơn khi khôi phục absences. Ở đây mình chấm G3 của mô hình dùng sáu đặc trưng và thay cách điền nhiều biến số. Hai phép đo không cùng mục tiêu, nên không thể lấy kết luận của một cột áp thẳng cho toàn pipeline.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 20. Ảnh hưởng khi mức thiếu tăng (20:00–21:00)

**Mục tiêu**

Ảnh hưởng khi mức thiếu tăng.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

model_performance.png có Mean ± SD. Với sáu cột che độc lập xác suất p, xác suất một hàng có ít nhất một ô thiếu là 1−(1−p)^6; tại p=0,15 xấp xỉ 62,3% theo thiết kế.

**Lời thoại**

Bây giờ thay vì chỉ nhìn 15 phần trăm, mình tăng xác suất che từ 5 lên 15 rồi 30 phần trăm. Trục dọc là RMSE G3 và đường ngang là mô hình có đầu vào đầy đủ trên cùng các lần chia.

Trong các cấu hình đã chạy, RMSE tăng khi mức thiếu tăng ở cả Ridge và Random Forest. Chẳng hạn với Mean, Ridge từ khoảng 1,543 ở mức 5 phần trăm lên 1,980 ở mức 30 phần trăm. Random Forest từ 1,484 lên 1,890.

Điền đủ ô giúp pipeline chạy được nhưng thông tin cá nhân đã mất chưa được phục hồi bằng một giá trị chung. Các đường của ba phương pháp khá gần nhau. Hình trong notebook có thêm SD để thấy dao động, tránh đọc khoảng cách nhỏ giữa đường trung bình như kết luận chắc chắn.

Mức thiếu là xác suất cho mỗi ô đầu vào. Nó không bằng tỷ lệ học sinh có ít nhất một đặc trưng thiếu; với sáu đặc trưng, tỷ lệ học sinh bị ảnh hưởng có thể lớn hơn.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 21. Thiếu khi học và thiếu khi áp dụng (21:00–22:00)

**Mục tiêu**

Thiếu khi học và thiếu khi áp dụng.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Hai pha chấm mọi dòng test của cùng split. Mốc đầy đủ dùng pipeline tham chiếu khác fit trên train đầy đủ. Không cộng trừ các cột như kết luận nhân quả ngoài thiết kế.

**Lời thoại**

Mình tách thêm hai thời điểm ảnh hưởng. Cột train thiếu nghĩa là pipeline học từ train có ô điền, nhưng kiểm tra trên test đầy đủ. Cột cuối dùng đúng pipeline đã fit đó để dự đoán test cũng có thiếu.

Với Median ở mức 15 phần trăm, RMSE Ridge từ mốc đầy đủ 1,379 lên 1,457 khi chỉ train thiếu, và 1,734 khi test cũng thiếu. Random Forest lần lượt là 1,359, 1,431 và 1,640.

Một phần thay đổi đến từ học trên đặc trưng đã điền, phần khác đến từ không biết đủ thông tin lúc áp dụng. Hai pha test dùng cùng mô hình đã fit nên không có khác biệt do huấn luyện lại giữa hai cột cuối.

Đây là phép đối chiếu có kiểm soát trong bộ dữ liệu và các mặt nạ đang xét, chưa phải phân rã nhân quả phổ quát. Cũng không dùng test đầy đủ để học thống kê điền.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 22. Dự đoán từng học sinh thay đổi ra sao? (22:00–23:00)

**Mục tiêu**

Dự đoán từng học sinh thay đổi ra sao?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

results/model_predictions.csv lưu từng dự đoán với row_id và cấu hình. Đây là ví dụ một lần chạy, không thay trung bình qua 20 tổ hợp.

**Lời thoại**

Trên hình, trục ngang là G3 thật, trục dọc là điểm mô hình dự đoán. Dự đoán chính xác nằm trên đường chéo. Mình lấy ví dụ split 42, mặt nạ 42, thiếu 30 phần trăm và điền Median.

Các điểm của mô hình đầu vào đã điền được so với dự đoán của mô hình đầy đủ. Một số điểm rời xa đường chéo hơn, thể hiện sai số tăng; từng học sinh vẫn có thể được dự đoán tốt hơn hoặc kém hơn. Điền khuyết không làm mọi dự đoán dịch cùng một hướng.

Hình giúp thấy tác động ở mức cá nhân, còn kết luận tổng thể dựa vào bảng qua nhiều lần chạy. Project lưu từng dòng dự đoán, điểm thật và cờ có thiếu đầu vào để kiểm tra lại hoặc chọn ví dụ khi hỏi đáp.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 23. Khi một giá trị chung chưa đủ (23:00–24:00)

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

## 24. Trở lại ô tuổi bị thiếu (24:00–25:00)

**Mục tiêu**

Giải thích nội dung trở lại ô tuổi bị thiếu trong lựa chọn giá trị điền.

**Chỉ hình**

Ba câu trả lời và lựa chọn 23 hay 34.

**Lời thoại**

Trở lại ô tuổi mở đầu, chọn 23 hay 34 phải gắn với mức phạt mình muốn giảm. Mean, Median, Mode có cơ sở tối ưu trong phạm vi một dự đoán hằng số và giả định đại diện phù hợp; chúng không tiết lộ chắc chắn giá trị thật của từng người.

Thực nghiệm trả lời thêm hai mức câu hỏi. Điền hằng số làm đổi phân phối, tăng tần suất tại giá trị điền và có thể đổi liên hệ giữa biến. Khi đưa vào huấn luyện dự đoán G3, cả hai mô hình đều có RMSE tăng so với đầu vào đầy đủ ở thiết kế này. Chọn cách điền còn phải kiểm chứng bằng chỉ tiêu của bài toán sử dụng dữ liệu.

Vì vậy quy trình của mình là xác định kiểu biến và mục tiêu, kiểm tra phân phối cùng cơ chế thiếu, học thống kê từ train, rồi đánh giá cả lỗi khôi phục và hiệu năng mô hình. Nếu cần giữ bất định hay quan hệ phức tạp, hãy thử phương pháp có điều kiện hoặc multiple imputation với giả định phù hợp.

**Chuyển tiếp**

Dành hai phút còn lại cho hỏi đáp.

## Hỏi đáp (25:00–27:00)

Dùng [bộ câu hỏi phản biện](questions_answers.md) và [lý thuyết đầy đủ](ly_thuyet.md) để chuẩn bị.
