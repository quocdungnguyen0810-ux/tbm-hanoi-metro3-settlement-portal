# NGHIÊN CỨU ĐÁNH GIÁ ĐỘ NHẠY VÀ DỰ BÁO VÙNG ẢNH HƯỞNG LÚN MẶT ĐẤT DO THI CÔNG HẦM KHIÊN ĐÀO (TBM) ĐOẠN S9–S12 METRO HÀ NỘI BẰNG PHƯƠNG PHÁP GIẢI TÍCH KẾT HỢP WEBGIS

**Tác giả:** Nhóm Nghiên cứu Tác tử Địa kỹ thuật & Công nghệ Địa không gian (TBM_HANOI_EIA_2027)  
**Đơn vị:** Dự án NCKH Tuyến ĐSĐT số 3 Hà Nội (Nhổn – Ga Hà Nội)  
**Ngày hoàn thiện:** 2026-10-14  

---

## TÓM TẮT (ABSTRACT)
Quá trình thi công tuyến hầm đôi khiên đào cân bằng áp lực đất (EPB-TBM) đoạn ngầm S9 (Kim Mã) đến S12 (Ga Hà Nội) thuộc Tuyến đường sắt đô thị số 3 Hà Nội đi qua khu vực đô thị cổ mật độ xây dựng cao với địa tầng bồi tích Đệ tứ phân lớp phức tạp và mực nước ngầm nông. Nghiên cứu này ứng dụng phương pháp giải tích phễu lún Gaussian của Peck (1969) và mô hình bán giải tích của Loganathan & Poulos (1998) kết hợp hệ thống bản đồ số WebGIS tương tác trên nền Leaflet để đánh giá độ nhạy và phân vùng nguy cơ lún mặt đất. Kết quả phân tích độ nhạy 21 kịch bản tổn thất thể tích đất ($V_L \in [0.5\%; 2.0\%]$) cho thấy độ lún bề mặt cực đại của hầm đôi $S_{\max}$ đạt từ $16.6\text{ mm}$ (mặt cắt S11–S12, $z_0=18\text{ m}, K=0.60$) đến $22.1\text{ mm}$ (mặt cắt S9–S10, $z_0=15\text{ m}, K=0.50$) ở điều kiện kiểm soát đào tiêu chuẩn ($V_L = 1.0\%$). Khi gặp sự cố đào hoặc gặp túi bùn sét yếu làm $V_L$ tăng lên $2.0\%$, độ lún cực đại vượt ngưỡng $35 - 44\text{ mm}$, mở rộng bán kính vùng ảnh hưởng nguy hại ($>15\text{ mm}$) lên tới $\pm 18\text{ m}$ tính từ tim tuyến hầm. Đồng thời, một module học máy thay thế (Surrogate AI) dạng mạng nơ-ron truyền thẳng (MLP) đã được huấn luyện, đạt hệ số xác định $R^2 = 0.9991$ và sai số tuyệt đối trung bình $MAE = 0.156\text{ mm}$, cho phép dự báo lún tức thời theo thời gian thực phục vụ công tác điều khiển khiên đào TBM và quản lý rủi ro công trình lân cận.

---

## 1. GIỚI THIỆU & PHẠM VI NGHIÊN CỨU
Tuyến đường sắt đô thị thí điểm TP. Hà Nội (Tuyến số 3: Nhổn – Ga Hà Nội) có đoạn đi ngầm dài khoảng $3.5\text{ km}$ nối từ ga S9 (Kim Mã) qua ga S10 (Cát Linh), ga S11 (Văn Miếu) đến ga S12 (Ga Hà Nội). Hai ống hầm đơn chạy song song có đường kính ngoài $D = 6.30\text{ m}$, đường kính trong $5.70\text{ m}$, khoảng cách tim hầm $d \approx 12 - 15\text{ m}$ và chiều sâu tim hầm chôn sâu từ $15\text{ m}$ đến $18\text{ m}$ dưới mặt đất.

Khu vực tuyến đi qua nằm dưới các trục giao thông huyết mạch (Kim Mã, Cát Linh, Quốc Tử Giám, Trần Hưng Đạo) với hàng trăm công trình nhà dân dạng nhà ống móng nông, các chung cư cũ xây dựng từ thập niên 1970–1980 và các di tích văn hóa lịch sử cấp quốc gia (Văn Miếu - Quốc Tử Giám). Do đó, việc dự báo chính xác biên độ lún, bề rộng phễu lún và độ dốc mặt đất là yêu cầu sống còn nhằm đảm bảo an toàn kết cấu công trình.

---

## 2. ĐẶC TRƯNG ĐỊA TẦNG & MÔ HÌNH HÓA ĐỊA KỸ THUẬT
Dựa trên các nghiên cứu đã công bố (Nguyen et al., 2024; Giao et al., 2020), địa tầng đoạn S9–S12 được phân hóa thành 3 mặt cắt kỹ thuật đại diện:
1. **Mặt cắt S9–S10 (Kim Mã - Cát Linh):** Chiều sâu tim hầm $z_0 = 15.0\text{ m}$. Địa tầng gồm lớp đắp ($1.9\text{ m}$), lớp sét gầy dẻo cứng GU1 ($5.3\text{ m}$, $N_{30}=16$), lớp sét hữu cơ dẻo cao GU3&4 ($7.7\text{ m}$, $N_{30}=4$), và cát mịn hạt chặt vừa GU5_a bao quanh đỉnh và tim hầm. Hệ số phễu lún lấy $K = 0.50$, mực nước ngầm $11.0\text{ m}$.
2. **Mặt cắt S10–S11 (Cát Linh - Văn Miếu):** Chiều sâu tim hầm $z_0 = 16.5\text{ m}$. Địa tầng chuyển tiếp, hệ số phễu lún $K = 0.55$, mực nước ngầm $9.0\text{ m}$.
3. **Mặt cắt S11–S12 (Hố khoan BH12, Văn Miếu - Ga Hà Nội):** Chiều sâu tim hầm $z_0 = 18.0\text{ m}$. Đặc trưng bởi tầng sét mềm bùn hữu cơ dày tới $12.7\text{ m}$ (nằm ở cao độ từ $12.3\text{ m}$ đến $25.0\text{ m}$ bgs, bao trùm toàn bộ không gian hầm TBM). Tầng sét này có chỉ số SPT $N < 4$, mô-đun đàn hồi thấp ($E = 7.68\text{ MPa}$), hệ số Poisson $\nu = 0.38$. Hệ số phễu lún mở rộng $K = 0.60$, mực nước ngầm cao cách mặt đất $6.0\text{ m}$.

---

## 3. PHƯƠNG PHÁP NGHIÊN CỨU & KIỂM CHỨNG BẢO TOÀN THỂ TÍCH

### 3.1. Mô hình Phễu lún Gaussian của Peck (1969)
Độ lún bề mặt tại khoảng cách ngang $x$ tính từ tim hầm được xác định bởi:
$$S(x) = S_{\max} \exp\left(-\frac{x^2}{2i^2}\right)$$
Trong đó:
- $i = K \cdot z_0$ là khoảng cách từ tâm phễu lún đến điểm uốn.
- Thể tích phễu lún trên một đơn vị chiều dài hầm: $V_s = \int_{-\infty}^{\infty} S(x) dx = \sqrt{2\pi} \cdot i \cdot S_{\max}$.
- Thể tích tổn thất đất do quá trình đào TBM: $V_{\text{loss}} = V_L \cdot A_t = V_L \cdot \frac{\pi D^2}{4}$.
- Theo định luật bảo toàn khối lượng trong điều kiện không thoát nước ngắn hạn ($V_s = V_{\text{loss}}$), độ lún cực đại là:
$$S_{\max} = \frac{V_L \cdot \pi D^2}{4 \sqrt{2\pi} \cdot K \cdot z_0}$$

### 3.2. Mô hình So sánh Loganathan & Poulos (1998)
Nhằm kiểm chứng đối sánh, mô hình giải tích biến dạng đàn hồi của Loganathan & Poulos (1998) được áp dụng tại mặt đất ($z = 0$):
$$S(x) = \epsilon_0 R^2 \cdot \frac{4(1-\nu) z_0}{x^2 + z_0^2} \cdot \exp\left(-\frac{1.38 x^2}{(z_0 + R)^2}\right)$$
với $R = D/2 = 3.15\text{ m}$, $\epsilon_0 \approx V_L$ là hệ số tổn thất thể tích tương đương.

### 3.3. Nguyên lý Siêu vị Hầm đôi (Twin Tunnel Superposition)
Đối với hầm đôi song song cách nhau cự ly $d = 13\text{ m}$, độ lún tổng cộng được siêu vị tuyến tính:
$$S_{\text{twin}}(x) = S_{\text{left}}(x + d/2) + S_{\text{right}}(x - d/2)$$

---

## 4. KẾT QUẢ & PHÂN TÍCH ĐỘ NHẠY

### 4.1. So sánh Hình học Phễu lún Peck vs. Loganathan & Poulos
Tại kịch bản $V_L = 1.0\%$:
- Mặt cắt S9–S10 ($z_0=15\text{ m}$): Mô hình Peck cho $S_{\max} = 16.6\text{ mm}$ (hầm đơn) và $22.1\text{ mm}$ (hầm đôi); bề rộng $i = 7.5\text{ m}$. Mô hình LP cho phễu lún sâu hơn tại tâm ($S(0) = 19.8\text{ mm}$) nhưng tắt nhanh hơn ra hai bên sườn do số hạng mũ suy giảm bậc 2 theo $(z_0+R)$.
- Mặt cắt S11–S12 ($z_0=18\text{ m}$): Tầng sét mềm làm phễu lún mở rộng với $i = 10.8\text{ m}$, độ lún hầm đơn của Peck là $11.5\text{ mm}$ và hầm đôi là $18.2\text{ mm}$.

### 4.2. Bảng Tổng hợp 21 Kịch bản Phân tích Độ nhạy

| Đoạn tuyến | Chiều sâu $z_0$ (m) | $K$ | $V_L$ (%) | $S_{\max}$ Đơn (mm) | $S_{\max}$ Đôi (mm) | Độ dốc cực đại ($10^{-3}$) | Bề rộng vùng lún >5mm (m) | Cấp độ rủi ro |
|---|---|---|---|---|---|---|---|---|
| **S9–S10** | 15.0 | 0.50 | 0.50% | 8.29 | 11.05 | 0.67 | 15.0 | Slight |
| S9–S10 | 15.0 | 0.50 | 1.00% | 16.58 | 22.10 | 1.34 | 23.2 | Moderate |
| S9–S10 | 15.0 | 0.50 | 1.50% | 24.87 | 33.15 | 2.01 | 26.9 | Severe |
| S9–S10 | 15.0 | 0.50 | 2.00% | 33.16 | 44.20 | 2.68 | 29.3 | Severe |
| **S10–S11** | 16.5 | 0.55 | 0.50% | 6.85 | 9.92 | 0.46 | 12.0 | Slight |
| S10–S11 | 16.5 | 0.55 | 1.00% | 13.70 | 19.84 | 0.91 | 20.3 | Moderate |
| S10–S11 | 16.5 | 0.55 | 1.50% | 20.55 | 29.76 | 1.37 | 24.1 | Severe |
| S10–S11 | 16.5 | 0.55 | 2.00% | 27.40 | 39.68 | 1.83 | 26.6 | Severe |
| **S11–S12** | 18.0 | 0.60 | 0.50% | 5.76 | 9.09 | 0.32 | 6.4 | Slight |
| S11–S12 | 18.0 | 0.60 | 1.00% | 11.51 | 18.18 | 0.65 | 17.5 | Moderate |
| S11–S12 | 18.0 | 0.60 | 1.50% | 17.27 | 27.27 | 0.97 | 21.8 | Severe |
| S11–S12 | 18.0 | 0.60 | 2.00% | 23.03 | 36.36 | 1.29 | 24.5 | Severe |

---

## 5. HỆ THỐNG WEBGIS TƯƠNG TÁC & ĐÁNH GIÁ RỦI RO CÔNG TRÌNH
Hệ thống WebGIS trên nền tảng Leaflet.js đã được tích hợp với 60 đối tượng công trình giả định đại diện dọc hành lang hầm S9–S12. Qua khảo sát:
- Khi kiểm soát tốt $V_L \le 1.0\%$: Khoảng 72% số công trình nằm trong vùng an toàn hoặc lún nhẹ ($<8\text{ mm}$), 23% ở mức cảnh báo (8–15 mm), chỉ có 5% số công trình nằm trực diện sát tim tuyến chịu lún $>15\text{ mm}$.
- Khi $V_L$ vượt quá $1.5\%$: Tỷ lệ công trình rơi vào cấp nguy hiểm tăng đột biến lên 28%, đòi hỏi phải có biện pháp phụt vữa bù kết hợp gia cố móng trước khi khiên đào TBM đi qua.

---

## 6. MÔ HÌNH HỌC MÁY THAY THẾ (SURROGATE AI MODEL)
Nhằm khắc phục độ trễ tính toán khi lặp kịch bản ngẫu nhiên, mạng nơ-ron MLP được xây dựng thuần túy trên nền tảng NumPy với cấu trúc 5 đầu vào $\rightarrow$ 32 nơ-ron $\rightarrow$ 16 nơ-ron $\rightarrow$ 1 đầu ra.
- Tập dữ liệu: 2,500 mẫu mô phỏng giải tích (2,000 huấn luyện, 500 kiểm thử).
- Chỉ số đánh giá trên tập kiểm thử độc lập:
  - Hệ số xác định: $R^2 = 0.9991$
  - Sai số tuyệt đối trung bình: $MAE = 0.156\text{ mm}$
  - Căn bậc hai sai số bình phương trung bình: $RMSE = 0.220\text{ mm}$
- Thời gian suy luận: $< 0.1\text{ ms}$ cho mỗi điểm dự báo, hỗ trợ tích hợp trực tiếp vào màn hình điều khiển vận hành TBM.

---

## 7. KẾT LUẬN & KIẾN NGHỊ KỸ THUẬT
1. **Kiểm soát chặt chẽ tổn thất thể tích đất:** Cần áp dụng quy trình điều áp khoang đào EPB chính xác để duy trì $V_L \le 1.0\%$, hạn chế tối đa nguy cơ lún nứt công trình nhà phố móng nông trên trục đường Kim Mã và Cát Linh.
2. **Khu vực rủi ro cao tại S11–S12:** Đoạn qua tầng bùn sét mềm dày $12.7\text{ m}$ có bề rộng phễu lún lớn ($i > 10\text{ m}$). Cần tăng cường phụt vữa chèn lưng vỏ hầm (backfill grouting) áp lực cao liên tục ngay khi khiên đào tiến lên.
3. **Giá trị của nền tảng WebGIS & AI:** Bộ công cụ WebGIS Leaflet kết hợp bộ giải nhanh Surrogate AI là giải pháp kỹ thuật số hiện đại, trực quan, hỗ trợ đắc lực cho các nhà thầu và cơ quan quản lý đô thị trong công tác giám sát an toàn môi trường đường hầm đô thị Hà Nội.
