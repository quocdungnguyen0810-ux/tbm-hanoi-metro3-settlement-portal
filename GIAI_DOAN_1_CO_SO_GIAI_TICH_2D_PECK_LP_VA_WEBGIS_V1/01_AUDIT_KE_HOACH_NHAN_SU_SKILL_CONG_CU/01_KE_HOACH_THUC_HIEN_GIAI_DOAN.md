# KẾ HOẠCH THỰC HIỆN & AUDIT TIẾN ĐỘ: GIAI ĐOẠN 1: MÔ HÌNH GIẢI TÍCH 2D (PECK 1969 & LOGANATHAN-POULOS 1998), ĐỘ NHẠY OAT 21 KỊCH BẢN, 60 CÔNG TRÌNH & WEBGIS V1.0 (GATES 2 - 5)

- **Mã giai đoạn:** `GIAI_DOAN_1` (`STAGE_1`)
- **Thời gian thực hiện:** Tháng 01/2027 – Tháng 04/2027 (Chuẩn hóa Baseline Địa kỹ thuật, Giải tích 2D, Độ nhạy OAT & Nghiệm thu Bộ môn GĐ1)
- **Thư mục quản lý:** `QUAN_TRI_DU_AN_TBM_PHAN_KY_GIAI_DOAN/GIAI_DOAN_1_CO_SO_GIAI_TICH_2D_PECK_LP_VA_WEBGIS_V1/`

## 1. Mục tiêu Trọng tâm của Giai đoạn

1. Chuẩn hóa hệ đơn vị SI cho thông số hầm TBM (D = 6.3m, z0 = 16.5m, d = 13.0m) và địa tầng hố khoan BH12.
2. Lập trình và kiểm thử độc lập mô hình giải tích Peck (1969) và Loganathan & Poulos (1998) cho hầm đơn và hầm đôi.
3. Thực hiện phân tích độ nhạy OAT 21 kịch bản theo dải tổn thất thể tích VL = [0.5%, 1.0%, 1.5%, 2.0%] và K = [0.4, 0.5, 0.6].
4. Xây dựng bộ 4 file Excel tính toán chuyên nghiệp, 11 hình vẽ 300–350 DPI, ứng dụng WebGIS v1.0 (60 công trình) và Bản thảo Luận án 9 chương.

## 2. Cấu trúc Phân tách 7 Phân khu Dữ liệu & Sản phẩm trong Giai đoạn

| STT | Thư mục con chuẩn hóa | Chức năng & Nội dung lưu trữ | Số tệp đã phân bổ |
|:---:|---|---|:---:|
| 1 | `01_AUDIT_KE_HOACH_NHAN_SU_SKILL_CONG_CU/` | Phân khu `audit_plan_hr_skill` | 0 |
| 2 | `02_DU_LIEU_DAU_VAO/` | Phân khu `input_data` | 7 |
| 3 | `03_DU_LIEU_PHAN_TICH/` | Phân khu `analysis_data` | 12 |
| 4 | `04_KET_QUA_BANG_BIEU_HINH_VE_CHAT_LUONG_CAO/` | Phân khu `figures_tables` | 13 |
| 5 | `05_FILE_HIEN_HANH_HTML_WEB/` | Phân khu `web_html` | 3 |
| 6 | `06_MA_NGUON_SCRIPT_VA_KIEM_THU/` | Phân khu `scripts_tests` | 15 |
| 7 | `07_FILE_DU_THAO_BAO_CAO_VA_NGHIEM_THU/` | Phân khu `drafts_dossiers` | 32 |

## 3. Sản phẩm Đầu ra Bắt buộc (Deliverables)

- 4 Workbook Excel GĐ1: `TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx`, `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx`, `TBM_BUILDING_RISK_EXPOSURE.xlsx`, `EVIDENCE_TRACEABILITY_AUDIT_MATRIX.xlsx`.
- 11 Hình vẽ chất lượng cao (4 hình run 350 DPI + 7 hình luận án 300 DPI `FIG_01` đến `FIG_07`).
- Ứng dụng WebGIS v1.0: `webgis_settlement_map.html` kèm 3 lớp GeoJSON (`alignment_wgs84.geojson`, `buildings_exposure_60.geojson`, `stations_wgs84.geojson`).
- Bản thảo Luận án hoàn chỉnh 9 chương (`.md` và `.docx`) cùng Hồ sơ nghiệm thu cấp Bộ môn GĐ1.
