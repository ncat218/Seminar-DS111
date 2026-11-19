# Nội dung trình chiếu DS111

9 slide, 13 phút trình bày và 2 phút hỏi đáp. Ba câu hỏi xuyên suốt gồm vì sao dùng giá trị đại diện, khi nào hợp lý và dữ liệu biến dạng thế nào.

## 1. Nên điền 23 hay 34? (00:00–01:00)

**Nội dung chiếu**

Tuổi = [20, 22, 23, 25, 80, NaN]. Mean = 34, Median = 23.
Vì sao dùng được giá trị đại diện?
Khi nào thay thế hợp lý?
Dữ liệu sau điền thay đổi ra sao?

**Đồ họa** · Ví dụ tuổi và ba câu hỏi xuyên suốt.

---

## 2. Giá trị đại diện là một dự đoán chung (01:00–02:30)

**Nội dung chiếu**

Chỉ dùng cột tuổi, dự đoán cùng một giá trị c.
Cần phần quan sát đại diện phù hợp cho phần bị thiếu.
MAE trên năm tuổi quan sát nhỏ nhất tại 23.
RMSE trên năm tuổi quan sát nhỏ nhất tại 34.
Tuổi thật ở ô NaN vẫn chưa biết.

**Đồ họa** · Hai đường sai số trên 5 tuổi đã biết.

---

## 3. Mean, Median và Mode theo mục tiêu sai số (02:30–04:00)

**Nội dung chiếu**

| Mục tiêu của dự đoán chung | Giá trị tối ưu | Thông tin được dùng |
|---|---|---|
| Giảm sai số bình phương | Mean   x̄ = Σxᵢ / n | Độ lớn của mọi quan sát |
| Giảm sai số tuyệt đối | Median | Vị trí giữa theo thứ hạng |
| Tăng số nhãn đoán đúng | Mode | Tần suất xuất hiện |
Size [M, M, L, S, NaN, M] có Mode M.
X [2, 2, 3, 8, 8, NaN] có mốt 2 và 8. SimpleImputer chọn 2.

**Đồ họa** · Bảng mục tiêu và thống kê có thể chỉnh sửa.

---

## 4. Khi nào phần quan sát đủ đại diện? (04:00–05:30)

**Nội dung chiếu**

Normal, Gamma và Gamma phản chiếu minh họa hình dạng.
MCAR cho phép phần quan sát đại diện theo cơ chế che.
Nếu thiếu liên quan nhóm, cần xét phân phối trong nhóm.
Chọn theo mục tiêu sai số và ý nghĩa biến.

**Đồ họa** · Ba phân phối lý thuyết và các điều kiện áp dụng.

---

## 5. Kiểm chứng trên Student Performance (05:30–07:15)

**Nội dung chiếu**

UCI Student Performance, 649 dòng môn tiếng Bồ Đào Nha.
G1 gần đối xứng ở vùng trung tâm, absences lệch phải.
486 train, 163 test. Fit trên train đã che, chấm ô test đã che.
MCAR 5%, 15%, 30%, mỗi mức 12 mặt nạ.

**Đồ họa** · Histogram và boxplot cùng thiết kế train/test.

---

## 6. Cùng dữ liệu, khác mục tiêu sai số (07:15–09:00)

**Nội dung chiếu**

Mean: MAE 2,83, RMSE 3,69
Median: MAE 2,52, RMSE 3,86
Median có MAE thấp hơn 10/12, hòa 1.
Mean có RMSE thấp hơn 11/12.
Guardian, Mode có Accuracy 68,87%.

**Đồ họa** · Biểu đồ cột editable và số lần thắng theo cặp.

---

## 7. Giá trị điền làm đổi phân phối (09:00–10:30)

**Nội dung chiếu**

SD absences từ 4,66 xuống 4,31 khi điền Mean.
Tỷ trọng mother từ 70,3% lên 74,6%.
Tương quan G3–GP 0,284 trên bản đầy đủ, trung bình sau điền Mean 0,264 qua 300 lần che.

**Đồ họa** · Histogram trước/sau và tỷ trọng mother chỉnh sửa được.

---

## 8. Khi một giá trị chung chưa đủ (10:30–12:00)

**Nội dung chiếu**

| G3, MCAR 15% | MAE | RMSE |
|---|---|---|
| Median chung | 2,42 | 3,17 |
| Theo trường | 2,35 | 3,19 |
Giữ 15 điểm G3 = 0 trong phân tích chính, 14 thuộc MS.
Dùng thông tin nhóm vẫn cần kiểm chứng.

**Đồ họa** · Histogram từ demo và bảng benchmark trên test.

---

## 9. Trở lại ô tuổi bị thiếu (12:00–13:00)

**Nội dung chiếu**

Vì sao dùng được? Giá trị tối ưu cho dự đoán chung theo tổn thất.
Khi nào hợp lý? Phần quan sát đủ đại diện và kiểu biến phù hợp.
Sai lệch thế nào? Giảm biến thiên, tăng tần suất và đổi quan hệ.
23 theo MAE, 34 theo RMSE trên phân phối quan sát. Tuổi thật vẫn chưa biết.

**Đồ họa** · Ba câu trả lời và ví dụ mở đầu.

[Nguồn tham khảo](references.md)
