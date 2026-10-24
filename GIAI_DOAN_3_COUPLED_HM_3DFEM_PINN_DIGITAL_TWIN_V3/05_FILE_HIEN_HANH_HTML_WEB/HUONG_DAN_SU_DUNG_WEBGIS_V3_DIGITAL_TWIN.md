# HƯỚNG DẪN VẬN HÀNH HỆ THỐNG DIGITAL TWIN 3.0 & WEBGIS GIÁM SÁT LÚN
### DỰ ÁN LUẬN ÁN: TƯƠNG TÁC ĐA TRƯỜNG THẤM - BIẾN DẠNG VÀ DIGITAL TWIN TBM S9–S12 METRO 3 HÀ NỘI

**Tệp tin ứng dụng:** `webgis_digital_twin_tbm_v3.html`  
**Môi trường vận hành:** Trình duyệt web hiện đại (Google Chrome, Microsoft Edge, Mozilla Firefox, Apple Safari). Không cần cài đặt web server; có thể mở trực tiếp từ tệp tin cục bộ.  

---

### I. CÁC TÍNH NĂNG CHÍNH CỦA DIGITAL TWIN 3.0
1. **Mô phỏng động thái khiên đào TBM:** Thanh trượt từ Ring 0 đến Ring 2,500 cho phép điều khiển bước tiến gương đào trong không gian 3 chiều.
2. **Cập nhật động độ lún đa trường:** Kết hợp đồng thời lún cơ học TBM và lún cố kết hạ mực nước ngầm theo thời gian.
3. **Quản lý rủi ro 150 công trình:** 150 điểm marker đổi màu trực tiếp theo 4 cấp cảnh báo sớm TARP (Xanh, Vàng, Cam, Đỏ).
4. **Bảo tồn di tích lịch sử:** Theo dõi riêng biệt Văn Miếu - Quốc Tử Giám và Chùa Phổ Giác.
5. **Biểu đồ kép trực quan:** Biểu đồ trắc ngang phễu lún đa trường cập nhật liên tục.

---
### II. QUY TRÌNH PHẢN HỒI THEO TIÊU CHUẨN TARP
- **Mức 0 (Xanh - S < 8mm):** Trạng thái bình thường, duy trì chu kỳ quan trắc định kỳ 1 lần/tuần.
- **Mức 1 (Vàng - 8 <= S < 15mm):** Trạng thái cần lưu ý, nâng tần suất đo đạc lên 2 lần/ngày, kiểm tra áp lực gương đào $P_s$.
- **Mức 2 (Cam - 15 <= S < 25mm):** Trạng thái hành động, tăng áp lực vữa chèn đuôi khiên $P_a = 2.0\text{ bar}$, giảm tốc độ đào khiên.
- **Mức 3 (Đỏ - S >= 25mm):** Trạng thái khẩn cấp, tạm dừng đào khiên, kích cọc gia cố móng và phụt vữa bù lún Polymer hóa cứng nhanh.