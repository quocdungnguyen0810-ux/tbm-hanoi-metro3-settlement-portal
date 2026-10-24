# ĐỀ CƯƠNG CHI TIẾT BẢN THẢO LUẬN ÁN (DISSERTATION SYLLABUS & OUTLINE)
## ĐỀ TÀI: NGHIÊN CỨU ĐÁNH GIÁ ĐỘ NHẠY VÀ DỰ BÁO VÙNG ẢNH HƯỞNG LÚN MẶT ĐẤT DO THI CÔNG HẦM KHIÊN ĐÀO (TBM) ĐOẠN S9–S12 METRO HÀ NỘI BẰNG PHƯƠNG PHÁP GIẢI TÍCH KẾT HỢP WEBGIS

**Ngành:** Kỹ thuật Xây dựng Công trình Ngầm và Mỏ / Kỹ thuật Địa kỹ thuật  
**Mã số:** 9580204 / 9580211  
**Quy chuẩn biên soạn:** Tiêu chuẩn Luận án Tiến sĩ / Thạc sĩ Kỹ thuật, TCVN, ASTM, BS EN Eurocode 7  

---

### MỤC LỤC TỔNG THỂ

- **LỜI CAM ĐOAN & LỜI CẢM ƠN**
- **TÓM TẮT LUẬN ÁN (TIẾNG VIỆT & TIẾNG ANH)**
- **DANH MỤC CÁC KÝ HIỆU, CHỮ VIẾT TẮT VÀ ĐƠN VỊ ĐO**
- **DANH MỤC BẢNG BIỂU**
- **DANH MỤC HÌNH VẼ & ĐỒ THỊ**

---

### NỘI DUNG CÁC CHƯƠNG CHI TIẾT

#### CHƯƠNG 1: TỔNG QUAN VÀ ĐẶT VẤN ĐỀ NGHIÊN CỨU
- **1.1. Bối cảnh phát triển đường sắt đô thị và công nghệ khiên đào TBM tại Việt Nam**
  - 1.1.1. Hiện trạng ùn tắc giao thông đô thị và quy hoạch mạng lưới Metro Hà Nội.
  - 1.1.2. Dự án Tuyến đường sắt đô thị số 3 (Nhổn - Ga Hà Nội) và đặc điểm đoạn đi ngầm S9–S12.
- **1.2. Tổng quan tình hình nghiên cứu biến dạng đất nền do thi công hầm ngầm trên thế giới và trong nước**
  - 1.2.1. Các nghiên cứu kinh điển về phễu lún bề mặt (Peck, Schmidt, O'Reilly & New, Mair).
  - 1.2.2. Các nghiên cứu cơ học giải tích đàn dẻo (Sagaseta, Verruijt & Booker, Loganathan & Poulos).
  - 1.2.3. Các nghiên cứu địa kỹ thuật tuyến hầm Metro tại Hà Nội và TP. Hồ Chí Minh.
- **1.3. Khoảng trống tri thức khoa học (Research Gaps)**
  - 1.3.1. Sự thiếu hụt cơ sở dữ liệu kiểm định nguồn mở minh bạch về địa tầng S9–S12.
  - 1.3.2. Nguy cơ biến dạng đối với các công trình móng nông và di tích lịch sử nhạy cảm cao.
  - 1.3.3. Nhu cầu cấp thiết về công cụ số hóa WebGIS và AI Surrogate phục vụ điều khiển TBM thời gian thực.
- **1.4. Mục tiêu, đối tượng, phạm vi và phương pháp nghiên cứu**
- **1.5. Ý nghĩa khoa học và giá trị thực tiễn của luận án**
- **1.6. Cấu trúc luận án**

#### CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ PHƯƠNG PHÁP TÍNH TOÁN GIẢI TÍCH
- **2.1. Cơ chế biến dạng đất nền xung quanh hầm khiên đào cân bằng áp lực đất (EPB-TBM)**
  - 2.1.1. Các thành phần tổn thất thể tích đất trong chu kỳ đào ($V_{\text{face}}, V_{\text{shield}}, V_{\text{tail}}, V_{\text{consolidation}}$).
  - 2.1.2. Khái niệm và định nghĩa tỷ lệ tổn thất thể tích đất $V_L$ (Volume Loss Ratio).
- **2.2. Mô hình phễu lún Gaussian của Peck (1969)**
  - 2.2.1. Phương trình toán học dạng chuẩn của phễu lún ngang.
  - 2.2.2. Bán kính phễu lún và khoảng cách điểm uốn $i$ (Công thức O'Reilly & New 1982).
  - 2.2.3. Chứng minh toán học định luật bảo toàn thể tích ($V_s = V_{\text{loss}}$) trong điều kiện không thoát nước.
- **2.3. Mô hình bán giải tích Loganathan & Poulos (1998)**
  - 2.3.1. Cơ sở lý thuyết giải tích đàn hồi giải phóng ứng suất xung quanh lỗ rỗng tròn.
  - 2.3.2. Phương trình chuyển vị lún bề mặt $S(x)$ tại $z=0$.
  - 2.3.3. Phạm vi ứng dụng, ưu điểm và giới hạn của mô hình LP so với Peck.
- **2.4. Nguyên lý siêu vị hầm đôi song song (Twin Tunnel Superposition)**
  - 2.4.1. Tương tác hình học giữa hai ống hầm cách nhau cự ly $d$.
  - 2.4.2. Độ dốc mặt đất $\theta(x)$ (Tilt/Slope) và bán kính cong lún (Curvature).
- **2.5. Tiêu chuẩn đánh giá nguy cơ tổn hại kết cấu công trình (Burland 1995, Mair et al. 1996)**
  - 2.5.1. Phân loại cấp độ hư hại từ Cấp 0 (Không đáng kể) đến Cấp 5 (Sụp đổ).
  - 2.5.2. Tương quan giữa độ dốc góc xoay $\beta$, độ lún tuyệt đối $S_v$ và biến dạng kéo ngang $\epsilon_{br}$.

#### CHƯƠNG 3: ĐẶC TRƯNG ĐỊA KỸ THUẬT VÀ XÁC LẬP BỘ DỮ LIỆU ĐOẠN S9–S12
- **3.1. Điều kiện địa hình, địa mạo và địa chất thủy văn khu vực nghiên cứu**
  - 3.1.1. Cấu trúc địa tầng bồi tích Đệ tứ vùng trũng Hà Nội.
  - 3.1.2. Chế độ thủy văn và sự biến động mực nước ngầm tầng nông Holocen và tầng sâu Pleistocen.
- **3.2. Dữ liệu địa tầng hố khoan BH12 (đoạn S11–S12) có kiểm định nguồn**
  - 3.2.1. Phân tích chi tiết 6 lớp thạch học theo bài báo Nguyen, Kohata & Nguyen (TCXD 2024).
  - 3.2.2. Đánh giá đặc biệt về tầng bùn sét dẻo mềm hữu cơ dày $12.7\text{ m}$ ($N < 4, E = 7.68\text{ MPa}$).
- **3.3. Mặt cắt địa tầng đại diện đoạn S9–S10 (Kim Mã - Cát Linh)**
  - 3.3.1. Các đơn nguyên địa chất công trình từ GU1 đến GU8 theo Nguyen et al. (ETASR 2024).
  - 3.3.2. Tương quan cơ lý và vị trí hầm TBM nằm trong tầng cát mịn GU5_a.
- **3.4. Kiểm tra chéo dữ liệu khu vực toàn tuyến theo Giao et al. (2020)**
- **3.5. Xác lập bộ thông số hình học và địa kỹ thuật chuẩn hóa phục vụ tính toán**
  - 3.5.1. Bảng tổng hợp thông số 3 mặt cắt kỹ thuật (S9–S10, S10–S11, S11–S12).
  - 3.5.2. Nhật ký kiểm định Audit và các điểm bôi vàng lưu ý cần hiệu chỉnh hiện trường.

#### CHƯƠNG 4: KẾT QUẢ TÍNH TOÁN VÀ PHÂN TÍCH ĐỘ NHẠY BIẾN DẠNG MẶT ĐẤT
- **4.1. Kết quả tính toán biến dạng phễu lún tại kịch bản tiêu chuẩn ($V_L = 1.0\%$)**
  - 4.1.1. Biên độ lún cực đại $S_{\max}$ hầm đơn và hầm đôi tại 3 mặt cắt.
  - 4.1.2. So sánh đối sánh dạng hình học phễu lún giữa Peck (1969) và Loganathan & Poulos (1998).
- **4.2. Phân tích độ nhạy đa kịch bản (21 kịch bản tổn thất thể tích đất $V_L \in [0.5\%; 2.0\%]$)**
  - 4.2.1. Quy luật biến thiên tuyến tính của $S_{\max}$ theo $V_L$.
  - 4.2.2. Sự phát triển của bề rộng vùng ảnh hưởng nguy hại ($S > 5\text{ mm}$ và $S > 10\text{ mm}$).
  - 4.2.3. Đánh giá gradient độ dốc cực đại $\theta_{\max}$ và nguy cơ vặn xoắn móng.
- **4.3. Đánh giá mức độ nhạy cảm của các thông số đầu vào**
  - 4.3.1. Ảnh hưởng của chiều sâu chôn hầm $z_0$ và tỷ số $z_0/D$.
  - 4.3.2. Ảnh hưởng của hệ số phễu lún $K$ phụ thuộc loại đất bao quanh đỉnh hầm.

#### CHƯƠNG 5: ĐÁNH GIÁ NGUY CƠ HƯ HỎNG CÔNG TRÌNH VÀ TÍCH HỢP HỆ THỐNG WEBGIS
- **5.1. Khảo sát hiện trạng công trình dọc hành lang hầm S9–S12**
  - 5.1.1. Đặc điểm kết cấu công trình đô thị cổ Hà Nội (nhà ống móng nông, chung cư cũ, di tích lịch sử).
  - 5.1.2. Xây dựng cơ sở dữ liệu không gian cho 60 công trình đại diện trong dải đệm $\pm 35\text{ m}$.
- **5.2. Đánh giá nguy cơ hư hại công trình theo các kịch bản thi công**
  - 5.2.1. Phân loại nguy cơ theo tiêu chuẩn Burland (1995) tại $V_L = 0.5\%, 1.0\%, 1.5\%, 2.0\%$.
  - 5.2.2. Xác định các công trình có mức độ ưu tiên bảo vệ đặc biệt (công trình di tích, công trình móng nông sát tim hầm).
- **5.3. Phát triển hệ thống WebGIS tương tác giám sát lún**
  - 5.3.1. Kiến trúc công nghệ hệ thống (Leaflet.js, GeoJSON, OpenStreetMap/Esri Satellite).
  - 5.3.2. Trực quan hóa các vùng đệm lún (5mm, 10mm, 15mm, 20mm) và truy xuất dữ liệu động từng công trình.

#### CHƯƠNG 6: PHÁT TRIỂN MÔ HÌNH HỌC MÁY THAY THẾ (SURROGATE AI) DỰ BÁO TỨC THỜI
- **6.1. Đặt bài toán và sự cần thiết của mô hình thay thế**
- **6.2. Thu thập và chuẩn hóa tập dữ liệu mô phỏng**
  - 6.2.1. Không gian tham số đầu vào ($x, z_0, K, V_L, d$).
  - 6.2.2. Tạo lập 2,500 mẫu dữ liệu giải tích và kỹ thuật chia tách Train/Test (80/20).
- **6.3. Kiến trúc mạng nơ-ron và quy trình huấn luyện thuần NumPy**
  - 6.3.1. Cấu trúc mạng MLP đa tầng (5 $\rightarrow$ 32 $\rightarrow$ 16 $\rightarrow$ 1).
  - 6.3.2. Thuật toán tối ưu hóa Adam, hàm kích hoạt ReLU và hàm mất mát MSE.
- **6.4. Đánh giá độ chính xác và độ tin cậy của mô hình**
  - 6.4.1. Các chỉ số thống kê trên tập kiểm thử độc lập ($R^2 = 0.9991, MAE = 0.156\text{ mm}, RMSE = 0.220\text{ mm}$).
  - 6.4.2. Phân tích đồ thị tương quan Parity và phân bố sai số phần dư.
- **6.5. Khả năng ứng dụng tích hợp điều khiển TBM thời gian thực**

#### CHƯƠNG 7: KẾT LUẬN, KIẾN NGHỊ VÀ QUY TRÌNH QUAN TRẮC HIỆN TRƯỜNG
- **7.1. Các kết luận khoa học chính của luận án**
- **7.2. Những đóng góp mới của đề tài**
- **7.3. Kiến nghị về biện pháp kỹ thuật kiểm soát rủi ro khi thi công TBM**
  - 7.3.1. Kiểm soát áp lực khoang đào EPB và thể tích đất đào.
  - 7.3.2. Quy trình phụt vữa chèn lưng vỏ hầm (backfill grouting) áp lực cao qua tầng bùn sét S11–S12.
- **7.4. Đề xuất quy trình quan trắc địa kỹ thuật tự động và hiệu chỉnh ngược tham số**
  - 7.4.1. Bố trí lưới quan trắc mốc lún bề mặt và piezometer đo áp lực nước ngầm.
  - 7.4.2. Quy trình kiểm định Audit và ngưỡng hành động khẩn cấp (Trigger Action Response Plan - TARP).

#### CHƯƠNG 8: TÀI LIỆU THAM KHẢO CHUẨN MỰC
- Toàn bộ danh mục tài liệu tham khảo trong nước và quốc tế có DOI, mã định danh và đường dẫn kiểm chứng đầy đủ.

#### PHỤ LỤC & MA TRẬN BẰNG CHỨNG
- **Phụ lục A:** Bảng thông số cơ lý chi tiết hố khoan BH12 và phân tầng địa chất S9–S10.
- **Phụ lục B:** Bảng số liệu chi tiết 21 kịch bản phân tích độ nhạy.
- **Phụ lục C:** Danh mục chi tiết 60 công trình khảo sát nguy cơ lún.
- **Phụ lục D:** Nhật ký kiểm định Audit Gates 1–5 và ma trận truy xuất nguồn gốc.
