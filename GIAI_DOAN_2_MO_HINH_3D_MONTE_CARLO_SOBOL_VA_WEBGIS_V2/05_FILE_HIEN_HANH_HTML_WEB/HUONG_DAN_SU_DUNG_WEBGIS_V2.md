# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG WEBGIS 2.0 TƯƠNG TÁC
### GIÁM SÁT LÚN 3D VÀ MÔ PHỎNG BƯỚC TIẾN KHIÊN ĐÀO TBM ĐOẠN S9–S12 METRO 3 HÀ NỘI

**Tên ứng dụng:** `webgis_settlement_advance_v2.html`  
**Công nghệ:** Leaflet.js, Chart.js, HTML5/CSS3, GeoJSON chuẩn WGS-84 (EPSG:4326)  
**Nguyên tắc vận hành:** Chạy độc lập trực tiếp trên mọi trình duyệt web (Chrome, Edge, Firefox), không yêu cầu cài đặt web server phức tạp.

---

### I. CÁC TÍNH NĂNG MỚI ĐỘT PHÁ CỦA PHIÊN BẢN 2.0

1. **Thanh trượt mô phỏng tiến độ khiên đào TBM (Ring 0 đến Ring 2,500):**
   - Cho phép người dùng kéo thanh trượt từ Ga S9 đến Ga S12.
   - Vị trí gương đào TBM (vòng tròn đỏ đậm) di chuyển trực tiếp trên nền bản đồ ảnh vệ tinh Esri World Imagery.
   - Hiển thị lý trình đào chính xác (Km 0+000 đến Km 3+500) và địa phận thi công tương ứng.

2. **Cơ sở dữ liệu mở rộng 100 công trình thực tế:**
   - Nâng cấp từ 60 lên 100 công trình khảo sát dọc tuyến Kim Mã, Cát Linh, Quốc Tử Giám, Văn Miếu, Trần Hưng Đạo.
   - Mỗi công trình được mã hóa màu động theo 5 cấp rủi ro Burland (1995): Xanh lục (Cấp 0), Vàng (Cấp 1), Cam (Cấp 2), Đỏ (Cấp 3), Tím (Cấp 4).

3. **Biểu đồ kép thời gian thực (Dual Live Charts):**
   - Biểu đồ 1: Trắc dọc lún động $U_z(y)$ mô tả diễn biến lún trước gương, tại gương đào (~50% lún) và sau đuôi khiên.
   - Biểu đồ 2: Trắc ngang phễu lún siêu vị hầm đôi $S(x)$ tại mặt cắt gương đào.

4. **Tra cứu, tương tác và xuất dữ liệu hiện trường:**
   - Ô tìm kiếm lọc nhanh công trình theo tên, địa chỉ hoặc cấp nguy hiểm.
   - Nhấp vào bất kỳ công trình nào trên bản đồ hoặc bảng tra cứu để phóng to và hiển thị popup chi tiết thông số kết cấu ($L, H, L/H$), độ lún $S_v$, góc nghiêng $\theta$, biến dạng kéo $\epsilon_{\max}$ và khuyến nghị giải pháp xử lý.
   - Nút **'Xuất CSV'** trích xuất toàn bộ dữ liệu 100 công trình của kịch bản đang chọn để in ấn và báo cáo.

---

### II. HƯỚNG DẪN THAO TÁC

1. Nhấp đúp chuột vào file `webgis_settlement_advance_v2.html` để mở trên trình duyệt.
2. Tại góc trên bên trái, chọn kịch bản tổn thất thể tích $V_L$ ($0.5\%, 1.0\%, 1.5\%, 2.0\%$). Quan sát sự đổi màu của 100 công trình trên bản đồ và sự thay đổi của bảng thống kê rủi ro.
3. Kéo thanh trượt 'Tiến độ đào TBM' để theo dõi hành trình của máy đào và tương tác không gian với các công trình lân cận.
