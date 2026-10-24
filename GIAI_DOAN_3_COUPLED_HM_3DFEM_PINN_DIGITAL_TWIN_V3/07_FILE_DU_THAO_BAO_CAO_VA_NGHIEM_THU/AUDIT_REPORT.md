# BÁO CÁO AUDIT ĐỘC LẬP TOÀN DỰ ÁN TBM HÀ NỘI

**Run audit:** `2026-10-15_144716`  
**Phạm vi:** toàn bộ workspace `TBM_ĐTM`, năm Audit Gate bắt buộc, các gói mở rộng GĐ2–GĐ3, mã nguồn, kiểm thử, GeoJSON, workbook, hồ sơ nghiệm thu, manifest và checksum.  
**Chế độ:** chỉ đọc đối với nguồn và sản phẩm hiện có; mọi tệp mới của audit nằm trong thư mục run này.  
**Quy ước:** `VERIFIED`, `VERIFIED_CONDITIONAL`, `PARTIALLY_VERIFIED`, `UNVERIFIED`, `BLOCKED`, `RETRACTED`.

## 1. Phán quyết điều hành

**Dự án hiện chưa đủ điều kiện nghiệm thu khoa học, công bố, dùng cho quyết định rủi ro công trình hoặc gọi là Digital Twin/FEM/PINN đã kiểm chứng.**

Phần duy nhất được giữ ở mức `VERIFIED_CONDITIONAL` là nhánh Peck Gaussian cơ sở: công thức, SI nội bộ, quy ước lún dương xuống và bảo toàn thể tích của implementation hiện tại. Tất cả trạng thái `PASSED` khác phải được xem là giả thuyết cho tới khi tái kiểm toán bằng dữ liệu và runtime thực.

Ba nguyên nhân gốc:

1. **Gate bị vượt khi finding nghiêm trọng vẫn mở.** `Issue_Log.csv` còn ba finding critical/open, trong khi `AGENT_STATE.json` ghi `blockers=[]` và 11 Gate đều `PASSED`.
2. **Dữ liệu/kết quả tổng hợp bị nâng cấp thành quan trắc hoặc mô hình thật.** 100/150 công trình, FEM, PINN, loss curve, parity test và một phần GSA được tạo trực tiếp bằng RNG/hàm đóng nhưng hồ sơ gọi là khảo sát, FEM, PINN và kiểm thử độc lập.
3. **Checksum chứng minh bất biến byte, không chứng minh tính đúng khoa học.** GĐ2 và GĐ3 khớp toàn bộ hash đã khai báo, nhưng hash đang niêm phong cả nội dung sai nhãn hoặc không có lineage.

## 2. Các kiểm tra đã thực hiện

| Hạng mục | Kết quả | Diễn giải |
|---|---:|---|
| Inventory ban đầu | 213 tệp | Không có Git repository; không thể dùng lịch sử commit để chứng minh nguồn gốc/thời điểm thay đổi. |
| Unit tests cơ học | 7/7 đạt | Chỉ bao phủ Peck cơ bản, LP symmetry và một bất đẳng thức siêu vị; không bao phủ LP gốc, GSA, FEM, PINN, GIS, workbook hoặc Gate. |
| Tests điều phối | 2/2 đạt | Gọi trực tiếp hai test pytest-style vì runtime bundled không có pytest. |
| Python syntax | 29 scripts compile | Không có lỗi cú pháp; còn một số `SyntaxWarning` escape sequence. Compile success không xác nhận tính đúng khoa học. |
| Workbook | 25/25 đọc được | 25 workbook đọc được bằng openpyxl read-only; nhiều workbook kết quả là dữ liệu tĩnh, không phải mô hình có công thức. |
| Formula cache | 100% công thức không có cached value | Các workbook có công thức chứa tổng cộng nhiều nghìn công thức nhưng toàn bộ ô công thức đều không có giá trị cache; chưa có bằng chứng đã recalculation trong Excel/engine tương đương trước khi niêm phong. |
| GeoJSON | 18 tệp đọc được | Dữ liệu GĐ2/GĐ3 có 100/150 đối tượng nhưng không có năm trường provenance bắt buộc; nhiều lớp gốc không khai báo CRS trong file. |
| Baseline GĐ1 | 2/2 hash khớp | Chỉ gồm `normalized_sources.csv` và `normalized_parameters.csv`; manifest chưa bao phủ schema, assumption register, code/environment và nguồn đầu vào. |
| Manifest GĐ2 | 55/55 hash khớp | `VERIFIED` về toàn vẹn byte; không xác nhận validity của nội dung. |
| Manifest GĐ3 | 47/47 hash khớp | `VERIFIED` về toàn vẹn byte; không xác nhận validity của nội dung. |
| Manifest GĐ1 dossier | 40/41 kiểm được và khớp | File DOCX luận án đang bị khóa nên `BLOCKED`; kích thước hiện tại 2,870,789 byte không phù hợp kích thước 2,576.2 KB đã niêm phong. |

Chi tiết máy đọc nằm trong `artifact_audit.json`; script tái chạy là `audit_artifacts.py`.

## 3. Phát hiện critical

### C-01. Gate governance không hợp lệ — `VERIFIED`

- `research_outputs/2026-10-13_152753/09_logs/Issue_Log.csv:2-6` còn `ISS-001`, `ISS-002`, `ISS-005` ở mức critical/open.
- `AGENT_STATE.json:99-107` đồng thời thừa nhận thiếu EIA gốc, CP03, dữ liệu TBM/quan trắc, hình học có CRS và phương trình LP gốc, nhưng `blockers=[]`.
- `research_outputs/2026-10-13_152753/RUN_SUMMARY.md:18` nói Gate 1 `IN_PROGRESS`; `WF05_GATE_1_AUDIT_REPORT.md:5` chỉ nói `PASSED (CONDITIONAL PILOT MODE)`; `AGENT_STATE.json:14-80` lại chuyển Gate 1–11 thành `PASSED`.

**Hệ quả:** thu hồi trạng thái `PASSED`; khóa phát hành khoa học cho tới khi tái lập state từ evidence.

### C-02. Provenance schema vi phạm quy tắc bắt buộc — `VERIFIED`

- `research/stratigraphy_raw.csv:1` thiếu `source_id`, `value_basis`, `confidence`, `qa_flag`.
- `normalized_parameters.csv:1` thiếu `source_id`, `source_locator`, `value_basis`, `confidence`.
- `WF19_TRACEABILITY_MATRIX.csv:1` thiếu `source_id` và `confidence`.
- GeoJSON GĐ1–GĐ3 không mang đủ `source_id`, `source_locator`, `value_basis`, `confidence`, `qa_flag`; nhiều feature không có bất kỳ trường nào trong số này.
- Các nhãn ghép như `direct_text_and_table` và `direct_table_plus_derived_depth` trộn evidence class, trái quy định tách lớp.

**Hệ quả:** Gate 1–3 không thể coi là đạt; mọi phân tích downstream thiếu lineage ở cấp giá trị.

### C-03. 100/150 công trình tổng hợp bị trình bày thành thực địa — `VERIFIED`

- GĐ2 sinh RNG tại `scripts/generate_stage_2_models_and_excel.py:507-561`, sau đó ghi “100 công trình thực tế” tại dòng 709–713 và `observed / Số hóa OpenStreetMap & Khảo sát` tại dòng 899–911.
- GĐ3 tạo tên, loại móng và khoảng cách bằng code/RNG tại `scripts/generate_stage_3_models_and_excel.py:308-344`, nhưng dòng 406–412 ghi “Khảo sát thực địa” và `PASSED`.

**Hệ quả:** toàn bộ lớp exposure 60/100/150 phải gắn `scenario_assumption` hoặc `synthetic_demonstration`; không được dùng để đánh giá công trình thật.

### C-04. “3D FEM” không có solver lineage — `VERIFIED`

- `scripts/generate_stage_3_models_and_excel.py:203-212` tạo `fem_val = 20.8*exp(...)` trực tiếp.
- `scripts/generate_stage_3_figures.py:64-78` dựng mặt lún bằng công thức giải tích.
- Không tìm thấy file model, mesh, phase, material assignment, solver log, convergence hoặc raw result.
- Báo cáo GĐ3 lại tuyên bố HSS, 85.000 phần tử và hội tụ lưới.

**Hệ quả:** Gate 9 `RETRACTED_UNSUPPORTED`; các hình/workbook “FEM” chỉ được giữ như minh họa tổng hợp.

### C-05. “PINN” không tồn tại như mô hình huấn luyện — `VERIFIED`

- `scripts/generate_stage_3_models_and_excel.py:251-269` tạo 50 giá trị `exact` tổng hợp và cộng nhiễu Gaussian.
- `scripts/generate_stage_3_figures.py:85-106` tạo loss từ hàm mũ có nhiễu; parity có 100 điểm nhưng nhãn ghi 500 điểm.
- Không có network definition, autodiff, PDE residual, optimizer, collocation data, checkpoint, split hay inference benchmark.

**Hệ quả:** R2=0.9994, RMSE=0.12 mm và 0.008 ms là `UNVERIFIED`; Gate 10 `RETRACTED_UNSUPPORTED`.

### C-06. Sobol/GSA bị ghi đè bằng hằng số — `VERIFIED`

- `scripts/generate_stage_2_models_and_excel.py:259-279` dùng random sampling thông thường, không phải LHS/Saltelli.
- `E` và `nu` không tham gia output ở dòng 281–287 nhưng vẫn được gán sensitivity khác 0.
- Estimator dạng binning được tính ở dòng 289–312 rồi toàn bộ chỉ số bị ghi đè bằng hằng số ở dòng 314–318.

**Hệ quả:** tuyên bố `VL = 67.2%` và Gate 7 phải `RETRACTED_PENDING_RECALCULATION`.

### C-07. Lún cố kết sai hệ số 10 — `VERIFIED`

Theo chính công thức workbook tại `scripts/generate_stage_3_models_and_excel.py:155-165`:

`2.5 × 9.81 × 0.00045 × 12.7 × 1000 = 140.16 mm`.

Báo cáo/hình tại `scripts/build_stage_3_reports_and_dossier.py:143-148` và `scripts/generate_stage_3_figures.py:36-39` dùng 14.1 mm. Với lún TBM 19.7 mm, tổng theo đầu vào mã là khoảng 159.86 mm, không phải 33.8 mm.

**Hệ quả:** rút toàn bộ kết luận HM/risk/TARP dùng 14.1 và 33.8 mm; kiểm tra lại đơn vị, `m_v`, phạm vi lớp nén và điều kiện thoát nước.

### C-08. “Digital Twin realtime/offline” là demo tĩnh và tự mâu thuẫn — `VERIFIED`

- `webgis_digital_twin_tbm_v3.html:7-9,90-93` phụ thuộc CDN và tile server nên không hoạt động ngoại tuyến đầy đủ.
- Không có API, WebSocket, telemetry, timestamped ingestion, state estimation hoặc control loop. Slider ở dòng 161–172 chỉ đổi nhãn/di chuyển marker, không cập nhật lún, TARP hoặc chart.
- Bảng HTML ghi `52/44/36/18`, trong khi đếm trực tiếp GeoJSON 150 công trình cho kết quả `50/36/25/39`.
- Hình 18 sinh một tập RNG khác cho số lượng `59/26/32/33`; legend/Hình 19 vẫn ghi cứng `52/44/36/18`.

**Hệ quả:** Gate 11 không thể xác nhận chức năng/science; đổi tên thành `static scenario viewer` và derive mọi thống kê từ một dataset duy nhất.

## 4. Phát hiện high

### H-01. Loganathan–Poulos chưa được xác minh — `BLOCKED`

- `scripts/analytical_engine.py:56-86` tự gắn `secondary_source_unverified_original`.
- `AGENT_STATE.json:105` thừa nhận bản gốc và điều kiện áp dụng chưa có trong source pool.
- Trang nhà xuất bản ASCE xác nhận bài báo 1998, DOI, trang 846–856 và định nghĩa “equivalent ground loss” liên quan gap `g`; metadata này không đủ để xác minh công thức/định nghĩa/validity range đầy đủ.
- Implementation đang đồng nhất trực tiếp `epsilon_0 = VL`; tích phân độc lập implementation cho sai lệch thể tích khoảng 11.19% với bộ tham số kiểm tra, nên tuyên bố bảo toàn LP hiện không hợp lệ.

**Hệ quả:** LP là `experimental_unverified`, không phải benchmark đã kiểm chứng.

### H-02. “Coupled HM” chỉ là cộng hai hàm tách rời — `VERIFIED`

Không có hệ Biot/Darcy, permeability, storage, boundary/drainage condition, time stepping hoặc coupling hai chiều. Hàm `U(t)=1-exp(-t/45)` không được suy ra từ `c_v` và chiều dài đường thoát.

**Hệ quả:** chỉ được gọi là kịch bản cộng lún cơ học + cố kết 1D giả định, không phải coupled HM.

### H-03. Baseline “frozen” có thể bị pipeline ghi đè — `VERIFIED`

`scripts/freeze_baseline.py:37-50` sao chép đè file frozen và viết lại manifest. `scripts/run_full_pipeline.py:36-42` gọi bước freeze mỗi lần chạy. Vì vậy timestamp/manifest đóng băng thay đổi khi tái chạy pipeline.

**Hệ quả:** Gate 3 chỉ `PARTIALLY_VERIFIED`; cần immutable versioned freeze mới.

### H-04. Gate 5 không tái lập toàn bộ dự án — `VERIFIED`

`scripts/run_full_pipeline.py:34-43` chỉ chạy bảy script GĐ1 và không tạo lại workbook, luận án, hồ sơ nghiệm thu, figures/checksums GĐ2–GĐ3. Không có lockfile môi trường hoặc execution log sạch. Ma trận traceability chỉ có 13 claim.

**Hệ quả:** thu hồi “100% reproducible”.

### H-05. Workbook chưa có bằng chứng recalculation — `VERIFIED`

- 25/25 workbook đọc được.
- Các workbook Monte Carlo, building risk GĐ2 và building risk GĐ3 có 0 công thức: là snapshot tĩnh.
- Tất cả ô có công thức ở 13 workbook formula-bearing đều không có cached value, gồm 2.226 công thức trong analytical engine, 205 trong HM, 124 trong FEM và 50 trong PINN.
- Không có log mở/tái tính bằng Excel hoặc engine tương đương, formula error scan sau recalc và render inspection toàn bộ sheet.

**Hệ quả:** workbook chưa đạt tiêu chí artifact delivery/reproducibility dù file tồn tại và hash đúng.

21 hình GĐ1–GĐ3 có kích thước/DPI phù hợp và các mẫu kiểm tra trực quan rõ; tuy nhiên lineage của các hình FEM/PINN/TARP không đạt. Trong run GĐ1, chỉ một hình là 350 DPI, ba hình còn lại 300 DPI, trái claim “350 DPI” cho toàn bộ bộ hình.

### H-06. Spatial validity chưa được chứng minh — `VERIFIED`

- Các GeoJSON GĐ2/GĐ3 khai báo CRS84 nhưng feature không có provenance.
- Buildings 100/150 là điểm, không phải footprint kiểm chứng; khoảng cách tới tim hầm do RNG sinh.
- Không có CRS nguồn, phép biến đổi, vertical datum, control points hoặc spatial accuracy report.
- WebGIS là client-side visualization; không có live data connector, telemetry, write-back, alert service hoặc control loop.
- Không tìm thấy `*.gpkg`, `*.qgz`, `*.qgs` hoặc `*.shp`, dù task queue đánh dấu workflow QGIS/GeoPackage hoàn thành.

**Hệ quả:** gọi sản phẩm là “WebGIS demo tĩnh”, không phải Digital Twin thời gian thực.

### H-07. State và hồ sơ không đồng bộ — `VERIFIED`

- `AGENT_STATE.json` vừa ghi đang ở `PHASE_3_PLANNING...`, vừa ghi Gate 9–11 `PASSED`, vừa ghi handoff GĐ3 `COMPLETED`.
- `updated_at` sớm hơn một handoff nằm trong chính state.
- Nhiều handoff WF03–WF20 còn `DISPATCHED` dù task queue/hồ sơ nói hoàn thành.

**Hệ quả:** không dùng `AGENT_STATE.json` làm source of truth cho đến khi rebuild bằng event log bất biến.

### H-08. Gate 2 QC có phạm vi hẹp hơn claim — `VERIFIED`

`scripts/qc_checks.py:12-48` chỉ kiểm bốn giới hạn số học `D`, `z0`, `K`, `nu`, nhưng report kết luận cả physical, geometry và unit plausibility. Script không kiểm CRS, geometry validity, unit conversion lineage, provenance fields hoặc conflicts.

**Hệ quả:** Gate 2 phải chạy lại với bộ kiểm tra địa kỹ thuật–đơn vị–không gian độc lập.

## 5. Gate reassessment

| Gate | Verdict audit | Điều kiện mở lại |
|---|---|---|
| Gate 1 | `RETRACTED_BLOCKED` | EIA gốc/page locators, CP03 và LP gốc; schema provenance đủ năm trường; đóng critical issues. |
| Gate 2 | `RETRACTED_BLOCKED` | Hình học/CRS/vertical datum và buildings thực có lineage; QC đơn vị/địa kỹ thuật/spatial độc lập. |
| Gate 3 | `RETRACTED_PARTIALLY_VERIFIED` | Freeze versioned bất biến, manifest bao phủ data+schema+assumptions+code+environment. |
| Gate 4 | `RETRACTED_PARTIALLY_VERIFIED` | Giữ Peck; khóa LP/GSA/GIS field-risk; chạy validation độc lập. |
| Gate 5 | `RETRACTED_FAILED` | Full clean-room reproduction, claim matrix đầy đủ, workbook recalc/render, report regenerated. |
| Gate 6 | `RETRACTED_BLOCKED` | Xác minh bản gốc LP và benchmark độc lập. |
| Gate 7 | `RETRACTED_UNSUPPORTED` | Saltelli/Sobol thật, CI và convergence. |
| Gate 8 | `INTEGRITY_VERIFIED_CONTENT_RETRACTED` | Hash đã đúng; phải thay nội dung sai nhãn rồi niêm phong version mới. |
| Gate 9 | `RETRACTED_UNSUPPORTED` | Solver/model/log/mesh convergence thật và sửa HM units. |
| Gate 10 | `RETRACTED_UNSUPPORTED` | PINN code/checkpoint/residual/test độc lập và exposure thực. |
| Gate 11 | `INTEGRITY_VERIFIED_FUNCTION_SCIENCE_UNVERIFIED` | Chứng minh live data/control architecture; niêm phong nội dung đã tái kiểm toán. |

`GATE_REASSESSMENT.csv` là bản máy đọc có đủ locator, basis, confidence và QA flag.

## 6. Hướng phát triển đề xuất

### P0 — 0 đến 3 ngày: containment và khôi phục liêm chính

1. Không sửa/xóa hồ sơ cũ; đánh dấu release GĐ1–GĐ3 hiện tại là `RETRACTED_FOR_REAUDIT` trong state mới có version.
2. Dừng dùng các cụm “thực tế”, “observed”, “khảo sát thực địa”, “FEM”, “PINN”, “Digital Twin realtime” cho artifact tổng hợp.
3. Đóng Word rồi băm lại DOCX GĐ1; nếu khác, phát hành manifest/version mới, không sửa manifest cũ.
4. Tạo issue register mới cho các finding C-01…C-08/H-01…H-08 và khóa Gate transition nếu còn critical/open.

### P1 — 1 đến 2 tuần: phục hồi nền khoa học tối thiểu

1. Giữ riêng `Peck verified baseline v1`; thêm test `VL→0`, `x→∞`, `D→0`, độ sâu lớn, integration tolerance `1e-6` và sign convention metadata.
2. Lập long-form value register với `source_id`, `source_locator`, `value_basis`, `confidence`, `qa_flag`; một dòng cho một giá trị.
3. Thu thập EIA cập nhật 08/2013 từ trang ADB dự án 40080-013, CP03 borehole/design logs và bản gốc LP có quyền truy cập hợp lệ.
4. Tạo freeze mới theo content-addressed/versioned path; không cho pipeline ghi đè.
5. Xây claim-to-evidence matrix bao phủ toàn bộ số trong manuscript/workbook/figures, không chỉ 13 claim.

### P2 — 2 đến 6 tuần: tái lập phân tích minh bạch

1. Làm lại GSA bằng sampling/estimator hợp lệ; output thực sự phụ thuộc biến; seed, convergence theo N, bootstrap CI.
2. Giữ groundwater settlement thành nhánh kịch bản 1D độc lập cho tới khi có `c_v`, drainage path, boundary condition và calibration.
3. Chỉ xây exposure trên alignment/building thật có CRS và lineage; synthetic scenarios ở layer/tên file riêng.
4. Regenerate workbook từ source duy nhất; recalculation, formula-error scan và render review tất cả sheet trước seal.

### P3 — chỉ sau Gate 4 hợp lệ: FEM/PINN/Digital Twin

1. FEM: lưu input model, material provenance, mesh, phases, boundary checks, solver/version, raw exports và convergence study.
2. PINN: chỉ sau khi có solver/monitoring ground truth độc lập; lưu code train, PDE residual, weights, checkpoint, data split và timing protocol.
3. Digital Twin: yêu cầu live ingestion, timestamped telemetry, data-quality gate, state estimation, alert audit trail và fail-safe; nếu không có, giữ tên “WebGIS scenario viewer”.

## 7. Điều kiện nghiệm thu lại

Chỉ cho phép `PASSED` khi đồng thời có:

- không còn critical/open ở Gate hiện tại hoặc Gate trước;
- tất cả scientific value có năm trường provenance bắt buộc;
- code, raw input, runtime log và final artifact tạo thành lineage liền mạch;
- kết quả kiểm thử độc lập đúng phạm vi claim;
- workbook đã recalculation + formula scan + visual render;
- manifest/checksum lập sau validation, trong version mới và không bị pipeline ghi đè;
- reviewer độc lập ký verdict từ evidence, không từ chuỗi `PASSED` được generator ghi sẵn.

## 8. Tài liệu nguồn ngoài đã kiểm tra

- ASCE: Loganathan & Poulos (1998), *Analytical Prediction for Tunneling-Induced Ground Movements in Clays*, DOI `10.1061/(ASCE)1090-0241(1998)124:9(846)`, pp. 846–856. Trang publisher xác nhận metadata và khái niệm equivalent ground loss/gap; toàn văn phương trình vẫn cần quyền truy cập hợp lệ để audit equation-level.
- ADB project 40080-013: trang dự án chính thức liệt kê *Updated Environmental Impact Assessment*, August 2013; đây là nguồn cần thu thập và lưu cục bộ có checksum/page locators cho Gate 1.

