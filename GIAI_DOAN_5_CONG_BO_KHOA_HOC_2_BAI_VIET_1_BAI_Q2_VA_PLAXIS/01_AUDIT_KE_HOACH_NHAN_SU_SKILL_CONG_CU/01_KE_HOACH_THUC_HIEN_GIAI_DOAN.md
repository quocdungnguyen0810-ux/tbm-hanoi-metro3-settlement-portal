# 01. KẾ HOẠCH THỰC HIỆN GIAI ĐOẠN 5: CÔNG BỐ KHOA HỌC (02 BÀI BÁO TIẾNG VIỆT, 01 BÀI BÁO QUỐC TẾ Q2) & ĐỐI SÁNH PHẦN MỀM PLAXIS

- **Mã giai đoạn:** `GIAI_DOAN_5_CONG_BO_KHOA_HOC_2_BAI_VIET_1_BAI_Q2_VA_PLAXIS`
- **Cơ quan chủ trì:** Bộ môn Địa kỹ thuật và Không gian ngầm – Khoa Công trình – Trường Đại học Giao thông vận tải (UTC)
- **Trạng thái nghiệm thu:** `HOÀN THÀNH 100% — ĐÃ KIỂM ĐỊNH GATES P1–P5 & ĐỒNG BỘ GITHUB PORTAL`

---

## 1. Mục tiêu Khoa học & Sản phẩm Đầu ra Bắt buộc

1. **Đối sánh định lượng với phần mềm PLAXIS (2D Mohr-Coulomb vs. Hardening Soil & DCM + 3D FEM):**
   - Lập mô hình 11 lớp địa chất chuẩn tại 02 mặt cắt đặc trưng: S9–S10 (Kim Mã – Cát Linh, $z_0 = 15,0\text{ m}$) và S11–S12 (Hố khoan BH12, Văn Miếu – Ga Hà Nội, $z_0 = 18,0\text{ m}$).
   - Chứng minh cơ học tại sao mô hình Mohr-Coulomb (`PLAXIS_MC`) làm phễu lún bè rộng giả tạo ($i_x = 12,50\text{ m}$) và đánh giá thấp độ lún cực đại ($S_{\max} = 9,39\text{ mm}$ tại $V_L = 1,0\%$), trong khi mô hình Hardening Soil kết hợp điều kiện biên hội tụ không đồng đều (`PLAXIS_HS_DCM`, $E_{ur} = 3 E_{50}$) hội tụ sát với lời giải giải tích Loganathan & Poulos (1998) ($R^2 = 0,9465$) và mô phỏng 3D FEM Midas GTS NX ($43,09\text{ mm}$, sai khác $< 4,4\%$).
2. **Hoàn thiện trọn gói 03 Bản thảo Bài báo Khoa học (Độ trùng lặp chéo $< 7,5\%$):**
   - **Bài báo Tiếng Việt số 1 (*Tạp chí Khoa học Giao thông vận tải - TCSJ*):** Dự báo phễu lún ngắn hạn và dài hạn (chuẩn hóa $m_v = 8,113 \times 10^{-5}\text{ kPa}^{-1}$ tại BH12) kết hợp WebGIS 2.0 TARP.
   - **Bài báo Tiếng Việt số 2 (*Tạp chí Xây dựng - TCXD*):** Đối sánh PLAXIS (MC vs. HS-DCM) với lời giải giải tích trong đánh giá biến dạng kéo và phân cấp hư hại 100 công trình theo Burland (1995).
   - **Bài báo Quốc tế Q2 (*Geotechnical and Geological Engineering*, Springer Nature, OpenAlex ID `S202628778`):** Khắc phục "điểm mù độ cứng" của phương trình Gaussian trong phân tích độ nhạy toàn cục Sobol (28.672 mẫu Saltelli-LHS, 400 Bootstrap) và xây dựng họ đường cong xác suất tổn thương Fragility Curves.
