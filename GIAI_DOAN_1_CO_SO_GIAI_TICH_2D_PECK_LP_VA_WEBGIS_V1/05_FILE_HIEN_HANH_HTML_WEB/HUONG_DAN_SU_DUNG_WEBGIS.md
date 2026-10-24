# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG WEBGIS TƯƠNG TÁC GIÁM SÁT LÚN TBM
## ĐOẠN ĐI NGẦM S9–S12 METRO TUYẾN 3 HÀ NỘI

**Mục tiêu hệ thống:** Trực quan hóa số liệu địa kỹ thuật, mô hình phễu lún giải tích Peck (1969), đánh giá nguy cơ tổn hại kết cấu theo tiêu chuẩn Burland (1995) trên nền bản đồ số không gian WGS-84 cho 60 công trình móng nông dọc tuyến ngầm S9–S12 (Kim Mã - Cát Linh - Quốc Tử Giám - Ga Hà Nội).

---

### I. CẤU TRÚC THƯ MỤC WEBGIS
```
05_he_thong_webgis_tuong_tac/
├── webgis_settlement_map.html       # Ứng dụng WebGIS độc lập (chạy trực tiếp trên trình duyệt)
├── data/
│   ├── alignment_wgs84.geojson      # Bình đồ tuyến hầm đôi TBM (D=6.3m, cự ly tim 13m)
│   ├── stations_wgs84.geojson       # Tọa độ và thông số 4 ga ngầm (S9, S10, S11, S12)
│   └── buildings_exposure_60.geojson # Cơ sở dữ liệu không gian 60 công trình khảo sát
└── HUONG_DAN_SU_DUNG_WEBGIS.md      # Tài liệu hướng dẫn sử dụng
```

---

### II. CÁCH KHỞI ĐỘNG VÀ VẬN HÀNH
1. **Khởi động ứng dụng:**
   - Nhấp đúp chuột trực tiếp vào file `webgis_settlement_map.html` trên máy tính.
   - Ứng dụng tự động chạy trên mọi trình duyệt hiện đại (Google Chrome, Microsoft Edge, Firefox, Safari) mà không cần cài đặt Web Server hay phần mềm GIS cồng kềnh.
2. **Chọn lớp bản đồ nền (Basemap):**
   - Góc trên bên trái: Nhấp vào biểu tượng Layer để chuyển đổi giữa:
     - *Bản đồ Đô thị (Voyager):* Thể hiện rõ tên phố, ranh giới thửa đất.
     - *OpenStreetMap:* Bản đồ giao thông chuẩn quốc tế.
     - *Ảnh Vệ tinh (Esri World Imagery):* Quan sát mái nhà và mật độ xây dựng thực tế.
3. **Thao tác tương tác mô hình dự báo:**
   - **Thanh trượt Tổn thất Thể tích $V_L$ ($0.5\% \div 2.0\%$):** Kéo thanh trượt để quan sát phễu lún và nguy cơ công trình thay đổi tức thời (Real-time).
   - **Chọn mặt cắt địa chất:** Lựa chọn giữa S9–S10 (Kim Mã, $z_0=15\text{ m}$), S10–S11 (Cát Linh, $z_0=16.5\text{ m}$) và S11–S12 (Văn Miếu, $z_0=18.0\text{ m}$, tầng bùn sét dày $12.7\text{ m}$).
   - **Bảng chỉ số KPI:** Tự động tính toán $S_{\max}$, bề rộng phễu lún $i$, độ dốc cực đại $\theta_{\max}$ và bán kính vùng ảnh hưởng nguy hại ($S > 10\text{ mm}$).
   - **Đồ thị Phễu lún ngang:** Trực quan hóa hình học mặt cắt lún ngang $S(x)$ trong dải $\pm 35\text{ m}$.
4. **Tra cứu và kiểm tra 60 Công trình:**
   - Nhấp vào bất kỳ hình chữ nhật công trình nào trên bản đồ để mở Popup hiển thị đầy đủ: Mã công trình, Tên địa chỉ, Lý trình, Khoảng cách tim hầm, Kết cấu, Số tầng, Loại móng, Độ lún tính toán, Độ nghiêng góc xoay $\theta$, Cấp rủi ro Burland và Mức độ ưu tiên bảo vệ.
   - Nhấp vào hàng tương ứng trong bảng danh mục phía dưới sidebar để tự động zoom (FlyTo) đến vị trí công trình trên bản đồ.

---

### III. QUY CHUẨN MÀU SẮC RỦI RO (BURLAND 1995)
- **Màu Xanh lá (Cấp 0):** Không đáng kể ($S_v < 10\text{ mm}, \theta < 2.0 \times 10^{-3}$).
- **Màu Xanh lơ (Cấp 1):** Rất nhẹ ($10 \le S_v < 15\text{ mm}$).
- **Màu Vàng (Cấp 2):** Nhẹ ($15 \le S_v < 25\text{ mm}$, xuất hiện vết nứt chân chim).
- **Màu Cam (Cấp 3):** Trung bình ($25 \le S_v < 50\text{ mm}$, nứt kết cấu, cần gia cố hoặc quan trắc đặc biệt).
- **Màu Đỏ (Cấp 4):** Nghiêm trọng ($S_v \ge 50\text{ mm}$, nguy cơ mất an toàn kết cấu).
