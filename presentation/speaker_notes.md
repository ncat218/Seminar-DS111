# Lời thoại · Mini seminar DS111

Trình bày 00:00–13:00. Dành 13:00–15:00 cho hỏi đáp. Các chỉ dẫn trong ngoặc vuông dành cho người trình bày.

## 1. Điền khuyết bằng Mean, Median và Mode · 00:00–00:45

**Mục tiêu** · Đặt câu hỏi về việc chọn giá trị điền.

**Chỉ hình** · Dãy tuổi trên slide. Dừng ở ô NaN.

**Lời thoại**

Giả sử chúng ta có một cột tuổi: 20, 22, 23, 25, 80 và một giá trị bị thiếu. Nếu cột này phải được điền đủ, em nên dùng 23 hay 34? [Dừng vài giây.] Hai con số đều tính được từ chính dữ liệu, nhưng chúng mô tả hai điều khác nhau. Con số 23 ở giữa về thứ hạng. Con số 34 dùng độ lớn của mọi quan sát, kể cả 80. Hôm nay em sẽ giải thích cách chọn một giá trị như vậy và kiểm chứng lựa chọn đó bằng cách che thử những ô đã biết giá trị thật.

**Chuyển tiếp** · Trước hết, cần biết ô nào thực sự bị thiếu và thiếu bao nhiêu.

## 2. Giá trị thiếu trong EDA · 00:45–02:00

**Mục tiêu** · Xác định cách ghi nhận, tỷ lệ và hệ quả của thiếu dữ liệu.

**Chỉ hình** · Công thức tỷ lệ thiếu rồi trỏ tới nguyên nhân và tác động.

**Lời thoại**

Trong bảng dữ liệu, em có thể gặp NaN, None, pd.NA hoặc ô trống. Quy ước đến từ bộ dữ liệu. Ví dụ 0 có thể là số lần mua hợp lệ, còn −999 có thể là mã thiếu nếu tài liệu dữ liệu quy định như vậy. Có nhiều lý do để trống một ô: người trả lời bỏ qua câu hỏi, thiết bị ghi lỗi hoặc câu hỏi vốn không áp dụng cho đối tượng đó. Khi dùng pandas, em xem số ô thiếu bằng isna rồi sum, và xem tỷ lệ bằng isna rồi mean. Mẫu số là số dòng trong cột. Một mẫu thiếu có hệ thống có thể khiến thống kê trên phần quan sát thiên lệch, và một số mô hình cần dữ liệu đầu vào đủ.

Trong thực nghiệm hôm nay, em tạo thiếu hoàn toàn ngẫu nhiên, gọi là MCAR, bằng cách che độc lập với giá trị dữ liệu. Với MAR, khả năng thiếu có thể phụ thuộc vào phần quan sát được. Với MNAR, phần chưa quan sát vẫn liên quan đến khả năng thiếu sau khi đã xét phần quan sát. [Dừng ở đây một nhịp.] Tỷ lệ thiếu hoặc biểu đồ có thể gợi ý điều tra thêm, nhưng riêng chúng không xác nhận được cơ chế nào đã tạo thiếu.

**Chuyển tiếp** · Sau khi nhận diện NaN, ta cần quyết định thống kê nào có ý nghĩa đối với cột đó.

## 3. Ba thước đo xu hướng trung tâm · 02:00–03:30

**Mục tiêu** · Phân biệt độ lớn, thứ hạng và tần suất.

**Chỉ hình** · Lần lượt trỏ vào công thức Mean, ô giữa của Median và tần suất của Mode.

**Lời thoại**

Mean là tổng các giá trị quan sát chia cho số quan sát hợp lệ, ký hiệu là n trong công thức này. Nếu một giá trị tăng thêm 30 trong một mẫu có 5 quan sát, Mean tăng 6. Đây là lý do một điểm xa phần còn lại có thể ảnh hưởng mạnh. Một giá trị như tuổi 23,4 có thể xuất hiện khi tính Mean hoặc Median. Tùy biến đang đo tuổi liên tục hay số năm tuổi nguyên mà ta xem xét miền giá trị điền.

Median dùng thứ tự sau khi sắp xếp. Khi số quan sát lẻ, chọn vị trí giữa. Với số chẵn, lấy trung bình hai giá trị giữa cho biến định lượng. Nếu chỉ làm điểm cao nhất lớn hơn nữa mà thứ hạng giữa giữ nguyên, Median giữ nguyên. Mode dựa trên số lần xuất hiện. Nó hợp với nhãn loại như S, M, L và có thể hữu ích cho biến rời rạc. [Chỉ vào cột Mode.] Khi hai giá trị xuất hiện nhiều nhất ngang nhau, cả hai đều là Mode. Với dữ liệu liên tục, giá trị chính xác thường hiếm khi lặp. Histogram có thể cho thấy một đỉnh theo khoảng giá trị, nhưng đỉnh đó còn phụ thuộc việc chia khoảng.

**Chuyển tiếp** · Hình dạng phân phối sẽ cho thấy vì sao các thống kê này có thể cách xa nhau.

## 4. Vị trí của Mean, Median và Mode · 03:30–05:30

**Mục tiêu** · Dùng ba phân phối để giải thích đuôi dài và mức nhạy của Mean.

**Chỉ hình** · Ba đường mật độ. Trỏ từ đỉnh đến đuôi trên hình lệch phải, rồi so sánh với hình phản chiếu.

**Lời thoại**

Trên hình thứ nhất, em dùng phân phối chuẩn làm ví dụ đối xứng một đỉnh. Đỉnh mật độ nằm ở giữa, hai phía cân đối, nên ba đường tâm trùng nhau. Tính đối xứng cũng có thể gặp ở phân phối tam giác hoặc hỗn hợp hai cụm. Vì vậy, khi Mean và Median gần nhau, em vẫn xem hình dạng thực tế trước khi nói về phân phối.

Hình thứ hai dùng phân phối Gamma. [Trỏ lần lượt vào Mode, Median rồi Mean.] Mode ở đỉnh. Median chia xác suất thành hai nửa. Một số giá trị rất lớn phía đuôi phải có thể đóng góp nhiều vào tổng, kéo Mean sang phải. Theo quy ước Fisher–Pearson, skewness dương thường đi cùng đuôi phải. Hình thứ ba phản chiếu phân phối Gamma để có đuôi trái và skewness âm. Lúc này Mean nằm phía trái Median. Ba thứ tự hiện trên slide áp dụng cho ba ví dụ cụ thể. Với dữ liệu nhiều đỉnh hoặc hình dạng phức tạp, thứ tự giữa các thước đo có thể khác.

Thực tế em đọc histogram để thấy cụm, đỉnh và đuôi. Boxplot là cách nhanh để xem trung vị, khoảng tứ phân vị và điểm ngoài hàng rào 1,5 lần IQR. Moment bậc ba trong skewness rất nhạy với các điểm xa tâm, vì vậy em dùng nó cùng biểu đồ và thống kê mô tả. Một điểm ngoài hàng rào có thể là quan sát hợp lệ, chẳng hạn đuôi thật của phân phối lognormal. [Dừng và chỉ lại đuôi phải.] Ta kiểm tra nguồn gốc của điểm đó trước khi quyết định xử lý.

**Chuyển tiếp** · Kết hợp kiểu biến với hình dạng này, ta có thể chọn các phương pháp để thử.

## 5. Chọn phương pháp theo đặc điểm biến · 05:30–07:00

**Mục tiêu** · Đọc bảng quyết định và gắn lựa chọn với tiêu chí kiểm tra.

**Chỉ hình** · Ba dòng đầu cho lựa chọn cơ bản. Hai dòng cuối cho các ngoại lệ.

**Lời thoại**

Với biến định lượng gần đối xứng, ít ngoại lệ, em thử Mean trước vì nó dùng độ lớn của tất cả quan sát và thường gần trung tâm. Em vẫn kiểm tra miền giá trị. Nếu histogram lệch rõ hoặc có đuôi rất dài, Median là cách lấy một số gần vùng điển hình hơn. Khi có một hàm mất mát cụ thể, kết quả có thể thay đổi: sai số tuyệt đối ưu tiên Median của phân phối mục tiêu, còn sai số bình phương ưu tiên Mean. Trong mẫu hữu hạn, ta chỉ có ước lượng của các đại lượng đó.

Với nhãn loại, em thử Mode, đồng thời xem nhãn phổ biến chiếm bao nhiêu và có đồng hạng hay không. Nếu biến có hai cụm, một hằng số gộp có thể rơi vào vùng thưa. Các nhóm thực sự khác nhau có thể cần thống kê riêng, với điều kiện cột nhóm có sẵn lúc điền và mỗi nhóm còn đủ điểm để ước lượng. Nhóm hiếm hoặc chưa gặp cần quy tắc dự phòng. [Chỉ hai dòng cuối.] Bảng là thứ tự ưu tiên để đặt giả thuyết. Ngữ nghĩa, phân phối và thước đo mục tiêu giúp kiểm tra giả thuyết đó.

**Chuyển tiếp** · Ba tình huống nhỏ giúp thấy vì sao các điều kiện này quan trọng.

## 6. Tuổi, nhãn Size và đa Mode · 07:00–08:30

**Mục tiêu** · Tính tay và giải thích sự khác nhau giữa các giá trị điền.

**Chỉ hình** · Chỉ tuổi 80, sau đó lần lượt chỉ hai ví dụ bên dưới.

**Lời thoại**

Quay lại dãy tuổi. Tổng năm giá trị là 170. Chia 5 được Mean bằng 34, còn số thứ ba sau khi sắp xếp là 23. Trong mẫu nhỏ này, 80 cao hơn cụm 20 đến 25 và làm tăng Mean. Nếu mục đích là lấy một giá trị gần cụm điển hình, 23 là một lựa chọn dễ giải thích. Tuổi 80 có thể hoàn toàn hợp lệ. Với ô bị thiếu, ta đang đưa ra một ước lượng, và tuổi thật của người đó vẫn chưa biết.

Ví dụ Size có ba chữ M, một L và một S. M có tần suất lớn nhất, nên một baseline là điền M. Nếu em đổi cách gán mã số cho từng nhãn, Mean của mã có thể đổi dù bảng Size vẫn như cũ. Cuối cùng, dãy 2, 2, 3, 8, 8 có hai Mode, là 2 và 8. Mean ở 4,6, Median bằng 3. Nếu buộc phải điền một Mode theo scikit-learn, phần mềm chọn giá trị nhỏ nhất trong các giá trị đồng hạng. [Ngừng một nhịp.] Đó là cách phân xử ổn định. Nếu 2 và 8 đến từ hai nhóm có thật, nên kiểm tra nhóm trước khi quyết định.

**Chuyển tiếp** · Ta thử quy trình tương tự trên một bảng đủ lớn để có biểu đồ và điểm số.

## 7. EDA và cách chạy benchmark · 08:30–10:30

**Mục tiêu** · Dùng kết quả EDA đo được để giải thích các lựa chọn và chống leakage.

**Chỉ hình** · Chỉ hai histogram, hai boxplot, khối mã và dòng train/test. Nếu trình chiếu notebook, mở mục 3 trước giờ nói.

**Lời thoại**

Dữ liệu mô phỏng có 3.200 dòng. Em sinh một biến tam giác gần đối xứng, một biến lognormal lệch phải, một biến có hai cụm theo nhóm và nhãn M, S, L. Trước mắt là một lần che kiểu MCAR ở mức danh nghĩa 15%. Chẳng hạn cột lệch phải thiếu 474 trên 3.200 ô, tức khoảng 14,81%. Cột nhóm luôn quan sát được.

[Chỉ hình bên trái.] Biến gần đối xứng có skewness khoảng 0,04. Mean khoảng 49,83 và Median khoảng 49,91, hai đường gần như trùng, và boxplot không gắn cờ điểm nào. [Chỉ hình bên phải.] Biến lệch phải có skewness 3,41. Mean khoảng 23,51 so với Median khoảng 16,00. Boxplot gắn cờ 183 điểm, phù hợp với đuôi dài của biến sinh lognormal. Từ EDA này, em kỳ vọng hai phương pháp cho kết quả gần nhau trên biến thứ nhất và khác nhiều hơn trên biến thứ hai. Với Size mô phỏng, M là nhãn phổ biến, nên em thử Mode.

Để chấm sai số, em dùng lại bản đầy đủ và chia theo hàng thành 75% train và 25% test. Sau đó mới tạo mặt nạ train và test bằng hai luồng ngẫu nhiên riêng. Đoạn mã khớp bộ điền trên train đã che, rồi áp dụng lên test đã che. Mean và Median dùng cùng một mặt nạ để so sánh công bằng. Em chỉ xem lại giá trị gốc ở các ô test mà em đã cố tình che. Thuật toán thử mức 5%, 15% và 30%, mỗi mức lặp 12 mặt nạ. Khác với benchmark, phần EDA dùng Mean của chính bảng quan sát để giải thích thay đổi của phân phối.

**Chuyển tiếp** · Khi chấm điểm và xem lại phân phối, hai cách đánh giá trả lời hai câu hỏi khác nhau.

## 8. Sai số và biến dạng phân phối · 10:30–12:30

**Mục tiêu** · Đọc thứ hạng theo từng metric và giải thích hệ quả của điền một hằng số.

**Chỉ hình** · Chỉ hai nhóm cột MAE/RMSE, đỉnh histogram, rồi dòng Mode. Nếu có thêm thời gian, mở hình hai cụm ở notebook.

**Lời thoại**

Biểu đồ dùng kết quả trung bình ở mức thiếu 15%. MAE là trung bình độ lệch tuyệt đối. RMSE lấy căn của sai số bình phương trung bình nên nhạy hơn với các lỗi lớn. Cả hai dùng cùng đơn vị của biến. [Trỏ vào MAE.] Trên biến lệch phải, Median có MAE 15,87, thấp hơn 16,50 của Mean. [Trỏ RMSE.] Mean có RMSE 25,83, thấp hơn 27,55 của Median. Với một giá trị điền duy nhất, Median phù hợp với mất mát tuyệt đối, trong khi Mean phù hợp với mất mát bình phương. Đây là kết quả của mô phỏng cụ thể. Trên biến gần đối xứng, điểm hai cách gần như trùng. Độ lệch chuẩn của điểm qua 12 mặt nạ có trong notebook.

Hình bên phải đặt dữ liệu quan sát cạnh dữ liệu sau điền. Ta thấy đỉnh mới tại giá trị điền. Khi điền bằng Mean của chính phần quan sát, Mean giữ nguyên và độ lệch chuẩn mẫu của biến lệch giảm từ 23,55 xuống 21,74. Các ô điền có độ lệch bằng 0 so với Mean, còn số quan sát dùng để chia tăng. Điều đó cũng có thể làm thay đổi tương quan khi ta phân tích nhiều biến.

Mode dự đoán đúng khoảng 60,56% ô test bị che, nhưng trong demo tỷ trọng M tăng từ 60,5% lên 66,3%. Phương pháp dồn mọi ô thiếu về lớp đa số. Ví dụ hai cụm cũng cho thấy tiềm năng của nhóm: Median theo nhóm cho MAE 3,12, so với 14,75 khi dùng Median gộp. Nhóm A/B có thông tin theo thiết kế, nên cần kiểm tra lại điều kiện đó ở dữ liệu sử dụng.

**Chuyển tiếp** · Với một cột mới, em sẽ làm ba việc trước khi chọn dùng kết quả điền.

## 9. Quyết định điền khuyết · 12:30–13:00

**Mục tiêu** · Tóm tắt quy trình có thể áp dụng trong EDA.

**Chỉ hình** · Đọc lần lượt ba dòng. Chuyển sang hỏi đáp ở phút 13.

**Lời thoại**

Đầu tiên, xem biến đo gì, thiếu bao nhiêu, có đuôi dài, ngoại lệ hoặc nhiều cụm không. Sau đó chọn Mean, Median hoặc Mode theo dữ liệu và mục tiêu sai số. Cuối cùng, dùng ô đã che để chấm thử, rồi kiểm tra lại biểu đồ và thống kê. Điền hết NaN giải quyết phần dữ liệu trống. Mỗi giá trị điền vẫn là một ước lượng.

**Chuyển tiếp** · Em xin dành hai phút cho câu hỏi.

## Hỏi đáp · 13:00–15:00

Mở [bộ câu hỏi phản biện](questions_answers.md) khi cần. Câu hỏi “Nếu chỉ dùng một metric thì sao?” có thể minh họa ngay bằng hai thứ hạng ngược chiều trên slide 8. Với cơ chế thiếu hoặc tài liệu môn học, xem [nguồn và phạm vi](references.md).
