# BÁO CÁO AUDIT QUÁ TRÌNH, CỔNG KIỂM SOÁT (GATES) & KẾT QUẢ ĐẦU RA: GIAI_DOAN_3

## 1. Phán quyết Kiểm toán Độc lập tại các Cổng Kiểm soát (Audit Gates)

| Cổng Kiểm soát (Audit Gate) | Phán quyết Kiểm toán Độc lập (Reassessed Verdict) |
|---|---|
| **`GATE_9_MULTIPHYSICS_NUMERICAL_SETUP`** | RETRACTED_UNSUPPORTED -> QUARANTINED_SYNTHETIC_DEMO (Phát hiện C-04 & C-07: Đường cong FEM được tạo từ hàm giải tích Gaussian và lún cố kết Terzaghi bị sai lệch hệ số 10 [14.1 mm vs 140.16 mm]. Đã cách ly tại Q-001 và Q-004) |
| **`GATE_10_PINN_EXPOSURE_QC`** | RETRACTED_UNSUPPORTED -> QUARANTINED_SYNTHETIC_DEMO (Phát hiện C-05 & C-03: Dữ liệu PINN và 150 công trình được sinh từ hàm mũ + nhiễu RNG; đã chuyển nhãn sang `synthetic_demonstration` tại Q-003 và Q-004) |
| **`GATE_11_STAGE_3_DIGITAL_TWIN_PACKAGING`** | INTEGRITY_VERIFIED_FUNCTION_SCIENCE_UNVERIFIED (47/47 tệp khớp SHA-256; đã định danh lại WebGIS v3.0 là `WebGIS Scenario Viewer v3.0` và đồng bộ số liệu phân cấp rủi ro 50/36/25/39) |

## 2. Các Phát hiện Kiểm toán Trọng yếu (Key Audit Findings) & Xử lý Cách ly

- [PHÁT HIỆN TRỌNG YẾU C-07 -> CÁCH LY Q-001] Công thức lún cố kết trong `generate_stage_3_models_and_excel.py:155-165` với Δh=2.5m, mv=0.00045 m2/kN, H=12.7m cho kết quả vật lý 140.16 mm, nhưng báo cáo ghi 14.1 mm (sai lệch 10 lần). Đã đưa vào vùng cách ly `data/quarantine/` và hiệu chỉnh thuyết minh.
- [PHÁT HIỆN TRỌNG YẾU C-04 & C-05 -> CÁCH LY Q-004] Các tệp kết quả 3D FEM và PINN trong GĐ3 là dữ liệu minh họa sinh bằng hàm giải tích + nhiễu Gaussian, không phải xuất từ phần mềm PLAXIS/OpenSeesPy hay PyTorch autodiff. Đã gắn nhãn bắt buộc `synthetic_demonstration`.
- [PHÁT HIỆN TRỌNG YẾU C-08] Bảng thống kê trên HTML WebGIS v3.0 ghi cứng 52/44/36/18 công trình, trong khi đếm thực tế từ `buildings_exposure_150.geojson` là 50/36/25/39. Đã ghi nhận trong biên bản kiểm toán GĐ3.

## 3. Bảng Kiểm kê Toàn bộ Tệp tin Đầu ra của Giai đoạn kèm Mã băm SHA-256 & Provenance

| STT | Phân khu | Tên tệp | Kích thước (Bytes) | Giá trị cơ sở (`value_basis`) | Độ tin cậy (`confidence`) | Cờ QA (`qa_flag`) | Mã băm SHA-256 |
|:---:|---|---|---:|---|---|---|---|
| 1 | `input_data` | `DANH_MUC_SAO_LUU_VA_PHAN_LOAI_DU_LIEU_G1_G2.md` | 5,625 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `28f6de1ba7439002...` |
| 2 | `input_data` | `TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx` | 14,668 | `direct_table` | `high` | `VERIFIED_BYTE_INTEGRITY` | `91302aae5f63206c...` |
| 3 | `input_data` | `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx` | 31,226 | `derived` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bce723d4c9c226d4...` |
| 4 | `input_data` | `TBM_HANOI_G2_LOGANATHAN_POULOS_3D.xlsx` | 14,881 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a18a43dc97398771...` |
| 5 | `input_data` | `TBM_HANOI_G2_MONTE_CARLO_SENSITIVITY.xlsx` | 32,321 | `model_assumption` | `low_synthetic_demo` | `QUARANTINE_Q002_SOBOL_CONSTANT` | `e7069a9a2e772b4b...` |
| 6 | `input_data` | `TBM_HANOI_G2_BUILDING_STRAIN_DAMAGE_100.xlsx` | 33,190 | `scenario_assumption` | `high` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `6be40143d48c50e8...` |
| 7 | `input_data` | `buildings_exposure_100.geojson` | 80,005 | `scenario_assumption` | `medium_scenario_model` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `811b4f4416a73ad9...` |
| 8 | `analysis_data` | `TBM_HANOI_G3_COUPLED_HYDRO_MECHANICAL.xlsx` | 11,223 | `model_assumption` | `low_synthetic_demo` | `QUARANTINE_Q001_FACTOR_10_CHECK` | `8297b24d176ec862...` |
| 9 | `analysis_data` | `TBM_HANOI_G3_COUPLED_HM_MV_CALIBRATED.xlsx` | 10,270 | `model_assumption` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6b334f5087033ac1...` |
| 10 | `analysis_data` | `LAYER_COMPRESSIBILITY_MV_VERIFICATION.csv` | 2,922 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6a83ec6b6dd3ed42...` |
| 11 | `analysis_data` | `CONSOLIDATION_SCENARIOS_COMPARISON.csv` | 2,694 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `651b1fb75fba3be3...` |
| 12 | `analysis_data` | `TBM_HANOI_G3_NUMERICAL_3D_FEM_BENCHMARK.xlsx` | 10,686 | `model_assumption` | `low_synthetic_demo` | `SYNTHETIC_BENCHMARK_DEMO_Q004` | `3ba0343433d8dfdb...` |
| 13 | `analysis_data` | `TBM_HANOI_G3_PINN_DEEP_SURROGATE_AI.xlsx` | 11,229 | `model_assumption` | `low_synthetic_demo` | `SYNTHETIC_BENCHMARK_DEMO_Q004` | `a8cf5560933642d2...` |
| 14 | `analysis_data` | `TBM_HANOI_G3_BUILDING_RISK_EXPOSURE_150.xlsx` | 17,097 | `scenario_assumption` | `high` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `e94eaeb43ade8ad2...` |
| 15 | `analysis_data` | `EVIDENCE_TRACEABILITY_AUDIT_MATRIX_GIAI_DOAN_3.xlsx` | 9,872 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `4d775df710a70119...` |
| 16 | `analysis_data` | `alignment_complete_wgs84.geojson` | 831 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bd30125716aabc79...` |
| 17 | `analysis_data` | `buildings_exposure_150.geojson` | 88,489 | `scenario_assumption` | `medium_scenario_model` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `6bd957a7225cba9d...` |
| 18 | `analysis_data` | `groundwater_drawdown_contours.geojson` | 5,134 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6792d59a91fb71d9...` |
| 19 | `analysis_data` | `artifact_audit.json` | 44,597 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `56d45eb75f19c762...` |
| 20 | `analysis_data` | `GATE_REASSESSMENT.csv` | 4,529 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b532befce1f89335...` |
| 21 | `figures_tables` | `DANH_MUC_HINH_VE_300DPI_GIAI_DOAN_3.md` | 1,933 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `bedc553c29672df7...` |
| 22 | `figures_tables` | `FIG_15_Coupled_Hydro_Mechanical_Consolidation.png` | 367,208 | `model_assumption` | `low_synthetic_demo` | `QUARANTINE_Q001_FACTOR_10_CHECK` | `cc4d4418851a59b0...` |
| 23 | `figures_tables` | `FIG_15B_Calibrated_mv_Consolidation_Reconciliation.png` | 516,378 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `889b798301253046...` |
| 24 | `figures_tables` | `LAYER_COMPRESSIBILITY_MV_VERIFICATION.csv` | 2,922 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `6a83ec6b6dd3ed42...` |
| 25 | `figures_tables` | `CONSOLIDATION_SCENARIOS_COMPARISON.csv` | 2,694 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `651b1fb75fba3be3...` |
| 26 | `figures_tables` | `FIG_16_3D_Numerical_FEM_Stress_Strain_Field.png` | 816,363 | `model_assumption` | `low_synthetic_demo` | `SYNTHETIC_BENCHMARK_DEMO_Q004` | `4596894fc31eb34e...` |
| 27 | `figures_tables` | `FIG_17_PINN_Architecture_and_Loss_Convergence.png` | 384,378 | `model_assumption` | `low_synthetic_demo` | `SYNTHETIC_BENCHMARK_DEMO_Q004` | `f850a222fb9012e9...` |
| 28 | `figures_tables` | `FIG_18_Building_Risk_Zoning_150_Structures.png` | 269,721 | `scenario_assumption` | `high` | `RELABELED_SCENARIO_ASSUMPTION_Q003` | `e460c8230b0b8908...` |
| 29 | `figures_tables` | `FIG_19_Realtime_Digital_Twin_TARP_Protocol.png` | 173,513 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e27c824468b4223e...` |
| 30 | `figures_tables` | `FIG_20_Longitudinal_3D_Displacement_Evolution.png` | 320,544 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `0e83418ff7f5a26e...` |
| 31 | `figures_tables` | `FIG_21_Integrated_Methodological_Framework_Phase3.png` | 287,489 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `810d04d80deea183...` |
| 32 | `figures_tables` | `GATE_REASSESSMENT.csv` | 4,529 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b532befce1f89335...` |
| 33 | `web_html` | `webgis_digital_twin_tbm_v3.html` | 81,085 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `62606113e3851d71...` |
| 34 | `web_html` | `HUONG_DAN_SU_DUNG_WEBGIS_V3_DIGITAL_TWIN.md` | 1,987 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `93a048ac4ea1e6b6...` |
| 35 | `scripts_tests` | `setup_stage_3_backup.py` | 9,157 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `ca1160a6e9744380...` |
| 36 | `scripts_tests` | `generate_stage_3_models_and_excel.py` | 25,593 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `18b32739e297aecb...` |
| 37 | `scripts_tests` | `generate_stage_3_figures.py` | 15,600 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `59f191cc71356885...` |
| 38 | `scripts_tests` | `build_stage_3_webgis.py` | 19,222 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `8e5955d8c6533926...` |
| 39 | `scripts_tests` | `build_stage_3_reports_and_dossier.py` | 28,903 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `94c320742366cea4...` |
| 40 | `scripts_tests` | `audit_artifacts.py` | 7,917 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `56b8ad64f13a1a99...` |
| 41 | `scripts_tests` | `scripts__project_stage_organizer.py` | 8,460 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fac0b5761681334a...` |
| 42 | `scripts_tests` | `geotechnical_and_gsa_reconciliation.py` | 33,654 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `500ada8506243261...` |
| 43 | `scripts_tests` | `execute_reconciliation_and_updates.py` | 66,252 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `461d7a681bef70e0...` |
| 44 | `scripts_tests` | `tests__test_project_stage_organizer.py` | 3,763 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `299aa9f6e0b5b1b4...` |
| 45 | `scripts_tests` | `test_geotechnical_and_gsa_reconciliation.py` | 3,783 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `50e8aa904fdd5e0d...` |
| 46 | `drafts_dossiers` | `BAO_CAO_THAM_DINH_VA_HIEU_CHINH_MV_GIAI_DOAN_3.md` | 6,293 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `7c04e1eff2f3ce16...` |
| 47 | `drafts_dossiers` | `KE_HOACH_THUC_THI_CHI_TIET_GIAI_DOAN_3.md` | 18,866 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `dc5b1c89b264337f...` |
| 48 | `drafts_dossiers` | `MA_TRAN_PHOI_HOP_TAC_TU_VA_CONG_CU_GIAI_DOAN_3.md` | 11,094 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a92891493f61b756...` |
| 49 | `drafts_dossiers` | `BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_3.md` | 12,625 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `07faef6b8901ab34...` |
| 50 | `drafts_dossiers` | `BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_3.docx` | 2,482,309 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `b790553768bfd62b...` |
| 51 | `drafts_dossiers` | `BAO_CAO_TOM_TAT_NGHIEM_THU_GIAI_DOAN_3.md` | 1,683 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `7a169767f623d762...` |
| 52 | `drafts_dossiers` | `BAO_CAO_TOM_TAT_NGHIEM_THU_GIAI_DOAN_3.docx` | 36,680 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `2a2aac2f0ff60632...` |
| 53 | `drafts_dossiers` | `BIEN_BAN_KIEM_TOAN_KHOA_HOC_GIAI_DOAN_3_GATES.md` | 1,472 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `02507e67e5aad05c...` |
| 54 | `drafts_dossiers` | `BIEN_BAN_KIEM_TOAN_KHOA_HOC_GIAI_DOAN_3_GATES.docx` | 36,564 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `e5e9f5de1309c49d...` |
| 55 | `drafts_dossiers` | `DANH_MUC_HO_SO_VA_CHECKSUM_SHA256_GIAI_DOAN_3.md` | 9,764 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `35f78ed2121c581d...` |
| 56 | `drafts_dossiers` | `PHIEU_DANH_GIA_NGHIEM_THU_GIAI_DOAN_3.md` | 1,504 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `c5c5db82a9c7eb3b...` |
| 57 | `drafts_dossiers` | `PHIEU_DANH_GIA_NGHIEM_THU_GIAI_DOAN_3.docx` | 36,549 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `cb2ffaf795f50975...` |
| 58 | `drafts_dossiers` | `TO_TRINH_XIN_NGHIEM_THU_GIAI_DOAN_3.md` | 1,436 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `a7ace7476df30293...` |
| 59 | `drafts_dossiers` | `TO_TRINH_XIN_NGHIEM_THU_GIAI_DOAN_3.docx` | 36,534 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `fcec8f6a90981d86...` |
| 60 | `drafts_dossiers` | `AUDIT_REPORT.md` | 19,851 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `f8746947759cd3cf...` |
| 61 | `drafts_dossiers` | `README.md` | 664 | `direct_text` | `high` | `VERIFIED_BYTE_INTEGRITY` | `d127d90fccfc943c...` |
