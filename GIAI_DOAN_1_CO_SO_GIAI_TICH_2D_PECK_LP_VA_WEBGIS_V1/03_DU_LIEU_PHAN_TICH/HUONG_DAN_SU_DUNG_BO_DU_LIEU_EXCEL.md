# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG DỮ LIỆU BẢNG TÍNH EXCEL CHUYÊN NGHIỆP
## DỰ ÁN LUẬN ÁN TBM METRO TUYẾN 3 HÀ NỘI (S9–S12)

Hệ thống bảng tính bao gồm 4 tệp tin Excel chuyên nghiệp được thiết kế theo tiêu chuẩn tư vấn quốc tế (FIDIC, Eurocode 7, TCVN). 100% các bảng tính sử dụng công thức động (Excel dynamic formulas), liên kết bảng tra cứu (LOOKUP/INDEX-MATCH), có trang Metadata, Data Dictionary và cột kiểm định Audit Status bôi vàng cảnh báo.

---

### I. DANH MỤC 4 FILE EXCEL CHUYÊN NGHIỆP

#### 1. `TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx`
- **Mục tiêu:** Lưu trữ và chuẩn hóa toàn bộ cơ sở dữ liệu địa chất công trình và địa chất thủy văn đoạn S9–S12.
- **Cấu trúc Sheet:**
  - `Muc_Luc_Metadata`: Giới thiệu dự án, quy ước ký hiệu, nguồn tài liệu và lịch sử phiên bản.
  - `Dia_Tang_BH12`: Cột địa tầng chi tiết 6 lớp của hố khoan BH12 (đoạn S11–S12) theo bài báo Tạp chí Xây dựng (05/2024), nổi bật với tầng bùn sét dày 12.7m.
  - `Mat_Cat_S9_S10`: Dữ liệu 6 đơn nguyên thạch học (GU1 đến GU8) theo bài báo ETASR (2024).
  - `Thong_So_Co_Ly_Tong_Hop`: Bảng so sánh các chỉ tiêu cơ lý cốt lõi ($\gamma, e, c', \phi', E, N_{\text{SPT}}, k$).
  - `Audit_Nhat_Ky_Kiem_Dinh`: Nhật ký theo dõi tính hợp lệ của từng tham số và gắn cờ cảnh báo đối với các giá trị chuyển giao khu vực.

#### 2. `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx`
- **Mục tiêu:** Động cơ tính toán giải tích phễu lún bề mặt theo mô hình Peck (1969) và Loganathan & Poulos (1998).
- **Cấu trúc Sheet:**
  - `Gioi_Thieu_Va_Cong_Thuc`: Tổng hợp hệ phương trình toán học giải tích, định nghĩa biến số và chứng minh định luật bảo toàn thể tích phễu lún ($V_s = V_{\text{loss}}$).
  - `Bang_21_Kich_Ban_Tong_Hop`: Ma trận tính toán 21 kịch bản kết hợp giữa 3 mặt cắt kỹ thuật và 7 mức tổn thất thể tích đất ($V_L = 0.5\% \div 2.0\%$).
  - `Profile_Ngang_S9_S10`: Bảng tính chi tiết phân bố lún ngang $S(x)$ và độ nghiêng $\theta(x)$ từ $x = -35\text{ m}$ đến $+35\text{ m}$ đoạn S9–S10.
  - `Profile_Ngang_S11_S12`: Bảng tính chi tiết phân bố lún ngang qua tầng bùn sét dày đoạn S11–S12, so sánh đối sánh giữa phễu lún hầm đơn và hầm đôi.
  - `Tieu_Chuan_Hu_Hong_Burland`: Bảng tra cứu ngưỡng biến dạng giới hạn theo tiêu chuẩn Burland (1995) và Mair et al. (1996).

#### 3. `TBM_BUILDING_RISK_EXPOSURE.xlsx`
- **Mục tiêu:** Đánh giá nguy cơ biến dạng và cấp độ hư hỏng cho 60 công trình móng nông dọc hành lang tuyến.
- **Cấu trúc Sheet:**
  - `Metadata_Quy_Chuan`: Định nghĩa các cấp độ hư hỏng từ Cấp 0 (Không đáng kể) đến Cấp 5 (Sụp đổ kết cấu).
  - `Danh_Muc_60_Cong_Trinh`: Bảng kê chi tiết 60 công trình từ Km 8.400 đến Km 11.500:
    - Cột định danh: Mã công trình, Tên/địa chỉ, Lý trình Km, Đoạn tuyến, Khoảng cách lệch tim $x$.
    - Cột kết cấu: Loại nhà, Số tầng, Loại móng.
    - Cột tính toán động: Độ lún $S_v$, độ dốc góc xoay $\theta$, Cấp rủi ro tại $V_L = 1.0\%$ và $V_L = 2.0\%$.
    - Cột phân loại ưu tiên: Cảnh báo "ƯU TIÊN CAO" cho các công trình móng nông nằm trong vùng phễu lún nguy hại ($S > 15\text{ mm}$).

#### 4. `EVIDENCE_TRACEABILITY_AUDIT_MATRIX.xlsx`
- **Mục tiêu:** Đảm bảo nguyên tắc minh bạch học thuật tuyệt đối (Audit Traceability).
- **Cấu trúc Sheet:**
  - `Tong_Quan_Kiem_Toan`: Báo cáo kết quả vượt qua 5 Audit Gates.
  - `Danh_Muc_Tai_Lieu_Nguon`: Bảng tổng hợp trích dẫn gốc, mã định danh DOI/ISBN, số trang, số bảng/hình gốc và mức độ tin cậy khoa học của từng nguồn dữ liệu.

---

### II. NGUYÊN TẮC QUY ĐỊNH MÀU SẮC TRONG BẢNG TÍNH
- **Ô màu xám nhạt (`#EAECEE`):** Tiêu đề bảng biểu (Headers).
- **Ô màu xanh lá nhạt (`#D4EDDA`):** Dữ liệu đo đạc thực tế có kiểm chứng (Observed / Validated).
- **Ô màu vàng cảnh báo (`#FFF3CD`):** Giá trị giả định mô hình cần bổ sung số liệu quan trắc thực địa (Audit Pending).
- **Ô màu xanh da trời (`#D1ECF1`):** Kết quả tính toán tự động bằng công thức Excel.
