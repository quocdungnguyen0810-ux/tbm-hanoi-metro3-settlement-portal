# Kế hoạch thực thi dự án TBM–ĐTM Hà Nội

**Đề tài:** Nghiên cứu đánh giá độ nhạy và dự báo vùng ảnh hưởng lún mặt đất do thi công hầm khiên đào (TBM) trong điều kiện địa chất đô thị Hà Nội bằng phương pháp giải tích kết hợp GIS  
**Phạm vi:** đoạn ngầm S9–S12, Metro Nhổn–Ga Hà Nội  
**Chế độ:** `auto_guarded`  
**Chính sách model:** `inherit` — tác tử kế thừa model mặc định của môi trường; chỉ đổi năng lực khi routing rule yêu cầu  
**Ngày lập:** 13/10/2026 (UTC+7)

## 1. Quyết định triển khai

**GO có điều kiện** cho ba sản phẩm ngay từ dữ liệu hiện có:

1. Registry nguồn, schema, provenance và Audit Gates.
2. Mô hình giải tích Peck minh bạch, chạy theo kịch bản và gắn nhãn giả định.
3. Pipeline GIS/QGIS ở dạng schema và local/schematic coordinates.

**NO-GO tạm thời** cho hai tuyên bố/sản phẩm:

1. Bản đồ vùng ảnh hưởng theo tọa độ thực và overlay công trình cụ thể.
2. “Dự báo đã kiểm chứng thực địa” hoặc hiệu chỉnh tham số.

Lý do: chưa có alignment/CRS/datum được kiểm chứng, tọa độ hố khoan, footprint công trình, chuỗi quan trắc lún và log vận hành TBM. AUTO mode không được tự suy diễn các dữ liệu này.

## 2. Cơ sở hiện có đã kiểm kê

- 7 bản ghi hồ sơ chính thức trong `research/official_docs.csv`.
- 18 bản ghi địa tầng trong `research/stratigraphy_raw.csv`: 6 S9–S10, 6 BH12/S11–S12, 6 kiểm tra chéo toàn tuyến.
- 9 CSV template mới có header.
- 1 PDF toàn văn cục bộ: bài TCXD 2024 về BH12/S11–S12.
- 3 JSON Crossref chỉ dùng để kiểm chứng metadata/DOI, không phải bằng chứng cho số liệu địa kỹ thuật.
- 1 sơ đồ khái niệm GIS.

Khoảng trống mức critical/high được ghi trong `09_logs/Issue_Log.csv`: EIA 2013 gốc và locator; hồ sơ CP03; alignment/CRS/datum; dữ liệu quan trắc và TBM; footprint công trình; bản gốc công thức Loganathan–Poulos.

## 3. Câu hỏi nghiên cứu khóa trước

1. Với `V_L = 0.5%–2.0%`, biên độ, bề rộng và độ dốc phễu lún biến đổi thế nào tại các mặt cắt địa chất có chứng cứ cho S9–S12?
2. Bất định của `V_L`, bề rộng phễu `i`/hệ số `K`, chiều sâu tim hầm và đường kính ảnh hưởng thế nào đến `S_max`, độ dốc và độ cong?
3. Phạm vi ảnh hưởng theo các ngưỡng lún được định nghĩa trước giao cắt với công trình như thế nào khi dữ liệu không gian đủ điều kiện?
4. Peck và Loganathan–Poulos khác nhau thế nào khi dùng cùng hình học, cùng pha thi công và cùng quy ước tổn thất đất?

Kết quả khi chưa có quan trắc phải gọi là **đánh giá kịch bản/độ nhạy**, không gọi là dự báo đã hiệu chỉnh.

## 4. Protocol cơ học

Quy ước bảng: lún dương xuống. Với phễu Gaussian:

\[
S(x)=S_{max}\exp\left(-\frac{x^2}{2i^2}\right)
\]

\[
V_s=\sqrt{2\pi}\,iS_{max}=V_L A_t,\qquad A_t=\pi D^2/4
\]

Do đó:

\[
S_{max}=\frac{V_L A_t}{\sqrt{2\pi}\,i}
\]

`V_L` nhập vào code là tỷ số thập phân; 0,5% phải là `0.005`. Bộ test bắt buộc phát hiện lỗi phần trăm/tỷ số, bán kính/đường kính, chiều sâu phủ/chiều sâu tim và dấu lún.

`i = K z_0` chỉ được dùng khi định nghĩa `K` và `z_0` có nguồn/phạm vi áp dụng. Không gán một giá trị `K` duy nhất cho toàn S9–S12 nếu chưa có hiệu chỉnh hoặc chứng cứ.

Loganathan–Poulos là nhánh benchmark riêng. Việc viết công thức vào code bị chặn cho đến khi lưu được bản gốc hợp pháp, kiểm tra equation/page, định nghĩa gap/ground loss, giả thiết đất đồng nhất–ngắn hạn và miền hiệu lực. Không coi mô hình này là ground truth cho địa tầng Hà Nội phân lớp.

## 5. Thiết kế độ nhạy

### Tầng A — OAT minh bạch

- Grid bắt buộc: `V_L = 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00%`.
- Giữ cố định `D`, `z0`, `i` theo từng section đã khóa.
- Xuất `S_max`, profile `S(x)`, width tại ngưỡng, slope và curvature.

### Tầng B — bất định phối hợp

- Biến ứng viên: `V_L`, `K/i`, `z0`, `D`, vị trí tim hầm và sai số không gian.
- Chỉ gán phân phối xác suất khi có dữ liệu/nguồn đủ căn cứ; nếu không dùng interval/scenario.
- Morris dùng cho sàng lọc khi số biến lớn; Sobol/Monte Carlo chỉ mở khi phân phối đầu vào có căn cứ.
- Hai ống hầm chạy riêng, sau đó siêu vị tuyến tính như baseline; không gọi siêu vị là mô hình tương tác hai hầm.
- Tách lún tức thời do đào khỏi lún cố kết/hạ nước ngầm. GWL không được đưa trực tiếp vào Peck như một biến cơ học không có mô hình liên kết.

## 6. Kiến trúc tác tử và routing

| Tác tử | Nhiệm vụ | Điều kiện bàn giao |
|---|---|---|
| `general_contractor` | WBS, DAG, state, gate, handoff | Chỉ tác tử này cập nhật trạng thái tổng |
| `source_harvester` | EIA/ADB/CP03, PDF/OCR/table | File + hash + license + page/table locator |
| `evidence_auditor` | kiểm chứng độc lập nguồn/xung đột | Không tự duyệt sản phẩm của chính mình |
| `data_engineer` | schema, PK/FK, đơn vị, quarantine, freeze | QC pass + manifest SHA-256 |
| `mechanics_reviewer` | công thức, giả thiết, validity | Memo kiểm chứng độc lập |
| `analytical_modeler` | Peck và nhánh LP đã xác minh | unit/dimensional/mass-balance tests |
| `sensitivity_analyst` | OAT/UQ/ranking/envelope | scenario completeness + reproducibility |
| `gis_analyst` | CRS, GPKG, QGIS, exposure | spatial QC; không đo trên CRS hiển thị |
| `reporting_editor` | bảng/hình/bài báo | claim–number–source traceability |
| `pipeline_engineer` | lỗi code/test/môi trường | test tái hiện + bản sửa cục bộ |

Tác tử FEM/OpenSeesPy và ML ở trạng thái `conditional`: không kích hoạt mặc định. ML không được huấn luyện trên dữ liệu do chính công thức sinh rồi dùng SHAP để tuyên bố cơ chế thực địa.

## 7. WBS và năm Audit Gates

### Gate 1 — Source acquisition & extraction integrity

- WF-01 khóa phạm vi, câu hỏi, đơn vị, quy ước dấu và taxonomy bằng chứng.
- WF-02 lập inventory/hash toàn bộ hiện trạng.
- WF-03 thu bản gốc EIA/ADB/CP03 và quyền sử dụng.
- WF-04 trích geometry, địa tầng, nước ngầm, TBM, quan trắc.
- WF-05 kiểm chứng độc lập page/table/equation.

**Đạt khi:** 100% đầu vào khoa học dùng tiếp có `source_id`, locator, checksum, license/access; nguồn chưa có toàn văn vẫn mang `pending`, không được dùng làm số liệu nền.

### Gate 2 — Physical, data and spatial plausibility

- WF-06 chuẩn hóa 9 bảng quan hệ.
- WF-07 kiểm tra PK/FK, đơn vị, lớp đất, `bottom>top`, `V_L`, `D/R`, `z0`, GWL, geometry và CRS.
- WF-08 giải quyết hoặc quarantine bất thường; giữ xung đột BH12 12,3/12,7 m.

**Đạt khi:** orphan FK = 0; thiếu dữ liệu là null; mọi assumed/derived có nhãn; geometry không rõ CRS bị loại khỏi overlay; không còn lỗi critical chưa xử lý.

### Gate 3 — Baseline freeze

- WF-09 tạo `clean baseline`, assumptions register, manifest và SHA-256.

**Đạt khi:** raw không đổi; clean có version; hash kiểm lại khớp; imputation/derived đều truy vết được.

### Gate 4 — Analytical, sensitivity and GIS verification

- WF-10 xác minh bản gốc Peck và Loganathan–Poulos.
- WF-11 triển khai Peck.
- WF-12 triển khai LP sau verification và benchmark cùng hình học/pha.
- WF-13 chạy OAT và UQ.
- WF-14 tạo GeoPackage/QGIS workflow và influence layers.
- WF-15 validation độc lập nếu có quan trắc; nếu không ghi `NO_FIELD_VALIDATION`.
- WF-16 phản biện độc lập cơ học–độ nhạy–GIS.

**Đạt khi:** tích phân số profile khớp `V_L A_t`; symmetry/limiting/unit tests đạt; grid 0,5–2,0% đầy đủ; GIS chỉ dùng CRS đo lường đã xác minh; mọi map mang scenario/model/version và uncertainty.

### Gate 5 — Reporting & reproducibility

- WF-17 bảng, hình >=350 DPI và chart data.
- WF-18 Methods–Results–Discussion–Limitations.
- WF-19 ma trận claim–number–source–formula–file/hash.
- WF-20 audit cuối và release recommendation.

**Đạt khi:** một lệnh tái tạo được output; bảng/hình khớp dữ liệu; kết luận không vượt bằng chứng; unresolved critical issues = 0 hoặc gói phát hành ghi rõ `DRAFT/BLOCKED`.

## 8. Data/GIS target

GeoPackage mục tiêu gồm:

- `src_sources`;
- `geo_alignment_centerline`, `geo_stations_structures`, `geo_tunnel_axis`;
- `geo_investigation_points` + `tbl_stratigraphy_intervals` + `tbl_groundwater_observations`;
- `geo_monitoring_points` + `tbl_monitoring_readings`;
- `geo_buildings` và lớp parcel restricted nếu có quyền;
- `tbl_tbm_parameters`, `tbl_scenarios`, `tbl_analytical_parameters`;
- `geo_settlement_profiles`, `geo_settlement_isolines`, `geo_influence_zones`, `geo_exposure_intersections`;
- `tbl_qc_results`, `tbl_processing_log`.

Quy tắc CRS:

- Bảo toàn native CRS; CRS chưa biết -> quarantine.
- Chỉ dùng hệ chiếu mét đã được tài liệu xác nhận để buffer/distance/area.
- EPSG:4326 chỉ trao đổi/hiển thị; EPSG:3857 không dùng để đo.
- Không gán EPSG hoặc vertical datum bằng suy đoán.
- Mọi transform lưu pipeline, phiên bản PROJ, control points và residual/RMSE.

“Công khai trên Internet” không đồng nghĩa open license. Mỗi nguồn/layer phải lưu quyền tái phân phối và quyền tạo dẫn xuất. Dữ liệu địa chính/địa chỉ/công trình nhạy cảm mặc định tách lớp restricted.

## 9. Cơ chế AUTO có kiểm soát

1. Đọc `.agents/task_queue.json` và `AGENT_STATE.json`.
2. Chọn task ưu tiên cao nhất có mọi dependency `COMPLETED/WAIVED`.
3. Route theo `.agents/agents.json` và tạo handoff JSON.
4. Worker kiểm hash input, chỉ ghi generated outputs, chạy acceptance tests.
5. Lỗi mạng/I/O retry tối đa 2; lỗi khoa học/QC -> quarantine + Issue Log, không retry mù.
6. Gate fail chặn tất cả task hậu duệ.
7. Chỉ GC cập nhật state tổng; worker giao artifact + evidence.

Lệnh vận hành:

```powershell
python scripts/orchestrate.py status
python scripts/orchestrate.py dispatch
python scripts/orchestrate.py set-status WF-01 COMPLETED --evidence "research_outputs/.../protocol.md"
python scripts/build_inventory.py
python -m pytest -q
```

`dispatch` chỉ tạo gói bàn giao xác định; host Codex/agent runner tiêu thụ gói đó để chạy tác tử. Nó không tự gọi dịch vụ bên ngoài hoặc tự phát hành dữ liệu.

## 10. Sản phẩm nghiệm thu

1. File inventory và source manifest có SHA-256.
2. Workflow + AGENT_STATE + task queue + Issue Log.
3. Data dictionary, assumptions register, clean/frozen datasets.
4. Mã nguồn Peck/LP đã xác minh và test suite.
5. Scenario matrix 0,5–2,0%, bảng độ nhạy và uncertainty envelopes.
6. GeoPackage, QGIS project dùng relative paths, styles/layout, metadata và QC report.
7. Bộ hình >=350 DPI + chart data.
8. Evidence traceability matrix và reproducibility manifest.
9. Bản thảo khoa học, nêu rõ mức validation và hạn chế.

## 11. Điểm dừng cần Chủ nhiệm xác nhận

- Dùng waiver để đóng gate còn nguồn/CRS/đơn vị mơ hồ.
- Chọn ngưỡng lún/độ dốc/biến dạng để gọi “vùng ảnh hưởng” hoặc “rủi ro”.
- Sử dụng/phát hành dữ liệu địa chính hoặc tọa độ công trình nhạy cảm.
- Mở rộng phạm vi sang OpenSeesPy/FEM hoặc ML.
- Phát hành/nộp bài ra bên ngoài.

## 12. Thứ tự khởi động đề xuất

1. Chốt WF-01 bằng protocol này.
2. Chạy inventory/hashing WF-02.
3. Mở nhánh song song WF-03: EIA/ADB/CP03 và bản gốc LP.
4. Chỉ sau Gate 1–3 mới triển khai code mô hình và GIS thực.

