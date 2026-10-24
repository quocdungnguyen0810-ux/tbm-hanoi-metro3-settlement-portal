# KẾ HOẠCH THỰC HIỆN & AUDIT TIẾN ĐỘ: GIAI ĐOẠN 3: KỊCH BẢN LÚN CỐ KẾT THẤM - CƠ HỌC, ĐỐI SÁNH 3D FEM & MẠNG PINN SURROGATE, 150 CÔNG TRÌNH DI TÍCH & WEBGIS V3.0 SCENARIO VIEWER (GATES 9 - 11)

- **Mã giai đoạn:** `GIAI_DOAN_3` (`STAGE_3`)
- **Thời gian thực hiện:** Tháng 09/2027 – Tháng 12/2027 (Mô hình mở rộng Đa trường, AI Surrogate, TARP 150 công trình & Tổng kết Đề tài)
- **Thư mục quản lý:** `QUAN_TRI_DU_AN_TBM_PHAN_KY_GIAI_DOAN/GIAI_DOAN_3_COUPLED_HM_3DFEM_PINN_DIGITAL_TWIN_V3/`

## 1. Mục tiêu Trọng tâm của Giai đoạn

1. Đánh giá kịch bản kết hợp lún tức thời do đào hầm TBM và lún cố kết thấm dài hạn khi hạ mực nước ngầm.
2. Xây dựng bộ khung minh họa đối sánh 3D FEM, mạng Surrogate AI và bản đồ phơi nhiễm mở rộng 150 công trình.
3. Thực hiện Kiểm toán Độc lập toàn diện (Independent Audit `2026-10-15_144716` & `2026-10-24`) để rà soát toàn bộ mã nguồn, công thức Excel, GeoJSON và tách bạch rõ dữ liệu thực nghiệm với dữ liệu mô phỏng kịch bản.

## 2. Cấu trúc Phân tách 7 Phân khu Dữ liệu & Sản phẩm trong Giai đoạn

| STT | Thư mục con chuẩn hóa | Chức năng & Nội dung lưu trữ | Số tệp đã phân bổ |
|:---:|---|---|:---:|
| 1 | `01_AUDIT_KE_HOACH_NHAN_SU_SKILL_CONG_CU/` | Phân khu `audit_plan_hr_skill` | 0 |
| 2 | `02_DU_LIEU_DAU_VAO/` | Phân khu `input_data` | 7 |
| 3 | `03_DU_LIEU_PHAN_TICH/` | Phân khu `analysis_data` | 13 |
| 4 | `04_KET_QUA_BANG_BIEU_HINH_VE_CHAT_LUONG_CAO/` | Phân khu `figures_tables` | 12 |
| 5 | `05_FILE_HIEN_HANH_HTML_WEB/` | Phân khu `web_html` | 2 |
| 6 | `06_MA_NGUON_SCRIPT_VA_KIEM_THU/` | Phân khu `scripts_tests` | 11 |
| 7 | `07_FILE_DU_THAO_BAO_CAO_VA_NGHIEM_THU/` | Phân khu `drafts_dossiers` | 16 |

## 3. Sản phẩm Đầu ra Bắt buộc (Deliverables)

- 5 Workbook Excel GĐ3: `TBM_HANOI_G3_COUPLED_HYDRO_MECHANICAL.xlsx`, `TBM_HANOI_G3_NUMERICAL_3D_FEM_BENCHMARK.xlsx`, `TBM_HANOI_G3_PINN_DEEP_SURROGATE_AI.xlsx`, `TBM_HANOI_G3_BUILDING_RISK_EXPOSURE_150.xlsx`, `EVIDENCE_TRACEABILITY_AUDIT_MATRIX_GIAI_DOAN_3.xlsx`.
- 7 Hình vẽ 300 DPI (`FIG_15` đến `FIG_21`).
- Ứng dụng WebGIS v3.0: `webgis_digital_twin_tbm_v3.html` kèm 3 lớp GeoJSON (`alignment_complete_wgs84.geojson`, `buildings_exposure_150.geojson`, `groundwater_drawdown_contours.geojson`).
- Hồ sơ Kiểm toán Độc lập (`AUDIT_REPORT.md`, `GATE_REASSESSMENT.csv`, `artifact_audit.json`) và Hồ sơ Cách ly Dữ liệu (`data/quarantine/`).
