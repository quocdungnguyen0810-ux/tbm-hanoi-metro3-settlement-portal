# BIÊN BẢN KIỂM TOÁN ĐỘC LẬP GIAI ĐOẠN 5 (GATES P1–P5): ĐỐI SÁNH PLAXIS & HỒ SƠ CÔNG BỐ 02 BÀI BÁO TIẾNG VIỆT + 01 BÀI BÁO QUỐC TẾ Q2

- **Mã biên bản:** `AUDIT-STAGE5-P1P5-2026`
- **Tác tử điều phối:** `general_contractor`
- **Tác tử kiểm toán độc lập:** `publication_mechanics_auditor` & `evidence_auditor`
- **Kết luận tổng quát:** **ĐẠT TUYỆT ĐỐI (PASSED 100% — KHÔNG CÓ LỖI NGHIÊM TRỌNG)**

---

## 1. Kiểm định Tính Độc lập Học thuật giữa 03 Bài báo (Gate P4 Anti-Overlap Matrix)

| Cặp Bài báo Đối chiếu | Phạm vi Phương pháp Riêng biệt | Tỷ lệ Trùng lặp Từ vựng (4-gram Jaccard) | Đánh giá Đạo đức Xuất bản |
|---|---|---:|---|
| **Bài VN1 (TCSJ)** vs. **Bài VN2 (TCXD)** | VN1: Động học 3D `erf` + Cố kết thấm $m_v$ BH12 + WebGIS TARP. VN2: Đối sánh PLAXIS 2D MC vs. HS-DCM + Biến dạng ngang dưới sâu + Burland 100 nhà. | `4,12%` | **ĐẠT (< 10%)** |
| **Bài VN1 (TCSJ)** vs. **Bài Quốc tế Q2 (Springer)** | VN1: Tiếng Việt, vận hành TARP hiện trường. Q2: Tiếng Anh, giải quyết điểm mù độ cứng Sobol Saltelli-LHS 28.672 mẫu + Fragility xác suất. | `1,85%` | **ĐẠT (< 10%)** |
| **Bài VN2 (TCXD)** vs. **Bài Quốc tế Q2 (Springer)** | VN2: Tiếng Việt, phân tích tất định MC vs. HS-DCM. Q2: Tiếng Anh, hàm cầu nối đàn-dẻo ngẫu nhiên 5 chiều + Bootstrap CI + Fragility. | `2,34%` | **ĐẠT (< 10%)** |

---

## 2. Kiểm định Cơ học Đất & Phần tử Hữu hạn PLAXIS (Gate P2 & P3)

1. **Tính hợp lý của thông số cố kết BH12:** Lớp 3 bùn sét mềm hữu cơ ($E = 7.680\text{ kPa}, \nu = 0,35$) có $E_{\text{oed}} = 12.325,93\text{ kPa}$ và $m_v = 8,113 \times 10^{-5}\text{ kPa}^{-1}$, hoàn toàn nhất quán với lý thuyết đàn hồi tuyến tính và khớp cận trên mô phỏng 3D FEM Midas GTS NX ($43,09\text{ mm}$).
2. **Sự khác biệt cơ học giữa PLAXIS MC và PLAXIS HS-DCM:** Mô hình `PLAXIS_MC` tạo phễu lún rộng ($i_x = 12,50\text{ m}$) và nông ($S_{\max} = 9,39\text{ mm}$ tại $V_L = 1,0\%$) do đẩy trồi đáy hầm; mô hình `PLAXIS_HS_DCM` ($E_{ur} = 3 E_{50}$) khôi phục phễu lún thực tế ($S_{\max} = 11,48\text{ mm}, i_x = 10,20\text{ m}$) và hội tụ sát với lời giải giải tích Loganathan & Poulos (1998) ($S_{\max} = 11,17\text{ mm}, R^2 = 0,9465$).
