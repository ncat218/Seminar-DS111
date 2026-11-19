# Điền khuyết ảnh hưởng mô hình dự đoán G3 thế nào?

Đích là điểm cuối kỳ G3. Đầu vào gồm G1, G2, age, absences, guardian và school. G3 luôn được giữ đầy đủ. Bối cảnh dự đoán là sau khi đã có điểm G1/G2.

Thiết kế gồm 5 lần chia 75/25 × 4 mặt nạ tại mỗi mức thiếu. Mỗi phương pháp dùng cùng hàng và mặt nạ. Học imputer, mã hóa, chuẩn hóa và mô hình chỉ từ train. Giữ siêu tham số cố định trước khi chấm test.

Biến số so Mean, Median, Mode. Biến loại dùng Mode ở cả ba phương án. Các biến số là điểm, tuổi và số buổi vắng dạng rời rạc, nên Mode là baseline có ý nghĩa. Kết quả chính chấm mọi dòng test bằng nhãn G3 thật.

## Mốc dùng đầu vào đầy đủ

| Mô hình | MAE | RMSE | R² |
|---|---:|---:|---:|
| Ridge | 0.829 | 1.379 | 0.827 |
| Random Forest | 0.810 | 1.359 | 0.832 |
| Predict train mean | 2.431 | 3.324 | -0.005 |

## Cả train và test có đầu vào thiếu 15%

| Mô hình | Điền biến số | MAE | RMSE | R² | ΔRMSE so đầu vào đầy đủ |
|---|---|---:|---:|---:|---:|
| Ridge | Mean | 1.074 | 1.728 | 0.725 | +0.349 |
| Ridge | Median | 1.078 | 1.734 | 0.723 | +0.355 |
| Ridge | Mode | 1.087 | 1.748 | 0.719 | +0.369 |
| Random Forest | Mean | 0.973 | 1.614 | 0.760 | +0.255 |
| Random Forest | Median | 1.001 | 1.640 | 0.752 | +0.282 |
| Random Forest | Mode | 1.004 | 1.646 | 0.750 | +0.287 |

## Cách diễn giải

Bảng model_evaluation.csv có đủ 5%, 15%, 30%, hai pha và ba tập dòng test. Pha train thiếu/test đầy đủ khảo sát mô hình học từ đầu vào đã điền. Pha cả hai thiếu thêm ảnh hưởng của đầu vào mất thông tin lúc áp dụng. Cùng mô hình đã fit được dùng để dự đoán hai pha, nên khác biệt pha không đến từ việc huấn luyện lại.

Trong CSV, row_missing và các nhóm Missing input / Complete input được xác định bằng mặt nạ test. Ở pha clean test, chúng vẫn chỉ cùng các hàng của mặt nạ đối chiếu để so sánh theo cặp; đầu vào thực tế ở pha này đầy đủ. All test luôn gồm mọi dòng test.

Prediction shift là trung bình độ lệch tuyệt đối giữa dự đoán hiện tại và dự đoán từ mô hình học/áp dụng trên đầu vào đầy đủ, ghép đúng split và row_id. Nó đo độ thay đổi dự đoán, còn MAE/RMSE/R² đo độ đúng với G3 thật.

SD mô tả dao động của 20 tổ hợp chia/che trên cùng dataset. Các tập test chồng lấn giữa lần chia, nên không xem chúng như 20 mẫu học sinh độc lập. Mốc đầu vào đầy đủ là điểm tham chiếu của từng mô hình, không bảo đảm là cận trên hiệu năng. Không điều chỉnh siêu tham số theo các điểm test đã báo.

Sai số khôi phục một đặc trưng và sai số dự đoán G3 có hai hàm mục tiêu khác nhau. Lựa chọn tốt cần được kiểm chứng bằng chỉ tiêu của tác vụ cuối cùng. Các kết quả giới hạn ở hai mô hình, sáu biến, MCAR và bộ Student Performance này.
