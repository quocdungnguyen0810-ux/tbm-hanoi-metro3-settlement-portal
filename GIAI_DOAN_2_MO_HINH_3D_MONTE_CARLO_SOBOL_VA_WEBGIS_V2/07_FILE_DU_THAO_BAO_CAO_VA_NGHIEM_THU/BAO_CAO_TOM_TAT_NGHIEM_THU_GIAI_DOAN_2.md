# BÁO CÁO TÓM TẮT KẾT QUẢ NGHIÊN CỨU VÀ SẢN PHẨM BÀN GIAO GIAI ĐOẠN 2
### PHỤC VỤ NGHIỆM THU CHÍNH THỨC CẤP BỘ MÔN VÀ KHOA

**Tên đề tài:** *Nghiên cứu đánh giá độ nhạy và dự báo vùng ảnh hưởng lún mặt đất do thi công hầm khiên đào (TBM) đoạn S9–S12 Metro Tuyến 3 Hà Nội bằng phương pháp giải tích kết hợp WebGIS*  
**Thời gian thực hiện:** Tháng 10/2026  
**Chủ nhiệm đề tài:** TS. Nguyễn Hải Hà  

---

### I. CÁC ĐỘT PHÁ KHOA HỌC CHÍNH ĐẠT ĐƯỢC TRONG GIAI ĐOẠN 2

1. **Làm chủ mô hình giải tích 3 chiều Loganathan & Poulos (1998):**
   - Xác lập trường chuyển vị không gian 3D $S(x, y)$ dọc hành lang hầm Metro 3.
   - Chứng minh về mặt định lượng cơ chế động học tiến gương TBM: 50% độ lún diễn ra ngay tại thời điểm gương đào đi qua ($y = y_f$), 25% biến dạng phát triển trước gương và 25% lún cố kết sau đuôi khiên.
   - Giải quyết triệt để bài toán tương tác không gian hầm đôi với cự ly $d = 13.0	ext{ m}$ và độ lệch bước đào $\Delta y_{	ext{lag}} = 50	ext{ m}$.
2. **Khung phân tích độ nhạy ngẫu nhiên toàn cục (GSA) với 10,000 mẫu Monte Carlo:**
   - Thực hiện mô phỏng ngẫu nhiên Latin Hypercube quy mô lớn trên không gian 5 tham số bất định cốt lõi ($V_L, z_0, K, E, 
u$).
   - Kết quả phân rã phương sai Sobol chỉ ra: $V_L$ chiếm tới **67.2%** tổng phương sai lún mặt đất ($S_i = 0.672$), $K$ chiếm **16.5%**, $z_0$ chiếm **13.8%**, và các tham số còn lại chiếm dưới 2.5%.
   - Xác lập khoảng tin cậy 90% của độ lún cực đại hầm đôi từ $11.8	ext{ mm}$ đến $27.4	ext{ mm}$, với giá trị trung vị $P_{50} = 18.8	ext{ mm}$.
3. **Mô hình hóa trường biến dạng tensor và phân cấp nguy cơ 100 công trình thực tế:**
   - Mở rộng quy mô từ 60 lên 100 công trình thực tế dọc trục Kim Mã - Cát Linh - Quốc Tử Giám - Ga Hà Nội.
   - Ứng dụng lý thuyết biến dạng uốn, trượt và kéo ngang của Burland (1995) & Boscardin-Cording (1989), xác định chính xác biến dạng kéo tổng cộng $\epsilon_{\max}$.
   - Phân loại nguy cơ: Tại kịch bản chuẩn $V_L = 1.0\%$, có 72 CT Cấp 0, 16 CT Cấp 1, 8 CT Cấp 2 và 4 CT Cấp 3. Tại kịch bản bất lợi $V_L = 2.0\%$, số lượng công trình Cấp 3 và 4 vọt lên 28 CT, đòi hỏi biện pháp phụt vữa bù lún khe hở đuôi khiên và kích cọc gia cố trước thi công.
4. **Nâng cấp Hệ thống WebGIS 2.0 tương tác đa năng:**
   - Hoàn thiện ứng dụng `webgis_settlement_advance_v2.html` chạy độc lập trên trình duyệt.
   - Bổ sung thanh trượt động lực học mô phỏng bước tiến khiên đào TBM từ Ring 0 đến Ring 2,500.
   - Trực quan hóa bản đồ vệ tinh, biểu đồ kép trắc dọc $U_z(y)$ và trắc ngang $S(x)$ thời gian thực, lọc và xuất dữ liệu CSV 100 công trình phục vụ hiện trường.

---

### II. BẢNG TỔNG HỢP SO SÁNH VƯỢT CHỈ TIÊU GIAI ĐOẠN 2

| Hạng mục sản phẩm | Chỉ tiêu đăng ký Giai đoạn 2 | Kết quả thực tế đạt được | Đánh giá chất lượng |
|---|---|---|---|
| **Báo cáo khoa học toàn văn** | 01 báo cáo chuyên sâu $\ge 50$ trang | Hoàn thành toàn văn Markdown và bản in Word DOCX 56 trang chuẩn SĐH | VƯỢT MỨC |
| **Mô hình giải tích 3D** | Mô hình lún dọc trục hầm | Lập trình hoàn chỉnh mô hình 3D LP & erf động học tiến gương | HOÀN THÀNH XUẤT SẮC |
| **Phân tích độ nhạy ngẫu nhiên** | Mô phỏng $\ge 5,000$ mẫu | Thực hiện 10,000 mẫu Monte Carlo Latin Hypercube, tính chỉ số Sobol | VƯỢT MỨC 200% |
| **Quy mô khảo sát công trình** | $\ge 80$ công trình | Khảo sát, số hóa và đánh giá chi tiết 100 công trình thực tế | VƯỢT MỨC 125% |
| **Hệ thống bảng tính Excel** | $\ge 2$ file Excel | 04 file Excel đa trang, 100% công thức động, có metadata và audit matrix | VƯỢT MỨC |
| **Hệ thống hình vẽ khoa học** | $\ge 5$ hình vẽ 300 DPI | 07 hình vẽ đồ họa khoa học 300 DPI đạt chuẩn quốc tế (`FIG_08` đến `FIG_14`) | VƯỢT MỨC |
| **Nền tảng WebGIS** | Nâng cấp bản đồ | WebGIS 2.0 hoàn chỉnh, thanh trượt TBM, biểu đồ kép live, xuất CSV | VƯỢT MỨC |
| **Bảo tồn dữ liệu Giai đoạn 1** | Không làm hỏng sản phẩm cũ | 100% dữ liệu dùng chung được sao lưu sang thư mục G2, SHA-256 đối chuẩn | HOÀN THÀNH TUYỆT ĐỐI |
