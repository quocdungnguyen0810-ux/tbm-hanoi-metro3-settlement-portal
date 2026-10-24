# HỒ SƠ CÁCH LY DỮ LIỆU & DỊ BIỆT VẬT LÝ (DATA QUARANTINE REGISTER)

- **Thời gian thiết lập:** `2026-10-24 12:19:17`
- **Nguyên tắc thực thi:** Tuân thủ tuyệt đối Quy tắc An toàn Số liệu (Không tự ý xóa bỏ tệp gốc; mọi điểm dị biệt vật lý hoặc sai lệch nhãn chứng cứ đều được lập biên bản nguyên nhân và đưa vào vùng cách ly `data/quarantine/`).

## 1. Kết quả Kiểm tra Ràng buộc Logic Vật lý Tự động (Physical Plausibility Checks)

| Mã kiểm tra | Tham số / Phương trình | Giá trị khai báo | Giá trị tính lại vật lý | Đơn vị | Hợp lý vật lý | Trạng thái QA | Giải thích kỹ thuật |
|---|---|---:|---:|---|---|---|---|
| `PHYS-01` | `tunnel_geometry_z0_vs_R` | 17.8 | 3.15 | `m` | ĐẠT | `PASS` | Hợp lý vật lý: z0=17.80m > R=3.15m (tỷ số C/D=2.33). |
| `PHYS-02` | `volume_loss_ratio_VL` | 0.01 | 0.01 | `ratio` | ĐẠT | `PASS` | Hợp lý vật lý: VL=1.00% nằm trong dải vận hành EPB-TBM đất yếu [0.1%, 5.0%]. |
| `PHYS-03` | `poisson_ratio_nu` | 0.35 | 0.35 | `dimensionless` | ĐẠT | `PASS` | Hợp lý nhiệt động lực học đàn hồi: nu=0.35 thuộc (0, 0.5]. |
| `PHYS-04` | `terzaghi_1d_consolidation_settlement` | 14.1 | 140.16 | `mm` | **KHÔNG ĐẠT (CÁCH LY)** | `QUARANTINE_UNIT_FACTOR_10_ERROR` | PHÁT HIỆN LỖI HỆ SỐ 10 (C-07): Giá trị báo cáo GĐ3 (14.10 mm) sai lệch 10 lần so với tích số vật lý Δu·mv·H = 2.5×9.81×0.00045×12.7×1000 = 140.16 mm (hoặc mv phải là 0.000045 m2/kN thay vì 0.00045 m2/kN). Đưa vào vùng cách ly (Quarantine)! |

## 2. Danh mục 05 Hạng mục Đưa vào Vùng Cách ly (`QUARANTINE_REGISTER_20261024.csv`)

| Mã cách ly | Giai đoạn | Mã phát hiện | Tệp liên quan | Hiện trạng khai báo | Thực tế kiểm toán | Biện pháp xử lý & Cách ly |
|---|---|---|---|---|---|---|
| `Q-001` | `GIAI_DOAN_3` | `C-07 / PHYS-04` | `scripts/generate_stage_3_models_and_excel.py:155-165; TBM_HANOI_G3_COUPLED_HYDRO_MECHANICAL.xlsx` | S_hydro_max = 14.1 mm (Total = 33.8 mm) | S_hydro_max = 140.16 mm (Total = 159.86 mm) với Δh=2.5m, mv=0.00045 m2/kN, H=12.7m | Đưa vào vùng cách ly; không dùng con số 33.8 mm để ra quyết định thực địa cho đến khi xác minh lại hệ số nén lún thể tích mv từ thí nghiệm nén cố kết Oedometer. |
| `Q-002` | `GIAI_DOAN_2` | `C-06` | `scripts/generate_stage_2_models_and_excel.py:259-318; TBM_HANOI_G2_MONTE_CARLO_SENSITIVITY.xlsx` | Sobol S1 = [0.672, 0.145, 0.112, 0.048, 0.018] cho [VL, z0, K, E, nu] | Trong công thức Peck 2D cơ bản, E và nu không xuất hiện trực tiếp nên S1(E)=0, S1(nu)=0 trừ khi giải bằng công thức đàn hồi Loganathan-Poulos có phụ thuộc nu và g(E). | Cách ly bộ chỉ số Sobol ghi đè; gắn nhãn `QUARANTINED_PENDING_SALTELLI_RECALC`. |
| `Q-003` | `GIAI_DOAN_1_2_3` | `C-03 / H-06` | `buildings_exposure_60.geojson; buildings_exposure_100.geojson; buildings_exposure_150.geojson` | value_basis = 'observed' / 'Khảo sát thực địa' | Tọa độ và khoảng cách tới tim hầm được sinh từ hàm ngẫu nhiên có hạt giống (RNG seed) để minh họa phương pháp phân vùng rủi ro. | Giữ nguyên tệp gốc không xóa, nhưng chuyển toàn bộ phân loại chứng cứ sang `scenario_assumption` / `synthetic_demonstration`. |
| `Q-004` | `GIAI_DOAN_3` | `C-04 / C-05` | `TBM_HANOI_G3_NUMERICAL_3D_FEM_BENCHMARK.xlsx; TBM_HANOI_G3_PINN_DEEP_SURROGATE_AI.xlsx` | Kết quả mô phỏng phần tử hữu hạn 3D (85.000 phần tử HSS) và mạng nơ-ron vật lý PINN (R2=0.9994) | Dữ liệu được tạo từ hàm đóng giải tích Gaussian + nhiễu ngẫu nhiên nhỏ, chưa có file mesh/solver log hay trọng số huấn luyện PyTorch. | Cách ly khỏi các kết luận thực nghiệm; chỉ sử dụng như `synthetic_demonstration` (bản mẫu kiến trúc tích hợp). |
| `Q-005` | `GIAI_DOAN_1_2` | `H-01` | `scripts/analytical_engine.py:56-86` | Đồng nhất trực tiếp epsilon_0 = VL trong công thức Loganathan & Poulos (1998) | Tích phân số cho thấy sai lệch thể tích ~11.19% so với VL*At khi đồng nhất trực tiếp epsilon_0 = VL mà không quy đổi qua gap parameter g. | Giữ nhánh Peck (1969) làm chuẩn đã kiểm chứng (`VERIFIED_CONDITIONAL`); gắn nhãn nhánh LP là `experimental_unverified`. |
