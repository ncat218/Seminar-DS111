# Nội dung trình chiếu · DS111

9 slide, 13 phút trình bày và 2 phút hỏi đáp. Xem [lời thoại và mốc giờ](speaker_notes.md).

## 1. Điền khuyết bằng Mean, Median và Mode · 00:00–00:45

**Nội dung chiếu**

Điền khuyết bằng Mean, Median và Mode

Tuổi quan sát    20   22   23   25   80   NaN

**Nên điền 23 hay 34?**

**Đồ họa** · Dãy tuổi đặt cạnh hai giá trị ứng viên.

---

## 2. Giá trị thiếu trong EDA · 00:45–02:00

**Nội dung chiếu**

- NaN, None, pd.NA hoặc ô trống theo quy ước. 0 có thể là quan sát hợp lệ.
- Tỷ lệ thiếu = số ô thiếu / tổng số dòng. `df.isna().sum()` và `df.isna().mean()`.
- Bỏ qua câu hỏi, lỗi thiết bị, câu hỏi không áp dụng.
- Giảm số quan sát, có thể làm lệch thống kê. Cơ chế thiếu có thể là MCAR, MAR hoặc MNAR.

**Đồ họa** · Công thức tỷ lệ thiếu và hai lệnh pandas.

---

## 3. Ba thước đo xu hướng trung tâm · 02:00–03:30

**Nội dung chiếu**

- **Mean** · x̄ = Σ xᵢ / n. Dùng độ lớn của mọi quan sát. Nhạy với giá trị cực đoan.
- **Median** · Giá trị giữa sau khi sắp xếp. n chẵn lấy trung bình hai số giữa. Bền với giá trị cực đoan.
- **Mode** · Giá trị có tần suất cao nhất. Hợp với nhãn loại. Có thể có nhiều Mode.

**Đồ họa** · Ba cột định nghĩa với công thức Mean, cách lấy Median và định nghĩa Mode.

---

## 4. Vị trí của Mean, Median và Mode · 03:30–05:30

**Nội dung chiếu**

- Đối xứng một đỉnh (Normal): Mean = Median = Mode.
- Lệch phải (Gamma): Mode < Median < Mean.
- Lệch trái (Gamma phản chiếu): Mean < Median < Mode.
- Skewness thường dương với đuôi phải, âm với đuôi trái. Thứ tự trên ứng với ba ví dụ.

**Đồ họa** · Ba đường mật độ có mốc Mean, Median và Mode từ các phân phối lý thuyết.

---

## 5. Chọn phương pháp theo đặc điểm biến · 05:30–07:00

**Nội dung chiếu**

| Đặc điểm biến | Nên thử trước | Vì sao | Cần kiểm tra |
|---|---|---|---|
| Gần đối xứng, ít ngoại lệ | Mean | Dùng mọi độ lớn | Miền giá trị, RMSE |
| Lệch hoặc có ngoại lệ | Median | Bền theo thứ hạng | MAE và đỉnh sau điền |
| Nhãn loại | Mode | Nhãn phổ biến nhất | Lớp hiếm, đồng hạng |
| Các nhóm khác biệt | Thống kê theo nhóm | Tận dụng thông tin nhóm | Cỡ nhóm, leakage |
| Nhiều đỉnh hoặc đa Mode | Phân tích nhóm trước | Một số khó đại diện | Nguồn gốc các đỉnh |

Xem đây là điểm bắt đầu. Điều chỉnh theo mục tiêu và ngữ nghĩa biến.

**Đồ họa** · Bảng quyết định có thể chỉnh sửa trong PowerPoint.

---

## 6. Tuổi, nhãn Size và đa Mode · 07:00–08:30

**Nội dung chiếu**

- **Age** · [20, 22, 23, 25, 80, NaN]. Mean = 170/5 = 34. Median = 23. Tuổi 80 kéo Mean lên.
- **Size** · [M, M, L, S, NaN, M]. Mode = M.
- **X** · [2, 2, 3, 8, 8, NaN]. Mode = {2, 8}. Mean = 23/5 = 4,6. Median = 3. Nếu buộc chọn, mặc định scikit-learn chọn 2.

**Đồ họa** · Ba mẫu có NaN và kết quả tính tay.

---

## 7. EDA và cách chạy benchmark · 08:30–10:30

**Nội dung chiếu**

UCI Student Performance · 649 dòng môn tiếng Bồ Đào Nha

- Demo: che 94/649 ô absences (14,48%).
- G1. Skewness 0,01 · 14 điểm gắn cờ.
- absences. Skewness 2,08 · 18 điểm gắn cờ.
- Train/test 75/25 · MCAR 5%, 15%, 30% · 12 lần che mỗi mức.
- Chấm ở ô test bị che.

```python
imputer.fit(train_masked)
test_filled = imputer.transform(test_masked)
```

**Đồ họa** · Histogram theo khoảng nguyên, đường Mean/Median và boxplot trên dữ liệu quan sát từ demo 15%.

---

## 8. Sai số và biến dạng phân phối · 10:30–12:30

**Nội dung chiếu**

Benchmark MCAR 15%, điểm trung bình qua 12 lần che.

| Metric | Mean | Median |
|---|---:|---:|
| MAE | 2,83 | 2,52 |
| RMSE | 3,69 | 3,86 |

- Median giảm MAE. Mean giảm RMSE.
- SD mẫu từ 4,66 xuống 4,31 khi điền Mean.
- Mode đúng 68,87% ô người giám hộ bị che. Tỷ trọng nhãn mẹ từ 70,3% lên 74,6%.
- Với G3, MAE Median toàn cục 2,42, theo trường 2,35 (mở rộng nêu trong lời thoại).

**Đồ họa** · Biểu đồ cột PowerPoint cho MAE/RMSE và histogram trước/sau của số buổi vắng.

---

## 9. Quyết định điền khuyết · 12:30–13:00

**Nội dung chiếu**

1. **Hiểu biến.** Kiểu dữ liệu, tỷ lệ thiếu, phân phối và ngoại lệ.
2. **Chọn phương pháp.** Mean, Median hoặc Mode theo kiểu biến và mục tiêu.
3. **Kiểm chứng.** Chấm trên ô đã che và đối chiếu phân phối.

Hỏi đáp · 2 phút.

**Đồ họa** · Ba bước tương ứng với quy trình EDA, điền khuyết và đánh giá.

[Nguồn và giới hạn truy cập](references.md)
