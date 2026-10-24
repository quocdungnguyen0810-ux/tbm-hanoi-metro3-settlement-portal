# KẾ HOẠCH THỰC HIỆN & AUDIT TIẾN ĐỘ: GIAI ĐOẠN 0: HỒ SƠ THUYẾT MINH ĐỀ TÀI NCKH CẤP TRƯỜNG T2027, KHỞI TẠO QUẢN TRỊ & THU THẬP NGUỒN (GATE 0 - GATE 1)

- **Mã giai đoạn:** `GIAI_DOAN_0` (`STAGE_0`)
- **Thời gian thực hiện:** Tháng 10/2026 – Tháng 01/2027 (Chuẩn bị, Thẩm định Thuyết minh & Khởi tạo Baseline)
- **Thư mục quản lý:** `QUAN_TRI_DU_AN_TBM_PHAN_KY_GIAI_DOAN/GIAI_DOAN_0_HO_SO_THUYET_MINH_T2027_VA_KHOI_TAO/`

## 1. Mục tiêu Trọng tâm của Giai đoạn

1. Hoàn thiện hồ sơ Thuyết minh đề tài NCKH cấp Trường mã số T2027_TMĐK_Nguyen_Hai_Ha (kinh phí 25.000.000 VNĐ, thời gian 12 tháng).
2. Thiết lập quy chuẩn quản trị Multi-Agent (`AGENTS.md`, `.agents/agents.json`, `configs/project_config.json`).
3. Thu thập bộ dữ liệu nguồn ban đầu (`research/`), chuẩn hóa từ điển dữ liệu (`data_dictionary.md`) và 9 biểu mẫu CSV chuẩn SI.
4. Kiểm toán độc lập hồ sơ thuyết minh và đánh giá phản biện sắc bén (Grill-Me Gate 0 & Gate 1).

## 2. Cấu trúc Phân tách 7 Phân khu Dữ liệu & Sản phẩm trong Giai đoạn

| STT | Thư mục con chuẩn hóa | Chức năng & Nội dung lưu trữ | Số tệp đã phân bổ |
|:---:|---|---|:---:|
| 1 | `01_AUDIT_KE_HOACH_NHAN_SU_SKILL_CONG_CU/` | Phân khu `audit_plan_hr_skill` | 0 |
| 2 | `02_DU_LIEU_DAU_VAO/` | Phân khu `input_data` | 24 |
| 3 | `03_DU_LIEU_PHAN_TICH/` | Phân khu `analysis_data` | 9 |
| 4 | `04_KET_QUA_BANG_BIEU_HINH_VE_CHAT_LUONG_CAO/` | Phân khu `figures_tables` | 5 |
| 5 | `05_FILE_HIEN_HANH_HTML_WEB/` | Phân khu `web_html` | 1 |
| 6 | `06_MA_NGUON_SCRIPT_VA_KIEM_THU/` | Phân khu `scripts_tests` | 9 |
| 7 | `07_FILE_DU_THAO_BAO_CAO_VA_NGHIEM_THU/` | Phân khu `drafts_dossiers` | 14 |

## 3. Sản phẩm Đầu ra Bắt buộc (Deliverables)

- Hồ sơ thuyết minh hoàn chỉnh: `T2027_TMĐK_Nguyen_Hai_Ha.docx` & bản PDF `T2027_Thuyetminh_Nguyen_Hai_Ha.pdf`.
- Biên bản Audit Thuyết minh: `BIEN_BAN_AUDIT_VA_HOAN_THIEN_THUYET_MINH_T2027.md`.
- Bộ 9 biểu mẫu chuẩn hóa dữ liệu đầu vào (`alignments.csv`, `stratigraphy_intervals.csv`, `tbm_parameters.csv`, ...).
- Báo cáo thu thập nguồn và bằng chứng trích xuất: `WF03_SOURCE_HARVEST_REPORT.md`, `WF04_EXTRACTION_EVIDENCE.md`, `WF05_GATE_1_AUDIT_REPORT.md`.
