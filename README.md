# 📘 Dự đoán kết quả bóng đá từ dữ liệu lịch sử

## 🧠 Giới thiệu

* **Tên môn học**: Tiền xử lý và xây dựng bộ dữ liệu
* **Mã môn học**: DS108 - **Lớp**: DS108.P11
* **Năm học**: Học kì 2 - Năm học: 2024 - 2025
* **Giảng viên**: 
  * **Giảng viên lý thuyết**: TS. Nguyễn Gia Tuấn Anh
  * **Giảng viên thực hành**: CN. Trần Quốc Khánh
* **Mục tiêu đồ án**: Đồ án thực hiện cào dữ liệu từ trang web về các trận bóng đá, sau đó tiền xử lý và áp dụng các mô hình học máy để dự đoán kết quả các trận đấu từ tương lai từ dữ liệu là các trận đấu trong lịch sử
# 📂 Mô tả chức năng các file

### 📁 Notebook xử lý và huấn luyện:

- **`DataPreprocessing_Rolling.ipynb`** Tiền xử lý dữ liệu theo tiêu chuẩn *Medallion Architecture* và tạo đặc trưng bằng phương pháp **Rolling Window**.
- **`DataPreprocessing_Rolling_Form.ipynb`** Tương tự như trên nhưng bổ sung đặc trưng từ thông tin **Form** (hiệu suất gần đây của đội bóng).
- **`EDA_Visualization.ipynb`** Trực quan hóa dữ liệu với các biểu đồ phục vụ phân tích và đánh giá.
- **`Main_Rolling.ipynb`** Huấn luyện và kiểm thử các mô hình sử dụng đặc trưng từ **Rolling Window**.
- **`Main_Rolling_Form.ipynb`** Huấn luyện và kiểm thử mô hình với đặc trưng từ **Rolling Window** và **Form**.
- **`TimeSplitValidation.ipynb`** Đánh giá khả năng tổng quát của mô hình bằng kỹ thuật **TimeSeriesSplit** (walk-forward validation).
---

### ⚙️ Chương trình ứng dụng dự đoán:

- **`predictor.py`** Load mô hình và dữ liệu; định nghĩa hàm dự đoán cho giao diện thử nghiệm.
- **`PredictApp.py`** Xây dựng giao diện người dùng bằng **Streamlit**, tương tác với `predictor.py`.

---

### 📊 Dữ liệu:

- **`FPro_data.csv`** Dữ liệu gốc thu thập từ web crawling — tương ứng với **Bronze Layer**.
- **`silver_FPro_data.csv`** Dữ liệu đã được xử lý — đạt chuẩn **Silver Layer**, được tạo bởi các file `DataPreprocessing`.
- **`gold_FPro_data_rolling.csv`** Dữ liệu Silver có thêm đặc trưng **Rolling Window** — đạt chuẩn **Gold Layer**, được tạo bởi `DataPreprocessing_Rolling.ipynb`.
- **`gold_FPro_data_combination.csv`** Dữ liệu Silver có thêm đặc trưng **Rolling Window** và **Form** — đạt chuẩn **Gold Layer**, được tạo bởi `DataPreprocessing_Rolling_Form.ipynb`.
---

### 🤖 Mô hình cuối cùng:

- **`Final_chosen_model.pkl`** Mô hình **XGBoost** với tham số tối ưu, được chọn làm mô hình dự đoán cuối cùng — được lưu từ `Main_Rolling_Form.ipynb`.
---

## 🚀 HƯỚNG DẪN CHẠY GIAO DIỆN DỰ ĐOÁN

1. Cài đặt thư viện
   ```
   pip install streamlit
   ```
2. Trong terminal, di chuyển đến thư mục chứa file **`PredictApp.py`** và chạy lệnh:
   ```
   streamlit run 22520550_22520884_PredictApp.py
   ```
3. Để thoát ứng dụng, nhấn tổ hợp phím **`Ctrl + C`** trong Terminal
---

## Thành viên nhóm: 
| STT    | MSSV          | Họ và Tên              |Vai trò    | Email                   |
| ------ |:-------------:| ----------------------:|----------:|-------------------------:
| 1      |22520550|Lương Anh Huy|Trưởng nhóm| 22520550@gm.uit.edu.vn|
| 2      |22520884|Phan Công Minh|Thành viên| 22520884@gm.uit.edu.vn|


## 🛠️ Công nghệ và thư viện
Python 3.x | Scikit-learn | Numpy | Pandas | Matplotlib | Seaborn | Streamlit | XGBoost

## 📊 Kết quả So sánh Mô hình

### Chiến lược Holdout Validation
* Sử dụng 6 mùa cho huấn luyện và 1 mùa cho kiểm thử
* Các độ đo hiển thị là **Weighted Avg** trong classification report

| Mô hình                     | Accuracy | Precision | Recall | F1-Score
|----------------------------|----------|-----------|--------|--------|
|Logistic Regression + Tham số mặc định + Đặc trưng Rolling | 0.66 | 0.66 | 0.66 | 0.65 |
|Logistic Regression + Tham số tối ưu + Đặc trưng Rolling | 0.70 | 0.69 | 0.70 | 0.69 |
|Logistic Regression + Tham số mặc định + Đặc trưng Rolling + Đặc trưng Form | 0.84 | 0.84 | 0.84 | 0.84 |
|Logistic Regression + Tham số tối ưu + Đặc trưng Rolling + Đặc trưng Form | 0.92 | 0.93 | 0.92 | 0.92 |
|Random Forest + Tham số mặc định + Đặc trưng Rolling | 0.60 | 0.57 | 0.60 | 0.57 |
|Random Forest + Tham số tối ưu + Đặc trưng Rolling | 0.64 | 0.63 | 0.64 | 0.61 |
|Random Forest + Tham số mặc định + Đặc trưng Rolling + Đặc trưng Form | 0.80 | 0.80 | 0.80 | 0.80 |
|Random Forest + Tham số tối ưu + Đặc trưng Rolling + Đặc trưng Form | 0.82 | 0.82 | 0.82 | 0.82 |
|XGBoost + Tham số mặc định + Đặc trưng Rolling | 0.63 | 0.64 | 0.63 | 0.63 |
|XGBoost + Tham số tối ưu + Đặc trưng Rolling | 0.63 | 0.62 | 0.63 | 0.62 |
|XGBoost + Tham số mặc định + Đặc trưng Rolling + Đặc trưng Form | 0.91 | 0.92 | 0.91 | 0.91 |
|XGBoost + Tham số tối ưu + Đặc trưng Rolling + Đặc trưng Form | 0.90 | 0.90 | 0.90 | 0.90 |

### Chiến lược TimeSeriesValidation
* Sử dụng TimeSeriesSplit với `n_splits = 10` để kiểm tra hiệu suất của từng mô hình có duy trì trên nhiều thời điểm không

| Mô hình           | Average Accuracy |
|-------------------|------------------|
|Logistic Regression + Tham số tối ưu + Đặc trưng Rolling + Đặc trưng Form | 0.9043 |
|Random Forest + Tham số tối ưu + Đặc trưng Rolling + Đặc trưng Form | 0.8777 |
|XGBoost + Tham số tối ưu + Đặc trưng Rolling + Đặc trưng Form | 0.9036 |
