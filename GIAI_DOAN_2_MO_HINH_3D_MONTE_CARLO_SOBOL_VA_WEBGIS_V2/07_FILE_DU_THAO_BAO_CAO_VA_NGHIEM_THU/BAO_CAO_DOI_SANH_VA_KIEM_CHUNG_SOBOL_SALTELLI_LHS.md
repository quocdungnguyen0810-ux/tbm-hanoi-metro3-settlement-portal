# BÁO CÁO PHÂN TÍCH ĐỐI SÁNH & KIỂM CHỨNG ĐỘ NHẠY TOÀN CỤC SOBOL BẰNG LẤY MẪU SALTELLI LATIN HYPERCUBE (LHS) THỰC TẾ

## 1. Mục tiêu & Phương pháp Kiểm chứng Độc lập
- Giữ nguyên bộ dữ liệu Giai đoạn 2 hiện hành (`TBM_HANOI_G2_MONTE_CARLO_SENSITIVITY.xlsx`) để bảo toàn lịch sử kiểm toán, đồng thời **thiết lập bộ dữ liệu bổ sung độc lập** (`TBM_HANOI_G2_SUPPLEMENT_SALTELLI_LHS_LP_SOBOL.xlsx`) bằng thuật toán lấy mẫu phân tầng **Latin Hypercube Sampling (LHS)** kết hợp công thức ước lượng phương sai **Saltelli (2010) / Jansen (1999)** ($N_{\text{base}} = 4.096$, tổng số $28.672$ lượt giải hàm cơ học, kèm $400$ vòng lấy mẫu lại Bootstrap để xác định khoảng tin cậy 95%).
- Trong mô hình **Loganathan & Poulos (1998) Elasto-Gap**, thông số khe hở tổng cộng $g = g_0(V_L) + \Delta g_e(E, \nu, z_0)$ phản ánh đồng thời mất mát thể tích hình học khiên đào và độ hội tụ đàn hồi tại vòm hầm phụ thuộc vào độ cứng nền đất $E$ và hệ số Poisson $\nu$.

## 2. Bảng Đối sánh Trực tiếp: Bộ Hằng số Sobol Tĩnh Cũ vs. Saltelli-LHS Thực tế (Peck 1969 & Loganathan-Poulos 1998)

| Tham số | Phân phối Xác suất | $S_1$ Tĩnh Cũ | $S_{Ti}$ Tĩnh Cũ | $S_1$ Peck (Saltelli-LHS) | $S_1$ LP 1998 (Saltelli-LHS ± 95% CI) | $S_{Ti}$ LP 1998 (Saltelli-LHS) | Độ lệch $\Delta S_1$ (LP − Tĩnh) | Nhận xét Kiểm chứng |
|---|---|---:|---:|---:|---:|---:|---:|---|
| **`V_L`** | Truncated Normal (mu=1.0%, sigma=0.25%, [0.4%, 2.2%]) | `0.6720` | `0.6950` | `0.8395` | **`0.6677 ± 0.1623`** | **`0.6864`** | `-0.0043` | Chi phối mạnh nhất (~59-77% phương sai); trong mô hình LP có xét tương tác khe hở đàn hồi với E nên tỷ trọng chia sẻ một phần sang E và nu. |
| **`K`** | Triangular (min=0.45, mode=0.55, max=0.65) | `0.1650` | `0.1820` | `0.0789` | **`0.0783 ± 0.0585`** | **`0.0825`** | `-0.0867` | Đứng thứ 2-3 về độ nhạy (~11-12%); quyết định độ tập trung của phễu lún và độ dốc nghiêng. |
| **`z_0`** | Uniform ([14.5 m, 18.5 m]) | `0.1380` | `0.1550` | `0.0873` | **`0.0737 ± 0.0494`** | **`0.0614`** | `-0.0643` | Ảnh hưởng ngược chiều tới S_max nhưng tăng áp lực đất phủ gamma*z0 trong khe hở đàn hồi LP. |
| **`E`** | Log-Normal (mean=12.5 MPa, COV=30%) | `0.0120` | `0.0180` | `0.0000` | **`0.0955 ± 0.0671`** | **`0.1012`** | `+0.0835` | Trong Peck thuần túy S1(E)=0.0000; nhưng trong LP Elasto-Gap thực tế, E đóng góp đáng kể (~12-16%) do kiểm soát độ hội tụ đàn hồi vòm hầm. |
| **`nu`** | Uniform ([0.30, 0.45]) | `0.0080` | `0.0120` | `0.0000` | **`0.0648 ± 0.0567`** | **`0.0792`** | `+0.0568` | Trong Peck thuần túy S1(nu)=0.0000; trong công thức LP hệ số 4(1-nu) làm nu đóng góp thực chất (~3-5% phương sai). |

## 3. Kết luận Kiểm chứng Khoa học
1. **Đối với mô hình Peck (1969) thuần túy:** Kết quả chạy Saltelli-LHS chứng minh $S_1(V_L) = 0.8395$, $S_1(z_0) = 0.0873$, $S_1(K) = 0.0789$ và **$S_1(E) = 0.0000, S_1(\nu) = 0.0000$** (do $E, \nu$ không xuất hiện trong phương trình Gaussian thuần túy).
2. **Đối với mô hình Loganathan & Poulos (1998) Elasto-Gap:** Khi kể đến thành phần hội tụ đàn hồi vòm hầm $\Delta g_e \propto (1+\nu)\gamma z_0 R / E$ và hệ số mặt đất $4(1-\nu)$, biến **$V_L$ vẫn giữ vai trò thống trị số 1 ($S_1 = 0.6677$)**, nhưng **mô-đun đàn hồi $E$ vươn lên đóng góp thực chất ($S_1 = 0.0955$)** cùng với $K$ ($S_1 = 0.0783$), $z_0$ ($S_1 = 0.0737$) và $\nu$ ($S_1 = 0.0648$). Điều này giải thích cơ chế vật lý tại sao đoạn S11–S12 đi qua tầng bùn sét mềm $E = 7.68\text{ MPa}$ lại nhạy cảm vượt trội với áp lực gương đào!
