# Kết luận từ thực nghiệm DS111

Tập tiếng Bồ Đào Nha của UCI Student Performance gồm 649 dòng thực tế. Bốn cột phân tích đầy đủ trước khi che. Chia train/test 75/25, giữ nguyên lần chia.
Ở mỗi mức thiếu 5%, 15%, 30%, lặp 12 bộ mặt nạ MCAR. Các sai số dưới đây là trung bình ± SD qua lần che ở mức danh nghĩa 15%. SD mô tả độ dao động theo mặt nạ.

| Biến | Phương pháp | MAE | RMSE |
|---|---|---:|---:|
| G1 | Mean | 2.41 ± 0.36 | 2.99 ± 0.44 |
| G1 | Median | 2.44 ± 0.35 | 3.07 ± 0.44 |
| absences | Mean | 2.83 ± 0.36 | 3.69 ± 0.81 |
| absences | Median | 2.52 ± 0.47 | 3.86 ± 0.93 |
| G3 | Mean | 2.43 ± 0.25 | 3.19 ± 0.47 |
| G3 | Median | 2.42 ± 0.25 | 3.17 ± 0.48 |
| G3 | Group Median | 2.35 ± 0.31 | 3.19 ± 0.52 |

- **Điểm kỳ đầu G1:** skewness 0.01, Mean 11.35 và Median 11.00, 14 điểm bị gắn cờ theo 1,5 IQR. Hai tâm gần nhau. Đọc cả hình dạng và điểm đuôi trước khi chọn.
- **Số buổi vắng absences:** skewness 2.08, Mean 3.71 và Median 2.00, 18 điểm bị gắn cờ. Ở mức 15%, Median có MAE thấp hơn và Mean có RMSE thấp hơn. Số 0 là vắng 0 buổi, một quan sát hợp lệ. Mean có thể cho kết quả lẻ, phù hợp với dự đoán điểm theo mất mát bình phương. Nếu đầu ra cần số đếm nguyên, cần định nghĩa quy tắc và đánh giá lại. Với một hằng số, Median tối thiểu hóa tổng sai số tuyệt đối và Mean tối thiểu hóa tổng bình phương trên tập tối ưu. Thứ hạng test phụ thuộc vào mức đại diện của train.
- **Người giám hộ guardian:** Accuracy của Mode đạt 68.87% ± 6.54 điểm phần trăm. Tỷ trọng nhãn mẹ trong các giá trị có mặt tăng từ 70.3% lên 74.6% trong demo EDA. Điền nhãn đa số cho mọi ô che làm giảm khả năng khôi phục các lớp hiếm.
- **Phân phối:** SD mẫu cột lệch từ 4.66 xuống 4.31 khi điền Mean trong cùng demo. Điền Mean toàn cục cho điểm G3 làm tương quan Pearson với chỉ báo trường GP đổi từ 0.310 thành 0.287. Điền Median cũng tạo một đỉnh nhân tạo. Với hằng số khác Mean quan sát, thay đổi phương sai phụ thuộc vào vị trí hằng số.
- **Mở rộng theo trường:** MAE của Median G3 toàn cục là 2.42 ± 0.25, Median theo nhóm là 2.35 ± 0.31. RMSE lần lượt là 3.17 ± 0.48 và 3.19 ± 0.52. Chênh lệch quan sát giữa trường không xác lập tác động nhân quả. Cần kiểm tra trường có sẵn lúc sử dụng và đủ quan sát, vì benchmark này dùng fallback Median train toàn cục cho nhóm hiếm hoặc chưa gặp.

Các kết quả giới hạn ở mẫu môn tiếng Bồ Đào Nha, lần chia và cơ chế che MCAR này. Số liệu do thực nghiệm trên bộ dữ liệu thật tạo ra. Cách thiếu ngoài đời có thể khác.
