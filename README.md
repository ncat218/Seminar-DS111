# DS111 · Điền khuyết bằng Mean, Median và Mode

Bộ seminar có **bản đầy đủ 24 slide, khoảng 25 phút** và **bản chọn 13 slide cho 13 phút nói + 2 phút hỏi đáp**. Nội dung đi từ chứng minh toán học cho Mean/Median/Mode đến khôi phục ô thiếu, biến dạng phân phối và **huấn luyện thật Ridge, Random Forest để dự đoán G3** trên UCI Student Performance. [Student Performance — UCI](https://archive.ics.uci.edu/dataset/320/student-performance)

## Trình chiếu

[Bản thuyết trình đầy đủ dạng PDF](output/pdf/ban_thuyet_trinh_day_du.pdf) có 32 trang A4, gồm lời thoại biên tập cho đủ 24 slide, câu chuyển ý cụ thể, hướng dẫn chỉ hình, giải thích học thuật và phụ lục. Mỗi slide có một trang lời thoại riêng. Mục lục và bookmark giúp tra nhanh. Bản này dùng khoảng 25 phút trình bày; lộ trình 15 phút có lời thoại rút gọn riêng bên dưới.

Bài đi theo ba câu hỏi. Vì sao giá trị đại diện có thể ước lượng ô thiếu? Khi nào thay thế hợp lý? Dữ liệu sau điền sai lệch ra sao? Ví dụ tuổi được nối với lựa chọn hằng số theo hàm mất mát, điều kiện đại diện của phần quan sát và kiểm chứng trên dữ liệu thực tế.

- [PowerPoint đầy đủ 24 slide](presentation/seminar_day_du.pptx) · [PDF đầy đủ](presentation/seminar_day_du.pdf).
- [PowerPoint 15 phút](presentation/seminar_15min_cap_nhat.pptx) · [PDF 15 phút](presentation/seminar_15min_cap_nhat.pdf) · [lời thoại 15 phút](presentation/speaker_notes_15min.md).
- [Lộ trình và ánh xạ slide](presentation/lo_trinh_15phut.md). PowerPoint có speaker notes; PDF dùng ảnh render 1920 × 1080 để trình chiếu dự phòng.
- [Lời thoại có mốc giờ](presentation/speaker_notes.md), [nội dung từng slide](presentation/slide_content.md), [câu hỏi phản biện](presentation/questions_answers.md) và [nguồn tham khảo](presentation/references.md).
- [Script có thuật ngữ và giải thích mã](presentation/script_va_thuat_ngu.md) dành cho ôn tập và hỏi đáp.
- [Notebook đã lưu đầu ra](notebooks/seminar_imputation.ipynb) có thể dùng để mở phần demo hoặc kết quả.

[Lý thuyết đầy đủ](presentation/ly_thuyet.md) gồm các dạng phân phối, skewness và IQR, công thức Mean/Median/Mode, ba bài toán tối ưu cùng chứng minh.

Để xuất lại PDF lời thuyết trình từ [nguồn lời thoại đã biên tập](presentation/script_pdf_content.json):

```powershell
python -m pip install -r requirements-pdf.txt
python -m src.build_speech_pdf
```

Mã dùng Arial trên Windows hoặc DejaVu Sans trên Linux; có thể truyền `--font-dir`. Đầu ra mặc định ở `output/pdf/ban_thuyet_trinh_day_du.pdf`. Lệnh này chỉ dàn trang lời thoại và đọc bảng kết quả hiện có.

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
.\.venv\Scripts\jupyter-nbconvert.exe --to notebook --execute --ExecutePreprocessor.timeout=600 --inplace notebooks/seminar_imputation.ipynb
```

Trên macOS/Linux, dùng `.venv/bin/python` và `.venv/bin/jupyter-nbconvert`. Chạy riêng `python -m src.prepare_data` nếu chỉ cần các CSV phân tích. Tác vụ `src.run_experiments` đọc dữ liệu gốc và tái tạo mặt nạ, bảng, kết luận và biểu đồ. Slide đã xuất dùng kết quả của lần chạy kèm theo.

Notebook đã lưu bảng và hình từ các cell chạy theo thứ tự trên Python 3.14.4. Các lệnh JupyterLab và nbconvert ở trên dành cho môi trường đã cài các thư viện trong `requirements.txt`. Phần kiểm tra tại workspace thực thi mã cell trực tiếp bằng Python, do môi trường tạo file thiếu kernel Jupyter.

## Dataset và thiết kế

Tập `student-por.csv` gồm **649 dòng của môn tiếng Bồ Đào Nha** tại hai trường trung học. Bản CSV gốc có 33 cột và không có ô thiếu. Thí nghiệm khôi phục chọn năm cột bên dưới, thêm `row_id` theo thứ tự dòng để ghép mặt nạ với dữ liệu gốc, rồi che thử bốn cột. Chỉ dùng một môn để giữ bối cảnh điểm số nhất quán và tránh tính lặp khi ghép hai tệp môn học. [Student Performance — UCI](https://archive.ics.uci.edu/dataset/320/student-performance)

| Cột | Ý nghĩa và mục đích |
|---|---|
| `G1` | Điểm kỳ đầu, thang 0–20. Vùng trung tâm gần đối xứng. |
| `absences` | Số buổi vắng, có đuôi dài bên phải. Giá trị 0 nghĩa là không vắng. |
| `G3` | Điểm cuối kỳ, thang 0–20. Dùng để so sánh Median toàn cục với Median theo trường. |
| `guardian` | Người giám hộ, gồm `mother`, `father`, `other`. |
| `school` | Mã trường GP hoặc MS. Giữ quan sát đầy đủ để thử thống kê theo trường. |

Demo mô tả dùng một mặt nạ Bernoulli MCAR 15% và fit trên phần quan sát của demo để đo biến dạng của chính cột đó. Benchmark chia riêng train/test 75/25 với seed 42, sau đó che độc lập train và test. Seed mặt nạ 42–53 lặp tại ba mức 5%, 15%, 30%. Mỗi phương pháp so sánh trong cùng lần chạy dùng cùng ô test. Các mức là xác suất che danh nghĩa nên tỷ lệ thực tế dao động. Fit chỉ trên train đã che và chấm chỉ trên test bị che bằng giá trị gốc. Group Median dùng Median toàn cục của train cho nhóm có dưới 20 giá trị quan sát hoặc chưa gặp.

## Huấn luyện mô hình sau khi điền

Chạy `python -m src.run_experiments` tái tạo cả hai thí nghiệm. Chạy riêng `python -m src.run_model_experiments` để chỉ tái tạo mô hình. Seed cố định; không cần tải thêm dữ liệu.

**Bài toán:** dự đoán G3 từ G1, G2, age, absences, guardian, school. G3 luôn đầy đủ và không nằm trong X. Bối cảnh là sau khi có G1/G2; không diễn giải thành dự báo đầu năm.

**Thiết kế:** 5 lần chia 75/25 (seed 42–46) × 4 mặt nạ (42–45) × mức thiếu 5%, 15%, 30%. Che cả sáu đầu vào bằng MCAR. Biến số so Mean/Median/Mode, biến loại đều dùng Mode. Mỗi phương pháp nhận cùng hàng và mặt nạ. Pipeline fit imputer, one-hot và mô hình chỉ từ train; Ridge chuẩn hóa thêm biến số. Ridge alpha=1; Random Forest 100 cây, min_samples_leaf=3, random_state=42. Tổng cộng **370 lần fit**, gồm 360 cấu hình có thiếu và 10 mốc đầy đủ; siêu tham số cố định trước.

**Chấm:** MAE, RMSE, R² của G3 trên mọi dòng test. Hai pha dùng cùng pipeline đã học từ train thiếu để dự đoán test đầy đủ và test thiếu. Mốc đầy đủ dùng cùng split. Mean ± SD mô tả 20 tổ hợp chia/che tại mỗi mức. Các lần chia chồng lấn nên SD không phải CI từ các mẫu độc lập.

| Mô hình | Đầy đủ, RMSE | Điền Mean | Điền Median | Điền Mode |
|---|---:|---:|---:|---:|
| Ridge | 1,379 | 1,728 | 1,734 | 1,748 |
| Random Forest | 1,359 | 1,614 | 1,640 | 1,646 |

Mức 15% ở cả train và test, đơn vị điểm G3. Trong thiết kế này, sai số tăng khi đầu vào thiếu; chênh giữa cách điền nhỏ hơn mức tăng so với mốc đầy đủ. Median giảm MAE khôi phục absences không bảo đảm RMSE G3 thấp nhất trong pipeline nhiều biến. Chưa xác lập ý nghĩa thống kê cho chênh lệch nhỏ. [Báo cáo mô hình](results/model_conclusions.md).

## Vị trí dữ liệu và cách đọc bảng

| Đường dẫn | Nội dung |
|---|---|
| `data/raw/student-por.csv` | CSV gốc do UCI phát hành, phân tách bằng dấu chấm phẩy |
| `data/student_complete.csv` | Năm cột phân tích và chỉ mục dòng, trước khi che |
| `data/student_missing_15pct.csv`, `student_mask_15pct.csv` | Bản quan sát và mặt nạ của demo |
| `data/student_model_complete.csv` | Sáu đầu vào và G3 đầy đủ cho thí nghiệm mô hình |
| `data/student_model_missing_15pct.csv`, `student_model_mask_15pct.csv` | Ví dụ chia/che seed 42, có tập train/test, G3 giữ đầy đủ |
| `results/missing_summary.csv`, `eda_numeric.csv` | Tỷ lệ thiếu thực tế, thống kê và số điểm ngoài hàng rào 1,5 IQR |
| `results/distribution_summary.csv`, `category_frequencies.csv` | Thống kê của dữ liệu gốc, quan sát và sau điền, bao gồm SD mẫu, tương quan và tần suất |
| `results/evaluation.csv` | Trung bình và SD qua các mặt nạ, phân theo mức thiếu, biến, phương pháp và metric |
| `results/evaluation_by_seed.csv` | Điểm và số ô che thực tế theo từng lần lặp |
| `results/paired_comparisons.csv` | Hiệu Median trừ Mean, số lần thắng và hòa trên cùng mặt nạ |
| `results/constant_prediction_loss.csv` | Sai số dự đoán hằng số trên năm tuổi đã quan sát |
| `results/correlation_repeats.csv` | Tương quan G3–GP qua 300 mặt nạ MCAR 15%, seed 0–299 |
| `results/zero_grade_sensitivity.csv` | Benchmark G3 sau khi loại điểm 0 rồi chia lại, dùng như phân tích độ nhạy |
| `results/model_evaluation.csv`, `model_evaluation_by_run.csv` | MAE/RMSE/R² và thay đổi dự đoán theo lần chạy, pha và nhóm hàng |
| `results/model_reference.csv`, `model_reference_by_split.csv` | Mô hình đầy đủ và mốc dự đoán Mean train |
| `results/model_predictions.csv` | Từng G3 thật, dự đoán, mốc tham chiếu và cờ đầu vào thiếu |
| `results/model_split_assignments.csv`, `model_evidence.json` | Chỉ mục train/test, seed, cấu hình, số lần fit và bảng tổng hợp |
| `results/model_coefficients.csv` | Ví dụ hệ số Ridge; thang chuẩn hóa thay đổi, không suy luận nhân quả |
| [Phiên bản chạy](results/runtime_versions.json), [kiểm tra đầu ra](results/validation_report.json) | Môi trường thực nghiệm và kiểm tra chéo file |
| [Kết luận mô hình](results/model_conclusions.md) | Ảnh hưởng đến dự đoán, hai pha test và giới hạn |
| [Kết luận thực nghiệm](results/conclusions.md) | Số liệu và diễn giải ở mức danh nghĩa 15% |
| `figures/` | Mười một biểu đồ PNG, gồm lý thuyết, EDA, trước/sau, sai số điền, G3 theo trường và ba hình kết quả mô hình |
| `src/`, `tests/` | Mã chuẩn bị dữ liệu, đánh giá, trực quan và kiểm thử |

MAE và RMSE dùng đơn vị gốc của biến, càng thấp càng tốt. Accuracy lưu dưới dạng tỷ lệ 0–1, càng cao càng tốt. SD trong bảng benchmark mô tả sự dao động của mặt nạ ở cùng một lần chia. Tỷ trọng lớp dùng mẫu số là số giá trị có mặt ở mỗi giai đoạn. Điểm và số buổi vắng là biến rời rạc. Benchmark giữ nguyên giá trị dự đoán lẻ để đánh giá dưới hàm mất mát đã chọn. Nếu hệ thống yêu cầu đầu ra nguyên, cần quy định rồi kiểm thử việc làm tròn.

## Phạm vi

Dữ liệu gốc là quan sát thực tế. Các ô thiếu xuất hiện từ mặt nạ do project tạo, vì vậy benchmark đo khả năng điền dưới MCAR. Kết quả giới hạn ở môn học, mẫu và lần chia đã dùng. Khi toàn bộ cột train thiếu hoặc kiểu biến sai, mã báo lỗi rõ để tránh tạo thống kê vô căn cứ. Giữ các điểm bị boxplot gắn cờ, kể cả điểm 0 và số buổi vắng bằng 0.

Dữ liệu của Paulo Cortez, *Student Performance* (2014), UCI Machine Learning Repository, DOI 10.24432/C5TG7T. Tệp gốc được giữ nguyên, các tệp phân tích là trích cột và tạo mặt nạ bởi project. [Nguồn UCI](https://doi.org/10.24432/C5TG7T) · [Giấy phép CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Khung môn học dựa trên phần tóm tắt slide 14–17 trong đặc tả đi kèm. Liên kết Drive chưa cung cấp được nội dung PDF trong môi trường này. [Chi tiết nguồn tham khảo](presentation/references.md)
