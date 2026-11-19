# Nội dung trình chiếu DS111

24 slide. Xem lời thoại và lộ trình để chọn thời lượng.

## 1. Nên điền 23 hay 34? (00:00–01:00)

**Nội dung chiếu**

Tuổi = [20, 22, 23, 25, 80, NaN]. Mean = 34, Median = 23.
Vì sao dùng được giá trị đại diện?
Khi nào thay thế hợp lý?
Dữ liệu sau điền thay đổi ra sao?

**Đồ họa** · Ví dụ tuổi và ba câu hỏi xuyên suốt.

---

## 2. Phân phối dữ liệu (01:00–02:00)

**Nội dung chiếu**

Đối xứng một đỉnh thường có Mean ≈ Median ≈ Mode.
Lệch phải điển hình: Mode < Median < Mean.
Lệch trái điển hình: Mean < Median < Mode.
Đối xứng có thể gặp ngoài Normal. Các thứ tự là ví dụ thường gặp.

**Đồ họa** · Normal, Gamma và Gamma phản chiếu.

---

## 3. Skewness và ngoại lệ (02:00–03:00)

**Nội dung chiếu**

Skewness gần 0 cần kiểm tra hình. Dương thường lệch phải, âm thường lệch trái.
IQR = Q3 − Q1.
Hàng rào [Q1 − 1,5 × IQR ; Q3 + 1,5 × IQR].
Demo absences có Q1=0, Q3=6, hàng rào −9 và 15, 18 điểm gắn cờ.

**Đồ họa** · Bảng dấu skewness, công thức hàng rào và boxplot absences.

---

## 4. Mean — Trung bình cộng (03:00–04:00)

**Nội dung chiếu**

Với n quan sát hợp lệ: x̄ = (1/n) Σᵢ xᵢ.
Mean dùng độ lớn của toàn bộ quan sát.
Tuổi [20,22,23,25,80] cho Mean = 34.
Đổi 80 thành 800, Mean = 178.
Một giá trị tăng Δ thì Mean tăng Δ/n.

**Đồ họa** · Công thức và ví dụ thay đổi một quan sát.

---

## 5. Median — Trung vị (04:00–05:00)

**Nội dung chiếu**

Sắp xếp x(1) ≤ … ≤ x(n).
Nếu n lẻ: Median = x((n+1)/2).
Nếu n chẵn: Median = [x(n/2) + x(n/2+1)]/2.
Ví dụ năm tuổi có Median=23. Bốn số [20,22,23,25] có Median=22,5.
Median bền hơn Mean với một vài giá trị cực đoan.

**Đồ họa** · Công thức cho n lẻ và chẵn, cùng hai ví dụ.

---

## 6. Mode — Mốt (05:00–06:00)

**Nội dung chiếu**

Modes(X) = arg max_v Count(v).
Hữu ích với nhóm máu, sản phẩm, chuyên ngành và nhãn người giám hộ.
Size [M,M,L,S,NaN,M] có Mode M.
X [2,2,3,8,8,NaN] có hai Mode {2,8}, Mean 4,6, Median 3.
Mọi giá trị xuất hiện một lần thì chưa có Mode duy nhất.

**Đồ họa** · Công thức tần suất và ví dụ một Mode, nhiều Mode.

---

## 7. Điền khuyết là ước lượng điều gì? (06:00–07:00)

**Nội dung chiếu**

M = 1 nếu quan sát, M = 0 nếu thiếu.
a* ∈ arg min_a E[L(X,a) | M=0].
Ước lượng a từ tổng mất mát trên các giá trị quan sát.
Cần phân phối quan sát đại diện phù hợp cho phần thiếu.

**Đồ họa** · Phân biệt rủi ro trên phần thiếu và tối ưu trên phần quan sát.

---

## 8. Vì sao Mean tối ưu sai số bình phương? (07:00–08:30)

**Nội dung chiếu**

E[(X−a)^2] = Var(X) + (μ−a)^2, μ=E[X].
Var(X) không phụ thuộc a. Chọn a=μ làm phần còn lại bằng 0.
Trên mẫu: f'(a)=2na−2Σxi=0, suy ra a=x̄.
Nghiệm tối ưu vẫn để lại rủi ro Var(X).

**Đồ họa** · Khai triển rủi ro kỳ vọng và đạo hàm trên mẫu.

---

## 9. Vì sao Median tối ưu sai số tuyệt đối? (08:30–10:00)

**Nội dung chiếu**

g(a)=Σ_i|xi−a|.
Khi a dịch sang phải, điểm bên trái làm tổng tăng, điểm bên phải làm tổng giảm.
Độ dốc = số điểm bên trái − số điểm bên phải khi a không trùng quan sát.
Median cân bằng hai phía. Với mẫu chẵn, cả khoảng giữa hai số giữa đều tối ưu.

**Đồ họa** · Độ dốc của tổng khoảng cách và điều kiện trung vị.

---

## 10. Vì sao Mode tối ưu số lần đoán sai? (10:00–11:00)

**Nội dung chiếu**

L(a)=Σ_i 1(xi≠a)=n−Count(a).
Giảm số lần sai tương đương tăng Count(a).
Trong [M,M,L,S,M], dự đoán M sai 2/5, dự đoán L sai 4/5.
Ở mức tổng thể, rủi ro 0–1 = 1−P(X=a).

**Đồ họa** · Đồng nhất thức n trừ tần suất và ví dụ nhãn.

---

## 11. Vì sao dùng các thống kê để điền khuyết? (11:00–12:00)

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

## 12. Từ phần quan sát đến ô bị thiếu (12:00–13:00)

**Nội dung chiếu**

Chỉ dùng cột tuổi, dự đoán cùng một giá trị c.
Cần phần quan sát đại diện phù hợp cho phần bị thiếu.
MAE trên năm tuổi quan sát nhỏ nhất tại 23.
RMSE trên năm tuổi quan sát nhỏ nhất tại 34.
Tuổi thật ở ô NaN vẫn chưa biết.

**Đồ họa** · Hai đường sai số trên 5 tuổi đã biết.

---

## 13. Kiểm chứng trên Student Performance (13:00–14:00)

**Nội dung chiếu**

UCI Student Performance, 649 dòng môn tiếng Bồ Đào Nha.
G1 gần đối xứng ở vùng trung tâm, absences lệch phải.
486 train, 163 test. Fit trên train đã che, chấm ô test đã che.
MCAR 5%, 15%, 30%, mỗi mức 12 mặt nạ.

**Đồ họa** · Histogram và boxplot cùng thiết kế train/test.

---

## 14. Hai mức đánh giá điền khuyết (14:00–15:00)

**Nội dung chiếu**

Khôi phục ô thiếu và dự đoán G3 có đích khác nhau.
Mức 1 chấm chỉ ô test đã che.
Mức 2 giữ G3 đầy đủ và chấm mọi dòng test.

**Đồ họa** · Bảng đối chiếu hai thí nghiệm.

---

## 15. Cùng dữ liệu, khác mục tiêu sai số (15:00–16:00)

**Nội dung chiếu**

Mean: MAE 2,83, RMSE 3,69
Median: MAE 2,52, RMSE 3,86
Median có MAE thấp hơn 10/12, hòa 1.
Mean có RMSE thấp hơn 11/12.
Guardian, Mode có Accuracy 68,87%.

**Đồ họa** · Biểu đồ cột editable và số lần thắng theo cặp.

---

## 16. Giá trị điền làm đổi phân phối (16:00–17:00)

**Nội dung chiếu**

SD absences từ 4,66 xuống 4,31 khi điền Mean.
Tỷ trọng mother từ 70,3% lên 74,6%.
Tương quan G3–GP 0,284 trên bản đầy đủ, trung bình sau điền Mean 0,264 qua 300 lần che.

**Đồ họa** · Histogram trước/sau và tỷ trọng mother chỉnh sửa được.

---

## 17. Bài toán huấn luyện dự đoán G3 (17:00–18:00)

**Nội dung chiếu**

Đích G3 giữ đầy đủ. Đầu vào số: G1, G2, age, absences.
Đầu vào loại: guardian, school.
So Mean/Median/Mode trên biến số. Biến loại đều điền Mode.
Bối cảnh là sau khi có G1/G2.

**Đồ họa** · Định nghĩa đầu vào, đích và các chiến lược.

---

## 18. Pipeline huấn luyện và kiểm tra (18:00–19:00)

**Nội dung chiếu**

Fit imputer, one-hot, chuẩn hóa và mô hình chỉ trên train.
5 lần chia × 4 mặt nạ tại mỗi mức. Cố định siêu tham số.
370 pipeline gồm 360 train có thiếu và 10 mốc đầy đủ.

**Đồ họa** · Bảng thiết kế huấn luyện và phép đo.

---

## 19. Mô hình sau điền thay đổi thế nào? (19:00–20:00)

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

## 20. Ảnh hưởng khi mức thiếu tăng (20:00–21:00)

**Nội dung chiếu**

RMSE G3 tại 5%, 15%, 30% cho Ridge và Random Forest.
Ba cách điền dùng cùng hàng và mặt nạ.
Điểm tham chiếu đầu vào đầy đủ từ cùng mô hình.

**Đồ họa** · Hai biểu đồ đường chỉnh sửa được.

---

## 21. Thiếu khi học và thiếu khi áp dụng (21:00–22:00)

**Nội dung chiếu**

| Mô hình | Đầy đủ | Train thiếu | Train/test thiếu |
|---|---|---|---|
| Ridge | 1,379 | 1,457 | 1,734 |
| Random Forest | 1,359 | 1,431 | 1,640 |
Dùng Median cho biến số, Mode cho biến loại, mức 15%. Cùng pipeline đã fit dự đoán hai pha test.

**Đồ họa** · Bảng tách hai pha và giải thích đối chiếu.

---

## 22. Dự đoán từng học sinh thay đổi ra sao? (22:00–23:00)

**Nội dung chiếu**

Ví dụ split 42, mask 42, thiếu 30%, điền Median.
So dự đoán với G3 thật và với mô hình đầu vào đầy đủ.
Đường chéo biểu diễn dự đoán khớp điểm thật.

**Đồ họa** · Scatter dự đoán từ dữ liệu chạy thật.

---

## 23. Khi một giá trị chung chưa đủ (23:00–24:00)

**Nội dung chiếu**

| G3, MCAR 15% | MAE | RMSE |
|---|---|---|
| Median chung | 2,42 | 3,17 |
| Theo trường | 2,35 | 3,19 |
Giữ 15 điểm G3 = 0 trong phân tích chính, 14 thuộc MS.
Dùng thông tin nhóm vẫn cần kiểm chứng.

**Đồ họa** · Histogram từ demo và bảng benchmark trên test.

---

## 24. Trở lại ô tuổi bị thiếu (24:00–25:00)

**Nội dung chiếu**

Vì sao dùng được? Giá trị tối ưu cho dự đoán chung theo tổn thất.
Khi nào hợp lý? Phần quan sát đủ đại diện và kiểu biến phù hợp.
Sai lệch thế nào? Đổi phân phối, quan hệ và chất lượng dự đoán.
23 theo MAE, 34 theo RMSE trên phân phối quan sát. Tuổi thật vẫn chưa biết.

**Đồ họa** · Ba câu trả lời và ví dụ mở đầu.

[Nguồn tham khảo](references.md)
