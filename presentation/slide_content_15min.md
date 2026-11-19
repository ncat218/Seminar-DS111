# Nội dung trình chiếu DS111

13 slide. Xem lời thoại và lộ trình để chọn thời lượng.

## 1. Nên điền 23 hay 34? (00:00–00:45)

**Nội dung chiếu**

Tuổi = [20, 22, 23, 25, 80, NaN]. Mean = 34, Median = 23.
Vì sao dùng được giá trị đại diện?
Khi nào thay thế hợp lý?
Dữ liệu sau điền thay đổi ra sao?

**Đồ họa** · Ví dụ tuổi và ba câu hỏi xuyên suốt.

---

## 2. Phân phối dữ liệu (00:45–01:45)

**Nội dung chiếu**

Đối xứng một đỉnh thường có Mean ≈ Median ≈ Mode.
Lệch phải điển hình: Mode < Median < Mean.
Lệch trái điển hình: Mean < Median < Mode.
Đối xứng có thể gặp ngoài Normal. Các thứ tự là ví dụ thường gặp.

**Đồ họa** · Normal, Gamma và Gamma phản chiếu.

---

## 3. Điền khuyết là ước lượng điều gì? (01:45–02:40)

**Nội dung chiếu**

M = 1 nếu quan sát, M = 0 nếu thiếu.
a* ∈ arg min_a E[L(X,a) | M=0].
Ước lượng a từ tổng mất mát trên các giá trị quan sát.
Cần phân phối quan sát đại diện phù hợp cho phần thiếu.

**Đồ họa** · Phân biệt rủi ro trên phần thiếu và tối ưu trên phần quan sát.

---

## 4. Vì sao Mean tối ưu sai số bình phương? (02:40–03:45)

**Nội dung chiếu**

E[(X−a)^2] = Var(X) + (μ−a)^2, μ=E[X].
Var(X) không phụ thuộc a. Chọn a=μ làm phần còn lại bằng 0.
Trên mẫu: f'(a)=2na−2Σxi=0, suy ra a=x̄.
Nghiệm tối ưu vẫn để lại rủi ro Var(X).

**Đồ họa** · Khai triển rủi ro kỳ vọng và đạo hàm trên mẫu.

---

## 5. Vì sao Median tối ưu sai số tuyệt đối? (03:45–04:50)

**Nội dung chiếu**

g(a)=Σ_i|xi−a|.
Khi a dịch sang phải, điểm bên trái làm tổng tăng, điểm bên phải làm tổng giảm.
Độ dốc = số điểm bên trái − số điểm bên phải khi a không trùng quan sát.
Median cân bằng hai phía. Với mẫu chẵn, cả khoảng giữa hai số giữa đều tối ưu.

**Đồ họa** · Độ dốc của tổng khoảng cách và điều kiện trung vị.

---

## 6. Vì sao Mode tối ưu số lần đoán sai? (04:50–05:45)

**Nội dung chiếu**

L(a)=Σ_i 1(xi≠a)=n−Count(a).
Giảm số lần sai tương đương tăng Count(a).
Trong [M,M,L,S,M], dự đoán M sai 2/5, dự đoán L sai 4/5.
Ở mức tổng thể, rủi ro 0–1 = 1−P(X=a).

**Đồ họa** · Đồng nhất thức n trừ tần suất và ví dụ nhãn.

---

## 7. Vì sao dùng các thống kê để điền khuyết? (05:45–06:40)

**Nội dung chiếu**

| Thước đo | Tối ưu theo | Ý nghĩa |
|---|---|---|
| Mean | Sai số bình phương | Giảm tổng bình phương độ lệch |
| Median | Sai số tuyệt đối | Giảm tổng khoảng cách tuyệt đối |
| Mode | Sai số nhãn 0–1 | Giảm số lần đoán sai |
Mean = arg min_a Σ_i(x_i−a)^2.
Median thuộc arg min_a Σ_i|x_i−a|.
Mode thuộc arg min_a Σ_i 1(x_i≠a).
Tối ưu trong phạm vi dự đoán bằng một hằng số trên tập đang xét.

**Đồ họa** · Bảng ba tổn thất và ba công thức tối ưu.

---

## 8. Kiểm chứng trên Student Performance (06:40–07:55)

**Nội dung chiếu**

UCI Student Performance, 649 dòng môn tiếng Bồ Đào Nha.
G1 gần đối xứng ở vùng trung tâm, absences lệch phải.
486 train, 163 test. Fit trên train đã che, chấm ô test đã che.
MCAR 5%, 15%, 30%, mỗi mức 12 mặt nạ.

**Đồ họa** · Histogram và boxplot cùng thiết kế train/test.

---

## 9. Cùng dữ liệu, khác mục tiêu sai số (07:55–09:05)

**Nội dung chiếu**

Mean: MAE 2,83, RMSE 3,69
Median: MAE 2,52, RMSE 3,86
Median có MAE thấp hơn 10/12, hòa 1.
Mean có RMSE thấp hơn 11/12.
Guardian, Mode có Accuracy 68,87%.

**Đồ họa** · Biểu đồ cột editable và số lần thắng theo cặp.

---

## 10. Giá trị điền làm đổi phân phối (09:05–10:05)

**Nội dung chiếu**

SD absences từ 4,66 xuống 4,31 khi điền Mean.
Tỷ trọng mother từ 70,3% lên 74,6%.
Tương quan G3–GP 0,284 trên bản đầy đủ, trung bình sau điền Mean 0,264 qua 300 lần che.

**Đồ họa** · Histogram trước/sau và tỷ trọng mother chỉnh sửa được.

---

## 11. Bài toán huấn luyện dự đoán G3 (10:05–11:10)

**Nội dung chiếu**

Đích G3 giữ đầy đủ. Đầu vào số: G1, G2, age, absences.
Đầu vào loại: guardian, school.
So Mean/Median/Mode trên biến số. Biến loại đều điền Mode.
Bối cảnh là sau khi có G1/G2.

**Đồ họa** · Định nghĩa đầu vào, đích và các chiến lược.

---

## 12. Mô hình sau điền thay đổi thế nào? (11:10–12:15)

**Nội dung chiếu**

| Mô hình | Đầu vào / điền | RMSE G3 | R² | ΔRMSE |
|---|---|---|---|---|
| Ridge | Đầy đủ | 1,379 | 0,827 | — |
| Ridge | Mean | 1,728 | 0,725 | +0,349 |
| Ridge | Median | 1,734 | 0,723 | +0,355 |
| Ridge | Mode | 1,748 | 0,719 | +0,369 |
| Random Forest | Đầy đủ | 1,359 | 0,832 | — |
| Random Forest | Mean | 1,614 | 0,760 | +0,255 |
| Random Forest | Median | 1,640 | 0,752 | +0,282 |
| Random Forest | Mode | 1,646 | 0,750 | +0,287 |
Thiếu 15% ở train và test, trung bình 20 tổ hợp chia/che.

**Đồ họa** · Bảng điểm từ mô hình đã huấn luyện.

---

## 13. Trở lại ô tuổi bị thiếu (12:15–13:00)

**Nội dung chiếu**

Vì sao dùng được? Giá trị tối ưu cho dự đoán chung theo tổn thất.
Khi nào hợp lý? Phần quan sát đủ đại diện và kiểu biến phù hợp.
Sai lệch thế nào? Đổi phân phối, quan hệ và chất lượng dự đoán.
23 theo MAE, 34 theo RMSE trên phân phối quan sát. Tuổi thật vẫn chưa biết.

**Đồ họa** · Ba câu trả lời và ví dụ mở đầu.

[Nguồn tham khảo](references.md)
