# Kết luận từ thực nghiệm DS111

Dữ liệu mô phỏng gồm 3,200 dòng. Chia train/test 75/25, giữ nguyên lần chia.
Ở mỗi mức thiếu 5%, 15%, 30%, lặp 12 bộ mặt nạ MCAR. Các sai số dưới đây là trung bình ± SD qua lần che ở mức danh nghĩa 15%. SD mô tả độ dao động theo mặt nạ.

| Biến | Phương pháp | MAE | RMSE |
|---|---|---:|---:|
| symmetric_numeric | Mean | 6.67 ± 0.34 | 8.20 ± 0.38 |
| symmetric_numeric | Median | 6.68 ± 0.34 | 8.21 ± 0.38 |
| skewed_numeric | Mean | 16.50 ± 2.22 | 25.83 ± 6.15 |
| skewed_numeric | Median | 15.87 ± 2.40 | 27.55 ± 6.38 |
| multimodal_numeric | Mean | 14.88 ± 0.33 | 15.38 ± 0.35 |
| multimodal_numeric | Median | 14.75 ± 0.46 | 16.13 ± 0.68 |
| multimodal_numeric | Group Median | 3.12 ± 0.20 | 3.90 ± 0.25 |

- **Gần đối xứng:** skewness 0.04, Mean 49.83 và Median 49.91, 0 điểm bị gắn cờ theo 1,5 IQR. Hai giá trị điền gần nhau nên sai số chênh ít trong benchmark này.
- **Lệch phải:** skewness 3.41, Mean 23.51 và Median 16.00, 183 điểm bị gắn cờ. Ở mức 15%, Median giảm MAE còn Mean giảm RMSE. Với một hằng số, trung vị tối thiểu hóa tổng sai số tuyệt đối và trung bình tối thiểu hóa tổng bình phương sai số trên tập dùng để tối ưu. Thứ hạng trên test còn phụ thuộc vào mức đại diện của train.
- **Biến loại:** Accuracy của Mode đạt 60.56 ± 3.19%. Tỷ trọng M trong các giá trị có mặt tăng từ 60.5% lên 66.3% trong demo EDA. Mọi ô che đều nhận M, nên accuracy bằng tỷ lệ M thật trong các ô che và tỷ lệ khôi phục của các lớp còn lại bằng 0 khi có mặt.
- **Phân phối:** SD mẫu cột lệch từ 23.55 xuống 21.74 khi điền Mean trong cùng demo. Điền Mean toàn cục cho cột hai cụm làm tương quan Pearson với chỉ báo nhóm B đổi từ 0.965 xuống 0.889. Điền Median cũng tạo một đỉnh nhân tạo. Với hằng số khác Mean quan sát, thay đổi phương sai phụ thuộc vào vị trí hằng số.
- **Mở rộng theo nhóm:** MAE của Median toàn cục là 14.75 ± 0.46, Median theo nhóm là 3.12 ± 0.20. Nhóm A/B mang thông tin theo cách sinh dữ liệu. Cần kiểm tra nhóm có sẵn lúc sử dụng và đủ quan sát, vì benchmark này dùng fallback Median train toàn cục cho nhóm hiếm hoặc chưa gặp.

Các kết quả giới hạn ở bộ sinh dữ liệu, lần chia và cơ chế MCAR này. Tiêu chí sai số từng ô, bảo toàn phân phối marginal và bảo toàn quan hệ giữa biến cần được kiểm tra riêng.
