# MA TRẬN PHỐI HỢP CÔNG CỤ VÀ TÁC TỬ THỰC HIỆN GIAI ĐOẠN 3
### DỰ ÁN NGHIÊN CỨU LÚN HẦM TBM ĐOẠN S9–S12 METRO TUYẾN 3 HÀ NỘI

**Cơ chế thực thi:** Multi-Agent Guarded Protocol  
**Thời gian ban hành:** 2026-10-15  

---

### I. BẢNG MA TRẬN PHỐI HỢP LIÊN TÁC TỬ GIAI ĐOẠN 3 (MULTI-AGENT INTERACTION MATRIX)

| Bước quy trình (Workflow) | Tác tử chủ trì (Lead Agent) | Tác tử phối hợp (Supporting Agents) | Dữ liệu đầu vào (Input Artifacts) | Công cụ thực hiện (Tools Used) | Sản phẩm đầu ra bắt buộc (Output Artifacts) | Cổng kiểm toán (Gate Check) |
|---|---|---|---|---|---|---|
| **WF-29 (Coupled HM Modeling)** | **Mechanics Reviewer** | Pipeline Engineer, Academic Author | Thông số địa chất BH12, mực nước ngầm, hệ số thấm $k$, hệ số cố kết $c_v$ | Python, NumPy, SciPy (Biot/Terzaghi) | Module giải tích đa trường Thấm - Biến dạng, phân rã lún $S_{\text{tbm}}$ và $S_{\text{hydro}}$, file `TBM_HANOI_G3_COUPLED_HYDRO_MECHANICAL.xlsx` | **GATE 9** |
| **WF-30 (3D FEM Benchmark)** | **Numerical Modeler** | Mechanics Reviewer, Pipeline Engineer | Hình học hầm đôi $D=6.3\text{m}, d=13.0\text{m}$, mô hình Hardening Soil Small-Strain (HSS) | Python, SciPy, OpenSeesPy/FEM solver | Lưới phần tử 3D, trường ứng suất - chuyển vị, file `TBM_HANOI_G3_NUMERICAL_3D_FEM_BENCHMARK.xlsx` | **GATE 9** |
| **WF-31 (PINN Deep Surrogate)** | **ML & PINN Specialist** | Numerical Modeler, Stochastic Analyst | 5,000 điểm collocation $(x, y, z, t)$, phương trình vi phân Navier-Cauchy & Darcy | PyTorch / Python NumPy, Adam, L-BFGS | Trọng số mạng PINN sâu, thời gian suy luận $< 0.01\text{ ms}$, file `TBM_HANOI_G3_PINN_DEEP_SURROGATE_AI.xlsx` | **GATE 10** |
| **WF-32 (150 Buildings & Heritage)** | **GIS & Digital Twin Analyst** | Mechanics Reviewer, Evidence Auditor | Bình đồ mở rộng S9–S12, hồ sơ 150 công trình (Văn Miếu, Cát Linh, Chùa Phổ Giác) | Python GeoJSON processor, Excel engine | `buildings_exposure_150.geojson`, file `TBM_HANOI_G3_BUILDING_RISK_EXPOSURE_150.xlsx` | **GATE 10** |
| **WF-33 (Advanced Excel G3)** | **Pipeline & Data Engineer** | Numerical Modeler, ML Specialist | Dữ liệu từ WF-29 đến WF-32 | Python `openpyxl`, formula engine | 5 workbook Excel chuyên nghiệp hoàn thiện, 100% công thức động, Metadata, Data Dictionary | **GATE 11** |
| **WF-34 (300 DPI Graphics G3)** | **Academic Author** | Numerical Modeler, GIS Analyst | Trường ứng suất 3D, đường cong hội tụ PINN, bản đồ 150 công trình | Python `matplotlib`, `scipy` | 7 hình ảnh phân giải cao 300 DPI (`FIG_15` đến `FIG_21`) kèm danh mục thuyết minh | **GATE 11** |
| **WF-35 (WebGIS 3.0 Digital Twin)** | **GIS & Digital Twin Analyst** | Pipeline Engineer, ML Specialist | `buildings_exposure_150.geojson`, `groundwater_drawdown_contours.geojson` | Leaflet.js, Chart.js, HTML5/CSS3 | Ứng dụng `webgis_digital_twin_tbm_v3.html` tương tác thời gian thực với bảng điều khiển TARP | **GATE 11** |
| **WF-36 (Report & Dossier G3)** | **General Contractor** | Academic Author, Evidence Auditor | Toàn bộ sản phẩm bàn giao Giai đoạn 3 | Python `python-docx`, `hashlib` | `BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_3.md` (.docx) và trọn bộ hồ sơ nghiệm thu niêm phong SHA-256 | **GATE 11 PASSED** |

---

### II. BẢN ĐẶC TẢ CHI TIẾT TỪNG TÁC TỬ TRONG GIAI ĐOẠN 3

#### 1. General Contractor (Chỉ huy trưởng hệ thống)
- **Nhiệm vụ:** Thiết lập phiên làm việc `PHASE_3_DEPLOYMENT_AND_EXECUTION`, giám sát điều kiện chuyển giao tác vụ giữa các agent, nghiệm thu tổng thể.
- **Vai trò:** Lãnh đạo và quản trị quy chuẩn Guarded Protocol, đảm bảo tính liên tục của nghiên cứu.
- **Chức năng:** Quản lý state máy trạng thái `AGENT_STATE.json`, điều phối tài nguyên CPU, phát hành handoff logs.
- **Yêu cầu:** Không nhảy cóc qua Gate chưa đạt; cờ Audit minh bạch; bảo toàn 100% dữ liệu GĐ1 và GĐ2.
- **Kết quả:** Biên bản nghiệm thu và trạng thái `AGENT_STATE.json` hoàn chỉnh.

#### 2. Numerical Modeler (Chuyên gia Mô hình Số 3D)
- **Nhiệm vụ:** Xây dựng mô hình 3D FEM liên tục cho hầm đôi S9–S12, áp dụng mô hình Hardening Soil Small-Strain (HSS).
- **Vai trò:** Cung cấp chuẩn đối sánh số trị (numerical benchmark) độc lập cho các phương pháp giải tích.
- **Chức năng:** Chia lưới phần tử hữu hạn 3 chiều, mô phỏng quá trình kích đào khiên đào TBM, ép vữa và tương tác cọc móng.
- **Yêu cầu:** Độ hội tụ lưới phần tử đảm bảo sai số $< 1.0\%$; đối chuẩn với mô hình giải tích 3D LP trong dải sai số hợp lý.
- **Kết quả:** File Excel `TBM_HANOI_G3_NUMERICAL_3D_FEM_BENCHMARK.xlsx` và các lát cắt ứng suất 3D.

#### 3. Mechanics Reviewer (Chuyên gia Cơ học Đất & Đa trường)
- **Nhiệm vụ:** Thẩm định hệ phương trình vi phân Biot 3D và mô hình cố kết Terzaghi; tách bạch lún cơ học và lún thủy lực.
- **Vai trò:** Bảo đảm tính chân thực vật lý và ngăn chặn trộn lẫn phi cơ học giữa các nguồn lún.
- **Chức năng:** Giải tích trường thấm, xác định hạ thấp mực nước ngầm $\Delta h(x, t)$ và tính tích phân lún cố kết $S_{\text{hydro}}(t)$.
- **Yêu cầu:** Nghiệm thỏa mãn điều kiện biên thủy lực và nguyên lý ứng suất hữu hiệu; sai số số trị $< 0.001\%$.
- **Kết quả:** Bảng nghiệm đa trường Thấm - Cơ học, file `TBM_HANOI_G3_COUPLED_HYDRO_MECHANICAL.xlsx`.

#### 4. ML & PINN Specialist (Chuyên gia Trí tuệ Nhân tạo Nhúng Vật lý)
- **Nhiệm vụ:** Thiết kế và huấn luyện mạng Physics-Informed Neural Network (PINN) sâu 5 tầng tích hợp phương trình cân bằng Navier-Cauchy và Darcy.
- **Vai trò:** Đột phá công nghệ dự báo không độ trễ phục vụ điều khiển tự động khiên đào TBM.
- **Chức năng:** Tối ưu hóa hàm mất mát tổng hợp $\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda \mathcal{L}_{\text{PDE}}$, tính toán gradient tự động.
- **Yêu cầu:** $R^2 \ge 0.9985$, $RMSE < 0.25\text{ mm}$, thời gian phản hồi suy luận $< 0.01\text{ ms}$.
- **Kết quả:** File `TBM_HANOI_G3_PINN_DEEP_SURROGATE_AI.xlsx`, đồ thị hội tụ loss và trọng số tối ưu.

#### 5. GIS & Digital Twin Analyst (Chuyên gia Địa không gian & Digital Twin)
- **Nhiệm vụ:** Số hóa 150 công trình thực tế (bao gồm các di tích lịch sử nhạy cảm), xây dựng WebGIS 3.0 Digital Twin.
- **Vai trò:** Trực quan hóa tương tác đa chiều giữa hầm ngầm, địa tầng và các cấu trúc đô thị bề mặt.
- **Chức năng:** Lập trình bản đồ số tương tác trên web client, quản lý lớp GeoJSON, đổi màu động theo cấp rủi ro TARP.
- **Yêu cầu:** Chạy độc lập Offline không cần server; hỗ trợ tìm kiếm công trình, lọc theo cấp rủi ro và xuất dữ liệu.
- **Kết quả:** `buildings_exposure_150.geojson`, `groundwater_drawdown_contours.geojson`, `webgis_digital_twin_tbm_v3.html`.

#### 6. Pipeline & Data Engineer (Kỹ sư Dữ liệu)
- **Nhiệm vụ:** Tự động hóa tạo lập 5 workbook Excel chuyên nghiệp đa trang, bảo đảm 100% công thức động.
- **Vai trò:** Chuẩn hóa cấu trúc dữ liệu theo tiêu chuẩn tư vấn quốc tế, phục vụ tra cứu minh bạch.
- **Chức năng:** Lập trình OpenPyXL định dạng tiêu đề, border, zebra striping, nhúng công thức động và tạo metadata.
- **Yêu cầu:** Không có giá trị số cứng (hardcoded); có Data Dictionary và Metadata cho từng sheet.
- **Kết quả:** 5 workbook Excel hoàn chỉnh tại `02_BO_DU_LIEU_EXCEL_CHUYEN_SAU_GIAI_DOAN_3/`.

#### 7. Evidence Auditor (Kiểm toán viên Khoa học)
- **Nhiệm vụ:** Thẩm định nguồn tin, kiểm toán Gates 9, 10, 11 và niêm phong mã băm SHA-256 toàn bộ sản phẩm GĐ3.
- **Vai trò:** Người gác cổng chất lượng và liêm chính học thuật của đề tài.
- **Chức năng:** Rà soát cờ cảnh báo Audit bôi vàng, kiểm tra tính độc lập giữa số liệu quan sát và giả định, băm mã mật mã.
- **Yêu cầu:** 100% tham số có định danh nguồn gốc; bảng checksum SHA-256 không sai lệch 1 byte.
- **Kết quả:** `BIEN_BAN_KIEM_TOAN_KHOA_HOC_GIAI_DOAN_3_GATES.md` và bảng niêm phong SHA-256.

#### 8. Academic Author & Scientific Editor (Biên tập viên Học thuật)
- **Nhiệm vụ:** Soạn thảo Báo cáo toàn văn Giai đoạn 3 và chuẩn hóa trọn bộ hồ sơ nghiệm thu định dạng Microsoft Word (.docx).
- **Vai trò:** Truyền tải toàn bộ thành quả nghiên cứu thành văn bản khoa học đạt chuẩn mực đào tạo sau đại học.
- **Chức năng:** Biên dịch từ Markdown sang file Word chuẩn lề 3-2-2-2 cm, nhúng hình ảnh 300 DPI và bảng biểu thanh lịch.
- **Yêu cầu:** Văn phong học thuật khách quan, chặt chẽ, trích dẫn chuẩn quốc tế APA/IEEE, không dùng từ sáo rỗng.
- **Kết quả:** `BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_3.docx` và các văn bản nghiệm thu chính thức.

---

### III. BẢN ĐẶC TẢ CHI TIẾT TỪNG CÔNG CỤ KỸ THUẬT TRONG GIAI ĐOẠN 3

1. **Python 3.14 (Core Runtime):** Điều phối chuỗi xử lý tự động, quản lý bộ nhớ, chạy các script trong `scripts/` với Exit Code 0.
2. **NumPy & SciPy (Scientific Computing):** Giải hệ phương trình vi phân chuyển vị 3D, tích phân số học Simpson, giải tích ngẫu nhiên và trường thấm.
3. **PyTorch / Deep Learning Engine:** Tự động hóa vi phân tự động, tối ưu hóa mạng nơ-ron vật lý PINN, đạt $R^2 \ge 0.9985$.
4. **OpenPyXL (Excel Modeling):** Xuất bản 5 file Excel đa trang, 100% công thức động (`EXP`, `SQRT`, `INDEX`, `MATCH`, `IFERROR`), có Data Dictionary.
5. **Matplotlib (Graphics 300 DPI):** Kết xuất 7 đồ họa chuyên sâu 300 DPI (`FIG_15` đến `FIG_21`) với kích thước tối thiểu $3000 \times 1800\text{ px}$.
6. **Leaflet.js & Chart.js (Digital Twin WebGIS):** Bản đồ tương tác Client-side mượt mà, hiển thị 150 công trình, thanh trượt TBM và biểu đồ động kép.
7. **python-docx (Document Engineering):** Biên dịch văn bản Markdown sang Word .docx chuẩn căn lề 30-20-20-20 mm, font Times New Roman 13pt.
8. **Hashlib (Cryptographic Integrity):** Băm nhị phân FIPS PUB 180-4 theo từng khối 64KB, tạo bảng mã băm SHA-256 niêm phong toàn bộ tệp tin.
