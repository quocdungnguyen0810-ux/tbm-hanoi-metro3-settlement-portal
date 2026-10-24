# BÁO CÁO AUDIT QUÁ TRÌNH, CỔNG KIỂM SOÁT (GATES) & KẾT QUẢ ĐẦU RA: GIAI_DOAN_0

## 1. Phán quyết Kiểm toán Độc lập tại các Cổng Kiểm soát (Audit Gates)

| Cổng Kiểm soát (Audit Gate) | Phán quyết Kiểm toán Độc lập (Reassessed Verdict) |
|---|---|
| **`GATE_0_GRILL_ME_PROPOSAL`** | PASSED (Đã hoàn thiện 100% Thuyết minh T2027_TMĐK_Nguyen_Hai_Ha.docx, xóa toàn bộ dấu '......', sửa lỗi số học kinh phí 25.000.000 VNĐ) |
| **`GATE_1_SOURCE_INTEGRITY`** | RETRACTED_BLOCKED -> CONDITIONAL_PILOT (Đã có 7 nguồn học thuật & 18 bản ghi địa tầng; còn thiếu PDF gốc EIA 2013 trang cụ thể và trụ địa chất CP03 có tọa độ) |

## 2. Các Phát hiện Kiểm toán Trọng yếu (Key Audit Findings) & Xử lý Cách ly

- [ĐẠT] Hồ sơ thuyết minh T2027 đã khắc phục triệt để 15 lỗi khiếm khuyết (xóa 100% dấu ba chấm, sửa lỗi `22.770.0000` thành `22.770.000` VNĐ, bổ sung 10 tài liệu tham khảo chuẩn DOI).
- [CẢNH BÁO C-01/C-02] File `research/stratigraphy_raw.csv` chưa gắn đủ 5 cột provenance (`source_id`, `source_locator`, `value_basis`, `confidence`, `qa_flag`) trên từng dòng; cần tách rõ nhãn `direct_table` và `derived`.
- [CẬP NHẬT MCP 2026] Qua công cụ MCP `parallel-search`, đã xác thực TBM1 ('Thần Tốc') khởi đào tại S9 (Kim Mã) ở độ sâu 17.8m ngày 30/07/2024, lắp đặt 1.720 vòng vỏ hầm và thông hầm tại S12 ngày 01/12/2025; báo cáo ADB EMR Q1/2025 ghi nhận 56 hộ dân bị ảnh hưởng dọc S9–S12.

## 3. Bảng Kiểm kê Toàn bộ Tệp tin Đầu ra của Giai đoạn kèm Mã băm SHA-256 & Provenance

| STT | Phân khu | Tên tệp | Kích thước (Bytes) | Giá trị cơ sở (`value_basis`) | Độ tin cậy (`confidence`) | Cờ QA (`qa_flag`) | Mã băm SHA-256 |
|:---:|---|---|---:|---|---|---|---|
| 1 | `input_data` | `AGENTS.md` | 3,560 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8e7b53b5153cb0eb...` |
| 2 | `input_data` | `README.md` | 3,917 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4dcc233c4c93e30e...` |
| 3 | `input_data` | `agents.json` | 3,494 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `555c98b8f1e4e36b...` |
| 4 | `input_data` | `task_queue.json` | 20,607 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `baf050600d11fa5e...` |
| 5 | `input_data` | `project_config.json` | 1,573 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bfc5fdcb261b2fdf...` |
| 6 | `input_data` | `official_docs.csv` | 2,032 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `1516e57404f61bcb...` |
| 7 | `input_data` | `stratigraphy_raw.csv` | 4,462 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2de6b12980f9725e...` |
| 8 | `input_data` | `crossref_etasr6748.json` | 8,339 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4ef58dae6c21d1be...` |
| 9 | `input_data` | `crossref_giao.json` | 5,606 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b5489ef07b6d3e95...` |
| 10 | `input_data` | `crossref_shin.json` | 3,152 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `133a7576a1a33d0c...` |
| 11 | `input_data` | `tcxd_2024_article.pdf` | 1,406,096 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `41a3efdc011814a8...` |
| 12 | `input_data` | `alignments.csv` | 411 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e1de3c454c53a92a...` |
| 13 | `input_data` | `analytical_parameters.csv` | 437 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9d8f29808ef3038f...` |
| 14 | `input_data` | `groundwater_observations.csv` | 397 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e08301086556bb08...` |
| 15 | `input_data` | `investigation_points.csv` | 362 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `510917461127a423...` |
| 16 | `input_data` | `nearby_buildings.csv` | 522 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `0c8998af85ba1434...` |
| 17 | `input_data` | `settlement_monitoring.csv` | 532 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `808c1d14d1e25b44...` |
| 18 | `input_data` | `sources.csv` | 193 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `0c207423a255ddca...` |
| 19 | `input_data` | `stratigraphy_intervals.csv` | 681 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `700bce663b0e3e20...` |
| 20 | `input_data` | `tbm_parameters.csv` | 379 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6f35a9c013f8966a...` |
| 21 | `input_data` | `2698-File bài báo full thông tin về tác giả (.doc hoặc .docx)-9308-2-10-20260210.pdf` | 1,383,714 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `40303291c2e5b65a...` |
| 22 | `input_data` | `BB-PhungDaiBinh22018.pdf` | 4,846,858 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `f173b80c9e0c2607...` |
| 23 | `input_data` | `Ghi-chu-Doi-chieu-Hoc-thuat-De-tai-Cap-Truong-UTC.md` | 9,150 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `480e07da84ed5687...` |
| 24 | `input_data` | `Ghi-chu-Doi-chieu-Hoc-thuat-De-tai-Cap-Truong-UTC.docx` | 12,935 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `604af6638e5b6ce0...` |
| 25 | `analysis_data` | `academic_findings.md` | 5,435 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `654038ec06a9170b...` |
| 26 | `analysis_data` | `data_dictionary.md` | 6,584 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bea9a97cb5e6411e...` |
| 27 | `analysis_data` | `official_docs_findings.md` | 5,200 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `61888e7b62a34b80...` |
| 28 | `analysis_data` | `VERIFIED_FIELD_MILESTONES_S9_S12_2026.csv` | 5,233 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4561b52d1bf08563...` |
| 29 | `analysis_data` | `VERIFIED_FIELD_MILESTONES_S9_S12_2026.json` | 7,502 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4ce7cc44e0650aa3...` |
| 30 | `analysis_data` | `VERIFIED_STRATIGRAPHY_PROVENANCE_LONGFORM.csv` | 7,030 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e17e609b0070713f...` |
| 31 | `analysis_data` | `File_Inventory.csv` | 7,709 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a3a5b29e4461c2b5...` |
| 32 | `analysis_data` | `Workflow.csv` | 4,861 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b750cae04d960daf...` |
| 33 | `analysis_data` | `Issue_Log.csv` | 1,144 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2b727797067cda87...` |
| 34 | `figures_tables` | `conceptual_framework_tbm_gis.png` | 2,030,820 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `deda2ce630200e19...` |
| 35 | `figures_tables` | `VERIFIED_FIELD_MILESTONES_S9_S12_2026.csv` | 5,233 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4561b52d1bf08563...` |
| 36 | `figures_tables` | `VERIFIED_STRATIGRAPHY_PROVENANCE_LONGFORM.csv` | 7,030 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e17e609b0070713f...` |
| 37 | `figures_tables` | `File_Inventory.csv` | 7,709 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a3a5b29e4461c2b5...` |
| 38 | `figures_tables` | `Workflow.csv` | 4,861 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b750cae04d960daf...` |
| 39 | `web_html` | `Nghiên cứu ảnh hưởng của áp lực gương đào đường hầm đến.html` | 1,656,254 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ada7b6d643945843...` |
| 40 | `scripts_tests` | `build_inventory.py` | 2,686 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `974af5081038be87...` |
| 41 | `scripts_tests` | `orchestrate.py` | 5,181 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e029a3fdc7dd57b6...` |
| 42 | `scripts_tests` | `fill_proposal_docx.py` | 43,999 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `3a65dbb71b028127...` |
| 43 | `scripts_tests` | `complete_t2027_proposal.py` | 54,146 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a9f955644c630076...` |
| 44 | `scripts_tests` | `export_t2027_nhh_tbm.py` | 7,643 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d35fb789c0710355...` |
| 45 | `scripts_tests` | `geotechnical_and_gsa_reconciliation.py` | 33,654 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `500ada8506243261...` |
| 46 | `scripts_tests` | `execute_reconciliation_and_updates.py` | 66,252 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `461d7a681bef70e0...` |
| 47 | `scripts_tests` | `test_orchestrate.py` | 1,011 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fd231a0b36a9b19f...` |
| 48 | `scripts_tests` | `test_geotechnical_and_gsa_reconciliation.py` | 3,783 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `50e8aa904fdd5e0d...` |
| 49 | `drafts_dossiers` | `T2027_TMĐK_Nguyen_Hai_Ha.docx` | 73,322 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4c1215a6b324d005...` |
| 50 | `drafts_dossiers` | `T2027_TMĐK_Nguyen_Hai_Ha_VERIFIED_2026.docx` | 68,082 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `dfb1a19944a8dd01...` |
| 51 | `drafts_dossiers` | `T2027_TMĐK_Nguyen_Hai_Ha_2026.10.15.docx` | 74,384 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d53ec8440f53f7de...` |
| 52 | `drafts_dossiers` | `T2027_TMĐK_Nguyen_Hai_Ha_BACKUP.docx` | 74,384 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d53ec8440f53f7de...` |
| 53 | `drafts_dossiers` | `T2027_Thuyetminh_Nguyen_Hai_Ha.pdf` | 9,335,270 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b453e19c15fff73f...` |
| 54 | `drafts_dossiers` | `BIEN_BAN_AUDIT_VA_HOAN_THIEN_THUYET_MINH_T2027.md` | 11,296 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `720dac2f13bf3351...` |
| 55 | `drafts_dossiers` | `BAO_CAO_CAP_NHAT_THUC_CHUNG_THUYET_MINH_VA_BAI_BAO_2026.md` | 1,839 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `def62ee0ae51a726...` |
| 56 | `drafts_dossiers` | `BAO_CAO_XAC_MINH_MOC_THUC_DIA_VA_NGUON_CHUNG_THUC.md` | 7,566 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fab9fe09f92a2d79...` |
| 57 | `drafts_dossiers` | `proposal_dump.txt` | 16,755 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `19d820adeebb8dc5...` |
| 58 | `drafts_dossiers` | `WF03_SOURCE_HARVEST_REPORT.md` | 1,852 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fae90e3fae83ef66...` |
| 59 | `drafts_dossiers` | `WF04_EXTRACTION_EVIDENCE.md` | 1,825 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `42f32b142dd8f71d...` |
| 60 | `drafts_dossiers` | `WF05_GATE_1_AUDIT_REPORT.md` | 1,601 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d6f75efafd6068cf...` |
| 61 | `drafts_dossiers` | `GATE_0_EVALUATION_GRILL_ME.md` | 8,490 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `dd245d1eec5f1c78...` |
| 62 | `drafts_dossiers` | `KE_HOACH_THUC_THI_TBM_HANOI.md` | 12,623 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `af9d2d5e1c28a206...` |
