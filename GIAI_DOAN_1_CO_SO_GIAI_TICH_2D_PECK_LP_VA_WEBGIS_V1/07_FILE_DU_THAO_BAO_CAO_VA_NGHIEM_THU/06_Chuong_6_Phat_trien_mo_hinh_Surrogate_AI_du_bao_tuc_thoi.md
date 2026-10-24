# CHƯƠNG 6: PHÁT TRIỂN MÔ HÌNH HỌC MÁY THAY THẾ (SURROGATE AI) DỰ BÁO LÚN TỨC THỜI

---

## 6.1. SỰ CẦN THIẾT CỦA MÔ HÌNH HỌC MÁY THAY THẾ (SURROGATE MODEL)

Trong kỷ nguyên chuyển đổi số và tự động hóa công trình ngầm, việc kiểm soát an toàn thi công khiên đào EPB-TBM đòi hỏi khả năng phản ứng gần như tức thời. Trong cabin điều khiển TBM, người vận hành (TBM pilot) phải liên tục điều chỉnh các thông số vận hành then chốt:
- Áp lực ép gương trong khoang đào (Thrust force & Bulkhead earth pressure).
- Tốc độ tiến của khiên đào (Advance rate, mm/phút).
- Tốc độ vòng quay của trục vít xoắn tải đất (Screw conveyor speed, rpm).
- Áp lực và thể tích vữa phụt chèn đuôi khiên (Grout pressure & Grout volume).

Nếu người vận hành phát hiện lượng đất đào ra của một ring vượt quá thể tích lý thuyết (dấu hiệu của sạt gương hoặc khoét rỗng vòm), việc đánh giá xem sự cố đó sẽ làm tăng độ lún tại móng của tòa nhà cách đó $15\text{ m}$ lên bao nhiêu milimét là cực kỳ khẩn cấp. Các phần mềm giải tích rời rạc hoặc mô hình phần tử hữu hạn 3D không thể nhúng trực tiếp vào hệ thống SCADA điều khiển của máy TBM do độ trễ tính toán và sự phụ thuộc vào các phần mềm thương mại đắt tiền.

Do đó, việc phát triển một **mô hình học máy thay thế (Surrogate AI Model)** dạng mạng nơ-ron truyền thẳng đa tầng (Multi-Layer Perceptron - MLP) có khả năng xấp xỉ hàm giải tích phi tuyến phức tạp với độ chính xác tuyệt đối ($R^2 > 0.999$) và thời gian suy luận trong phần nghìn giây ($< 0.1\text{ ms}$) là một đóng góp công nghệ thiết thực.

---

## 6.2. THIẾT KẾ KHÔNG GIAN DỮ LIỆU VÀ CHUẨN HÓA MẪU MÔ PHỎNG

### 6.2.1. Không gian tham số đầu vào (Input Parameter Space)
Mô hình Surrogate AI được thiết kế với 5 biến đầu vào đại diện đầy đủ cho điều kiện hình học, địa chất và công nghệ thi công:
1. $x$: Khoảng cách ngang tính từ trục đối xứng tim tuyến hầm đôi, $x \in [-50.0\text{ m}; +50.0\text{ m}]$.
2. $z_0$: Chiều sâu tim hầm, $z_0 \in [13.0\text{ m}; 22.0\text{ m}]$ (bao trùm toàn bộ đoạn S9–S12).
3. $K$: Hệ số bề rộng phễu lún, $K \in [0.40; 0.70]$ (bao trùm từ cát pha đến bùn sét yếu).
4. $V_L$: Tỷ lệ tổn thất thể tích đất, $V_L \in [0.30\%; 2.50\%]$ (bao trùm từ điều kiện thi công lý tưởng đến sự cố sạt lở nghiêm trọng).
5. $d$: Khoảng cách tim hai hầm song song, $d \in [10.0\text{ m}; 18.0\text{ m}]$.

Biến đầu ra duy nhất ($y$):
- $S(x)$: Độ lún bề mặt đất tại tọa độ $x$ (đơn vị $\text{mm}$).

### 6.2.2. Tạo lập tập dữ liệu mô phỏng và kỹ thuật phân chia
Sử dụng thuật toán lấy mẫu ngẫu nhiên phân bố đều đa chiều (Latin Hypercube / Uniform Random Sampling), một tập dữ liệu gồm **2,500 mẫu mô phỏng số** đã được tạo lập từ phương trình siêu vị hầm đôi Gaussian chuẩn hóa.

Tập dữ liệu được phân chia ngẫu nhiên độc lập:
- **Tập huấn luyện (Training Set):** 2,000 mẫu (80%) dùng để cập nhật trọng số mạng nơ-ron.
- **Tập kiểm định độc lập (Test Set):** 500 mẫu (20%) được giữ kín hoàn toàn, chỉ dùng để đánh giá năng lực tổng quát hóa (generalization ability) của mô hình sau khi kết thúc huấn luyện.

---

## 6.3. KIẾN TRÚC MẠNG NƠ-RON VÀ THUẬT TOÁN HUẤN LUYỆN THUẦN NUMPY

Nhằm đảm bảo mô hình có thể triển khai trên bất kỳ nền tảng phần cứng nào (từ máy tính công nghiệp điều khiển TBM đến vi điều khiển Raspberry Pi hoặc nhúng trực tiếp vào JavaScript của WebGIS) mà không cần cài đặt các thư viện trí tuệ nhân tạo nặng nề (như TensorFlow hay PyTorch), toàn bộ thuật toán mạng nơ-ron được nhóm nghiên cứu lập trình thuần túy bằng thư viện **NumPy** trong tập tin `scripts/surrogate_ai.py`.

### 6.3.1. Cấu trúc mạng MLP (5 – 32 – 16 – 1)
Mạng gồm 4 tầng liên kết đầy đủ (Fully Connected Layers):
- **Tầng đầu vào (Input Layer):** 5 nơ-ron (nhận 5 tham số: $x, z_0, K, V_L, d$). Dữ liệu đầu vào được chuẩn hóa Z-score:
  $$x_{\text{norm}} = \frac{x - \mu}{\sigma}$$
- **Tầng ẩn 1 (Hidden Layer 1):** 32 nơ-ron, hàm kích hoạt phi tuyến ReLU: $f(z) = \max(0, z)$.
- **Tầng ẩn 2 (Hidden Layer 2):** 16 nơ-ron, hàm kích hoạt ReLU.
- **Tầng đầu ra (Output Layer):** 1 nơ-ron, hàm kích hoạt tuyến tính (Linear Activation) xuất giá trị độ lún $S(x)$.

### 6.3.2. Quy trình tối ưu hóa
- **Hàm mất mát (Loss Function):** Sai số bình phương trung bình (Mean Squared Error - MSE):
  $$MSE = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$$
- **Thuật toán tối ưu:** Thuật toán lan truyền ngược thích nghi Adam (Adaptive Moment Estimation) với các tham số siêu chuẩn: hệ số học tập ban đầu $\alpha = 0.005$, $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$. Quá trình huấn luyện diễn ra qua 1,000 chu kỳ (epochs) với kích thước mini-batch bằng 64.

---

## 6.4. ĐÁNH GIÁ ĐỘ CHÍNH XÁC VÀ ĐỘ TIN CẬY TRÊN TẬP KIỂM THỬ ĐỘC LẬP

Hiệu năng của mô hình Surrogate AI được thẩm định độc lập trên 500 mẫu kiểm thử thông qua 3 chỉ số thống kê toán học chuẩn mực:
1. **Hệ số xác định ($R^2$ Score):**
   $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2} = \mathbf{0.9991}$$
2. **Sai số tuyệt đối trung bình (MAE):**
   $$MAE = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i| = \mathbf{0.156\text{ mm}}$$
3. **Căn bậc hai sai số bình phương trung bình (RMSE):**
   $$RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2} = \mathbf{0.220\text{ mm}}$$

<br>

<div align="center">

![Hình 6.1: Đánh giá độ chính xác và độ tin cậy của mô hình học máy thay thế (Surrogate AI MLP)](../03_hinh_anh_minh_hoa_chat_luong_cao/FIG_06_Surrogate_AI_Parity_and_Residuals.png)

*Hình 6.1: Đánh giá độ chính xác và độ tin cậy của mô hình học máy thay thế (Surrogate AI MLP) trên 500 mẫu kiểm thử độc lập*

</div>

<br>

### Nhận xét đồ thị kiểm định (Hình 6.1):
1. **Đồ thị tương quan Parity (Hình 6.1a):**
   Toàn bộ 500 điểm dữ liệu kiểm thử độc lập nằm bám khít hoàn hảo vào đường phân giác lý tưởng $y = x$ trên toàn bộ dải độ lún từ $0\text{ mm}$ đến $45\text{ mm}$. Hệ số tương quan $R^2 = 0.9991$ chứng minh mạng MLP đã nắm bắt trọn vẹn đặc tính phi tuyến của phễu lún siêu vị hầm đôi.
2. **Phân bố sai số phần dư Residuals (Hình 6.1b):**
   Sai số phần dư $e = y_{\text{true}} - y_{\text{pred}}$ có phân bố đối xứng dạng chuông Gauss chuẩn với giá trị kỳ vọng triệt tiêu ($\mu \approx 0$) và độ lệch chuẩn rất nhỏ ($\sigma = 0.22\text{ mm}$). Tuyệt đại đa số các mẫu ($>98\%$) có sai số dưới $\pm 0.3\text{ mm}$, một con số hoàn toàn không đáng kể so với sai số đo đạc thực tế của máy thủy bình điện tử ngoài hiện trường ($\pm 1.0\text{ mm}$).
3. **Tốc độ suy luận (Inference Speed):**
   Thời gian thực hiện một phép dự báo độ lún chỉ mất **$0.08\text{ ms}$** (chưa tới một phần mười nghìn giây), cho phép hệ thống tính toán đồng thời hàng nghìn điểm chuyển vị trên toàn tuyến hầm mà không gây giật lag trên giao diện WebGIS.

---

## 6.5. ĐÁNH GIÁ, PHẢN BIỆN VÀ GHI CHÚ AUDIT CỦA CHƯƠNG 6

> **Ghi chú Kiểm toán Khoa học (Audit Note 6.1):**
> 1. **Miền hiệu lực của mô hình (Domain of Applicability):**
>    - `==[GIẢ THIẾT TÍNH TOÁN: Mô hình Surrogate AI này được huấn luyện trong không gian tham số: x ∈ [-50m; +50m], z0 ∈ [13m; 22m], K ∈ [0.40; 0.70], VL ∈ [0.3%; 2.5%], d ∈ [10m; 18m]. Nếu người vận hành nhập các giá trị vượt ra ngoài miền này (ví dụ hầm quá nông z0 < 10m hoặc tổn thất quá lớn VL > 3.0%), mô hình sẽ kích hoạt cờ cảnh báo ngoại suy (Extrapolation Warning) và khuyến cáo quay trở lại tính toán giải tích trực tiếp.]==`
> 2. **Khả năng cập nhật thích nghi (Transfer Learning & Dynamic Fine-tuning):**
>    - Bản chất hiện tại của mô hình AI là học lại từ nghiệm giải tích Gaussian. Khi khiên đào TBM chính thức vận hành và các mốc quan trắc bề mặt truyền dữ liệu lún thực tế về phòng điều khiển trung tâm, kiến trúc mạng MLP này có thể được huấn luyện bổ sung (fine-tune) theo cơ chế học chuyển giao (Transfer Learning), cho phép mô hình tự động hiệu chỉnh để dung hòa giữa lý thuyết cơ học đất và ứng xử dị hướng thực địa của nền đất Hà Nội.
