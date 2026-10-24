# MA TRẬN PHỐI HỢP CÔNG CỤ VÀ TÁC TỬ THỰC HIỆN GIAI ĐOẠN 2
### DỰ ÁN NGHIÊN CỨU LÚN HẦM TBM ĐOẠN S9–S12 METRO TUYẾN 3 HÀ NỘI

**Cơ chế thực thi:** Multi-Agent Guarded Protocol  
**Thời gian ban hành:** 2026-10-15  

---

### I. BẢNG MA TRẬN PHỐI HỢP LIÊN TÁC TỬ (MULTI-AGENT INTERACTION MATRIX)

Ma trận dưới đây xác lập mối quan hệ phụ thuộc, chuyển giao dữ liệu (Handoff) và trách nhiệm giải trình giữa các tác tử trong toàn bộ vòng đời Giai đoạn 2:

| Bước quy trình (Workflow) | Tác tử chủ trì (Lead Agent) | Tác tử phối hợp (Supporting Agents) | Dữ liệu đầu vào (Input Artifacts) | Công cụ thực hiện (Tools Used) | Sản phẩm đầu ra bắt buộc (Output Artifacts) | Cổng kiểm toán (Gate Check) |
|---|---|---|---|---|---|---|
| **WF-20B (Setup & Backup)** | **Pipeline & Data Engineer** | General Contractor, Evidence Auditor | Toàn bộ 4 file Excel, 3 GeoJSON, 7 ảnh từ Giai đoạn 1 | Python `shutil`, `hashlib` | `00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1/`, Bảng kiểm kê mã băm | Gate 1–5 Verification |
| **WF-21 (3D LP Modeling)** | **Mechanics Reviewer** | Pipeline Engineer, Academic Author | Thông số hình học $D=6.3\text{m}$, $z_0=15 \div 18\text{m}$, $V_L=0.5 \div 2.0\%$ | Python, NumPy, SciPy (Simpson integration) | Module giải tích 3D, dữ liệu chuyển vị $U_z(x, y)$, file `TBM_HANOI_G2_LOGANATHAN_POULOS_3D.xlsx` | **GATE 6** |
| **WF-22 (Monte Carlo & GSA)** | **Stochastic Analyst** | Mechanics Reviewer, Data Engineer | Phân phối thống kê $V_L, z_0, K, E, \nu$ (Mean, COV, Bounds) | Python, NumPy Latin Hypercube, Matplotlib | Bộ 10,000 mẫu ngẫu nhiên, chỉ số Sobol $S_i, S_{Ti}$, file `TBM_HANOI_G2_MONTE_CARLO_SENSITIVITY.xlsx` | **GATE 7** |
| **WF-23 (100 Buildings Risk)** | **GIS & Spatial Analyst** | Mechanics Reviewer, Evidence Auditor | Bình đồ tuyến Metro 3 WGS-84, hiện trạng 100 công trình Kim Mã - Ga HN | Python GeoJSON processor, Excel engine | `buildings_exposure_100.geojson`, file `TBM_HANOI_G2_BUILDING_STRAIN_DAMAGE_100.xlsx` | **GATE 6 & 8** |
| **WF-24 (Advanced Excel)** | **Pipeline & Data Engineer** | Mechanics Reviewer, Stochastic Analyst | Dữ liệu tính toán từ WF-21, WF-22, WF-23 | Python `openpyxl`, formula engine | 3 file Excel hoàn thiện, 100% công thức động, Metadata, Data Dictionary | **GATE 8** |
| **WF-25 (300 DPI Graphics)** | **Academic Author** | Stochastic Analyst, GIS Analyst | Dữ liệu 3D, Monte Carlo, Sobol, Burland 100 công trình | Python `matplotlib`, `scipy` | 7 hình ảnh phân giải cao 300 DPI (`FIG_08` đến `FIG_14`) | **GATE 8** |
| **WF-26 (WebGIS 2.0 Platform)** | **GIS & Spatial Analyst** | Pipeline Engineer, Academic Author | `buildings_exposure_100.geojson`, `alignment_longitudinal_wgs84.geojson` | Leaflet.js, Chart.js, HTML5/CSS3 | Ứng dụng `webgis_settlement_advance_v2.html` hoạt động offline/online | **GATE 8** |
| **WF-27 (Comprehensive Report)** | **Academic Author** | Scientific Editor, Mechanics Reviewer | Kết quả nghiên cứu trọn vẹn của các WF-21 đến WF-26 | Markdown editor, Python `python-docx` | `BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_2.md` và `.docx` | **GATE 8** |
| **WF-28 (Dossier & Seal)** | **General Contractor** | Evidence Auditor, Academic Editor | Tất cả sản phẩm bàn giao Giai đoạn 2 | Python `hashlib`, Markdown, `docx` | Bộ hồ sơ nghiệm thu (Tờ trình, Báo cáo tóm tắt, Biên bản kiểm toán, Checksum SHA-256) | **GATE 8 PASSED** |

---

### II. BẢN ĐẶC TẢ CHI TIẾT TỪNG TÁC TỬ TRONG GIAI ĐOẠN 2

#### 1. General Contractor (Chỉ huy trưởng hệ thống)
- **Nhiệm vụ:**
  - Thiết lập trạng thái phiên làm việc trong `AGENT_STATE.json` sang `PHASE_2_EXECUTION_AND_CONSOLIDATION`.
  - Phân bổ chỉ tiêu tiến độ, giám sát các điều kiện chuyển giao tác vụ giữa các agent.
  - Tổ chức rà soát chéo độc lập và chủ trì phiên họp bàn giao hồ sơ nghiệm thu Giai đoạn 2.
- **Tiêu chuẩn chất lượng:**
  - Không cho phép bất kỳ sản phẩm nào thiếu mã băm SHA-256 hoặc chứa thông tin giả định không được gắn cờ Audit.

#### 2. Mechanics Reviewer (Chuyên gia Cơ học Đất & Hầm ngầm)
- **Nhiệm vụ:**
  - Thẩm tra công thức 3 chiều của Loganathan & Poulos (1998):
    $$U_z(x, z=0, y) = 4(1 - \nu) \cdot \frac{R^2}{z_0} \cdot \exp\left(-\left[\frac{1.38 x^2}{(z_0 + R)^2} + \frac{0.69 z^2}{z_0^2}\right]\right) \cdot \epsilon_0 \cdot \left[1 - \Phi\left(\frac{y - y_f}{i_y}\right)\right]$$
  - Thẩm tra công thức biến dạng kéo giới hạn của Burland (1995) kết hợp Boscardin & Cording (1989):
    $$\epsilon_{\max} = \max\left(\epsilon_{br}, \epsilon_{dr}\right) + \epsilon_h$$
    Trong đó:
    $$\frac{\Delta}{L} = \frac{L}{12 t} \cdot \epsilon_{br} + \frac{3 I}{2 t A L} \cdot \frac{E}{G} \cdot \epsilon_{dr}$$
- **Tiêu chuẩn chất lượng:**
  - Bảo toàn thể tích tuyệt đối, không xảy ra kỳ dị toán học tại tâm hầm hoặc các điểm vô cực.

#### 3. Pipeline & Data Engineer (Kỹ sư Dữ liệu & Bảng tính)
- **Nhiệm vụ:**
  - Lập trình tự động tạo lập 3 workbook Excel chuẩn hóa theo phong cách Financial & Engineering Model quốc tế (tiêu đề Navy/Slate, chữ trắng đậm, zebra striping thanh lịch, khung viền mỏng).
  - Tích hợp 100% công thức động của Excel: `EXP`, `SQRT`, `NORMDIST`, `INDEX`, `MATCH`, `IFERROR`, `AVERAGE`, `STDEV.S`, `PERCENTILE.EXC`.
  - Thiết lập các trang phụ trợ bắt buộc: `Muc_Luc_Metadata` (Mục lục và siêu liên kết nội bộ), `Data_Dictionary` (Định nghĩa tường minh từng cột, đơn vị đo SI và ký hiệu).

#### 4. Stochastic & Sensitivity Analyst (Chuyên gia Ngẫu nhiên & Tối ưu)
- **Nhiệm vụ:**
  - Thực hiện sinh 10,000 mẫu ngẫu nhiên bằng phương pháp Latin Hypercube Sampling (LHS) đảm bảo quét đều không gian tham số 5 chiều.
  - Các biến ngẫu nhiên được gán phân phối thực tế:
    * Tổn thất thể tích $V_L$: Phân phối Chuẩn cụt (Truncated Normal) $\mu = 1.0\%$, $\sigma = 0.25\%$, dải $[0.4\%, 2.2\%]$.
    * Chiều sâu chôn hầm $z_0$: Phân phối Đều (Uniform) $[14.5\text{m}, 18.5\text{m}]$ bao trùm toàn bộ đoạn S9–S12.
    * Hệ số phễu lún $K$: Phân phối Tam giác (Triangular) $\min = 0.45, \text{mode} = 0.55, \max = 0.65$.
    * Mô-đun đàn hồi đất mềm $E$: Phân phối Log-Normal $\mu = 12.5\text{ MPa}, \text{COV} = 30\%$.
    * Hệ số Poisson $\nu$: Phân phối Đều $[0.30, 0.45]$.
  - Tính toán chỉ số Sobol bậc một $S_i = \frac{\mathbb{V}[\mathbb{E}(Y|X_i)]}{\mathbb{V}(Y)}$ và chỉ số tương tác tổng thể $S_{Ti}$.

#### 5. GIS & Spatial Analyst (Chuyên gia Địa không gian & WebGIS)
- **Nhiệm vụ:**
  - Xây dựng tập dữ liệu GeoJSON 100 công trình thực tế dọc hành lang 3.5 km của đoạn S9–S12 (độ chính xác tọa độ WGS-84 thập phân 6 chữ số).
  - Lập trình ứng dụng WebGIS 2.0 độc lập:
    * Thêm thanh trượt mô phỏng tiến độ khiên đào TBM (từ Ring 0 đến Ring 2,500).
    * Khi di chuyển thanh trượt, vị trí gương đào cập nhật trực tiếp trên bản đồ vệ tinh, đồng thời biểu đồ trắc dọc lún động cập nhật tức thời theo công thức hàm động học.
    * 100 công trình tự động đổi màu theo 5 cấp rủi ro Burland (Xanh lục = Cấp 0, Vàng = Cấp 1, Cam = Cấp 2, Đỏ cam = Cấp 3, Đỏ thẫm = Cấp 4).
    * Hỗ trợ bộ lọc tìm kiếm theo tên đường, theo cấp rủi ro và xuất file dữ liệu.

#### 6. Evidence Auditor (Kiểm toán viên Khoa học & Đảm bảo Chất lượng)
- **Nhiệm vụ:**
  - Thực thi kiểm tra Gate 6 (Toán học 3D), Gate 7 (Hội tụ ngẫu nhiên) và Gate 8 (Hoàn thiện hồ sơ & mã băm).
  - Đảm bảo toàn bộ tài liệu đều có mục cảnh báo bôi vàng đối với các dữ liệu hiện trường cần cập nhật khi có quan trắc hầm.
  - Niêm phong toàn bộ sản phẩm bằng thuật toán SHA-256.

#### 7. Academic Author & Scientific Editor (Biên tập & Chắp bút)
- **Nhiệm vụ:**
  - Chắp bút toàn văn bản thảo Báo cáo Giai đoạn 2 dài trên 100 trang Markdown với bố cục khoa học chuẩn mực.
  - Biên dịch tự động sang file Microsoft Word `.docx` hoàn hảo về mặt thẩm mỹ trình bày, sẵn sàng nộp nghiệm thu trước Hội đồng Khoa và Bộ môn.

---

### III. BẢN ĐẶC TẢ CHI TIẾT TỪNG CÔNG CỤ KỸ THUẬT TRONG GIAI ĐOẠN 2

#### 1. Python 3.14 (Môi trường Runtime Hạt nhân)
- **Vai trò:** Trung tâm điều phối logic tính toán và tự động hóa toàn bộ chuỗi công việc (Orchestration Engine).
- **Nhiệm vụ:** Thực thi các module mô phỏng, xử lý dữ liệu GeoJSON, băm mật mã và gọi các engine con.
- **Chức năng:** Hỗ trợ đa luồng, quản lý bộ nhớ linh hoạt, tích hợp chặt chẽ hệ sinh thái thư viện khoa học.
- **Yêu cầu:** Tương thích Windows PowerShell, mã hóa UTF-8 tuyệt đối, xử lý lỗi ngoại lệ có kiểm soát.
- **Kết quả:** Chuỗi script vận hành tự động trong `scripts/` thực hiện trơn tru từ đầu đến cuối với Exit Code 0.

#### 2. NumPy & SciPy (Động cơ Tính toán Giải tích & Thống kê Khoa học)
- **Vai trò:** Hạt nhân tính toán giải tích trường chuyển vị 3D và mô phỏng xác suất thống kê.
- **Nhiệm vụ:** Tính ma trận lún Loganathan & Poulos 3D, tích lũy lún dọc trục qua hàm `erf`, sinh 10,000 mẫu ngẫu nhiên Latin Hypercube, phân rã phương sai Sobol.
- **Chức năng:** Vector hóa mảng nhiều chiều, tích phân số học Simpson, giải tích ngẫu nhiên phi tuyến.
- **Yêu cầu:** Độ chính xác float64, thời gian xử lý mảng $10,000 \times 100$ điểm dưới 3 giây, độ hội tụ thống kê cao.
- **Kết quả:** Bộ dữ liệu chuyển vị 3D, thống kê P5-P50-P95, chỉ số Sobol bậc 1 ($S_i$) và tương tác tổng ($S_{Ti}$).

#### 3. OpenPyXL (Động cơ Mô hình hóa Bảng tính Excel)
- **Vai trò:** Xây dựng hệ thống bảng tính khoa học và quản lý dữ liệu số liệu phục vụ tra cứu.
- **Nhiệm vụ:** Tạo lập 4 workbook Excel chuyên nghiệp chuẩn mô hình tài chính/kỹ thuật quốc tế.
- **Chức năng:** Tự động định dạng ô, tô màu zebra striping, kẻ viền, nhúng công thức động (`EXP`, `SQRT`, `VLOOKUP`, `INDEX/MATCH`).
- **Yêu cầu:** 100% công thức Excel hoạt động động lực học, có sheet `Muc_Luc_Metadata` và `Data_Dictionary`.
- **Kết quả:** 4 file Excel đa trang hoàn thiện tại `02_BO_DU_LIEU_EXCEL_NANG_CAO_GIAI_DOAN_2/`.

#### 4. Matplotlib (Động cơ Đồ họa Khoa học 300 DPI)
- **Vai trò:** Kết xuất hình ảnh đồ họa trực quan phục vụ công bố khoa học quốc tế.
- **Nhiệm vụ:** Thiết kế và xuất bản 7 đồ họa chuyên sâu (`FIG_08` đến `FIG_14`).
- **Chức năng:** Vẽ đồ thị vector/raster 2D/3D, phối màu ColorBrewer thân thiện, hỗ trợ font Times New Roman và ký hiệu LaTeX.
- **Yêu cầu:** Độ phân giải thực $\ge 300\text{ DPI}$, kích thước $3000 \times 1800\text{ px}$, chú thích song ngữ Anh - Việt.
- **Kết quả:** 7 file ảnh PNG 300 DPI sắc nét tại `03_HINH_ANH_MINH_HOA_CHAT_LUONG_CAO_GIAI_DOAN_2/`.

#### 5. Leaflet.js & Chart.js (Động cơ WebGIS & Bản đồ số Tương tác)
- **Vai trò:** Cung cấp giao diện trực quan hóa địa không gian cho người dùng và các bên liên quan.
- **Nhiệm vụ:** Xây dựng ứng dụng WebGIS 2.0 hiển thị 100 công trình, tim hầm và mô phỏng bước tiến TBM.
- **Chức năng:** Điều khiển bản đồ nền vệ tinh, lọc dữ liệu theo đường phố/cấp rủi ro, cập nhật biểu đồ động kép.
- **Yêu cầu:** Hoạt động độc lập không cần Web Server (chạy trực tiếp trên trình duyệt Client-side), mượt mà, responsive.
- **Kết quả:** Ứng dụng bản đồ số tương tác hoàn chỉnh `webgis_settlement_advance_v2.html`.

#### 6. python-docx (Động cơ Tự động hóa Soạn thảo Văn bản)
- **Vai trò:** Xuất bản tài liệu văn bản in ấn chính thức phục vụ nộp nghiệm thu.
- **Nhiệm vụ:** Tự động chuyển đổi toàn văn báo cáo Markdown và các hồ sơ nghiệm thu sang file Microsoft Word (.docx).
- **Chức năng:** Thiết lập lề trang, dãn dòng, tạo tiêu đề nhiều cấp, định dạng bảng có khung viền mỏng và chèn hình ảnh 300 DPI.
- **Yêu cầu:** Tuân thủ chặt chẽ thể thức văn bản luận án sau đại học (Lề 30-20-20-20 mm, font 13pt, cách đoạn 6pt).
- **Kết quả:** File Báo cáo toàn văn `.docx` và 5 file Word hồ sơ nghiệm thu hoàn hảo về thẩm mỹ.

#### 7. Hashlib (Động cơ Kiểm toán Mật mã & Toàn vẹn Dữ liệu)
- **Vai trò:** Công cụ bảo đảm liêm chính khoa học và phòng chống sửa đổi dữ liệu trái phép.
- **Nhiệm vụ:** Tính toán mã băm SHA-256 cho toàn bộ 54 tệp tin đầu vào và sản phẩm đầu ra Giai đoạn 2.
- **Chức năng:** Sinh chuỗi băm 256-bit chuẩn FIPS PUB 180-4 theo từng khối nhị phân 64KB.
- **Yêu cầu:** Tính toàn vẹn tuyệt đối; phát hiện ngay lập tức bất kỳ sự biến đổi nào dù chỉ là 1 byte.
- **Kết quả:** Bảng niêm phong mã băm `DANH_MUC_HO_SO_VA_CHECKSUM_SHA256_GIAI_DOAN_2.md`.

