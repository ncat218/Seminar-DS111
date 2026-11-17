# DS111 · Điền khuyết bằng Mean, Median và Mode

Bộ seminar tiếng Việt gồm 9 slide cho 13 phút trình bày và 2 phút hỏi đáp. Thực nghiệm dùng dữ liệu thực tế từ **UCI Student Performance** để đo sai số tại các ô được che thử và xem phân phối thay đổi thế nào sau khi điền. [Student Performance — UCI](https://archive.ics.uci.edu/dataset/320/student-performance)

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

Trên macOS/Linux, dùng `.venv/bin/python` và `.venv/bin/jupyter-nbconvert`. Chạy riêng `python -m src.prepare_data` nếu chỉ cần các CSV phân tích. Tác vụ `src.run_experiments` đọc dữ liệu gốc và tái tạo mặt nạ, bảng, kết luận và biểu đồ. Slide đã xuất dùng kết quả của lần chạy kèm theo.

Đã chạy toàn bộ 6 cell mã theo thứ tự trên Python 3.14.4 và lưu bảng, hình vào notebook. Máy tạo bộ seminar thiếu kernel Jupyter. Các lệnh JupyterLab và nbconvert ở trên dành cho môi trường đã cài các thư viện trong `requirements.txt`.

## Dataset và thiết kế

Tập `student-por.csv` gồm **649 dòng của môn tiếng Bồ Đào Nha** tại hai trường trung học. Bản CSV gốc có 33 cột và không có ô thiếu. Project chọn năm cột bên dưới, thêm `row_id` theo thứ tự dòng để ghép mặt nạ với dữ liệu gốc, rồi che thử bốn cột. Chỉ dùng một môn để giữ bối cảnh điểm số nhất quán và tránh tính lặp khi ghép hai tệp môn học. [Student Performance — UCI](https://archive.ics.uci.edu/dataset/320/student-performance)

| Cột | Ý nghĩa và mục đích |
|---|---|
| `G1` | Điểm kỳ đầu, thang 0–20. Vùng trung tâm gần đối xứng. |
| `absences` | Số buổi vắng, có đuôi dài bên phải. Giá trị 0 nghĩa là không vắng. |
| `G3` | Điểm cuối kỳ, thang 0–20. Dùng để so sánh Median toàn cục với Median theo trường. |
| `guardian` | Người giám hộ, gồm `mother`, `father`, `other`. |
| `school` | Mã trường GP hoặc MS. Giữ quan sát đầy đủ để thử thống kê theo trường. |

Demo mô tả dùng một mặt nạ Bernoulli MCAR 15% và fit trên phần quan sát của demo để đo biến dạng của chính cột đó. Benchmark chia riêng train/test 75/25 với seed 42, sau đó che độc lập train và test. Seed mặt nạ 42–53 lặp tại ba mức 5%, 15%, 30%. Mỗi phương pháp so sánh trong cùng lần chạy dùng cùng ô test. Các mức là xác suất che danh nghĩa nên tỷ lệ thực tế dao động. Fit chỉ trên train đã che và chấm chỉ trên test bị che bằng giá trị gốc. Group Median dùng Median toàn cục của train cho nhóm có dưới 20 giá trị quan sát hoặc chưa gặp.

## Vị trí dữ liệu và cách đọc bảng

| Đường dẫn | Nội dung |
|---|---|
| `data/raw/student-por.csv` | CSV gốc do UCI phát hành, phân tách bằng dấu chấm phẩy |
| `data/student_complete.csv` | Năm cột phân tích và chỉ mục dòng, trước khi che |
| `data/student_missing_15pct.csv`, `student_mask_15pct.csv` | Bản quan sát và mặt nạ của demo |
| `results/missing_summary.csv`, `eda_numeric.csv` | Tỷ lệ thiếu thực tế, thống kê và số điểm ngoài hàng rào 1,5 IQR |
| `results/distribution_summary.csv`, `category_frequencies.csv` | Thống kê của dữ liệu gốc, quan sát và sau điền, bao gồm SD mẫu, tương quan và tần suất |
| `results/evaluation.csv` | Trung bình và SD qua các mặt nạ, phân theo mức thiếu, biến, phương pháp và metric |
| `results/evaluation_by_seed.csv` | Điểm và số ô che thực tế theo từng lần lặp |
| [Kết luận thực nghiệm](results/conclusions.md) | Số liệu và diễn giải ở mức danh nghĩa 15% |
| `figures/` | Sáu biểu đồ PNG, gồm lý thuyết, EDA, trước/sau, sai số, người giám hộ và điểm G3 theo trường |
| `src/`, `tests/` | Mã chuẩn bị dữ liệu, đánh giá, trực quan và kiểm thử |

MAE và RMSE dùng đơn vị gốc của biến, càng thấp càng tốt. Accuracy lưu dưới dạng tỷ lệ 0–1, càng cao càng tốt. SD trong bảng benchmark mô tả sự dao động của mặt nạ ở cùng một lần chia. Tỷ trọng lớp dùng mẫu số là số giá trị có mặt ở mỗi giai đoạn. Điểm và số buổi vắng là biến rời rạc. Benchmark giữ nguyên giá trị dự đoán lẻ để đánh giá dưới hàm mất mát đã chọn. Nếu hệ thống yêu cầu đầu ra nguyên, cần quy định rồi kiểm thử việc làm tròn.

## Phạm vi

Dữ liệu gốc là quan sát thực tế. Các ô thiếu xuất hiện từ mặt nạ do project tạo, vì vậy benchmark đo khả năng điền dưới MCAR. Kết quả giới hạn ở môn học, mẫu và lần chia đã dùng. Khi toàn bộ cột train thiếu hoặc kiểu biến sai, mã báo lỗi rõ để tránh tạo thống kê vô căn cứ. Giữ các điểm bị boxplot gắn cờ, kể cả điểm 0 và số buổi vắng bằng 0.

Dữ liệu của Paulo Cortez, *Student Performance* (2014), UCI Machine Learning Repository, DOI 10.24432/C5TG7T. Tệp gốc được giữ nguyên, các tệp phân tích là trích cột và tạo mặt nạ bởi project. [Nguồn UCI](https://doi.org/10.24432/C5TG7T) · [Giấy phép CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Khung môn học dựa trên phần tóm tắt slide 14–17 trong đặc tả đi kèm. Liên kết Drive chưa cung cấp được nội dung PDF trong môi trường này. [Chi tiết nguồn tham khảo](presentation/references.md)
