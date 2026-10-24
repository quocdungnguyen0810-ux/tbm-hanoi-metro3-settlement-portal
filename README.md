# Hệ thống Quản trị, Kiểm toán Khoa học & WebGIS Dự báo Lún Hầm TBM Đoạn S9–S12 Metro Tuyến 3 Hà Nội

[![SHA-256 Verified](https://img.shields.io/badge/SHA--256_Manifest-288%2F288_Verified-success)](#)
[![Stage 2 Audit](https://img.shields.io/badge/Stage_2_Audit-52%2F52_Files_Passed-blue)](#)
[![Unit Tests](https://img.shields.io/badge/Unit_Tests-15%2F15_Passed-brightgreen)](#)

> **Mã đề tài:** `TBM_HANOI_EIA_SETTLEMENT_2027` (`T2027_TMĐK_Nguyen_Hai_Ha`)  
> **Đơn vị chủ trì:** Bộ môn Địa kỹ thuật và Không gian ngầm – Khoa Công trình – Trường Đại học Giao thông vận tải (UTC)  
> **Chủ nhiệm đề tài:** ThS. Nguyễn Hải Hà | **Thành viên:** ThS. Lê Anh Đức, KS. Trần Văn Long

---

## 1. Đường dẫn Truy cập Trực tiếp (Vercel & GitHub Pages Routes)

| Phân hệ / Ứng dụng | Đường dẫn Rút gọn (Vercel) | Đường dẫn Tệp Trực tiếp (GitHub Pages / Static) |
|---|---|---|
| **Cổng Quản trị Toàn Dự án (GĐ 0 → GĐ 4)** | `/` hoặc `/portal` | [`INDEX_PORTAL_TOAN_DU_AN.html`](./INDEX_PORTAL_TOAN_DU_AN.html) |
| **Dashboard Kiểm toán Giai đoạn 2** | `/giai-doan-2` | [`GIAI_DOAN_2.../dashboard_audit_giai_doan.html`](./GIAI_DOAN_2_MO_HINH_3D_MONTE_CARLO_SOBOL_VA_WEBGIS_V2/01_AUDIT_KE_HOACH_NHAN_SU_SKILL_CONG_CU/dashboard_audit_giai_doan.html) |
| **Ứng dụng WebGIS 2.0 (Lún 3D & Tiến gương TBM)** | `/webgis-v2` | [`GIAI_DOAN_2.../webgis_settlement_advance_v2.html`](./GIAI_DOAN_2_MO_HINH_3D_MONTE_CARLO_SOBOL_VA_WEBGIS_V2/05_FILE_HIEN_HANH_HTML_WEB/webgis_settlement_advance_v2.html) |
| **Thư viện Hình vẽ 300 DPI Giai đoạn 2** | `/thu-vien-hinh-g2` | [`GIAI_DOAN_2.../thu_vien_hinh_ve_bang_bieu.html`](./GIAI_DOAN_2_MO_HINH_3D_MONTE_CARLO_SOBOL_VA_WEBGIS_V2/04_KET_QUA_BANG_BIEU_HINH_VE_CHAT_LUONG_CAO/thu_vien_hinh_ve_bang_bieu.html) |
| **Ứng dụng WebGIS 1.0 (Giai đoạn 1 - 60 công trình)** | `/webgis-v1` | [`GIAI_DOAN_1.../webgis_settlement_map.html`](./GIAI_DOAN_1_CO_SO_GIAI_TICH_2D_PECK_LP_VA_WEBGIS_V1/05_FILE_HIEN_HANH_HTML_WEB/webgis_settlement_map.html) |
| **Ứng dụng WebGIS 3.0 Scenario Viewer (Giai đoạn 3)** | `/webgis-v3` | [`GIAI_DOAN_3.../webgis_digital_twin_tbm_v3.html`](./GIAI_DOAN_3_COUPLED_HM_3DFEM_PINN_DIGITAL_TWIN_V3/05_FILE_HIEN_HANH_HTML_WEB/webgis_digital_twin_tbm_v3.html) |
| **WebGIS StoryMap NCKH Sinh viên (Giai đoạn 4)** | `/storymap-sv` | [`GIAI_DOAN_4.../index.html`](./GIAI_DOAN_4_CHUYEN_GIAO_DAO_TAO_NCKH_SINH_VIEN/05_FILE_HIEN_HANH_HTML_WEB/index.html) |

---

## 2. Trọng tâm Học thuật & Kết quả Kiểm toán Giai đoạn 2 (`GIAI_DOAN_2`)

1. **Giải tích 3 chiều Loganathan & Poulos (1998) & Động học Tiến gương TBM (Gate 6):**
   - Tích hợp hàm lỗi tích lũy dọc trục $\mathrm{erf}\left(\frac{y - y_f}{\sqrt{2} i_y}\right)$ phản ánh chính xác 50% độ lún xuất hiện tại mặt gương đào ($y = y_f$) và tương tác hầm đôi song song ($d = 13.0\text{ m}, \Delta y_{\text{lag}} = 50\text{ m}$).
2. **Phân tích Độ nhạy Toàn cục Sobol bằng Lấy mẫu Saltelli-LHS Thực tế (Gate 7 - Khắc phục Cách ly `Q-002`):**
   - Thực thi $N_{\text{base}} = 4.096$ ($28.672$ lượt giải hàm cơ học kèm $400$ vòng Bootstrap) đối sánh giữa phương trình Peck (1969) và Loganathan & Poulos (1998) Elasto-Gap:
     - $S_1(V_L) = 0.6677 \pm 0.1623$ ($S_{Ti} = 0.6864$)
     - $S_1(E) = 0.0955 \pm 0.0671$ ($S_{Ti} = 0.1012$)
     - $S_1(K) = 0.0783 \pm 0.0585$ ($S_{Ti} = 0.0825$)
     - $S_1(z_0) = 0.0737 \pm 0.0494$ ($S_{Ti} = 0.0614$)
     - $S_1(\nu) = 0.0648 \pm 0.0567$ ($S_{Ti} = 0.0792$)
3. **Đánh giá Biến dạng Kéo 100 Công trình theo Burland (1995) & WebGIS 2.0 (Gate 8 - Nhãn `Q-003`):**
   - Phân hạng 5 cấp độ rủi ro hư hại cho 100 công trình dọc hành lang Kim Mã – Cát Linh – Quốc Tử Giám – Trần Hưng Đạo ứng với 4 kịch bản $V_L \in \{0.5\%, 1.0\%, 1.5\%, 2.0\%\}$.

---

## 3. Cấu trúc Phân kỳ 5 Giai đoạn × 7 Phân khu Chức năng

Mỗi giai đoạn từ `GIAI_DOAN_0` đến `GIAI_DOAN_4` đều được chuẩn hóa đồng nhất thành 7 phân khu:
- `01_AUDIT_KE_HOACH_NHAN_SU_SKILL_CONG_CU/`
- `02_DU_LIEU_DAU_VAO/`
- `03_DU_LIEU_PHAN_TICH/`
- `04_KET_QUA_BANG_BIEU_HINH_VE_CHAT_LUONG_CAO/`
- `05_FILE_HIEN_HANH_HTML_WEB/`
- `06_MA_NGUON_SCRIPT_VA_KIEM_THU/`
- `07_FILE_DU_THAO_BAO_CAO_VA_NGHIEM_THU/`
