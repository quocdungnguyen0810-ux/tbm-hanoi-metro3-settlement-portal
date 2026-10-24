# BÁO CÁO AUDIT QUÁ TRÌNH, CỔNG KIỂM SOÁT (GATES) & KẾT QUẢ ĐẦU RA: GIAI_DOAN_4

## 1. Phán quyết Kiểm toán Độc lập tại các Cổng Kiểm soát (Audit Gates)

| Cổng Kiểm soát (Audit Gate) | Phán quyết Kiểm toán Độc lập (Reassessed Verdict) |
|---|---|
| **`GATE_SV_1_PROPOSAL_AND_MANUAL_QC`** | PASSED (Đầy đủ Đề cương, Kế hoạch phân công, Sổ tay kỹ thuật `.md` & `.docx` và bảng tiến độ Gantt `.xlsx` cho cả 2 đề tài NCKH Sinh viên) |
| **`GATE_SV_2_STORYMAP_PROTOTYPE_VERIFICATION`** | PASSED (Ứng dụng mẫu `05_WEBGIS_PROTOTYPE/index.html` và 4 lớp GeoJSON hoạt động tốt, phân biệt rõ dữ liệu mẫu phục vụ đào tạo sinh viên) |

## 2. Các Phát hiện Kiểm toán Trọng yếu (Key Audit Findings) & Xử lý Cách ly

- [ĐẠT] Toàn bộ 4 file Excel và 6 file Word của 2 nhóm NCKH Sinh viên đều đọc tốt, định dạng chuẩn mực, không có lỗi công thức.
- [ĐẠT] Biểu mẫu thu thập dữ liệu thực địa (`04_BIEU_MAU_THU_THAP_DU_LIEU_THUC_DIA.xlsx` và `04_BO_CO_SO_DU_LIEU_VA_MAU_THU_THAP_GIS.xlsx`) là công cụ chuẩn để thu thập dữ liệu thực tế thay thế các bộ dữ liệu giả định ở GĐ1–GĐ3.

## 3. Bảng Kiểm kê Toàn bộ Tệp tin Đầu ra của Giai đoạn kèm Mã băm SHA-256 & Provenance

| STT | Phân khu | Tên tệp | Kích thước (Bytes) | Giá trị cơ sở (`value_basis`) | Độ tin cậy (`confidence`) | Cờ QA (`qa_flag`) | Mã băm SHA-256 |
|:---:|---|---|---:|---|---|---|---|
| 1 | `input_data` | `alignment_wgs84.geojson` | 1,836 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `df81e6972724b959...` |
| 2 | `input_data` | `stations_wgs84.geojson` | 1,550 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ae1330a66bd7e782...` |
| 3 | `input_data` | `TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx` | 14,668 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `91302aae5f63206c...` |
| 4 | `analysis_data` | `02_KE_HOACH_VA_TIEN_DO_GANTT.xlsx` | 7,974 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `40e8d493124bceb7...` |
| 5 | `analysis_data` | `04_BO_CO_SO_DU_LIEU_VA_MAU_THU_THAP_GIS.xlsx` | 12,344 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4d47319020785c5b...` |
| 6 | `analysis_data` | `metro_line.geojson` | 1,096 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2a911f119e99f9b9...` |
| 7 | `analysis_data` | `sensitive_points.geojson` | 2,488 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `0341e766381816f0...` |
| 8 | `analysis_data` | `settlement_zones.geojson` | 6,839 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `753338d4ba69f017...` |
| 9 | `analysis_data` | `stations.geojson` | 2,404 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bd553c9902bcece4...` |
| 10 | `analysis_data` | `NCKH_SV_2026_QuanLyDoThi__02_KE_HOACH_VA_TIEN_DO_GANTT.xlsx` | 8,593 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e92c660e675794f8...` |
| 11 | `analysis_data` | `04_BIEU_MAU_THU_THAP_DU_LIEU_THUC_DIA.xlsx` | 8,201 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e70146aba4988dad...` |
| 12 | `figures_tables` | `02_KE_HOACH_VA_TIEN_DO_GANTT.xlsx` | 7,974 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `40e8d493124bceb7...` |
| 13 | `figures_tables` | `04_BO_CO_SO_DU_LIEU_VA_MAU_THU_THAP_GIS.xlsx` | 12,344 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4d47319020785c5b...` |
| 14 | `figures_tables` | `NCKH_SV_2026_QuanLyDoThi__02_KE_HOACH_VA_TIEN_DO_GANTT.xlsx` | 8,593 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e92c660e675794f8...` |
| 15 | `figures_tables` | `04_BIEU_MAU_THU_THAP_DU_LIEU_THUC_DIA.xlsx` | 8,201 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e70146aba4988dad...` |
| 16 | `web_html` | `index.html` | 22,374 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `5e74743191a011b6...` |
| 17 | `scripts_tests` | `generate_huong4_deliverables.py` | 24,058 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `53eeceed8b1f0a27...` |
| 18 | `scripts_tests` | `build_huong4_webgis.py` | 33,303 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d57031c818142032...` |
| 19 | `scripts_tests` | `generate_nckh_sv_deliverables.py` | 35,665 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d255cd9ab346d69e...` |
| 20 | `drafts_dossiers` | `01_DE_CUONG_THUYET_MINH_NCKHSV.md` | 21,262 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `640bb7260a77db57...` |
| 21 | `drafts_dossiers` | `01_DE_CUONG_THUYET_MINH_NCKHSV.docx` | 39,618 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8096448cf920130f...` |
| 22 | `drafts_dossiers` | `02_KE_HOACH_TRIEN_KHAI_CHI_TIET_VA_PHAN_CONG.md` | 12,010 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d1ce33df25c456d4...` |
| 23 | `drafts_dossiers` | `02_KE_HOACH_TRIEN_KHAI_CHI_TIET_VA_PHAN_CONG.docx` | 30,277 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6f99b3295c14b8e4...` |
| 24 | `drafts_dossiers` | `03_SO_TAY_HUONG_DAN_KY_THUAT_CHO_SINH_VIEN.md` | 15,793 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `71c7b411b407a94c...` |
| 25 | `drafts_dossiers` | `03_SO_TAY_HUONG_DAN_KY_THUAT_CHO_SINH_VIEN.docx` | 37,550 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `c82fe2084421b73f...` |
| 26 | `drafts_dossiers` | `NCKH_SV_2026_QuanLyDoThi__01_DE_CUONG_THUYET_MINH_NCKHSV.md` | 12,147 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `7b18f64bd7bf5d6d...` |
| 27 | `drafts_dossiers` | `NCKH_SV_2026_QuanLyDoThi__01_DE_CUONG_THUYET_MINH_NCKHSV.docx` | 30,269 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `c18599b4bd58a874...` |
| 28 | `drafts_dossiers` | `NCKH_SV_2026_QuanLyDoThi__02_KE_HOACH_TRIEN_KHAI_CHI_TIET_VA_PHAN_CONG.md` | 8,037 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `22a95810aac45929...` |
| 29 | `drafts_dossiers` | `NCKH_SV_2026_QuanLyDoThi__02_KE_HOACH_TRIEN_KHAI_CHI_TIET_VA_PHAN_CONG.docx` | 29,861 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `3cd074fc60d66f96...` |
| 30 | `drafts_dossiers` | `NCKH_SV_2026_QuanLyDoThi__03_SO_TAY_HUONG_DAN_KY_THUAT_CHO_SINH_VIEN.md` | 10,113 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `51539105fe747e80...` |
| 31 | `drafts_dossiers` | `NCKH_SV_2026_QuanLyDoThi__03_SO_TAY_HUONG_DAN_KY_THUAT_CHO_SINH_VIEN.docx` | 28,470 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `945fec12474def5d...` |
