# Lời thoại seminar DS111

13 slide, 13 phút trình bày và 2 phút hỏi đáp. Dùng lời thoại rút gọn; công thức và giải thích sâu ở bản đầy đủ.

## 1. Nên điền 23 hay 34? (00:00–00:45)

**Mục tiêu**

Giải thích nội dung nên điền 23 hay 34? trong lựa chọn giá trị điền.

**Chỉ hình**

Dãy tuổi và ba câu hỏi xuyên suốt.

**Lời thoại**

Xin chào thầy và các bạn. Mình có tuổi 20, 22, 23, 25, 80 và một ô thiếu. Nên điền Median 23 hay Mean 34? Mình sẽ trả lời vì sao một giá trị đại diện dùng được, khi nào hợp lý và nó làm dữ liệu thay đổi thế nào. Bài có cả kiểm chứng giá trị điền và huấn luyện dự đoán điểm từ dữ liệu thật.

**Chuyển tiếp**

Tiếp theo là phân phối dữ liệu.

## 2. Phân phối dữ liệu (00:45–01:45)

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

Ở các phân phối minh họa này, đuôi dài kéo Mean về phía đuôi. Median thường ít bị một vài giá trị rất lớn ảnh hưởng. Đối xứng có thể gặp ngoài phân phối chuẩn; thứ tự Mean, Median, Mode trên hình là trường hợp điển hình. Ta xem histogram, boxplot, kiểu biến và mục tiêu sai số cùng nhau. Skewness mô tả bất đối xứng; điểm bị IQR gắn cờ cần kiểm tra nguồn gốc trước khi xử lý.

**Chuyển tiếp**

Tiếp theo là skewness và ngoại lệ.

## 3. Điền khuyết là ước lượng điều gì? (01:45–02:40)

**Mục tiêu**

Điền khuyết là ước lượng điều gì?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

$a^*\in\arg\min_a E[L(X,a)\mid M=0]$ là đích; $\hat a\in\arg\min_a\sum_{i:M_i=1}L(x_i,a)$ là ước lượng từ phần quan sát. Dưới MCAR, $F_{X\mid M=0}=F_{X\mid M=1}$. Nếu có thông tin nhóm, xét phân phối có điều kiện phù hợp.

**Lời thoại**

M bằng 0 nghĩa là thiếu, L là mức phạt cho dự đoán. Mục tiêu là chọn a làm mức phạt trung bình trên phần thiếu nhỏ nhất. Nhưng phần thiếu không có giá trị thật để tính, nên mình học a từ phần quan sát. Cần giả định hai phần có phân phối phù hợp để chuyển kết quả. MCAR giúp điều này theo cơ chế che, dù mẫu hữu hạn vẫn có sai số. Vậy nên chọn hằng số nào tùy cách định nghĩa mức phạt.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 4. Vì sao Mean tối ưu sai số bình phương? (02:40–03:45)

**Mục tiêu**

Vì sao Mean tối ưu sai số bình phương?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

$E[(X-a)^2]=\operatorname{Var}(X)+(\mu-a)^2$. Trên mẫu: $f'(a)=2na-2\sum x_i$ và $f''(a)=2n>0$. Nghiệm là $\bar x$. RMSE là căn của MSE nên có cùng nghiệm trên cùng tập dự đoán.

**Lời thoại**

Nếu mức phạt là bình phương sai số, khai triển rủi ro cho ra phương sai cộng bình phương khoảng cách từ a đến Mean. Phương sai không phụ thuộc a; chọn a bằng Mean làm phần còn lại nhỏ nhất. Trên mẫu, đạo hàm tổng bình phương sai số bằng 0 cũng cho Mean mẫu. Đây là cơ sở dùng Mean dưới tiêu chí MSE hoặc RMSE khi phần quan sát đại diện phù hợp. Phần phương sai vẫn còn: lựa chọn tối ưu không đồng nghĩa khôi phục chắc chắn tuổi thật của một người.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 5. Vì sao Median tối ưu sai số tuyệt đối? (03:45–04:50)

**Mục tiêu**

Vì sao Median tối ưu sai số tuyệt đối?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Ở vị trí không trùng quan sát, $g'(a)=\#\{x_i<a\}-\#\{x_i>a\}$. Median $m$ thỏa $P(X\le m)\ge1/2$ và $P(X\ge m)\ge1/2$. Nếu E|X| hữu hạn và phân phối liên tục thích hợp, đạo hàm rủi ro là $2F(a)-1$.

**Lời thoại**

Nếu mức phạt là trị tuyệt đối, hãy dịch a sang phải trên trục số. Mỗi điểm bên trái làm tổng khoảng cách tăng, mỗi điểm bên phải làm tổng giảm. Tổng nhỏ nhất ở vùng cân bằng hai phía, chính là trung vị. Với mẫu chẵn có thể có một khoảng nghiệm; lấy trung bình hai giá trị giữa là quy ước. Độ dốc phụ thuộc số điểm ở mỗi phía nên Median ít nhạy với độ lớn của vài điểm cực đoan. Đây là cơ sở dùng Median khi quan tâm sai số tuyệt đối.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 6. Vì sao Mode tối ưu số lần đoán sai? (04:50–05:45)

**Mục tiêu**

Vì sao Mode tối ưu số lần đoán sai?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

$\sum_i\mathbf1(x_i\ne a)=n-\operatorname{Count}(a)$; $E[\mathbf1(X\ne a)]=1-P(X=a)$. Nhãn đồng tần suất cực đại cùng tối ưu. Dùng nhãn rời rạc và chi phí sai bằng nhau.

**Lời thoại**

Với biến loại, mình phạt 0 nếu đúng nhãn và 1 nếu sai. Điền cùng nhãn a thì số sai bằng n trừ số lần a xuất hiện. Muốn số sai nhỏ nhất thì chọn nhãn phổ biến nhất, tức Mode. Điền M cho dãy M, M, L, S, M sai hai lần, còn điền L sai bốn lần. Lập luận giả sử chi phí sai bằng nhau; lớp hiếm quan trọng có thể cần mục tiêu khác.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 7. Vì sao dùng các thống kê để điền khuyết? (05:45–06:40)

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

Ba thước đo tương ứng ba hàm mất mát. Mean tối ưu tổng bình phương, Median tối ưu tổng trị tuyệt đối và Mode tối ưu số lần sai. Câu nói lệch thì chọn Median còn thiếu mục tiêu đánh giá. Trên dãy tuổi, 23 giảm MAE còn 34 giảm RMSE trên phần quan sát. Tuổi thật tại NaN chưa biết. Mình phải kiểm chứng cả việc khôi phục ô thiếu lẫn chất lượng mô hình sử dụng dữ liệu.

**Chuyển tiếp**

Tiếp theo là từ phần quan sát đến ô bị thiếu.

## 8. Kiểm chứng trên Student Performance (06:40–07:55)

**Mục tiêu**

Giải thích nội dung kiểm chứng trên student performance trong lựa chọn giá trị điền.

**Chỉ hình**

Histogram, boxplot và thiết kế train/test.

**Lời thoại**

Mình dùng student-por.csv của UCI: 649 quan sát thật, môn tiếng Bồ Đào Nha. Bản gốc đầy đủ, nên tự che MCAR để giữ giá trị thật đối chiếu. G1 có vùng trung tâm khá đối xứng; absences có đuôi phải rõ. Demo cho thấy hình dạng; benchmark chia train/test trước rồi fit thống kê từ train. Đây là dữ liệu thật với thiếu được tạo có kiểm soát; kết quả giới hạn trong cơ chế che này.

**Chuyển tiếp**

Tiếp theo là cùng dữ liệu, khác mục tiêu sai số.

## 9. Cùng dữ liệu, khác mục tiêu sai số (07:55–09:05)

**Mục tiêu**

Giải thích nội dung cùng dữ liệu, khác mục tiêu sai số trong lựa chọn giá trị điền.

**Chỉ hình**

Hai nhóm cột sai số và số lần thắng theo cặp.

**Lời thoại**

Ở mức che 15 phần trăm, khôi phục absences bằng Median có MAE khoảng 2,52, thấp hơn Mean 2,83. Nhưng Mean có RMSE 3,69, thấp hơn Median 3,86. Cùng dữ liệu mà thứ hạng đổi theo hàm mất mát. Mode với guardian có Accuracy khoảng 68,87 phần trăm, nhưng các lớp thiểu số trong phần bị che vẫn điền sai. Những điểm này chỉ chấm ô test bị che, không phải điểm dự đoán G3 của mô hình.

**Chuyển tiếp**

Tiếp theo là giá trị điền làm đổi phân phối.

## 10. Giá trị điền làm đổi phân phối (09:05–10:05)

**Mục tiêu**

Giải thích nội dung giá trị điền làm đổi phân phối trong lựa chọn giá trị điền.

**Chỉ hình**

Histogram trước/sau và tỷ trọng mother.

**Công thức và lưu ý để chuẩn bị**

Với $n$ quan sát và $m$ ô điền Mean quan sát, $s^2_{sau}=s^2_{quan\ sát}(n-1)/(n+m-1)$. Một lần che có thể có diễn biến tương quan khác xu hướng trung bình.

**Lời thoại**

Điền cùng hằng số tạo thêm khối tần suất tại giá trị đó. Trong demo absences, SD từ 4,664 xuống 4,312 sau Mean imputation. Với guardian, tỷ trọng mother từ khoảng 70,3 lên 74,6 phần trăm. Quan hệ giữa biến cũng có thể đổi. Vì vậy lỗi khôi phục thấp chưa đủ: tiếp theo mình huấn luyện thật để kiểm tra tác động đến dự đoán điểm.

**Chuyển tiếp**

Tiếp theo là khi một giá trị chung chưa đủ.

## 11. Bài toán huấn luyện dự đoán G3 (10:05–11:10)

**Mục tiêu**

Bài toán huấn luyện dự đoán G3.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Số: G1, G2, age, absences. Loại: guardian, school. Khi huấn luyện, G3 là y và không có trong X. Thí nghiệm khôi phục G3 là một thí nghiệm độc lập.

**Lời thoại**

Đích G3 được giữ đầy đủ. Sáu đầu vào gồm G1, G2, age, absences, guardian và school. Bối cảnh dự đoán sau khi có G1/G2. Mean, Median, Mode so trên biến số; biến loại đều dùng Mode. Pipeline học mọi bước chỉ trên train, với Ridge và Random Forest có cấu hình cố định. Có năm lần chia, bốn mặt nạ ở mỗi mức 5, 15 và 30 phần trăm, tổng cộng 370 lần fit gồm mốc đầy đủ. Điểm mô hình chấm G3 thật trên mọi dòng test.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 12. Mô hình sau điền thay đổi thế nào? (11:10–12:15)

**Mục tiêu**

Mô hình sau điền thay đổi thế nào?.

**Chỉ hình**

Chỉ công thức, bảng hoặc biểu đồ rồi giải thích theo lời thoại.

**Công thức và lưu ý để chuẩn bị**

Bảng lấy tự động từ results/model_evaluation.csv và model_reference.csv. Đây là trung bình RMSE từng lần chạy; không gộp các lần chia chồng lấn thành một test độc lập.

**Lời thoại**

Khi 15 phần trăm đầu vào train và test bị che, Ridge có RMSE từ 1,379 ở mốc đầy đủ lên 1,728 với Mean; Median là 1,734. Random Forest từ 1,359 lên 1,614 với Mean và 1,640 với Median. Mất thông tin làm dự đoán kém đi trong thiết kế này, và chênh giữa cách điền nhỏ hơn mức suy giảm ấy. Mean thấp nhất trong ba cấu hình tại đây nhưng chưa chứng minh luôn tốt hơn. Kết luận của một cột không tự động áp được cho mô hình dùng nhiều đặc trưng.

**Chuyển tiếp**

Nối kết luận vừa nêu với câu hỏi ở slide kế tiếp.

## 13. Trở lại ô tuổi bị thiếu (12:15–13:00)

**Mục tiêu**

Giải thích nội dung trở lại ô tuổi bị thiếu trong lựa chọn giá trị điền.

**Chỉ hình**

Ba câu trả lời và lựa chọn 23 hay 34.

**Lời thoại**

Mean, Median, Mode có cơ sở tối ưu theo các hàm mất mát khác nhau, khi phần quan sát đại diện phù hợp. Điền khuyết vẫn làm mất biến thiên và có thể ảnh hưởng dự đoán G3 như thực nghiệm đã thấy. Hãy chọn theo kiểu biến, mục tiêu và cơ chế thiếu; fit từ train rồi chấm cả lỗi khôi phục và mô hình. Ô tuổi thật vẫn chưa được biết chắc.

**Chuyển tiếp**

Dành hai phút còn lại cho hỏi đáp.

## Hỏi đáp (13:00–15:00)

Dùng [bộ câu hỏi phản biện](questions_answers.md) và [lý thuyết đầy đủ](ly_thuyet.md) để chuẩn bị.
