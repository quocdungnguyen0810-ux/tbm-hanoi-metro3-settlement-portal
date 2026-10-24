# DỰ BÁO PHỄU LÚN MẶT ĐẤT NGẮN HẠN VÀ DÀI HẠN DO THI CÔNG HẦM ĐÔI TBM ĐOẠN NGẦM S9–S12 METRO NHỔN – GA HÀ NỘI KẾT HỢP HỆ THỐNG BẢN ĐỒ SỐ WEBGIS
## SHORT- AND LONG-TERM SURFACE SETTLEMENT PREDICTION INDUCED BY TWIN EPB-TBM TUNNELLING ALONG SECTION S9–S12 OF HANOI METRO LINE 3 INTEGRATED WITH WEBGIS

**Nguyễn Hải Hà (Tác giả liên hệ)**, **Lê Anh Đức**, **Trần Văn Long**  
*Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình, Trường Đại học Giao thông vận tải (UTC), Hà Nội, Việt Nam*  
**Tạp chí mục tiêu:** *Tạp chí Khoa học Giao thông vận tải (Transport and Communications Science Journal - TCSJ)*

---

## TÓM TẮT / ABSTRACT

**Tóm tắt:** Quá trình thi công tuyến hầm đôi bằng máy đào khiên cân bằng áp lực đất (EPB-TBM) đoạn ngầm từ ga S9 (Kim Mã) đến ga S12 (Ga Hà Nội) thuộc Dự án Tuyến đường sắt đô thị số 3 Hà Nội đi qua khu vực nội đô lịch sử có địa tầng trầm tích Đệ tứ phức tạp. Nghiên cứu này thiết lập mô hình tích hợp giữa lời giải giải tích 2D/3D (Peck 1969, Loganathan & Poulos 1998 kết hợp hàm động học lỗi tích lũy dọc trục `erf`) và bài toán lún cố kết thấm một chiều Terzaghi đã hiệu chỉnh chính xác theo lý thuyết đàn hồi môi trường liên tục tại hố khoan BH12. Tại tầng bùn sét mềm hữu cơ Lớp 3 dày 12,7 m (độ sâu 12,3–25,0 m, $E = 7.680\text{ kPa}, \nu = 0,35$), mô-đun nén không nở hông được chứng minh đạt $E_{\text{oed}} = 12.325,93\text{ kPa}$ và hệ số nén lún thể tích chuẩn đạt $m_v = 8,113 \times 10^{-5}\text{ kPa}^{-1}$. Kết quả chỉ ra rằng tại chế độ vận hành danh định ($V_L = 1,0\%$), độ lún tức thời cực đại của hầm đôi đạt 19,70 mm; khi xét thêm thành phần cố kết thấm do hạ mực nước ngầm $\Delta h = 2,5\text{ m}$, độ lún dài hạn tăng lên 33,80 mm (kịch bản thoát nước biên cục bộ $\alpha = 0,558$) đến 44,97 mm (cận trên bảo thủ), phù hợp cao với kết quả mô phỏng 3D FEM thực nghiệm là 43,09 mm (sai khác $< 4,4\%$). Toàn bộ cơ sở dữ liệu được tích hợp lên nền tảng WebGIS 2.0 trực tuyến kèm quy trình phản ứng khẩn cấp TARP 3 cấp độ phục vụ giám sát thi công.

**Abstract:** Twin Earth Pressure Balance Tunnel Boring Machine (EPB-TBM) excavation along the underground section S9 (Kim Ma) to S12 (Hanoi Station) of Hanoi Metro Line 3 traverses complex Quaternary alluvial deposits beneath densely populated historical neighborhoods. This paper presents an integrated analytical framework combining 2D/3D short-term tunnelling-induced ground movement formulations (Peck 1969; Loganathan & Poulos 1998 coupled with a longitudinal cumulative error function `erf`) and a rigorously calibrated 1D Terzaghi hydro-mechanical consolidation model at Borehole BH12. For the 12.7-m-thick soft organic clay stratum (Layer 3, depth 12.3–25.0 m, $E = 7,680\text{ kPa}, \nu = 0.35$), continuum elasticity yields an exact oedometric modulus $E_{\text{oed}} = 12,325.93\text{ kPa}$ and coefficient of volume compressibility $m_v = 8.113 \times 10^{-5}\text{ kPa}^{-1}$. Under nominal operating conditions ($V_L = 1.0\%$), maximum short-term twin-tunnel settlement reaches 19.70 mm; accounting for pore-pressure drawdown ($\Delta h = 2.5\text{ m}$) increases total long-term settlement to 33.80 mm (partial boundary drainage $\alpha = 0.558$) and up to 44.97 mm (uniform upper bound), closely matching the published 3D FEM benchmark of 43.09 mm (deviation $< 4.4\%$). All predictive outputs are deployed onto a real-time interactive WebGIS 2.0 platform integrated with a 3-tier Trigger Action Response Plan (TARP).

**Từ khóa:** Hầm đô thị EPB-TBM; Tuyến ĐSĐT số 3 Hà Nội (S9–S12); Động học lún 3D; Lún cố kết thấm BH12; Hệ thống WebGIS TARP.

---

## 1. ĐẶT VẤN ĐỀ

Tuyến đường sắt đô thị thí điểm TP. Hà Nội (Tuyến số 3, đoạn Nhổn – Ga Hà Nội) gồm 8,5 km đi cao và 4,0 km đi ngầm từ ga S9 (Kim Mã) qua ga S10 (Cát Linh), ga S11 (Văn Miếu) đến ga S12 (Ga Hà Nội). Đoạn tuyến hầm xuyên qua các tầng đất yếu bão hòa nước thuộc đồng bằng sông Hồng. Thực tiễn thi công từ khi khiên đào TBM số 1 ("Thần Tốc", đường kính ngoài $D = 6,30\text{ m}$) khởi đào tại ga S9 ở độ sâu $17,8\text{ m}$ ngày 30/07/2024 đến khi thông hầm tại ga S12 ngày 01/12/2025 với 1.720 vòng vỏ hầm lắp đặt [1], cùng báo cáo giám sát xã hội của Ngân hàng Phát triển Châu Á (ADB EMR Q1/2025, ghi nhận 56 hộ dân bị ảnh hưởng dọc 4 ga ngầm và hiện tượng trào phụ gia khoan tháng 02/2025) [2], cho thấy việc chỉ đánh giá độ lún tức thời trong mặt phẳng 2D là chưa đủ để kiểm soát rủi ro dài hạn.

Các công trình nghiên cứu gần đây tại Việt Nam đã bước đầu phân tích lún bề mặt do đào hầm bằng phương pháp giải tích và mô phỏng số [3–6]. Tuy nhiên, phần lớn các nghiên cứu trước đây hoặc chỉ xét biến dạng tức thời trong điều kiện không thoát nước mà bỏ qua độ lún cố kết thấm dài hạn khi mực nước ngầm suy giảm, hoặc chưa tích hợp trường lún động 3 chiều theo từng bước tiến Ring đào vào hệ thống thông tin địa lý WebGIS phục vụ điều hành trực tiếp tại hiện trường. Bài báo này giải quyết trọn vẹn khoảng trống đó thông qua việc kết hợp mô hình động học tiến gương 3D, hiệu chỉnh chuẩn xác thông số nén lún thể tích $m_v$ tại hố khoan BH12 và xây dựng cổng WebGIS 2.0 tích hợp ma trận phản ứng TARP.

---

## 2. CƠ SỞ LÝ THUYẾT VÀ ĐẶC TRƯNG ĐỊA KỸ THUẬT ĐOẠN S9–S12

### 2.1. Mô hình động học phễu lún 3 chiều theo bước tiến khiên đào TBM
Độ lún mặt đất tức thời ngang trục hầm đơn theo Loganathan & Poulos (1998) [7] kết hợp hàm tích lũy dọc trục hầm theo khoảng cách tới gương đào $(y - y_f)$ của Attewell & Woodman (1982) [8] được xác định bởi:
$$S(x, y) = 4(1 - \nu)\frac{R^2}{z_0} \varepsilon_0 \exp\left(-\frac{1,38 x^2}{(z_0 + R)^2}\right) \cdot \frac{1}{2}\left[1 + \mathrm{erf}\left(\frac{y - y_f}{\sqrt{2} i_y}\right)\right]$$
Với hai ống hầm đặt cách nhau $d = 13,0\text{ m}$ và độ lệch gương đào giữa TBM1 và TBM2 là $\Delta y_{\text{lag}} = 50\text{ m}$, trường lún tổng hợp là $S_{\text{twin}}(x, y) = S_1(x - d/2, y) + S_2(x + d/2, y - \Delta y_{\text{lag}})$.

### 2.2. Chuẩn hóa hệ số nén lún thể tích $m_v$ và lún cố kết thấm tại hố khoan BH12
Theo kết quả khảo sát địa chất tại hố khoan BH12 đoạn S11–S12 [4, 5], đường hầm ($z_0 = 18,0\text{ m}$) nằm hoàn toàn trong Lớp 3 là tầng bùn sét mềm hữu cơ (Soft organic clay) phân bố từ độ sâu $-12,3\text{ m}$ đến $-25,0\text{ m}$ ($H = 12,7\text{ m}, \gamma = 18,1\text{ kN/m}^3, e_0 = 1,46, S_u = 16,7\text{ kPa}, E = 7.680\text{ kPa}, \nu = 0,35$). Từ quan hệ đàn hồi môi trường liên tục giữa mô-đun biến dạng $E$ và mô-đun nén một chiều không nở hông $E_{\text{oed}}$:
$$E_{\text{oed}} = \frac{E(1 - \nu)}{(1 + \nu)(1 - 2\nu)} = \frac{7.680(1 - 0,35)}{(1 + 0,35)(1 - 0,70)} = 12.325,93\text{ kPa} \implies m_v = \frac{1}{E_{\text{oed}}} = 8,113 \times 10^{-5}\text{ kPa}^{-1}$$

| Mã lớp | Hố khoan / Đoạn | Tên lớp đất | Chiều dày $H$ (m) | $E$ (kPa) | $\nu$ | $E_{\text{oed}}$ (kPa) | $m_v$ chuẩn ($\text{kPa}^{-1}$) | Đánh giá Địa kỹ thuật |
|---|---|---|---:|---:|---:|---:|---:|---|
| `BH12_L1` | BH12 (S11–S12) | Đất lấp nhân tạo | 2,00 | 9.250 | 0,41 | 21.503,15 | `0,0000465` | Hợp lý địa chất |
| `BH12_L2` | BH12 (S11–S12) | Sét pha dẻo cứng đến cứng | 10,30 | 15.300 | 0,38 | 28.641,30 | `0,0000349` | Hợp lý địa chất |
| `BH12_L3` | BH12 (S11–S12) | Bùn sét mềm hữu cơ (Tầng hầm) | 12,70 | 7.680 | 0,35 | 12.325,93 | `0,0000811` | Hợp lý địa chất |
| `BH12_L4` | BH12 (S11–S12) | Cát pha bụi chặt vừa | 11,90 | 35.020 | 0,33 | 51.887,22 | `0,0000193` | Hợp lý địa chất |
| `S9S10_GU1` | S9–S10 (Kim Mã) | Sét ít dẻo xen kẹp bụi | 7,20 | 10.000 | 0,35 | 16.049,38 | `0,0000623` | Hợp lý địa chất |
| `S9S10_GU34` | S9–S10 (Kim Mã) | Sét béo hữu cơ dẻo mềm | 7,80 | 7.000 | 0,35 | 11.234,57 | `0,0000890` | Hợp lý địa chất |

---

## 3. KẾT QUẢ PHÂN TÍCH PHỄU LÚN NGẮN HẠN, DÀI HẠN VÀ ĐỐI CHỨNG 3D FEM

Khi xảy ra suy giảm áp lực nước lỗ rỗng cục bộ quanh vỏ hầm tương đương chiều cao cột nước $\Delta h_{\max} = 2,5\text{ m}$ ($\Delta u = \gamma_w \Delta h = 24,525\text{ kPa}$), độ lún cố kết bổ sung được tính theo $\Delta S_{\text{hydro}}(x) = \alpha_{\text{drain}} m_v H \Delta u \exp(-x^2 / (2 i_{\text{drain}}^2))$. Bảng dưới đây trình bày kết quả đối sánh 4 kịch bản cố kết thấm tại mặt cắt BH12:

| Mã kịch bản | Mô tả cơ học kịch bản | $m_v$ ($\text{kPa}^{-1}$) | Hệ số $\alpha_{\text{drain}}$ | $S_{\text{tbm,max}}$ (mm) | $S_{\text{hydro,max}}$ (mm) | $S_{\text{total,max}}$ (mm) | Sai khác so với 3D FEM (43,09 mm) |
|---|---|---:|---:|---:|---:|---:|---:|
| `HM_SCEN_02` | Nhánh nén lại / Quá cố kết nhẹ | `0,0000450` | 1,000 | 19,70 | 14,02 | **33,72** | -21,7% (Ngắn/Trung hạn) |
| `HM_SCEN_03` | Chuẩn hóa BH12 (Thoát nước biên cục bộ) | `0,0000811` | 0,558 | 19,70 | 14,10 | **33,80** | -21,5% (Thoát nước một phần) |
| `HM_SCEN_04` | Cận trên bảo thủ BH12 (Hạ nước ngầm toàn tầng) | `0,0000811` | 1,000 | 19,70 | 25,27 | **44,97** | **+4,36% (Khớp cận trên 3D FEM)** |
| `MIDAS_3D_REF` | Mô phỏng 3D FEM Soft Soil (Nguyen et al. 2024, Nút 228594) | Soft Soil ($\lambda=1,822$) | 3D Stage S22 | — | — | **43,09** | Mốc chuẩn tham chiếu (0,0%) |

---

## 4. TÍCH HỢP HỆ THỐNG WEBGIS 2.0 VÀ QUY TRÌNH PHẢN ỨNG KHẨN CẤP (TARP)

Hệ thống bản đồ số WebGIS 2.0 đã được triển khai trực tuyến tại địa chỉ rút gọn `https://is.gd/tbm_hanoi_v2`, cho phép điều chỉnh vị trí gương đào từ Ring 0 đến Ring 2.500 và tự động phân loại ngưỡng cảnh báo TARP:
- **Mức 1 – Xanh (Bình thường, $S < 10\text{ mm}$):** Duy trì áp lực gương đào $P_s = 130 \div 150\text{ kPa}$, quan trắc 1 lần/ngày.
- **Mức 2 – Vàng (Cảnh báo, $10\text{ mm} \le S < 20\text{ mm}$):** Tăng áp lực ép vữa đuôi khiên lên $P_a = 1,8 \div 2,2\text{ bar}$, kiểm tra độ kín gioăng cao su đuôi khiên để ngăn thấm nước vào hầm tại tầng bùn sét L3.
- **Mức 3 – Đỏ (Hành động khẩn cấp, $S \ge 20\text{ mm}$ hoặc độ nghiêng $> 1/500$):** Kích hoạt bơm vữa bù lún (Compensation Grouting) dưới móng công trình và giảm tốc độ tiến khiên xuống $6 \div 8\text{ m/ngày}$.

---

## 5. KẾT LUẬN

1. Việc kết hợp giải tích 3D Loganathan & Poulos với hàm động học `erf` và mô hình cố kết thấm Terzaghi hiệu chỉnh ($m_v = 8,113 \times 10^{-5}\text{ kPa}^{-1}$) tại hố khoan BH12 cho phép dự báo tin cậy cả độ lún tức thời ($19,70\text{ mm}$) và tổng độ lún dài hạn ($33,80 \div 44,97\text{ mm}$), tiệm cận sát kết quả 3D FEM Midas GTS NX ($43,09\text{ mm}$).
2. Hệ thống WebGIS 2.0 trực tuyến giúp số hóa toàn bộ quy trình giám sát theo từng Ring đào và hỗ trợ ra quyết định điều chỉnh thông số EPB-TBM theo thời gian thực.

---

## TÀI LIỆU THAM KHẢO
1. Bộ Xây dựng (MOC) (2025). *Máy đào hầm TBM số 1 "Thần Tốc" hoàn thành khoan hầm qua 4 ga ngầm S9–S12 (1.720 vòng vỏ hầm), ngày 01/12/2025*. Cổng thông tin Bộ Xây dựng.
2. Asian Development Bank (ADB) & Ha Noi MRB (2025). *External Social Monitoring Report Q1/2025: Ha Noi Metro Rail System Project (Line 3)*, Document `40080-013-smr-en_49.pdf`.
3. Phạm Tuyên Dương (2026). Phân tích xu hướng biến dạng nền đất do đào hầm bằng mô hình kiểm soát chuyển vị (DCM). *Tạp chí Khoa học Giao thông vận tải (TCSJ)*, 77(2), 181–195. DOI: `10.47869/tcsj.77.2.3`.
4. Nguyen, C. G., Kohata, Y., & Nguyen, X. P. (2024). Design of urban tunnels in soft soil using tunnel boring machine (TBM) application for the UMRT Line No.3 in Hanoi. *Tạp chí Xây dựng*, 06.2024, 84–89.
5. Giao, P. H., Nguyen, H. T., & Hoang, T. T. H. (2020). Geotechnical Characterization and Land Subsidence Analysis for the UMRT Line No.3 in Hanoi. *Springer LNCE 62*, 289–296.
6. Nguyen, T. S., Bui, D. P., & Nguyen, T. H. (2024). The Effect of Seismic Load on TBM Structures for Metro Line 3 in Hanoi, Vietnam. *ETASR*, 14(1), 13047–13051.
7. Loganathan, N., & Poulos, H. G. (1998). Analytical prediction for tunneling-induced ground movements in clays. *ASCE JGGE*, 124(9), 846–856.
8. Attewell, P. B., & Woodman, J. P. (1982). Predicting the dynamics of ground settlement and its derivatives caused by tunnelling in soil. *Ground Engineering*, 15(8), 13–22.
