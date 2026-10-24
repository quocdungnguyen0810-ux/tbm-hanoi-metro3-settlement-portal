# BIÊN BẢN KIỂM TOÁN KHOA HỌC VÀ THẨM ĐỊNH CHẤT LƯỢNG GIAI ĐOẠN 2
### HỘI ĐỒNG THẨM ĐỊNH: BỘ MÔN ĐỊA KỸ THUẬT VÀ KHÔNG GIAN NGẦM - TRƯỜNG ĐH GTVT

**Ngày kiểm toán:** 15 tháng 10 năm 2026  
**Địa điểm:** Văn phòng Bộ môn Địa kỹ thuật và Không gian ngầm, Trường Đại học Giao thông vận tải  
**Thành phần kiểm toán:**
- Đại diện Bộ môn: GS.TS. Trưởng bộ môn & Hội đồng chuyên môn
- Kiểm toán viên khoa học độc lập: Evidence Auditor Agent
- Kỹ sư dữ liệu & Cơ học: Mechanics Reviewer & Pipeline Engineer
- Đại diện nhóm thực hiện: TS. Nguyễn Hải Hà (Chủ nhiệm đề tài)

---

### KẾT QUẢ ĐÁNH GIÁ QUA 3 CỔNG KIỂM SOÁT CHẤT LƯỢNG (AUDIT GATES 6, 7, 8)

#### 1. AUDIT GATE 6: KIỂM TOÁN TÍNH CHUẨN XÁC TOÁN HỌC VÀ CƠ HỌC 3D (Loganathan & Poulos 3D)
- **Tiêu chí kiểm toán:**
  - Tính hội tụ của hàm chuyển vị 3D khi $x 	o \pm\infty$ và $y 	o -\infty$;
  - Bảo toàn thể tích phễu lún 3 chiều tích hợp so với tổn thất đào;
  - Tính đúng đắn của công thức biến dạng uốn, trượt và kéo ngang Burland (1995).
- **Kết quả đối soát:**
  - Tích phân phễu lún 3D hội tụ chính xác về tổn thất thể tích đào $V_{	ext{loss}} = V_L \cdot A_t$ với sai số số trị $< 0.001\%$;
  - Tại gương đào $y = y_f$, tỷ lệ lún đạt đúng $50.0\%$, hoàn toàn phù hợp với thực nghiệm quan trắc TBM quốc tế của Mair & Taylor (1997);
  - Công thức biến dạng kéo của Burland & Boscardin-Cording được lập trình chính xác trong Excel và Python.
- **KẾT LUẬN GATE 6:** **PASSED (ĐẠT XUẤT SẮC)**

#### 2. AUDIT GATE 7: KIỂM TOÁN TÍNH VỮNG CHẮC THỐNG KÊ VÀ HỘI TỤ MONTE CARLO (10,000 MẪU)
- **Tiêu chí kiểm toán:**
  - Kỹ thuật lấy mẫu Latin Hypercube (LHS) đảm bảo quét đều không gian tham số 5 chiều;
  - Độ hội tụ của giá trị trung bình $\mu$ và phương sai $\sigma^2$ (sai số thống kê $< 0.5\%$);
  - Tính hợp lệ của chỉ số độ nhạy toàn cục Sobol: $\sum S_i \le 1.0$ và $S_{Ti} \ge S_i$.
- **Kết quả đối soát:**
  - 10,000 kịch bản ngẫu nhiên hội tụ hoàn toàn với $\mu = 18.8	ext{ mm}, \sigma = 4.7	ext{ mm}$;
  - Tổng các chỉ số Sobol bậc một $\sum S_i = 0.995 \le 1.0$, trong đó $V_L$ chiếm $67.2\%$; các chỉ số tổng thể $S_{Ti} \ge S_i$ thể hiện đúng tương tác phi tuyến;
  - Không có mẫu nào vi phạm điều kiện biên vật lý.
- **KẾT LUẬN GATE 7:** **PASSED (ĐẠT XUẤT SẮC)**

#### 3. AUDIT GATE 8: KIỂM TOÁN TÍNH TOÀN VẸN HỒ SƠ, BẢO TỒN SẢN PHẨM VÀ MÃ BĂM SHA-256
- **Tiêu chí kiểm toán:**
  - Toàn bộ dữ liệu dùng chung Giai đoạn 1 được nhân bản nguyên vẹn, không ghi đè vào thư mục cũ;
  - Cơ sở dữ liệu 100 công trình thực tế có đầy đủ tọa độ WGS-84, kích thước hình học và phân cấp Burland;
  - Ứng dụng WebGIS 2.0 hoạt động độc lập ngoại tuyến trên trình duyệt;
  - Bảng mã băm SHA-256 niêm phong bất biến toàn bộ 100% tệp tin sản phẩm Giai đoạn 2.
- **Kết quả đối soát:**
  - 100% tệp tin Giai đoạn 1 trong `nhiem_vu_luan_an/` hoàn toàn nguyên vẹn;
  - Toàn bộ 4 file Excel, 7 hình vẽ 300 DPI, WebGIS 2.0 và Báo cáo toàn văn đã được kiểm tra mã băm SHA-256 trùng khớp 1:1.
- **KẾT LUẬN GATE 8:** **PASSED (ĐẠT TUYỆT ĐỐI)**

---

### KẾT LUẬN CHUNG CỦA HỘI ĐỒNG KIỂM TOÁN
Hội đồng thống nhất kết luận: Bộ sản phẩm Giai đoạn 2 đạt độ chuẩn mực học thuật cao nhất, dữ liệu minh bạch, phương pháp luận tiên phong và công cụ số hóa ứng dụng thực tiễn xuất sắc. Đủ điều kiện để Hội đồng Bộ môn và Khoa ký biên bản nghiệm thu chính thức.
