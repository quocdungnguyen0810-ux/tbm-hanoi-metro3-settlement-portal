# 02. HỆ THỐNG NHÂN SỰ VÀ TÁC TỬ THỰC HIỆN (GENERAL CONTRACTOR MULTI-AGENT SYSTEM) — GIAI ĐOẠN 5

## 1. Tổ chức Nhóm Tác giả Khoa học (Con người)
- **Chủ nhiệm đề tài & Tác giả liên hệ (Bài VN1 & Q2):** ThS. Nguyễn Hải Hà (Bộ môn Địa kỹ thuật & Không gian ngầm, Trường ĐH GTVT).
- **Thành viên chính & Tác giả liên hệ (Bài VN2):** ThS. Lê Anh Đức (Mô phỏng số PLAXIS, tự động hóa GIS & phần tử hữu hạn).
- **Thành viên nghiên cứu:** ThS. Trần Văn Long (Xử lý dữ liệu địa chất hố khoan BH12, kiểm định thống kê Monte Carlo & Sobol).

## 2. Kiến trúc Tác tử Tổng thầu (`general_contractor`) và 07 Tác tử Chuyên gia
Hệ thống được định nghĩa chính thức trong `.agents/agents.json` (Schema v1.1) theo chuẩn `google-antigravity-sdk`:
1. **`general_contractor` (Tác tử Tổng thầu):** Điều phối DAG 5 cổng kiểm toán Gates P1–P5, quản lý trạng thái `AGENT_STATE.json` và bàn giao gói công việc.
2. **`source_harvester` (Khai thác Học thuật & OpenAlex):** Truy vấn cơ sở dữ liệu OpenAlex, bóc tách thông số thực nghiệm từ bài báo của Nguyen, Kohata & Nguyen (2024) và Phạm Tuyên Dương (2026).
3. **`mechanics_reviewer` (Kiểm toán Cơ học Đất):** Thẩm định đạo hàm mô-đun nén không nở hông $E_{\text{oed}} = 12,33\text{ MPa}$, hệ số $m_v = 8,113 \times 10^{-5}\text{ kPa}^{-1}$ và hàm cầu nối đàn-dẻo Loganathan-Poulos.
4. **`numerical_modeler` (Chuyên gia Mô phỏng Số PLAXIS & FEM):** Thực thi bộ giải phần tử hữu hạn biến dạng phẳng 2D (`PLAXIS_MC` vs. `PLAXIS_HS_DCM`) và script `plaxis_2d_s9_s12_automation.py`.
5. **`pipeline_engineer` (Kỹ sư Pipeline, Saltelli-LHS & Biểu đồ 300 DPI):** Thực thi 28.672 mẫu Saltelli-LHS, 400 Bootstrap và kết xuất 06 biểu đồ chuẩn xuất bản.
6. **`gis_analyst` (Chuyên gia WebGIS 5.0 & Fragility):** Phát triển cổng tương tác `webgis_plaxis_publication_v5.html` và tính toán biến dạng kéo Burland cho 100 công trình.
7. **`evidence_auditor` & `publication_mechanics_auditor` (Subagent Kiểm toán Độc lập):** Kiểm tra 5 trường truy xuất nguồn gốc, chạy độc lập bộ Unit Tests và kiểm tra chống đạo văn / trùng lặp chéo ($< 7,5\%$).
