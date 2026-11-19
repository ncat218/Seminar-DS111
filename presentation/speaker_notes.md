# Lời thoại seminar DS111

9 slide, 13 phút trình bày và 2 phút hỏi đáp. Ba câu hỏi xuyên suốt bài là vì sao có thể dùng giá trị đại diện để ước lượng ô thiếu, khi nào cách thay thế hợp lý, và nó làm biến dạng dữ liệu thế nào.

## 1. Nên điền 23 hay 34? (00:00–01:00)

**Mục tiêu**

Đặt câu hỏi nghiên cứu từ ví dụ tuổi.

**Chỉ hình**

Trỏ dãy tuổi, dừng ở NaN, rồi đọc ba câu hỏi.

**Lời thoại**

Xin chào thầy và tất cả các bạn đến với mini seminar hôm nay. Đầu tiên, mình có một cột tuổi gồm 20, 22, 23, 25, 80 và một ô bị thiếu. Theo các bạn, mình nên điền 23 là Median hay 34 là Mean? [Dừng hai giây.]

Hôm nay chúng ta cùng tìm hiểu việc vận dụng các thước đo xu hướng trung tâm để điền khuyết dữ liệu. Các bạn có thể đã gặp quy tắc chọn Mean, Median hoặc Mode. Trong bài này, tụi mình sẽ đi sâu vào cơ sở của các lựa chọn đó.

Câu hỏi xuyên suốt là vì sao một giá trị đại diện cho phân phối có thể dùng để ước lượng ô thiếu, khi nào cách thay thế ấy hợp lý, và nó làm dữ liệu sai lệch ra sao. Cuối bài, chúng ta sẽ quay lại lựa chọn 23 hay 34 với một cách lập luận đầy đủ hơn.

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

**Chuyển tiếp**

Mời thầy và các bạn đặt câu hỏi trong hai phút còn lại.

## Hỏi đáp (13:00–15:00)

Mở [câu hỏi phản biện](questions_answers.md), [script có thuật ngữ](script_va_thuat_ngu.md) và [nguồn tham khảo](references.md).
