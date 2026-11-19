# Phân phối dữ liệu và thước đo xu hướng trung tâm

Tài liệu học sâu đi kèm seminar. Phần I giải thích cách đọc phân phối. Phần II trình bày đầy đủ định nghĩa và cơ sở toán học dùng Mean, Median, Mode làm giá trị điền. Những phần chứng minh chi tiết dùng để chuẩn bị hỏi đáp.

## I. Phân phối dữ liệu (Data Distribution)

Phân phối mô tả các giá trị xuất hiện ở đâu và phổ biến đến mức nào. Khi dùng một thống kê để điền cả cột, cần hiểu thống kê đó đại diện cho vùng nào của phân phối.

### 1. Phân phối đối xứng (Symmetric Distribution)

Hai phía quanh tâm có hình dạng đối xứng. Với phân phối đối xứng, một đỉnh duy nhất tại tâm, Mean tồn tại và Median xác định tại tâm, ta có ba tâm trùng nhau ở mức tổng thể. Trong một mẫu hữu hạn, thường thấy

\[
\operatorname{Mean}\approx\operatorname{Median}\approx\operatorname{Mode}.
\]

Mean là lựa chọn đáng thử nếu dữ liệu định lượng, phần quan sát đại diện phù hợp, ít điểm cực đoan nghiêm trọng và mục tiêu liên quan sai số bình phương. Phân phối đối xứng còn có thể là tam giác hoặc nhiều dạng khác. Đối xứng riêng nó chưa bảo đảm Mean tồn tại, chẳng hạn với Cauchy. [NIST, Measures of Location](https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm)

### 2. Phân phối lệch phải (Right-skewed Distribution)

Đuôi kéo về phía các giá trị lớn. Thu nhập, giá nhà hoặc chi phí y tế có thể xuất hiện dạng này tùy mẫu và phạm vi khảo sát. Trong dạng một đỉnh điển hình được minh họa bằng Gamma, thường thấy

\[
\operatorname{Mode}<\operatorname{Median}<\operatorname{Mean}.
\]

Mean dùng độ lớn của mọi điểm nên một số giá trị rất lớn có thể kéo nó về đuôi. Median dựa trên thứ hạng nên thường gần vùng phổ biến hơn.

### 3. Phân phối lệch trái (Left-skewed Distribution)

Đuôi kéo về phía các giá trị nhỏ. Một bài kiểm tra dễ có nhiều điểm cao và một số ít điểm rất thấp có thể cho hình dạng này. Với ví dụ Gamma phản chiếu,

\[
\operatorname{Mean}<\operatorname{Median}<\operatorname{Mode}.
\]

Các giá trị nhỏ ở đuôi có thể kéo Mean xuống. Ba thứ tự trên là quan hệ của các dạng minh họa thường gặp. Một đỉnh tự nó chưa bảo đảm thứ tự ấy cho mọi phân phối.

### 4. Skewness và Outliers

**Skewness** là hệ số bất đối xứng. Một dạng Fisher–Pearson dùng moment bậc ba chuẩn hóa,

\[
g_1=\frac{\frac{1}{n}\sum_i(x_i-\bar{x})^3}
{\left(\frac{1}{n}\sum_i(x_i-\bar{x})^2\right)^{3/2}}.
\]

pandas `skew()` dùng hệ số đã hiệu chỉnh theo cỡ mẫu. Công thức trên cần độ phân tán khác 0.

| Skewness | Cách đọc và kiểm tra |
|---|---|
| Gần 0 | Ít bất đối xứng theo moment bậc ba. Xem histogram để kiểm tra hình dạng, nhiều đỉnh và đuôi |
| Dương | Thường có xu hướng lệch phải |
| Âm | Thường có xu hướng lệch trái |

Skewness gần 0 chưa đủ suy ra đối xứng hoặc chuẩn. Các thành phần của moment có thể bù nhau. Chọn phương pháp cần kết hợp histogram, boxplot, miền giá trị và cách thu thập dữ liệu. Ngưỡng skewness phù hợp phụ thuộc bối cảnh. [NIST, Skewness and Kurtosis](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm)

**Outlier** là quan sát khác biệt đáng kể so với cấu trúc thường gặp. Một cách gắn cờ dùng khoảng tứ phân vị,

\[
IQR=Q_3-Q_1.
\]

Điểm ngoài hàng rào

\[
[Q_1-1.5IQR,\ Q_3+1.5IQR]
\]

được đánh dấu để kiểm tra. Trong demo absences, Q1 = 0, Q3 = 6 và IQR = 6. Hai hàng rào là −9 và 15 buổi, có 18 điểm lớn hơn 15 bị gắn cờ. Giá trị vắng 0 buổi được giữ như quan sát hợp lệ.

Hàng rào gắn cờ ứng viên ngoại lệ. Cần kiểm tra nguyên nhân và ảnh hưởng trước khi sửa hoặc xóa. Râu boxplot thường dừng ở quan sát xa nhất còn nằm trong hàng rào, nên vị trí râu có thể khác vị trí hàng rào. [NIST, Detection of Outliers](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm)

## II. Thước đo xu hướng trung tâm (Measures of Central Tendency)

### 1. Mean — trung bình cộng

Với $n$ giá trị định lượng quan sát hợp lệ $X=\{x_1,\ldots,x_n\}$,

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i.
\]

Mean dùng độ lớn của toàn bộ giá trị. Nếu một quan sát tăng thêm $\Delta$, Mean tăng thêm $\Delta/n$, nên dễ bị ảnh hưởng bởi điểm cực đoan.

Với mẫu tuổi [20, 22, 23, 25, 80], Mean = 170/5 = 34. Nếu đổi 80 thành 800, Mean thành 890/5 = 178. Việc Mean thay đổi mạnh phản ánh độ nhạy của phép tổng. Tuổi 80 vẫn có thể là dữ liệu hợp lệ.

### 2. Median — trung vị

Sắp xếp tăng dần thành $x_{(1)}\le\ldots\le x_{(n)}$. Với biến định lượng,

\[
\tilde{x}=
\begin{cases}
x_{((n+1)/2)}, & n\text{ lẻ},\\
\frac{x_{(n/2)}+x_{(n/2+1)}}{2}, & n\text{ chẵn}.
\end{cases}
\]

Với mẫu tuổi năm số, Median là số thứ ba, bằng 23. Với [20, 22, 23, 25], Median = (22 + 23)/2 = 22,5.

Median có tính **robust**, tức ít nhạy hơn với một vài điểm cực đoan. Đổi 80 thành 800 giữ Median bằng 23 vì hai giá trị đều đứng cuối và thứ hạng ở giữa giữ nguyên. Median vẫn phụ thuộc vào thành phần mẫu và cơ chế thiếu.

### 3. Mode — mốt

Tập các giá trị có tần suất cực đại được viết

\[
\operatorname{Modes}(X)=\operatorname*{arg\,max}_v\operatorname{Count}(v).
\]

Nếu nghiệm duy nhất, gọi giá trị ấy là Mode. Mode phù hợp với nhãn loại như nhóm máu, loại sản phẩm, chuyên ngành hoặc người giám hộ.

- [M, M, L, S, M] có Mode M, xuất hiện ba lần.
- [2, 2, 3, 8, 8] có hai Mode 2 và 8. Mean bằng 4,6 và Median bằng 3.
- Nếu mọi giá trị xuất hiện một lần, phép đếm chưa cho một Mode duy nhất. Với biến liên tục, đỉnh mật độ hoặc khoảng histogram phổ biến là cách mô tả khác, phụ thuộc lựa chọn ước lượng.

Cần công bố cách phân xử khi hòa. `SimpleImputer(strategy="most_frequent")` chọn giá trị nhỏ nhất trong các giá trị đồng mốt. Mã số của nhãn danh nghĩa vẫn cần được xem là nhãn, thay vì tự động lấy trung bình. [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)

### 4. Vì sao ba thống kê dùng được để điền khuyết?

Khi chỉ dự đoán cùng một hằng số $a$ cho cột, cần xác định mức phạt cho sai số. Ba thống kê giải ba bài toán tối ưu khác nhau.

| Thước đo | Tiêu chí | Ý nghĩa |
|---|---|---|
| Mean | Sai số bình phương | Giảm tổng bình phương độ lệch |
| Median | Sai số tuyệt đối | Giảm tổng khoảng cách tuyệt đối |
| Mode | Sai số nhãn 0–1 | Giảm số lần đoán sai với dự đoán cố định |

**Mean tối thiểu hóa tổng sai số bình phương.**

\[
\bar{x}=\operatorname*{arg\,min}_{a\in\mathbb R}\sum_i(x_i-a)^2.
\]

Có thể chứng minh bằng

\[
\sum_i(x_i-a)^2=\sum_i(x_i-\bar{x})^2+n(a-\bar{x})^2.
\]

Vế đầu độc lập với $a$, vế sau nhỏ nhất khi $a=\bar{x}$. Chia cho $n$ hoặc lấy căn sau khi chia đều giữ nguyên điểm tối ưu, nên kết quả áp dụng cho MSE và RMSE.

**Median tối thiểu hóa tổng sai số tuyệt đối.**

\[
\tilde{x}\in\operatorname*{arg\,min}_{a\in\mathbb R}\sum_i|x_i-a|.
\]

Dịch $a$ sang phải làm khoảng cách với điểm bên trái tăng và với điểm bên phải giảm. Tổng nhỏ nhất tại vị trí cân bằng số điểm hai phía theo nghĩa trung vị. Với $n$ chẵn, cả khoảng giữa hai số giữa đều là nghiệm. Trung bình hai số giữa là một lựa chọn, vì vậy công thức dùng ký hiệu thuộc tập nghiệm.

**Mode tối thiểu hóa số lần đoán sai.**

\[
x_{\mathrm{mode}}\in\operatorname*{arg\,min}_a\sum_i\mathbf{1}(x_i\ne a).
\]

Vì $\sum_i\mathbf{1}(x_i\ne a)=n-\operatorname{Count}(a)$, chọn nhãn xuất hiện nhiều nhất làm số lần sai nhỏ nhất. Có thể có nhiều nghiệm đồng hạng.

### 5. Từ tối ưu trên mẫu đến ước lượng giá trị bị thiếu

Các kết quả trên chứng minh tối ưu trong phạm vi **một dự đoán hằng số trên tập dùng để tối ưu**. Khi dùng cho ô thiếu, Mean/Median/Mode từ phần quan sát là ước lượng cho các đại lượng tương ứng của phân phối cần dự đoán.

Cần giả định phần quan sát đủ đại diện cho phần thiếu hoặc nhóm đang xét. MCAR là điều kiện thuận lợi theo cơ chế che. Với các quan hệ có điều kiện, có thể cần thống kê theo nhóm hoặc phương pháp dùng thêm biến. Tối ưu trên train chưa bảo đảm thứ hạng trên mọi test.

Ở mẫu tuổi, MAE trên năm số đã quan sát nhỏ nhất tại 23 và RMSE nhỏ nhất tại 34. Tuổi thật ở ô NaN vẫn chưa biết. Trên absences của Student Performance, benchmark MCAR 15% cho MAE Median = 2,52 và Mean = 2,83, nhưng RMSE Mean = 3,69 và Median = 3,86. Các kết quả này minh họa vai trò của hàm mất mát khi lựa chọn phương pháp.
