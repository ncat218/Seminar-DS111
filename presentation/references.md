# Nguồn và phạm vi seminar

## Tài liệu môn DS111

Đặc tả đi kèm tóm tắt slide 14–17 của `Bai04_EDA.pdf` dựa trên ảnh chụp. Slide 14 đặt bối cảnh phân tích đơn biến, xu hướng trung tâm, độ phân tán và loại biểu đồ. Slide 15 minh họa ba hình dạng phân phối. Slide 16 giao mini seminar về điền khuyết. Slide 17 đặt câu hỏi về đa Mode. Truy cập liên kết qua công cụ tra cứu và từ máy làm việc đều chưa lấy được nội dung PDF, vì vậy mô tả trên dựa vào đặc tả. [Thư mục tài liệu của giảng viên](https://drive.google.com/drive/folders/1bMDbXUcBRzf-S_oPd2zcb0URljpDWD7d)

## Phần mở rộng

- Dự đoán hằng số là phạm vi xét khi liên hệ thống kê trung tâm với tổn thất. Các chiến lược Mean và Median được định nghĩa trong bộ dự đoán cơ sở. [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html)
- Mode chọn lớp phổ biến nhất khi dùng dự đoán cố định theo chi phí đúng/sai bằng nhau. [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)

- Định nghĩa thước đo vị trí, sự nhạy với đuôi phân phối và cách hiểu Mode cho biến liên tục. [NIST/SEMATECH, Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm)
- Skewness Fisher–Pearson dùng moment bậc ba chuẩn hóa. Khối lượng ở xa tâm có ảnh hưởng mạnh lên hệ số. Các thứ tự Mean/Median/Mode trên slide 4 là ví dụ của Normal, Gamma và Gamma phản chiếu. Skewness bằng 0 hoặc Mean gần Median đều có thể xuất hiện ngoài phân phối chuẩn. [NIST/SEMATECH, Measures of Skewness and Kurtosis](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm)
- Cơ chế thiếu và điều kiện suy luận khi quá trình tạo thiếu phụ thuộc dữ liệu. Seminar mô phỏng MCAR để có ground truth và tập trung vào ba phương pháp điền hằng số. [Rubin (1976), Inference and Missing Data](https://doi.org/10.1093/biomet/63.3.581)
- Mean, Median và Mode dùng `SimpleImputer`. `most_frequent` chọn giá trị nhỏ nhất khi hòa, với nhãn chuỗi đồng nhất là thứ tự từ điển. [Tài liệu SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
- Train/test chia trước khi fit tiền xử lý. Trong cross-validation, đưa imputer vào pipeline để fit trong từng fold. [scikit-learn, Data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)

## Dữ liệu thực nghiệm

Paulo Cortez (2014), *Student Performance*, UCI Machine Learning Repository, DOI 10.24432/C5TG7T. Dùng `student-por.csv`, 649 dòng môn tiếng Bồ Đào Nha tại hai trường trung học. Sao chép tệp gốc và ghi riêng bản trích cột, bản che nhân tạo và mặt nạ. Kết quả benchmark và biểu đồ được tính từ các tệp này. [Dữ liệu và từ điển biến](https://archive.ics.uci.edu/dataset/320/student-performance) · [Giấy phép CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Ví dụ tính tay tuổi, Size và đa Mode lấy từ đặc tả. Ba đường mật độ minh họa dùng Normal, Gamma và Gamma phản chiếu.
