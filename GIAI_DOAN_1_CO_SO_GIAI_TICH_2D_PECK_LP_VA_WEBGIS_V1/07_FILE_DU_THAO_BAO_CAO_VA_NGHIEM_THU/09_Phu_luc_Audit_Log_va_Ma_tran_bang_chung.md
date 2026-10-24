# CHƯƠNG 9: PHỤ LỤC, NHẬT KÝ KIỂM ĐỊNH AUDIT VÀ MA TRẬN BẰNG CHỨNG

---

## PHỤ LỤC A: BẢNG TỔNG HỢP KIỂM ĐỊNH 5 CỔNG NGHIỆM THU (AUDIT GATES 1–5)

Quy trình nghiên cứu của luận án được kiểm soát chất lượng nghiêm ngặt thông qua hệ thống **5 Cổng nghiệm thu kỹ thuật (Mandatory Audit Gates)** nhằm đảm bảo tính toàn vẹn dữ liệu, loại trừ hoàn toàn các suy đoán giả tạo và đảm bảo khả năng tái lập kết quả khoa học:

<br>

**Bảng Phụ lục A.1: Trạng thái thẩm định 5 Cổng nghiệm thu kỹ thuật**

| Cổng kiểm soát (Gate) | Tên nội dung kiểm soát | Tiêu chí nghiệm thu bắt buộc | Bằng chứng lưu trữ | Kết luận thẩm tra |
|---|---|---|---|---|
| **GATE 1** | Toàn vẹn nguồn thu thập (Source Acquisition & Extraction Integrity) | 100% các giá trị trích xuất từ tài liệu công bố phải có số trang, bảng, hình rõ ràng. Không tự suy diễn số liệu. | `01_project_inventory/WF05_GATE_1_AUDIT_REPORT.md` | **ĐẠT (PASSED)** |
| **GATE 2** | Tính hợp lý vật lý, cơ lý và không gian (Physical & Spatial QC) | Dung trọng $\gamma > 0$, mô-đun $E > 0$, chỉ số SPT $N \ge 0$. Không có mâu thuẫn cơ học đất Đệ tứ. | `09_logs/WF08_GATE_2_AUDIT_REPORT.md` | **ĐẠT (PASSED)** |
| **GATE 3** | Đóng băng dữ liệu cơ sở (Baseline Freeze & Checksums) | Tạo mã băm SHA-256 cho các tập tin tham số chuẩn hóa. Nghiêm cấm ghi đè hoặc chỉnh sửa dữ liệu gốc. | `09_logs/WF11_GATE_3_AUDIT_REPORT.md` | **ĐẠT (PASSED)** |
| **GATE 4** | Kiểm chứng giải tích và độ nhạy (Analytical Verification & GIS) | Kiểm chứng bảo toàn thể tích phễu lún Peck qua tích phân số trị ($V_s = V_{\text{loss}}$). Đối chiếu Loganathan & Poulos. | `09_logs/WF16_GATE_4_AUDIT_REPORT.md` | **ĐẠT (PASSED)** |
| **GATE 5** | Báo cáo khoa học và khả năng tái lập (Scientific Reporting) | Tách bạch hoàn toàn giữa quan sát thực địa và giả thiết mô hình. Toàn bộ bảng tính thể hiện trên Excel chuyên nghiệp. | `09_logs/WF20_FINAL_AUDIT_RELEASE.md` | **ĐẠT (PASSED)** |

---

## PHỤ LỤC B: NHẬT KÝ KIỂM TOÁN CÁC THAM SỐ GẮN CỜ AUDIT (AUDIT REGISTER)

Tất cả các tham số mang tính chất giả thiết tính toán, chuyển giao khu vực hoặc chưa có số đo hố khoan cụ thể đều được tổng hợp, gắn cờ cảnh báo và đề xuất giải pháp xử lý trong Bảng Phụ lục B.1:

<br>

**Bảng Phụ lục B.1: Nhật ký kiểm định chi tiết các tham số cần bổ sung khi thi công (Audit Register)**

| Mã Audit | Tham số kỹ thuật | Giá trị áp dụng trong mô hình | Nguồn gốc / Cơ sở xác định | Phân loại chứng cứ | Mức độ tin cậy | Đánh giá & Phản biện của Auditor | Yêu cầu hành động khi triển khai thi công |
|---|---|---|---|---|---|---|---|
| **AUDIT-01** | Đường kính khiên đào $D$ | $6.30\text{ m}$ | Báo cáo ĐTM ADB (2013), Nguyen et al. (2024) | `direct_text` | Cao (Confirmed) | Phù hợp với thông số chế tạo của khiên đào EPB Herrenknecht S-1070/1071. | Đối chiếu bản vẽ hoàn công vỏ hầm đúc sẵn thực tế. |
| **AUDIT-02** | Cự ly tim hầm đôi $d$ | $13.0\text{ m}$ | Nguyen et al. (2024); Khoảng biến thiên $12 - 15\text{ m}$ | `model_assumption` | Trung bình (Regional) | Khoảng cách tim hầm có thể thay đổi cục bộ tại đoạn gần ga và chuyển tiếp cong. | Cập nhật tim tuyến CAD chuẩn VN-2000 từ hồ sơ thi công CP03. |
| **AUDIT-03** | Hệ số $K$ tại S9–S10 | $0.50$ | Peck (1969), Mair et al. (1993) | `derived_empirical` | Khá (Literature) | Phù hợp với địa tầng cát mịn chặt vừa (GU5_a) phủ sét dẻo cứng. | Hiệu chỉnh ngược (Back-analysis) từ chuỗi mốc đo lún bề mặt. |
| **AUDIT-04** | Hệ số $K$ tại S11–S12 | $0.60$ | Clough & Schmidt (1981) | `derived_empirical` | Trung bình (Literature) | Tầng bùn sét hữu cơ dày $12.7\text{ m}$ ($N=3$) làm mở rộng phễu lún. | Bố trí dày các mặt cắt đo ngang tại phố Quốc Tử Giám. |
| **AUDIT-05** | Mực nước ngầm BH12 | $-6.0\text{ m}$ bgs | Nguyen, Kohata & Nguyen (2024, tr. 86) | `model_assumption` | Thấp (Model Input) | Là giá trị giả định của bài báo TCXD 2024, không phải số đo giếng quan trắc chuyên dụng. | Lắp đặt ống đo áp piezometer đo mực nước ngầm tự nhiên liên tục. |
| **AUDIT-06** | Mực nước ngầm S9–S10 | $-11.0\text{ m}$ bgs | Nguyen et al. (2024, tr. 13048) | `direct_text` | Khá (Range 10–12m) | Đo đạc từ giếng quan trắc khu vực ga S9 Kim Mã. | Theo dõi sự biến động mực nước ngầm theo mùa mưa lũ. |
| **AUDIT-07** | Mô hình 60 công trình | Cự ly $x_{\text{offset}} \in [-30\text{ m}; +30\text{ m}]$ | Số hóa bán giả định dọc hành lang tuyến | `scenario_assumption` | Trung bình (Representative) | Đại diện cho các dạng nhà ống 3-5 tầng móng nông và khu tập thể cũ. | Thực hiện khảo sát hiện trạng công trình trước thi công (PCS). |
| **AUDIT-08** | Dải tổn thất thể tích $V_L$ | $0.5\% - 2.0\%$ | Mair et al. (1996), Kinh nghiệm EPB | `scenario_assumption` | Cao (Industry Standard) | Bao quát đầy đủ từ điều kiện thi công lý tưởng đến sự cố đào hầm. | Cân đong thể tích đất đào và lượng vữa phụt từng ring TBM. |

---

## PHỤ LỤC C: MÃ BĂM TOÀN VẸN DỮ LIỆU (SHA-256 CHECKSUMS)

Để đảm bảo tính bất biến của cơ sở dữ liệu đã đóng băng, mã băm SHA-256 của các tập tin cốt lõi được lưu trữ công khai:

```text
7cfae8b15d2a939029a738fa093c401314ff99cb84f67d4f9bca886c99c42ee6  normalized_parameters.csv
853e32b6e1f0e4b48695029e1fa0a0db23ca7732a68c4cfb48fa88d5e7589d89  normalized_sources.csv
```

Mọi nỗ lực can thiệp hoặc sửa đổi dữ liệu thô mà không thông qua phê duyệt của Hội đồng Kiểm toán sẽ làm sai lệch mã băm và bị hệ thống tự động gắn cờ vô hiệu hóa.

---

## PHỤ LỤC D: DANH MỤC CÁC TẬP TIN DỮ LIỆU EXCEL VÀ HÌNH VẼ CHẤT LƯỢNG CAO

1. **Hệ thống 4 tập tin Excel chuyên nghiệp (`.xlsx`):**
   - [TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx](../02_du_lieu_excel_chuyen_nghiep/TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx): Cơ sở dữ liệu địa kỹ thuật, địa tầng BH12, S9–S10, kiểm tra chéo 17 hố khoan, nhật ký Audit.
   - [TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx](../02_du_lieu_excel_chuyen_nghiep/TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx): Mô hình toán giải tích sống, 21 kịch bản độ nhạy, mặt cắt lún ngang động, tiêu chuẩn Burland.
   - [TBM_BUILDING_RISK_EXPOSURE.xlsx](../02_du_lieu_excel_chuyen_nghiep/TBM_BUILDING_RISK_EXPOSURE.xlsx): Danh mục 60 công trình, phân loại rủi ro, ma trận tổn thất thể tích, biện pháp giảm thiểu.
   - [EVIDENCE_TRACEABILITY_AUDIT_MATRIX.xlsx](../02_du_lieu_excel_chuyen_nghiep/EVIDENCE_TRACEABILITY_AUDIT_MATRIX.xlsx): Ma trận truy xuất nguồn gốc, bằng chứng Gate 1–5, kiểm định tài liệu tham khảo.

2. **Hệ thống 7 hình vẽ minh họa xuất bản độ phân giải cao 300 DPI:**
   - `FIG_01_Geotechnical_Stratigraphy_BH12.png`: Cột địa tầng và chỉ tiêu cơ lý hố khoan BH12.
   - `FIG_02_Peck_vs_LoganathanPoulos_Transverse.png`: So sánh hình học phễu lún Peck vs Loganathan & Poulos.
   - `FIG_03_Twin_Tunnel_Interaction_Profiles.png`: Phân bố lún hầm đôi và sự phát triển phễu lún theo $V_L$.
   - `FIG_04_Sensitivity_Curves_Smax_Slope.png`: Đồ thị đường cong độ nhạy $S_{\max}$ và độ dốc cực đại theo $V_L$.
   - `FIG_05_Building_Risk_Zoning_Distribution.png`: Phân bố cấp độ rủi ro 60 công trình theo Burland (1995).
   - `FIG_06_Surrogate_AI_Parity_and_Residuals.png`: Đồ thị tương quan Parity và phân bố sai số phần dư của mạng AI MLP.
   - `FIG_07_Methodological_Workflow_Framework.png`: Sơ đồ khung phương pháp nghiên cứu tổng thể tích hợp.
