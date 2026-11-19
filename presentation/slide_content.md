# Nội dung trình chiếu DS111

13 slide, 13 phút trình bày và 2 phút hỏi đáp. Ba câu hỏi xuyên suốt gồm vì sao dùng giá trị đại diện, khi nào hợp lý và dữ liệu biến dạng thế nào.

## 1. Nên điền 23 hay 34? (00:00–00:45)

**Nội dung chiếu**

Tuổi = [20, 22, 23, 25, 80, NaN]. Mean = 34, Median = 23.
Vì sao dùng được giá trị đại diện?
Khi nào thay thế hợp lý?
Dữ liệu sau điền thay đổi ra sao?

**Đồ họa** · Ví dụ tuổi và ba câu hỏi xuyên suốt.

---

## 2. Phân phối dữ liệu (00:45–02:00)

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

## 4. Mean — Trung bình cộng (03:00–03:50)

**Nội dung chiếu**

Với n quan sát hợp lệ: x̄ = (1/n) Σᵢ xᵢ.
Mean dùng độ lớn của toàn bộ quan sát.
Tuổi [20,22,23,25,80] cho Mean = 34.
Đổi 80 thành 800, Mean = 178.
Một giá trị tăng Δ thì Mean tăng Δ/n.

**Đồ họa** · Công thức và ví dụ thay đổi một quan sát.

---

## 5. Median — Trung vị (03:50–04:40)

**Nội dung chiếu**

Sắp xếp x(1) ≤ … ≤ x(n).
Nếu n lẻ: Median = x((n+1)/2).
Nếu n chẵn: Median = [x(n/2) + x(n/2+1)]/2.
Ví dụ năm tuổi có Median=23. Bốn số [20,22,23,25] có Median=22,5.
Median bền hơn Mean với một vài giá trị cực đoan.

**Đồ họa** · Công thức cho n lẻ và chẵn, cùng hai ví dụ.

---

## 6. Mode — Mốt (04:40–05:30)

**Nội dung chiếu**

Modes(X) = arg max_v Count(v).
Hữu ích với nhóm máu, sản phẩm, chuyên ngành và nhãn người giám hộ.
Size [M,M,L,S,NaN,M] có Mode M.
X [2,2,3,8,8,NaN] có hai Mode {2,8}, Mean 4,6, Median 3.
Mọi giá trị xuất hiện một lần thì chưa có Mode duy nhất.

**Đồ họa** · Công thức tần suất và ví dụ một Mode, nhiều Mode.

---

## 7. Vì sao dùng các thống kê để điền khuyết? (05:30–06:45)

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

## 8. Từ phần quan sát đến ô bị thiếu (06:45–07:35)

**Nội dung chiếu**

Chỉ dùng cột tuổi, dự đoán cùng một giá trị c.
Cần phần quan sát đại diện phù hợp cho phần bị thiếu.
MAE trên năm tuổi quan sát nhỏ nhất tại 23.
RMSE trên năm tuổi quan sát nhỏ nhất tại 34.
Tuổi thật ở ô NaN vẫn chưa biết.

**Đồ họa** · Hai đường sai số trên 5 tuổi đã biết.

---

## 9. Kiểm chứng trên Student Performance (07:35–08:45)

**Nội dung chiếu**

UCI Student Performance, 649 dòng môn tiếng Bồ Đào Nha.
G1 gần đối xứng ở vùng trung tâm, absences lệch phải.
486 train, 163 test. Fit trên train đã che, chấm ô test đã che.
MCAR 5%, 15%, 30%, mỗi mức 12 mặt nạ.

**Đồ họa** · Histogram và boxplot cùng thiết kế train/test.

---

## 10. Cùng dữ liệu, khác mục tiêu sai số (08:45–10:00)

**Nội dung chiếu**

Mean: MAE 2,83, RMSE 3,69
Median: MAE 2,52, RMSE 3,86
Median có MAE thấp hơn 10/12, hòa 1.
Mean có RMSE thấp hơn 11/12.
Guardian, Mode có Accuracy 68,87%.

**Đồ họa** · Biểu đồ cột editable và số lần thắng theo cặp.

---

## 11. Giá trị điền làm đổi phân phối (10:00–11:00)

**Nội dung chiếu**

SD absences từ 4,66 xuống 4,31 khi điền Mean.
Tỷ trọng mother từ 70,3% lên 74,6%.
Tương quan G3–GP 0,284 trên bản đầy đủ, trung bình sau điền Mean 0,264 qua 300 lần che.

**Đồ họa** · Histogram trước/sau và tỷ trọng mother chỉnh sửa được.

---

## 12. Khi một giá trị chung chưa đủ (11:00–12:00)

**Nội dung chiếu**

| G3, MCAR 15% | MAE | RMSE |
|---|---|---|
| Median chung | 2,42 | 3,17 |
| Theo trường | 2,35 | 3,19 |
Giữ 15 điểm G3 = 0 trong phân tích chính, 14 thuộc MS.
Dùng thông tin nhóm vẫn cần kiểm chứng.

**Đồ họa** · Histogram từ demo và bảng benchmark trên test.

---

## 13. Trở lại ô tuổi bị thiếu (12:00–13:00)

**Nội dung chiếu**

Vì sao dùng được? Giá trị tối ưu cho dự đoán chung theo tổn thất.
Khi nào hợp lý? Phần quan sát đủ đại diện và kiểu biến phù hợp.
Sai lệch thế nào? Giảm biến thiên, tăng tần suất và đổi quan hệ.
23 theo MAE, 34 theo RMSE trên phân phối quan sát. Tuổi thật vẫn chưa biết.

**Đồ họa** · Ba câu trả lời và ví dụ mở đầu.

[Nguồn tham khảo](references.md)
