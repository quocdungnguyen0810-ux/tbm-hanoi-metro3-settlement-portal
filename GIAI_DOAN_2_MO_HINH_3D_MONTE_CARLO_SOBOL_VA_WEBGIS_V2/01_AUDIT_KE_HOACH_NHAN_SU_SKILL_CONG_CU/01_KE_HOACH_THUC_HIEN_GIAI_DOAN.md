# KẾ HOẠCH THỰC HIỆN & AUDIT TIẾN ĐỘ: GIAI ĐOẠN 2: GIẢI TÍCH 3D LOGANATHAN-POULOS, GIẢI TÍCH NGẪU NHIÊN 10.000 MẪU MONTE CARLO & CHỈ SỐ SOBOL, ĐÁNH GIÁ TỔN HẠI 100 CÔNG TRÌNH & WEBGIS V2.0 (GATES 6 - 8)

- **Mã giai đoạn:** `GIAI_DOAN_2` (`STAGE_2`)
- **Thời gian thực hiện:** Tháng 05/2027 – Tháng 08/2027 (Mở rộng 3D dọc trục tiến khiên TBM, Độ nhạy toàn cục GSA & WebGIS v2.0)
- **Thư mục quản lý:** `QUAN_TRI_DU_AN_TBM_PHAN_KY_GIAI_DOAN/GIAI_DOAN_2_MO_HINH_3D_MONTE_CARLO_SOBOL_VA_WEBGIS_V2/`

## 1. Mục tiêu Trọng tâm của Giai đoạn

1. Sao lưu nguyên vẹn 100% sản phẩm Giai đoạn 1 trước khi triển khai Giai đoạn 2.
2. Phát triển mô hình giải tích 3D xét đến vị trí gương đào TBM tiến dọc trục hầm từ S9 đến S12.
3. Thực hiện phân tích ngẫu nhiên 10.000 mẫu Monte Carlo và đánh giá độ nhạy toàn cục (Global Sensitivity Analysis).
4. Phân tích tương tác biến dạng uốn - kéo ngang Burland (1995) cho 100 công trình và xây dựng WebGIS v2.0.

## 2. Cấu trúc Phân tách 7 Phân khu Dữ liệu & Sản phẩm trong Giai đoạn

| STT | Thư mục con chuẩn hóa | Chức năng & Nội dung lưu trữ | Số tệp đã phân bổ |
|:---:|---|---|:---:|
| 1 | `01_AUDIT_KE_HOACH_NHAN_SU_SKILL_CONG_CU/` | Phân khu `audit_plan_hr_skill` | 0 |
| 2 | `02_DU_LIEU_DAU_VAO/` | Phân khu `input_data` | 8 |
| 3 | `03_DU_LIEU_PHAN_TICH/` | Phân khu `analysis_data` | 9 |
| 4 | `04_KET_QUA_BANG_BIEU_HINH_VE_CHAT_LUONG_CAO/` | Phân khu `figures_tables` | 10 |
| 5 | `05_FILE_HIEN_HANH_HTML_WEB/` | Phân khu `web_html` | 2 |
| 6 | `06_MA_NGUON_SCRIPT_VA_KIEM_THU/` | Phân khu `scripts_tests` | 8 |
| 7 | `07_FILE_DU_THAO_BAO_CAO_VA_NGHIEM_THU/` | Phân khu `drafts_dossiers` | 15 |

## 3. Sản phẩm Đầu ra Bắt buộc (Deliverables)

- 4 Workbook Excel GĐ2: `TBM_HANOI_G2_LOGANATHAN_POULOS_3D.xlsx`, `TBM_HANOI_G2_MONTE_CARLO_SENSITIVITY.xlsx`, `TBM_HANOI_G2_BUILDING_STRAIN_DAMAGE_100.xlsx`, `EVIDENCE_TRACEABILITY_AUDIT_MATRIX_GIAI_DOAN_2.xlsx`.
- 7 Hình vẽ 300 DPI (`FIG_08` đến `FIG_14`) minh họa phân phối Monte Carlo, chỉ số Sobol, trắc dọc động, mặt lún 3D và giản đồ Burland.
- Ứng dụng WebGIS v2.0: `webgis_settlement_advance_v2.html` kèm `buildings_exposure_100.geojson` và `alignment_longitudinal_wgs84.geojson`.
- Báo cáo toàn văn Giai đoạn 2 (`.md`, `.docx`) và Hồ sơ nghiệm thu GĐ2 niêm phong 55 mã băm SHA-256.
