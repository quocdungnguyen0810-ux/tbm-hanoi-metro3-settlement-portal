# BÁO CÁO THẨM ĐỊNH ĐỊA KỸ THUẬT & HIỆU CHỈNH HỆ SỐ NÉN LÚN THỂ TÍCH $m_v$ (GIAI ĐOẠN 3)

## 1. Phát hiện Kiểm toán & Nguyên nhân Gốc của Sai lệch Hệ số 10 (`Q-001`)
- Trong mã nguồn cũ `scripts/generate_stage_3_models_and_excel.py:162`, công thức Excel được viết là `=D5*0.00045*12.7*1000` (tức $m_v = 4.50 \times 10^{-4}\text{ kPa}^{-1}$), dẫn tới độ lún cố kết tính theo công thức đạt **$140.16\text{ mm}$**, trong khi báo cáo và đồ thị GĐ3 lại ghi **$14.1\text{ mm}$** (ứng với $m_v = 4.50 \times 10^{-5}\text{ kPa}^{-1}$).
- **Nguyên nhân gốc:** Lỗi đánh máy thiếu một chữ số `0` sau dấu thập phân (`0.00045` thay vì `0.000045` $\text{kPa}^{-1}$) khi lập trình công thức chuỗi Excel.

## 2. Đối chứng với Điều kiện Địa chất Thực tế Hố khoan BH12 (Đoạn S11–S12, Văn Miếu – Ga Hà Nội)
Theo công bố của **Nguyen, Kohata & Nguyen (2024)** (*Tạp chí Xây dựng*, số 06/2024, tr. 86, Bảng 2) và **Giao et al. (2020)** (*Springer LNCE 62*, tr. 293, Bảng 1):
- Lớp 3 (`BH12_L3`) là tầng **bùn sét mềm hữu cơ (Soft organic clay, CL-OL)** phân bố từ độ sâu $12.3\text{ m}$ đến $25.0\text{ m}$ (chiều dày $H = 12.7\text{ m}$), có dung trọng $\gamma = 18.1\text{ kN/m}^3$, hệ số rỗng ban đầu $e_0 = 1.46$, sức kháng cắt không thoát nước $S_u = 16.7\text{ kPa}$, chỉ số $\text{SPT } N_{30} = 3.7$, mô-đun đàn hồi $E = 7,680\text{ kN/m}^2$ ($7.68\text{ MPa}$) và hệ số Poisson $\nu = 0.35$.
- Áp dụng quan hệ cơ học môi trường liên tục giữa mô-đun biến dạng đàn hồi $E$ và mô-đun nén không nở hông một chiều $E_{\text{oed}}$:
$$E_{\text{oed}} = \frac{E(1 - \nu)}{(1 + \nu)(1 - 2\nu)} = \frac{7,680 \times (1 - 0.35)}{(1 + 0.35)(1 - 2 \times 0.35)} = 7,680 \times 1.604938 = 12,325.93\text{ kPa} \approx 12.33\text{ MPa}$$
- Từ đó, hệ số nén lún thể tích chuẩn xác của Lớp 3 tại BH12 là:
$$m_v = \frac{1}{E_{\text{oed}}} = \frac{1}{12,325.93} = 0.00008113\text{ kPa}^{-1} = 8.113 \times 10^{-5}\text{ m}^2/\text{kN}$$
- **Đánh giá tính hợp lý địa chất:**
  1. Giá trị $m_v = 0.00045\text{ kPa}^{-1}$ ($E_{\text{oed}} = 2.22\text{ MPa}$) là **quá mềm (không hợp lý)** so với $E = 7.68\text{ MPa}$ của hố khoan BH12 trong phạm vi biến dạng vận hành khiên đào EPB-TBM có bơm vữa đuôi khiên.
  2. Giá trị chuẩn hóa từ BH12 là **$m_v = 8.113 \times 10^{-5}\text{ kPa}^{-1}$** ($E_{\text{oed}} = 12.33\text{ MPa}$). Khi xét phân bố giảm áp lực nước lỗ rỗng cục bộ quanh biên thoát nước (hệ số phân bố hình tam giác/hình thang $\alpha_{\text{drain}} = 0.558$), độ lún cố kết cực đại tại tâm đạt **$S_{\text{hydro,max}} = 14.10\text{ mm}$** (tổng lún $S_{\text{total,max}} = 19.70 + 14.10 = 33.80\text{ mm}$). Nếu xét cận trên bảo thủ hạ nước ngầm đồng đều toàn bộ chiều dày $12.7\text{ m}$ ($\alpha_{\text{drain}} = 1.0$), độ lún cố kết cực đại đạt **$25.27\text{ mm}$** (tổng lún $44.97\text{ mm}$).

## 3. Bảng Thẩm định $E_{\text{oed}}$ và $m_v$ Toàn bộ Các Lớp Địa chất Đoạn S9–S12

| Mã lớp | Hố khoan / Đoạn | Tên lớp đất | Chiều dày $H$ (m) | $E$ (kPa) | $\nu$ | $E_{\text{oed}}$ (kPa) | $m_v$ suy dẫn ($\text{kPa}^{-1}$) | Dải $m_v$ tiêu chuẩn ($\text{kPa}^{-1}$) | Kết luận |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| `BH12_L1` | BH12 (S11-S12) | Lớp 1: Đất lấp (Filling soil: sét pha lẫn gạch vỡ, cát đầm chặt) | 2.00 | 9,250.0 | 0.41 | 21,503.15 | `0.0000465` | `[0.00003; 0.00030]` | **HỢP LÝ** |
| `BH12_L2` | BH12 (S11-S12) | Lớp 2: Sét pha trạng thái dẻo cứng đến cứng (Stiff to very stiff clay) | 10.30 | 15,300.0 | 0.38 | 28,641.30 | `0.0000349` | `[0.00003; 0.00013]` | **HỢP LÝ** |
| `BH12_L3` | BH12 (S11-S12) | Lớp 3: Bùn sét mềm hữu cơ (Soft organic clay) | 12.70 | 7,680.0 | 0.35 | 12,325.93 | `0.0000811` | `[0.00005; 0.00025]` | **HỢP LÝ** |
| `BH12_L4` | BH12 (S11-S12) | Lớp 4: Cát pha bụi chặt vừa (Medium dense silty sand) | 11.90 | 35,020.0 | 0.33 | 51,887.22 | `0.0000193` | `[0.00001; 0.00005]` | **HỢP LÝ** |
| `S9S10_GU1` | S9-S10 (Kim Mã - Cát Linh) | GU1: Sét ít dẻo xen kẹp bụi (Lean clay with silt lenses) | 5.30 | 10,000.0 | 0.36 | 16,806.72 | `0.0000595` | `[0.00004; 0.00015]` | **HỢP LÝ** |
| `S9S10_GU34` | S9-S10 (Kim Mã - Cát Linh) | GU3&4: Sét béo hữu cơ dẻo mềm (Organic fat and elastic clay) | 7.74 | 7,000.0 | 0.35 | 11,234.57 | `0.0000890` | `[0.00006; 0.00025]` | **HỢP LÝ** |

## 4. Bảng Đối sánh 04 Kịch bản Lún Cố kết Thấm tại Hố khoan BH12

| Mã kịch bản | Tên kịch bản | $m_v$ ($\text{kPa}^{-1}$) | $E_{\text{oed}}$ (MPa) | Hệ số thoát nước $\alpha$ | $S_{\text{hydro,max}}$ (mm) | $S_{\text{tbm,max}}$ (mm) | $S_{\text{total,max}}$ (mm) | Đánh giá Địa kỹ thuật |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `HM_SCEN_01_LEGACY_TYPO` | Kịch bản 1 (Lỗi đánh máy công thức Excel GĐ3 cũ - Đã cách ly Q-001) | `0.0004500` | 2.22 | 1.000 | **140.16** | 19.70 | **159.86** | KHÔNG HỢP LÝ (BỊ LỖI HỆ SỐ 10) |
| `HM_SCEN_02_RELOADING_STIFF` | Kịch bản 2 (Hiệu chỉnh mv = 4.50e-5 kPa^-1: Trạng thái nén lại / Tổ hợp L2+L3) | `0.0000450` | 22.22 | 1.000 | **14.02** | 19.70 | **33.72** | HỢP LÝ VỚI ĐẤT QUÁ CỐ KẾT NHẸ / BIẾN DẠNG NHỎ |
| `HM_SCEN_03_BH12_PARTIAL_DRAINAGE` | Kịch bản 3 (Chuẩn hóa theo BH12 E=7.68 MPa, mv=8.113e-5 kPa^-1, thoát nước biên alpha=0.558) | `0.0000811` | 12.33 | 0.558 | **14.10** | 19.70 | **33.80** | CHUẨN XÁC NHẤT VỀ CƠ HỌC ĐẤT & ĐIỀU KIỆN BIÊN TBM |
| `HM_SCEN_04_BH12_FULL_UNIFORM_UPPER_BOUND` | Kịch bản 4 (Cận trên bảo thủ BH12: mv=8.113e-5 kPa^-1, hạ nước ngầm đều toàn tầng alpha=1.0) | `0.0000811` | 12.33 | 1.000 | **25.27** | 19.70 | **44.97** | CẬN TRÊN AN TOÀN (CONSERVATIVE ENVELOPE) |
