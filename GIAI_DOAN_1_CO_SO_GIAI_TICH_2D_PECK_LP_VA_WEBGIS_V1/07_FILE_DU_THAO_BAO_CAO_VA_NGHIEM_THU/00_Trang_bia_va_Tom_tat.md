# BẢN THẢO LUẬN ÁN TIẾN SĨ / THẠC SĨ KỸ THUẬT

<br>

<div align="center">

### BỘ GIÁO DỤC VÀ ĐÀO TẠO — CÁC TRƯỜNG ĐẠI HỌC KỸ THUẬT & GIAO THÔNG
### VIỆN CÔNG TRÌNH NGẦM & ĐỊA KỸ THUẬT ĐÔ THỊ

---

<br><br>

## LUẬN ÁN KỸ THUẬT CÔNG TRÌNH NGẦM

<br>

# NGHIÊN CỨU ĐÁNH GIÁ ĐỘ NHẠY VÀ DỰ BÁO VÙNG ẢNH HƯỞNG LÚN MẶT ĐẤT DO THI CÔNG HẦM KHIÊN ĐÀO (TBM) ĐOẠN S9–S12 METRO HÀ NỘI BẰNG PHƯƠNG PHÁP GIẢI TÍCH KẾT HỢP WEBGIS

<br><br>

**Chuyên ngành:** Kỹ thuật Xây dựng Công trình Ngầm và Mỏ  
**Mã số chuyên ngành:** 9580204 / 9580211  
**Hướng nghiên cứu:** Cơ học biến dạng đất nền đô thị, Ứng dụng giải tích & Công nghệ địa không gian (WebGIS)  

<br><br>

**Nhóm Nghiên cứu Tác tử Địa kỹ thuật & Công nghệ Địa không gian (TBM_HANOI_EIA_2027)**  
*Dự án NCKH Tuyến ĐSĐT Thí điểm TP. Hà Nội (Tuyến 3: Nhổn – Ga Hà Nội)*  

<br>

**HÀ NỘI — 2026**

</div>

---

<br>

## TÓM TẮT LUẬN ÁN (VIETNAMESE ABSTRACT)

Thi công tuyến hầm đôi song song bằng khiên đào cân bằng áp lực đất (EPB-TBM) đoạn ngầm từ ga S9 (Kim Mã) qua ga S10 (Cát Linh), ga S11 (Văn Miếu) đến ga S12 (Ga Hà Nội) thuộc Tuyến đường sắt đô thị số 3 Hà Nội đi qua khu vực nội đô lịch sử với mật độ xây dựng dày đặc, địa tầng bồi tích Đệ tứ phân lớp phức tạp và mực nước ngầm nông. Luận án này tập trung nghiên cứu, xây dựng và ứng dụng hệ thống dự báo lún bề mặt đất kết hợp giữa phương pháp giải tích phễu lún Gaussian của Peck (1969), mô hình bán giải tích đàn dẻo của Loganathan & Poulos (1998) với nền tảng WebGIS tương tác đa lớp và mô hình học máy thay thế (Surrogate AI).

Cơ sở dữ liệu địa kỹ thuật được thu thập và thẩm định nghiêm ngặt từ các công bố khoa học quốc tế có bình duyệt (Nguyen et al., 2024 tại ETASR; Nguyen, Kohata & Nguyen, 2024 tại Tạp chí Xây dựng; Giao et al., 2020 tại Springer) và hồ sơ đánh giá tác động môi trường chính thức của ADB (2013). Các phát hiện địa kỹ thuật trọng yếu chỉ ra:
1. Tại đoạn S11–S12 (hố khoan kiểm chứng BH12), hầm TBM chôn sâu $z_0 = 18.0\text{ m}$ nằm trọn vẹn trong một tầng bùn sét dẻo mềm hữu cơ rất dày ($12.7\text{ m}$, cao độ từ $-12.3\text{ m}$ đến $-25.0\text{ m}$ bgs) có chỉ số SPT $N < 4$, mô-đun đàn hồi rất thấp ($E = 7.68\text{ MPa}$), dẫn đến hệ số phễu lún mở rộng $K = 0.60$ và khoảng cách điểm uốn $i = 10.8\text{ m}$.
2. Phân tích độ nhạy 21 kịch bản tổn thất thể tích đất ($V_L \in [0.5\%; 2.0\%]$) cho thấy độ lún bề mặt cực đại của hầm đôi $S_{\max}$ đạt từ $16.6\text{ mm}$ (S11–S12, $z_0=18\text{ m}$) đến $22.1\text{ mm}$ (S9–S10, $z_0=15\text{ m}$) ở điều kiện kiểm soát thi công chuẩn ($V_L = 1.0\%$). Nếu xảy ra sự cố áp lực gương đào hoặc bùn sét yếu chảy vào khe hở đuôi khiên làm $V_L$ tăng lên $2.0\%$, độ lún cực đại vượt ngưỡng $36.4 - 44.2\text{ mm}$, đẩy 43% số công trình móng nông lân cận vào cấp rủi ro hư hỏng vừa và nghiêm trọng (Cấp 3–4 theo Burland, 1995).
3. Hệ thống bản đồ số WebGIS tương tác trên nền tảng Leaflet.js đã số hóa 60 công trình điển hình trong dải đệm $\pm 35\text{ m}$, cho phép phân vùng rủi ro trực quan và đề xuất biện pháp xử lý nền trước khi khiên đào đi qua.
4. Một mô hình Surrogate AI dạng mạng nơ-ron truyền thẳng đa tầng (MLP 5-32-16-1) được huấn luyện trên 2,500 mẫu mô phỏng số, đạt độ chính xác cao ($R^2 = 0.9991, MAE = 0.156\text{ mm}$), cho phép dự báo biến dạng lún tức thời $(< 0.1\text{ ms})$ phục vụ đắc lực cho công tác điều khiển khiên TBM theo thời gian thực.

Toàn bộ hệ thống dữ liệu, bảng tính và công thức giải tích được xây dựng và chuẩn hóa trên 4 tập tin Excel chuyên nghiệp (`.xlsx`), kèm theo ma trận kiểm toán truy xuất nguồn gốc (Evidence Traceability Matrix). Mọi giá trị tham số là giả thiết tính toán hoặc chưa có số đo thực địa đều được bôi vàng cảnh báo Audit (`==[AUDIT CẦN BỔ SUNG]==`), đi kèm đánh giá rủi ro và quy trình hiệu chỉnh ngược (back-analysis) khi có số liệu quan trắc thực tế.

---

<br>

## DISSERTATION ABSTRACT (ENGLISH)

**Title:** SENSITIVITY EVALUATION AND GROUND SETTLEMENT INFLUENCE ZONE PREDICTION FOR EPB-TBM TUNNELLING IN THE S9–S12 SECTION OF HANOI METRO LINE 3 USING ANALYTICAL METHODS INTEGRATED WITH WEBGIS

The construction of twin parallel tunnels using Earth Pressure Balance Shield Tunnel Boring Machines (EPB-TBM) for the underground section from station S9 (Kim Ma) to S12 (Hanoi Central Station) of Hanoi Pilot Light Metro Line 3 traverses a densely populated historical urban center characterized by complex Quaternary alluvial stratigraphy and shallow groundwater tables. This dissertation develops an integrated scientific framework coupling empirical Gaussian trough analytical methods (Peck, 1969), elastoplastic closed-form solutions (Loganathan & Poulos, 1998), an interactive Leaflet-based WebGIS platform, and a Multi-Layer Perceptron (MLP) Neural Surrogate model.

Geotechnical parameters were rigorously collected and cross-audited from peer-reviewed literature (Nguyen et al., 2024 in ETASR; Nguyen, Kohata & Nguyen, 2024 in Journal of Construction; Giao et al., 2020 in Springer) and official ADB project documents. Crucial geotechnical findings reveal that along the S11–S12 section (verified borehole BH12), the TBM tunnels ($z_0 = 18.0\text{ m}, D = 6.3\text{ m}$) are completely embedded within a thick ($12.7\text{ m}$) soft organic clay stratum ($N_{\text{SPT}} < 4, E = 7.68\text{ MPa}$), yielding an extended settlement trough width parameter $K = 0.60$ and an inflection point distance $i = 10.8\text{ m}$.

A sensitivity matrix of 21 volume loss scenarios ($V_L \in [0.5\%; 2.0\%]$) demonstrates that the maximum twin-tunnel surface settlement $S_{\max}$ ranges from $16.6\text{ mm}$ to $22.1\text{ mm}$ under standard EPB operational control ($V_L = 1.0\%$). In case of operational face instability or ground loss ($V_L = 2.0\%$), maximum settlement escalates to $36.4 - 44.2\text{ mm}$, triggering moderate-to-severe damage risks (Burland Categories 3–4) for up to 43% of adjacent shallow-foundation structures within a $\pm 18\text{ m}$ buffer. The interactive WebGIS system catalogs 60 representative buildings, enabling dynamic risk zoning and proactive mitigation planning. Additionally, the calibrated MLP neural surrogate model ($R^2 = 0.9991, MAE = 0.156\text{ mm}$) provides millisecond-level $(< 0.1\text{ ms})$ inference capabilities suitable for real-time TBM steering and risk monitoring. All engineering datasets are documented in professional Excel workbooks with complete evidence audit trails.
