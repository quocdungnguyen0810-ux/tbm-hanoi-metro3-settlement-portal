# BÁO CÁO AUDIT QUÁ TRÌNH, CỔNG KIỂM SOÁT (GATES) & KẾT QUẢ ĐẦU RA: GIAI_DOAN_1

## 1. Phán quyết Kiểm toán Độc lập tại các Cổng Kiểm soát (Audit Gates)

| Cổng Kiểm soát (Audit Gate) | Phán quyết Kiểm toán Độc lập (Reassessed Verdict) |
|---|---|
| **`GATE_2_PHYSICAL_SPATIAL_QC`** | RETRACTED_BLOCKED -> PASS_MECHANICS_ONLY (Thông số D=6.3m, z0=16.5-17.8m, K=0.5, nu=0.35 hợp lý vật lý; nhưng 60 công trình là dữ liệu mô phỏng kịch bản cần gắn nhãn `scenario_assumption`) |
| **`GATE_3_BASELINE_FREEZE`** | PARTIALLY_VERIFIED (2 file CSV frozen khớp SHA-256 100%, đã khắc phục cơ chế chống ghi đè) |
| **`GATE_4_ANALYTICAL_SENSITIVITY_GIS`** | VERIFIED_CONDITIONAL (Nhánh Peck Gaussian đạt 7/7 unit tests bảo toàn thể tích sai số < 1e-4; nhánh LP 1998 cần lưu ý hệ số gap parameter g) |
| **`GATE_5_REPORTING_REPRODUCIBILITY`** | PARTIALLY_VERIFIED (Đã có đủ 9 chương bản thảo, 4 file Excel, 11 hình vẽ và WebGIS v1.0; cần mở rộng bảng Traceability Matrix) |

## 2. Các Phát hiện Kiểm toán Trọng yếu (Key Audit Findings) & Xử lý Cách ly

- [ĐẠT] Mô hình Peck (1969) bảo toàn 100% thể tích phễu lún tích phân số so với VL*At; đối xứng hoàn hảo và hội tụ về 0 khi x -> vô cùng (7/7 unit tests PASSED).
- [PHÁT HIỆN H-01] Nhánh Loganathan & Poulos (1998) trong `analytical_engine.py` đang gán trực tiếp epsilon_0 = VL; theo nguyên bản ASCE 1998 cần quy đổi qua thông số khe hở hình khuyên (gap parameter g). Đã gắn cờ `experimental_unverified`.
- [PHÁT HIỆN H-05] Các ô công thức trong `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx` được sinh bởi OpenPyXL nên cần mở bằng MS Excel và lưu lại để nạp giá trị cached values.
- [PHÁT HIỆN C-03] Lớp `buildings_exposure_60.geojson` được tái lập phục vụ mô phỏng kịch bản phơi nhiễm, đã chuyển nhãn sang `scenario_assumption`.

## 3. Bảng Kiểm kê Toàn bộ Tệp tin Đầu ra của Giai đoạn kèm Mã băm SHA-256 & Provenance

| STT | Phân khu | Tên tệp | Kích thước (Bytes) | Giá trị cơ sở (`value_basis`) | Độ tin cậy (`confidence`) | Cờ QA (`qa_flag`) | Mã băm SHA-256 |
|:---:|---|---|---:|---|---|---|---|
| 1 | `input_data` | `stratigraphy_raw.csv` | 4,462 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2de6b12980f9725e...` |
| 2 | `input_data` | `official_docs.csv` | 2,032 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `1516e57404f61bcb...` |
| 3 | `input_data` | `project_config.json` | 1,573 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bfc5fdcb261b2fdf...` |
| 4 | `input_data` | `normalized_parameters.csv` | 377 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `5ae8bcd5626b4c0c...` |
| 5 | `input_data` | `normalized_sources.csv` | 1,120 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6a69a0817083365b...` |
| 6 | `input_data` | `checksums.sha256` | 183 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d3f19e3c8b6c3590...` |
| 7 | `input_data` | `manifest.json` | 449 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bf98a5c235e828aa...` |
| 8 | `analysis_data` | `TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx` | 14,668 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `91302aae5f63206c...` |
| 9 | `analysis_data` | `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx` | 31,226 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bce723d4c9c226d4...` |
| 10 | `analysis_data` | `TBM_BUILDING_RISK_EXPOSURE.xlsx` | 13,322 | `scenario_assumption` | `high` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `d15cadc96ca7c6d6...` |
| 11 | `analysis_data` | `EVIDENCE_TRACEABILITY_AUDIT_MATRIX.xlsx` | 12,365 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `41d4342bc9aa53d3...` |
| 12 | `analysis_data` | `HUONG_DAN_SU_DUNG_BO_DU_LIEU_EXCEL.md` | 4,669 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6aa4a7ae2bd1b941...` |
| 13 | `analysis_data` | `alignment_wgs84.geojson` | 1,836 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `df81e6972724b959...` |
| 14 | `analysis_data` | `buildings_exposure_60.geojson` | 76,370 | `scenario_assumption` | `medium_scenario_model` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `1cbe4deaa9f72c16...` |
| 15 | `analysis_data` | `stations_wgs84.geojson` | 1,550 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ae1330a66bd7e782...` |
| 16 | `analysis_data` | `settlement_scenarios_summary.csv` | 2,343 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `afb2964faba9df08...` |
| 17 | `analysis_data` | `ai_surrogate_evaluation.json` | 253 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `1979244e6bd1e86f...` |
| 18 | `analysis_data` | `WF07_QC_REPORT.json` | 155 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `232b2da0f0373841...` |
| 19 | `analysis_data` | `WF19_TRACEABILITY_MATRIX.csv` | 1,778 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `935849f081075b16...` |
| 20 | `figures_tables` | `DANH_MUC_HINH_VE_300DPI_VA_CHU_THICH.md` | 3,478 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2840f3fe9edfd6eb...` |
| 21 | `figures_tables` | `FIG_01_Geotechnical_Stratigraphy_BH12.png` | 470,555 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `74850ae93a59ecf8...` |
| 22 | `figures_tables` | `FIG_02_Peck_vs_LoganathanPoulos_Transverse.png` | 344,679 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `31c86f8c815b2765...` |
| 23 | `figures_tables` | `FIG_03_Twin_Tunnel_Interaction_Profiles.png` | 517,361 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `dd850d9c1c94c716...` |
| 24 | `figures_tables` | `FIG_04_Sensitivity_Curves_Smax_Slope.png` | 425,787 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fc0e50b948363394...` |
| 25 | `figures_tables` | `FIG_05_Building_Risk_Zoning_Distribution.png` | 197,605 | `scenario_assumption` | `high` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `7715d3598d44eb8f...` |
| 26 | `figures_tables` | `FIG_06_Surrogate_AI_Parity_and_Residuals.png` | 436,730 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `7fe709df94dd105c...` |
| 27 | `figures_tables` | `FIG_07_Methodological_Workflow_Framework.png` | 370,821 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2c00a987ecab27ee...` |
| 28 | `figures_tables` | `peck_vs_lp_profiles.png` | 444,996 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9d74e599760f6730...` |
| 29 | `figures_tables` | `sensitivity_smax_vs_vl.png` | 233,728 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d126a2d302570282...` |
| 30 | `figures_tables` | `spatial_settlement_envelope.png` | 405,834 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e3ddd865e2530cd8...` |
| 31 | `figures_tables` | `ai_surrogate_accuracy.png` | 225,281 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `0e56e65bfa4e202b...` |
| 32 | `figures_tables` | `settlement_scenarios_summary.csv` | 2,343 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `afb2964faba9df08...` |
| 33 | `web_html` | `webgis_settlement_map.html` | 53,252 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `507ea27896e5b938...` |
| 34 | `web_html` | `HUONG_DAN_SU_DUNG_WEBGIS.md` | 3,967 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8869a3df1c8400d5...` |
| 35 | `web_html` | `06_tables__webgis_settlement_map.html` | 9,984 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `0dbab2c1069ab531...` |
| 36 | `scripts_tests` | `normalize_data.py` | 4,276 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d1643de7df1d384b...` |
| 37 | `scripts_tests` | `qc_checks.py` | 1,848 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9b0d860fcca0ee00...` |
| 38 | `scripts_tests` | `freeze_baseline.py` | 1,683 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `99325d6070a66173...` |
| 39 | `scripts_tests` | `analytical_engine.py` | 3,751 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8235752171482709...` |
| 40 | `scripts_tests` | `sensitivity_analysis.py` | 6,084 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `73253a10a840e246...` |
| 41 | `scripts_tests` | `spatial_engine.py` | 15,829 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `5d0917e60c8e1539...` |
| 42 | `scripts_tests` | `surrogate_ai.py` | 6,839 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `93f7f751860a160f...` |
| 43 | `scripts_tests` | `make_publication_figures.py` | 2,279 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2681b5f70b213ba7...` |
| 44 | `scripts_tests` | `run_full_pipeline.py` | 1,768 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `be38e1d5a1cf785b...` |
| 45 | `scripts_tests` | `generate_dissertation_excel_files.py` | 50,238 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e472ebccafb327f2...` |
| 46 | `scripts_tests` | `generate_dissertation_figures.py` | 23,303 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6ad7a622b88f8ced...` |
| 47 | `scripts_tests` | `build_webgis_package.py` | 38,926 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a9ac35cde02762b9...` |
| 48 | `scripts_tests` | `export_dissertation_docx.py` | 15,244 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `949ca6a4ad913ede...` |
| 49 | `scripts_tests` | `build_acceptance_dossier.py` | 42,933 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ab9b1f0f2851b17c...` |
| 50 | `scripts_tests` | `test_analytical_engine.py` | 2,476 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ed87626cc448f132...` |
| 51 | `drafts_dossiers` | `DE_CUONG_CHI_TIET_LUAN_AN.md` | 10,649 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `1d40246f210e4731...` |
| 52 | `drafts_dossiers` | `GRILL_ME_CRITICAL_REVIEW_AND_DECISIONS.md` | 10,490 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9839f38e4101bc65...` |
| 53 | `drafts_dossiers` | `KE_HOACH_THUC_THI_CHI_TIET.md` | 11,987 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `542f6b730c914d9e...` |
| 54 | `drafts_dossiers` | `00_Trang_bia_va_Tom_tat.md` | 7,405 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `5d35e3ae07347302...` |
| 55 | `drafts_dossiers` | `01_Chuong_1_Tong_quan_va_Dat_van_de.md` | 15,661 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9256503a67bc43e5...` |
| 56 | `drafts_dossiers` | `02_Chuong_2_Co_so_ly_thuyet_va_Mo_hinh_giai_tich.md` | 19,863 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `500c42b6ec114df8...` |
| 57 | `drafts_dossiers` | `03_Chuong_3_Dac_trung_dia_ky_thuat_va_Thong_so_dau_vao.md` | 12,564 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d1763fb89ae5de83...` |
| 58 | `drafts_dossiers` | `04_Chuong_4_Ket_qua_tinh_toan_va_Phan_tich_do_nhay.md` | 11,399 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9e7d6fa8edacd8cb...` |
| 59 | `drafts_dossiers` | `05_Chuong_5_Danh_gia_rui_ro_cong_trinh_va_Tich_hop_WebGIS.md` | 10,921 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `7bf0191192f94a2f...` |
| 60 | `drafts_dossiers` | `06_Chuong_6_Phat_trien_mo_hinh_Surrogate_AI_du_bao_tuc_thoi.md` | 9,570 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fa0da8ea3c06dd6c...` |
| 61 | `drafts_dossiers` | `07_Chuong_7_Ket_luan_Kien_nghi_va_Quy_trinh_quan_trac.md` | 10,363 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e6b71a25517af4fc...` |
| 62 | `drafts_dossiers` | `08_Tai_lieu_tham_khao_chuan_muc.md` | 6,721 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `80a926abe4eb27a8...` |
| 63 | `drafts_dossiers` | `09_Phu_luc_Audit_Log_va_Ma_tran_bang_chung.md` | 8,496 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `cdadaa9f3aabed6e...` |
| 64 | `drafts_dossiers` | `LUAN_AN_HOAN_CHINH_TBM_METRO3_HANOI.md` | 113,546 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ac63cd88f51fa901...` |
| 65 | `drafts_dossiers` | `LUAN_AN_HOAN_CHINH_TBM_METRO3_HANOI.docx` | 2,869,194 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `79035bd0da0a4c9a...` |
| 66 | `drafts_dossiers` | `BAO_CAO_TOM_TAT_NGHIEM_THU_GIAI_DOAN_1.md` | 7,856 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `3249a50256407616...` |
| 67 | `drafts_dossiers` | `BAO_CAO_TOM_TAT_NGHIEM_THU_GIAI_DOAN_1.docx` | 39,899 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bec8e330782b84a4...` |
| 68 | `drafts_dossiers` | `BIEN_BAN_KIEM_TOAN_KHOA_HOC_VA_BAN_GIAO_GATE_1_DEN_5.md` | 5,344 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2bc77b4927a0ca53...` |
| 69 | `drafts_dossiers` | `BIEN_BAN_KIEM_TOAN_KHOA_HOC_VA_BAN_GIAO_GATE_1_DEN_5.docx` | 38,676 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `31f094a4855d683f...` |
| 70 | `drafts_dossiers` | `DANH_MUC_HO_SO_VA_CHECKSUM_SHA256.md` | 8,027 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9c7fce3f03682f9c...` |
| 71 | `drafts_dossiers` | `PHIEU_DANH_GIA_NGHIEM_THU_THU_BO_MON.md` | 4,249 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `96807e6d89e31663...` |
| 72 | `drafts_dossiers` | `PHIEU_DANH_GIA_NGHIEM_THU_THU_BO_MON.docx` | 37,772 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `5dc4d9c5e015bd0a...` |
| 73 | `drafts_dossiers` | `TO_TRINH_XIN_NGHIEM_THU_THU_BO_MON.md` | 5,244 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a0561d5a58fecc4b...` |
| 74 | `drafts_dossiers` | `TO_TRINH_XIN_NGHIEM_THU_THU_BO_MON.docx` | 38,189 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `064b7341f807f5f9...` |
| 75 | `drafts_dossiers` | `MANUSCRIPT_TBM_HANOI_EIA.md` | 11,117 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `38c8c003ecfa0606...` |
| 76 | `drafts_dossiers` | `MANUSCRIPT_TBM_HANOI_EIA_VERIFIED_2026.md` | 15,836 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `5a72a481d41ac5c2...` |
| 77 | `drafts_dossiers` | `MANUSCRIPT_TBM_HANOI_EIA_VERIFIED_2026.docx` | 43,465 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `aef32cae1ca304b8...` |
| 78 | `drafts_dossiers` | `WF08_GATE_2_AUDIT_REPORT.md` | 1,504 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `55e6240c6ab49d33...` |
| 79 | `drafts_dossiers` | `WF10_MECHANICS_VERIFICATION_MEMO.md` | 2,207 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `70d7daf2560adad5...` |
| 80 | `drafts_dossiers` | `WF11_GATE_3_AUDIT_REPORT.md` | 1,190 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `f059f48c9a2c265a...` |
| 81 | `drafts_dossiers` | `WF16_GATE_4_AUDIT_REPORT.md` | 2,474 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a12f611e0ab0ad7c...` |
| 82 | `drafts_dossiers` | `WF20_FINAL_AUDIT_RELEASE.md` | 3,878 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9fe53b1991907db8...` |
