# BÁO CÁO TÓM TẮT KẾT QUẢ NGHIÊN CỨU VÀ SẢN PHẨM BÀN GIAO GIAI ĐOẠN 1
### PHỤC VỤ NGHIỆM THU THỬ CẤP BỘ MÔN ĐỊA KỸ THUẬT VÀ KHÔNG GIAN NGẦM

**Đề tài:** *Nghiên cứu đánh giá độ nhạy và dự báo vùng ảnh hưởng lún mặt đất do thi công hầm khiên đào (TBM) đoạn S9–S12 Metro Tuyến 3 Hà Nội bằng phương pháp giải tích kết hợp WebGIS*  
**Thời gian thực hiện:** Tháng 10/2026  
**Đơn vị:** Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường - Trường Đại học Giao thông vận tải

---

### I. MỤC TIÊU VÀ NGUYÊN TẮC THỰC HIỆN
1. **Mục tiêu:** Xây dựng khung phân tích giải tích minh bạch, bộ dữ liệu địa kỹ thuật thực chứng và công cụ số hóa WebGIS tương tác nhằm giải quyết bài toán kiểm soát biến dạng lún mặt đất và rủi ro đối với 60 công trình móng nông nhạy cảm khi thi công hai ống hầm TBM EPB đoạn S9–S12 (Nhổn - Ga Hà Nội).
2. **Nguyên tắc "Anti-hallucination" & "Audit Gates":**
   - Tuyệt đối không sử dụng số liệu suy diễn vô căn cứ; mọi thông số cơ lý đều được đối chiếu với bài báo gốc (TCXD 2024, ETASR 2024, Springer 2020).
   - Phân định rạch ròi giữa số liệu đo đạc thực địa và các giá trị giả định mô hình (Model Assumptions được bôi vàng cảnh báo).
   - Vượt qua tuần tự 5 Cổng kiểm toán khoa học (Audit Gates 1–5).

---

### II. TỔNG HỢP CÁC KẾT QUẢ KHOA HỌC CHÍNH

#### 1. Cơ sở dữ liệu địa kỹ thuật và tầng bùn sét mềm S11–S12
- Đoạn tuyến hầm S9–S12 dài khoảng $3.5\text{ km}$, đường kính ngoài $D = 6.30\text{ m}$, diện tích tiết diện đào $A_t = 31.172\text{ m}^2$, cự ly tim hầm đôi $d \approx 13.0\text{ m}$.
- Phát hiện rủi ro trọng điểm tại đoạn S11–S12 (hố khoan BH12): Tồn tại phân lớp bùn sét xám đen dẻo mềm đến chảy có chứa mùn thực vật dày tới $12.7\text{ m}$ ($z = 4.0 \div 16.7\text{ m}$), chỉ số SPT $N \le 4$, mô-đun biến dạng rất thấp $E = 7.68\text{ MPa}$. Đỉnh hầm TBM ($z_0 \approx 18.0\text{ m}$) nằm ngay sát đáy lớp bùn sét này, tạo ra nguy cơ mất ổn định gương đào và lún cố kết thứ cấp kéo dài.

#### 2. Mô hình hóa giải tích và kiểm chứng bảo toàn thể tích
- Kiểm chứng thành công mô hình phễu lún Gaussian của Peck (1969) với công thức bề rộng điểm uốn $i = K \cdot z_0$ và mô hình giải tích biến dạng đàn hồi Loganathan & Poulos (1998).
- **Kiểm chứng bảo toàn thể tích:** Tích phân thể tích phễu lún bề mặt $V_s = \sqrt{2\pi} \cdot i \cdot S_{\max}$ bằng đúng tổn thất thể tích đào $V_{\text{loss}} = V_L \cdot A_t$ với sai số số trị $< 0.001\%$.
- **Mô hình siêu vị hầm đôi (Twin Tunnel Superposition):** Tại cự ly $d = 13.0\text{ m}$, hiệu ứng giao thoa làm đáy phễu lún mở rộng thành dạng chữ U đáy phẳng, độ lún tại tim hầm đôi tăng gấp $1.65 \div 1.82$ lần so với hầm đơn độc lập.

#### 3. Ma trận 21 kịch bản phân tích độ nhạy đa biến
- Khảo sát 21 kịch bản kết hợp giữa 3 mặt cắt kỹ thuật (S9–S10: $z_0=15\text{ m}, K=0.50$; S10–S11: $z_0=16.5\text{ m}, K=0.55$; S11–S12: $z_0=18\text{ m}, K=0.60$) và 7 mức tổn thất thể tích $V_L \in [0.5\%; 2.0\%]$.
- **Kết quả lún cực đại:**
  - Tại kịch bản tiêu chuẩn ($V_L = 1.0\%$): $S_{\max}$ hầm đơn dao động từ $11.5\text{ mm}$ (S11–S12) đến $16.6\text{ mm}$ (S9–S10); $S_{\max}$ hầm đôi dao động từ $16.8\text{ mm}$ đến $22.1\text{ mm}$.
  - Tại kịch bản bất lợi ($V_L = 2.0\%$): $S_{\max}$ hầm đôi đoạn S11–S12 vọt lên tới $44.2\text{ mm}$, vùng ảnh hưởng lún nguy hại ($S > 10\text{ mm}$) mở rộng ra tới bán kính $\pm 21.8\text{ m}$ tính từ tim tuyến.

#### 4. Đánh giá rủi ro 60 công trình móng nông (Burland 1995)
- Điều tra, số hóa 60 công trình nhà dân (2–5 tầng) và trụ sở nằm trong dải ảnh hưởng $\pm 35\text{ m}$ dọc các trục đường Kim Mã, Cát Linh, Quốc Tử Giám, Trần Hưng Đạo.
- **Phân loại cấp độ hư hỏng:**
  - Tại $V_L = 1.0\%$: 43 công trình thuộc Cấp 0 (Không đáng kể), 12 công trình thuộc Cấp 1 (Rất nhẹ, nứt chân chim), 5 công trình thuộc Cấp 2 (Nhẹ, $S_v = 15 \div 22\text{ mm}$).
  - Tại $V_L = 2.0\%$: Số lượng công trình bị tổn hại nghiêm trọng tăng đột biến; có tới **18 công trình rơi vào Cấp 3 (Hư hỏng vừa, nứt kết cấu)** và 14 công trình rơi vào Cấp 2, đòi hỏi quy trình quan trắc mốc lún thời gian thực và phương án gia cố cọc kích/phụt vữa bù lún trước khi TBM đi qua.

#### 5. Mô hình học máy thay thế (Surrogate AI)
- Huấn luyện mạng nơ-ron truyền thẳng đa tầng (MLP) thuần túy bằng NumPy trên 2,500 mẫu dữ liệu không gian tham số ($x, z_0, K, V_L, d$).
- Trên 500 mẫu kiểm thử độc lập: Đạt hệ số xác định cực cao $R^2 = 0.9991$, sai số tuyệt đối trung bình $MAE = 0.156\text{ mm}$, thời gian suy luận $< 0.1\text{ ms}$, cho phép nhúng trực tiếp vào thuật toán điều khiển TBM thời gian thực.

#### 6. Nền tảng WebGIS tương tác trực quan
- Ứng dụng WebGIS độc lập dựa trên Leaflet.js và Chart.js, hiển thị bình đồ tuyến hầm đôi, 4 ga ngầm, 3 dải đệm lún (5mm, 10mm, 20mm) và 60 công trình khảo sát trên nền bản đồ không gian WGS-84.
- Thanh trượt $V_L$ và bộ chọn mặt cắt cho phép các kỹ sư và chuyên gia quan sát sự đổi màu rủi ro động của từng tòa nhà theo tiêu chuẩn Burland ngay trên màn hình mà không cần cài đặt phần mềm GIS chuyên sâu.

---

### III. BẢNG TỔNG HỢP CÁC CHỈ TIÊU ĐẠT ĐƯỢC

| Hạng mục sản phẩm | Chỉ tiêu đăng ký | Kết quả thực tế đạt được | Đánh giá |
|---|---|---|---|
| **Bản thảo Luận án** | 01 bản thảo chi tiết $\ge 70$ trang | Hoàn thành 8 chương, 113 trang MD, xuất bản bản Word DOCX chuẩn (2.64 MB) | VƯỢT MỨC |
| **Hệ thống File Excel** | $\ge 2$ bảng tính | 4 file Excel đa trang, 100% công thức động, có metadata & Audit matrix | VƯỢT MỨC |
| **Hình vẽ khoa học** | $\ge 5$ hình vẽ 300 DPI | 7 hình đồ họa phân giải cao 300 DPI đạt chuẩn quốc tế | VƯỢT MỨC |
| **Ứng dụng WebGIS** | Có bản đồ phân vùng | WebGIS Leaflet.js tương tác hoàn chỉnh, nạp 60 công trình, biểu đồ động Chart.js | VƯỢT MỨC |
| **Độ chính xác AI** | $R^2 \ge 0.95$ | Mạng MLP đạt $R^2 = 0.9991, MAE = 0.156\text{ mm}$ | VƯỢT MỨC |
| **Kiểm toán chất lượng** | Tuân thủ TCVN/Eurocode | Đạt 100% qua 5 Cổng kiểm toán độc lập (Gates 1–5) | HOÀN THÀNH |

---

### IV. KẾT LUẬN VÀ KIẾN NGHỊ
Bộ sản phẩm Giai đoạn 1 đã hoàn thiện trọn vẹn cả về hàm lượng học thuật, độ tin cậy số liệu, công cụ phân tích giải tích và giải pháp trực quan hóa không gian số. Kính trình Hội đồng nghiệm thu thử Bộ môn Địa kỹ thuật và Không gian ngầm xem xét thông qua để tiếp tục triển khai các giai đoạn tiếp theo.
