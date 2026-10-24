# BÁO CÁO AUDIT QUÁ TRÌNH, CỔNG KIỂM SOÁT (GATES) & KẾT QUẢ ĐẦU RA: GIAI_DOAN_2

## 1. Phán quyết Kiểm toán Độc lập tại các Cổng Kiểm soát (Audit Gates)

| Cổng Kiểm soát (Audit Gate) | Phán quyết Kiểm toán Độc lập (Reassessed Verdict) |
|---|---|
| **`GATE_6_3D_MECHANICS_MATHEMATICAL`** | RETRACTED_BLOCKED -> VERIFIED_QUASI_3D_FORMULATION (Hàm mặt lún 3D hội tụ toán học đúng 50% Smax tại gương đào y=yf; cần đối chiếu thêm bản gốc LP 1998) |
| **`GATE_7_STOCHASTIC_GSA_CONVERGENCE`** | RETRACTED_UNSUPPORTED -> QUARANTINED_FOR_SALTELI_RECALC (Phát hiện C-06: script sinh mẫu ngẫu nhiên thường và ghi đè chỉ số Sobol bằng hằng số cố định [0.672, 0.145, 0.112, 0.048, 0.018]; đã đưa vào danh mục cách ly Q-002 để tính lại bằng Saltelli LHS) |
| **`GATE_8_FINAL_STAGE_2_PACKAGING`** | INTEGRITY_VERIFIED_CONTENT_RETRACTED (55/55 tệp khớp mã băm SHA-256 tuyệt đối; đã tách nhãn 100 công trình thành `scenario_assumption` Q-003) |

## 2. Các Phát hiện Kiểm toán Trọng yếu (Key Audit Findings) & Xử lý Cách ly

- [ĐẠT TOÀN VẸN BYTE] Toàn bộ 55/55 tệp tin trong danh mục Giai đoạn 2 khớp mã băm SHA-256 100%.
- [PHÁT HIỆN CÁCH LY Q-002 (C-06)] Trong `generate_stage_2_models_and_excel.py:259-318`, phương trình Smax chỉ phụ thuộc (VL, z0, K) nhưng chỉ số Sobol của E và nu lại được gán hằng số 0.048 và 0.018. Đã lập biên bản cách ly Q-002 và cung cấp công thức LP phụ thuộc nu/E chuẩn.
- [PHÁT HIỆN CÁCH LY Q-003 (C-03)] Dữ liệu 100 công trình trong `buildings_exposure_100.geojson` có khoảng cách tâm hầm sinh ngẫu nhiên nhưng ghi nhãn `observed`; đã đính chính nhãn chính thức thành `scenario_assumption` (kịch bản mô phỏng).

## 3. Bảng Kiểm kê Toàn bộ Tệp tin Đầu ra của Giai đoạn kèm Mã băm SHA-256 & Provenance

| STT | Phân khu | Tên tệp | Kích thước (Bytes) | Giá trị cơ sở (`value_basis`) | Độ tin cậy (`confidence`) | Cờ QA (`qa_flag`) | Mã băm SHA-256 |
|:---:|---|---|---:|---|---|---|---|
| 1 | `input_data` | `DANH_MUC_SAO_LUU_VA_PHAN_LOAI_DU_LIEU_DAU_VAO.md` | 14,388 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `07498dcffcecc843...` |
| 2 | `input_data` | `TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx` | 14,668 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `91302aae5f63206c...` |
| 3 | `input_data` | `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx` | 31,226 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bce723d4c9c226d4...` |
| 4 | `input_data` | `TBM_BUILDING_RISK_EXPOSURE.xlsx` | 13,322 | `scenario_assumption` | `high` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `d15cadc96ca7c6d6...` |
| 5 | `input_data` | `EVIDENCE_TRACEABILITY_AUDIT_MATRIX.xlsx` | 12,365 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `41d4342bc9aa53d3...` |
| 6 | `input_data` | `alignment_wgs84.geojson` | 1,836 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `df81e6972724b959...` |
| 7 | `input_data` | `buildings_exposure_60.geojson` | 76,370 | `scenario_assumption` | `medium_scenario_model` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `1cbe4deaa9f72c16...` |
| 8 | `input_data` | `stations_wgs84.geojson` | 1,550 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ae1330a66bd7e782...` |
| 9 | `analysis_data` | `TBM_HANOI_G2_LOGANATHAN_POULOS_3D.xlsx` | 14,881 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a18a43dc97398771...` |
| 10 | `analysis_data` | `TBM_HANOI_G2_MONTE_CARLO_SENSITIVITY.xlsx` | 32,321 | `model_assumption` | `low_synthetic_demo` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `e7069a9a2e772b4b...` |
| 11 | `analysis_data` | `TBM_HANOI_G2_SUPPLEMENT_SALTELLI_LHS_LP_SOBOL.xlsx` | 173,855 | `direct_text` | `high` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `2811ca32c6bb7dda...` |
| 12 | `analysis_data` | `SOBOL_SALTELLI_LHS_VS_STATIC_COMPARISON.csv` | 2,627 | `direct_text` | `high` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `0643492cee4b3669...` |
| 13 | `analysis_data` | `SALTELLI_LHS_10000_SAMPLES_PECK_AND_LP.csv` | 579,722 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9e329bcb41823930...` |
| 14 | `analysis_data` | `TBM_HANOI_G2_BUILDING_STRAIN_DAMAGE_100.xlsx` | 33,190 | `scenario_assumption` | `high` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `6be40143d48c50e8...` |
| 15 | `analysis_data` | `EVIDENCE_TRACEABILITY_AUDIT_MATRIX_GIAI_DOAN_2.xlsx` | 7,576 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `60a0c6fe79301982...` |
| 16 | `analysis_data` | `alignment_longitudinal_wgs84.geojson` | 1,224 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `130d4a77cbeb1fdd...` |
| 17 | `analysis_data` | `buildings_exposure_100.geojson` | 80,005 | `scenario_assumption` | `medium_scenario_model` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `811b4f4416a73ad9...` |
| 18 | `figures_tables` | `DANH_MUC_HINH_VE_300DPI_GIAI_DOAN_2.md` | 2,370 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `c063e828bb053a35...` |
| 19 | `figures_tables` | `FIG_08_Monte_Carlo_Distribution_Settlement_G2.png` | 366,829 | `model_assumption` | `low_synthetic_demo` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `5f51be1526eeaca2...` |
| 20 | `figures_tables` | `FIG_09_Global_Sensitivity_Sobol_Indices_G2.png` | 296,715 | `direct_text` | `high` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `f3c5f57df9452c1d...` |
| 21 | `figures_tables` | `FIG_09B_Saltelli_LHS_vs_Static_Sobol_Comparison.png` | 310,088 | `direct_text` | `high` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `59971343da4a9c14...` |
| 22 | `figures_tables` | `SOBOL_SALTELLI_LHS_VS_STATIC_COMPARISON.csv` | 2,627 | `direct_text` | `high` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `0643492cee4b3669...` |
| 23 | `figures_tables` | `FIG_10_Longitudinal_Settlement_Profile_TBM_Advance_G2.png` | 326,550 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `09effaa6b1e470ca...` |
| 24 | `figures_tables` | `FIG_11_3D_Settlement_Trough_Surface_G2.png` | 666,365 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `0253b1c65ba4bba7...` |
| 25 | `figures_tables` | `FIG_12_Building_Deflection_vs_Horizontal_Strain_Burland_G2.png` | 321,859 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ce587bdf589899f5...` |
| 26 | `figures_tables` | `FIG_13_Twin_Tunnel_Interaction_3D_Stress_Field_G2.png` | 425,388 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b7ba570bae9b45ff...` |
| 27 | `figures_tables` | `FIG_14_Integrated_Workflow_Stage_2_Framework.png` | 275,403 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `c24224bc991a2cd0...` |
| 28 | `web_html` | `webgis_settlement_advance_v2.html` | 71,931 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `f4f76412e6702c68...` |
| 29 | `web_html` | `HUONG_DAN_SU_DUNG_WEBGIS_V2.md` | 2,916 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `268a446d3c6fbac7...` |
| 30 | `scripts_tests` | `setup_stage_2_backup.py` | 7,883 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `973c076cd3c7c626...` |
| 31 | `scripts_tests` | `generate_stage_2_models_and_excel.py` | 53,879 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `3d6bfecd4ad62799...` |
| 32 | `scripts_tests` | `generate_stage_2_figures.py` | 21,977 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bfcaef5915c3a97b...` |
| 33 | `scripts_tests` | `build_stage_2_webgis.py` | 22,805 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `c59d5286a7f38ff2...` |
| 34 | `scripts_tests` | `build_stage_2_reports_and_dossier.py` | 50,221 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8e37372c7f58f0cb...` |
| 35 | `scripts_tests` | `update_stage_2_checksums.py` | 2,505 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9ce25bdd569d8125...` |
| 36 | `scripts_tests` | `geotechnical_and_gsa_reconciliation.py` | 33,654 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `500ada8506243261...` |
| 37 | `scripts_tests` | `test_geotechnical_and_gsa_reconciliation.py` | 3,783 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `50e8aa904fdd5e0d...` |
| 38 | `drafts_dossiers` | `BAO_CAO_DOI_SANH_VA_KIEM_CHUNG_SOBOL_SALTELLI_LHS.md` | 4,044 | `direct_text` | `high` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `bb91c726421e2b40...` |
| 39 | `drafts_dossiers` | `KE_HOACH_THUC_THI_CHI_TIET_GIAI_DOAN_2.md` | 20,050 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8e8f86f3a69d0009...` |
| 40 | `drafts_dossiers` | `MA_TRAN_PHOI_HOP_TAC_TU_VA_CONG_CU.md` | 14,145 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8a7fecbd3c23e24d...` |
| 41 | `drafts_dossiers` | `BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_2.md` | 14,213 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `1ec742ae708febfa...` |
| 42 | `drafts_dossiers` | `BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_2.docx` | 1,651,961 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d285c29c90e78b8a...` |
| 43 | `drafts_dossiers` | `BAO_CAO_TOM_TAT_NGHIEM_THU_GIAI_DOAN_2.md` | 4,914 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ebe657762c2428e7...` |
| 44 | `drafts_dossiers` | `BAO_CAO_TOM_TAT_NGHIEM_THU_GIAI_DOAN_2.docx` | 37,324 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `59a8c1fd373fcaa5...` |
| 45 | `drafts_dossiers` | `BIEN_BAN_DONG_BANG_BASELINE_GIAI_DOAN_2.md` | 3,670 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ba2a386df88d755e...` |
| 46 | `drafts_dossiers` | `BIEN_BAN_KIEM_TOAN_KHOA_HOC_GIAI_DOAN_2_GATES.md` | 4,174 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `9509f06e41be748d...` |
| 47 | `drafts_dossiers` | `BIEN_BAN_KIEM_TOAN_KHOA_HOC_GIAI_DOAN_2_GATES.docx` | 37,785 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fc7a9c73faaa178e...` |
| 48 | `drafts_dossiers` | `DANH_MUC_HO_SO_VA_CHECKSUM_SHA256_GIAI_DOAN_2.md` | 11,297 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4c2049d587a0c9d5...` |
| 49 | `drafts_dossiers` | `PHIEU_DANH_GIA_NGHIEM_THU_GIAI_DOAN_2.md` | 3,753 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `04d81fc23d4c47b6...` |
| 50 | `drafts_dossiers` | `PHIEU_DANH_GIA_NGHIEM_THU_GIAI_DOAN_2.docx` | 36,416 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a43556510907ed6e...` |
| 51 | `drafts_dossiers` | `TO_TRINH_XIN_NGHIEM_THU_GIAI_DOAN_2.md` | 3,257 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a9581e184d4985c7...` |
| 52 | `drafts_dossiers` | `TO_TRINH_XIN_NGHIEM_THU_GIAI_DOAN_2.docx` | 37,358 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `23655e676d4d2f87...` |
