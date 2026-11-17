# DS111 · Điền khuyết bằng Mean, Median và Mode

Bộ seminar tiếng Việt gồm 9 slide cho 13 phút trình bày và 2 phút hỏi đáp. Thực nghiệm dùng dữ liệu mô phỏng để quan sát hai tiêu chí riêng biệt: sai số tại các ô bị che và mức thay đổi phân phối sau khi điền.

## Trình chiếu

- [PowerPoint](presentation/seminar_15min.pptx) có ghi chú cho người trình bày. [Bản PDF](presentation/seminar_15min.pdf) dùng ảnh render 1920 × 1080 mỗi slide để trình chiếu dự phòng.
- [Lời thoại có mốc giờ](presentation/speaker_notes.md), [nội dung từng slide](presentation/slide_content.md), [câu hỏi phản biện](presentation/questions_answers.md) và [nguồn tham khảo](presentation/references.md).
- [Notebook đã lưu đầu ra](notebooks/seminar_imputation.ipynb) có thể dùng để mở phần demo hoặc kết quả.

## Chạy lại thực nghiệm

Cần Python 3.10+ và các thư viện trong `requirements.txt`. Các lệnh dưới đây chạy từ thư mục chứa README. Sau bước cài thư viện, thực nghiệm chạy ngoại tuyến. Trên Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m src.run_experiments
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m jupyterlab notebooks/seminar_imputation.ipynb
```

Trong JupyterLab, chọn kernel của môi trường vừa cài rồi chạy **Restart Kernel and Run All Cells**. Để chạy không qua giao diện:

```powershell
.\.venv\Scripts\jupyter-nbconvert.exe --to notebook --execute --ExecutePreprocessor.timeout=180 --inplace notebooks/seminar_imputation.ipynb
```

Trên macOS/Linux, dùng `.venv/bin/python` và `.venv/bin/jupyter-nbconvert`. Chạy riêng `python -m src.generate_data` nếu chỉ cần CSV dữ liệu. Tác vụ `src.run_experiments` sinh lại dữ liệu, bảng, kết luận và biểu đồ. Slide đã xuất là bản chụp của lần chạy kèm theo.

Đã chạy toàn bộ 6 cell mã theo thứ tự trên Python 3.14.4 và lưu bảng, hình vào notebook. Máy tạo bộ seminar thiếu kernel Jupyter. Các lệnh JupyterLab và nbconvert ở trên dành cho môi trường đã cài các thư viện trong `requirements.txt`.

## Dataset và thiết kế

3.200 dòng, seed sinh 42, xác định bởi `row_id` (chỉ mục dùng để ghép các tập). Biến số dùng đơn vị mô phỏng. Mọi dòng đều đầy đủ trước khi che.

| Cột | Cách sinh và mục đích |
|---|---|
| `symmetric_numeric` | Phân phối tam giác min 30, đỉnh 50, max 70. Ví dụ gần đối xứng với đuôi hữu hạn. |
| `skewed_numeric` | Lognormal, μ = 2,8 và σ = 0,85 trên thang log tự nhiên. Đuôi phải chứa các giá trị lớn do quá trình sinh. |
| `multimodal_numeric` | Normal theo A/B, Mean 35/65 và SD 4. Phân phối gộp có hai cụm. |
| `category` | Nhãn M, S, L với xác suất lần lượt 0,61, 0,26, 0,13. |
| `group` | A hoặc B, mỗi nhóm có xác suất 0,5. Giữ quan sát được khi thử mở rộng theo nhóm. |

Demo mô tả dùng một mặt nạ Bernoulli MCAR 15% và fit trên phần quan sát của demo để đo biến dạng của chính cột đó. Benchmark chia riêng train/test 75/25 với seed 42, sau đó che độc lập train và test. Seed mặt nạ 42–53 lặp tại ba mức 5%, 15%, 30%. Mỗi phương pháp so sánh trong cùng lần chạy dùng cùng ô test. Các mức là xác suất che danh nghĩa nên tỷ lệ thực tế dao động. Fit chỉ trên train đã che và chấm chỉ trên test bị che bằng giá trị gốc. Group Median dùng Median toàn cục của train cho nhóm có dưới 20 giá trị quan sát hoặc chưa gặp.

## Vị trí dữ liệu và cách đọc bảng

| Đường dẫn | Nội dung |
|---|---|
| `data/synthetic_complete.csv` | Ground truth của mô phỏng |
| `data/synthetic_missing_15pct.csv`, `synthetic_mask_15pct.csv` | Bản quan sát và mặt nạ của demo |
| `results/missing_summary.csv`, `eda_numeric.csv` | Tỷ lệ thiếu thực tế, thống kê và số điểm ngoài hàng rào 1,5 IQR |
| `results/distribution_summary.csv`, `category_frequencies.csv` | Thống kê của dữ liệu gốc, quan sát và sau điền, bao gồm SD mẫu, tương quan và tần suất |
| `results/evaluation.csv` | Trung bình và SD qua các mặt nạ, phân theo mức thiếu, biến, phương pháp và metric |
| `results/evaluation_by_seed.csv` | Điểm và số ô che thực tế theo từng lần lặp |
| [Kết luận thực nghiệm](results/conclusions.md) | Số liệu và diễn giải ở mức danh nghĩa 15% |
| `figures/` | Sáu biểu đồ PNG, gồm lý thuyết, EDA, trước/sau, sai số, biến loại và hai nhóm |
| `src/`, `tests/` | Mã sinh dữ liệu, đánh giá, trực quan và kiểm thử |

MAE và RMSE dùng đơn vị biến số, càng thấp càng tốt. Accuracy lưu dưới dạng tỷ lệ 0–1, càng cao càng tốt. SD trong bảng benchmark mô tả sự dao động của mặt nạ ở cùng một lần chia. Phần chia tỷ trọng lớp dùng mẫu số là số giá trị có mặt ở mỗi giai đoạn. Ô trống ở cột Mode của bảng EDA nghĩa là các giá trị liên tục đều xuất hiện một lần.

## Phạm vi

Dữ liệu và cơ chế thiếu là mô phỏng. Kết quả không suy rộng trực tiếp sang MAR/MNAR, biến có ràng buộc khác hoặc tập dữ liệu thật. Khi toàn bộ cột train thiếu hoặc kiểu biến sai, mã báo lỗi rõ để tránh tạo thống kê vô căn cứ. Các điểm bị boxplot gắn cờ vẫn nằm trong dữ liệu gốc.

Khung môn học dựa trên phần tóm tắt slide 14–17 trong đặc tả đi kèm. Liên kết Drive chưa cung cấp được nội dung PDF trong môi trường này. [Chi tiết nguồn tham khảo](presentation/references.md)
