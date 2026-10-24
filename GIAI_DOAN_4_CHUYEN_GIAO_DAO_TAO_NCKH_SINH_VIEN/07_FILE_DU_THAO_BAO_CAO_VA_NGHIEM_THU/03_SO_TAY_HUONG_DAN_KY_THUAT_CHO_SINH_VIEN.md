# SỔ TAY HƯỚNG DẪN KỸ THUẬT VÀ CÔNG NGHỆ BẢN ĐỒ SỐ
## "CẦM TAY CHỈ VIỆC" CHO SINH VIÊN THỰC HIỆN ĐỀ TÀI WEBGIS & STORYMAP
### ĐỀ TÀI: XÂY DỰNG BẢN ĐỒ SỐ TƯƠNG TÁC (WEBGIS/STORYMAP) VÙNG ẢNH HƯỞNG HẦM METRO HÀ NỘI

---

Chào các em sinh viên đam mê công nghệ và bản đồ!  
Đừng lo lắng nếu các em chưa từng lập trình web hay chưa từng dùng phần mềm GIS chuyên sâu. Sổ tay này được biên soạn theo phương châm **"Học qua dự án thực tế (Project-Based Learning)"**, cung cấp từng bước chỉ dẫn tường minh, kèm theo các mẫu code và tài nguyên sẵn có để các em hoàn toàn làm chủ sản phẩm của mình chỉ sau 1–2 tuần.

---

### PHẦN 1: HƯỚNG DẪN XỬ LÝ VÀ CHUẨN HÓA DỮ LIỆU BẢN ĐỒ BẰNG QGIS

QGIS là phần mềm Hệ thống Thông tin Địa lý mã nguồn mở, hoàn toàn miễn phí và cực kỳ mạnh mẽ.

#### 1.1. Cài đặt và thiết lập hệ tọa độ
1. Tải và cài đặt phần mềm QGIS bản mới nhất tại: [qgis.org](https://qgis.org).
2. Khi mở QGIS, kiểm tra góc dưới bên phải màn hình: Hệ tọa độ mặc định của dự án nên để là `EPSG:4326 - WGS 84` hoặc `EPSG:3857 - WGS 84 / Pseudo-Mercator` (đây là hệ tọa độ chuẩn hiển thị trên bản đồ web toàn cầu).

#### 1.2. Nhập tọa độ tim hầm và vị trí ga từ bảng số liệu T2027
1. Giảng viên sẽ cung cấp bảng tọa độ các ga ngầm S9, S10, S11, S12 và các đỉnh tim tuyến hầm dạng bảng Excel (`.csv`).
2. Trong QGIS, vào menu `Layer` $\to$ `Add Layer` $\to$ `Add Delimited Text Layer`:
   - Chọn file `.csv`.
   - Mục **X field**: chọn cột Kinh độ (Longitude, ví dụ: $105.819...$).
   - Mục **Y field**: chọn cột Vĩ độ (Latitude, ví dụ: $21.031...$).
   - Bấm **Add**. Vị trí các ga và điểm tim hầm sẽ hiện ngay trên màn hình.

#### 1.3. Nối thành đường tim hầm (Line) và tạo các vùng đệm lún (Buffer Zones)
1. Dùng công cụ `Points to Path` trong QGIS để nối các điểm thành đường tim tuyến hầm đôi.
2. Để tạo các vùng dự báo ảnh hưởng lún theo mô hình Peck:
   - Vào menu `Vector` $\to$ `Geoprocessing Tools` $\to$ `Buffer`.
   - **Tạo Vùng 1 (15m - Vùng lún lớn/Giám sát đặc biệt):** Đặt `Distance = 15 meters`. Bấm Run. Đổi tên layer thành `Zone_15m_DacBiet`.
   - **Tạo Vùng 2 (35m - Vùng phễu lún ảnh hưởng chính):** Lặp lại với `Distance = 35 meters`. Đổi tên layer thành `Zone_35m_AnhHuong`.
   - **Tạo Vùng 3 (50m - Vùng đệm mở rộng an toàn):** Lặp lại với `Distance = 50 meters`. Đổi tên layer thành `Zone_50m_DemMoRong`.
3. **Xuất ra định dạng web GeoJSON:**
   - Chuột phải vào từng lớp $\to$ chọn `Export` $\to$ `Save Features As...`.
   - Mục Format: chọn `GeoJSON`.
   - Mục CRS: chọn `EPSG:4326 - WGS 84`.
   - Bấm OK để lưu các file: `stations.geojson`, `metro_line.geojson`, `buffer_zones.geojson`.

---

### PHẦN 2: HƯỚNG DẪN TRIỂN KHAI PHƯƠNG ÁN NO-CODE (DÀNH CHO NGƯỜI THÍCH ĐỒ HỌA, KHÔNG CẦN VIẾT CODE)

Nếu các em muốn tập trung vào đồ họa và giao diện kể chuyện mà không cần động đến một dòng mã nào, hai nền tảng sau là lựa chọn hoàn hảo:

#### 2.1. Nền tảng Google My Maps (Dễ nhất - Hoàn thành trong 30 phút)
1. Đăng nhập tài khoản Google, truy cập: [google.com/mymaps](https://www.google.com/mymaps).
2. Bấm nút **"Tạo bản đồ mới"**. Đặt tên: *"Bản đồ Giám sát Vùng ảnh hưởng Tuyến Metro số 3 Hà Nội"*.
3. Thêm các lớp (Layers):
   - Bấm **"Nhập"** (Import) $\to$ chọn file `.kml` xuất từ QGIS.
   - Lớp 1: *Hướng tuyến hầm ngầm & 4 Ga (S9, S10, S11, S12)*.
   - Lớp 2: *Vùng giám sát đặc biệt (15m)* $\to$ Đặt màu tô Đỏ cam trong suốt (Transparency 40%).
   - Lớp 3: *Vùng ảnh hưởng lún (35m)* $\to$ Đặt màu tô Vàng chanh trong suốt.
   - Lớp 4: *Vùng đệm quan sát (50m)* $\to$ Đặt màu tô Xanh lá cây nhạt.
4. Bấm vào từng trạm ga để thêm ảnh thực tế thi công, thông tin độ sâu đào và thời gian dự kiến máy TBM đi qua.
5. Bấm nút **"Chia sẻ"** $\to$ Bật chế độ "Bất kỳ ai có đường liên kết đều có thể xem". Nhúng bản đồ này vào website hoặc chia sẻ link cho người dân.

#### 2.2. Nền tảng ArcGIS Online StoryMaps (Chuyên nghiệp chuẩn quốc tế)
1. Đăng ký tài khoản ArcGIS Public miễn phí tại [storymaps.arcgis.com](https://storymaps.arcgis.com).
2. Tạo câu chuyện mới (**Create story**), chọn mẫu **Sidecar** hoặc **Guided Tour**.
3. Tải các file GeoJSON hoặc vẽ trực tiếp các điểm ga và tuyến hầm trên nền bản đồ vệ tinh ESRI độ phân giải cao.
4. Nhúng hình ảnh máy TBM, đồ họa infographic mặt cắt địa chất và video mô phỏng 3D.
5. Thiết lập tính năng cuộn trang (Scrollytelling): Khi người đọc cuộn chuột đến đâu, bản đồ tự động lướt và phóng to đến ga đó kèm lời thuyết minh khoa học.

---

### PHẦN 3: HƯỚNG DẪN TRIỂN KHAI PHƯƠNG ÁN LOW-CODE (WEBGIS LEAFLET & BOOTSTRAP - SẢN PHẨM CỐT LÕI)

Đây là phương án giúp các em ghi điểm tuyệt đối trước Hội đồng chấm NCKHSV vì có sản phẩm ứng dụng công nghệ độc lập, chạy cực nhẹ và không phụ thuộc vào nền tảng trả phí.

#### 3.1. Cấu trúc thư mục của dự án WebGIS
Các em tạo thư mục dự án gồm các file:
```
webgis_project/
│── index.html              <- Giao diện trang web chính
│── css/
│   └── style.css           <- Tùy chỉnh màu sắc, thanh điều khiển
│── js/
│   ├── main.js             <- Khởi tạo bản đồ Leaflet, tải dữ liệu
│   └── lookup.js           <- Tính năng tra cứu khoảng cách nhà dân
│── data/
│   ├── stations.geojson    <- Dữ liệu 4 ga ngầm
│   ├── metro_line.geojson  <- Dữ liệu tim hầm
│   └── buffer_zones.geojson<- Dữ liệu 3 dải đệm lún
└── images/                 <- Logo, ảnh máy TBM, infographic
```

#### 3.2. Đoạn mã HTML mẫu tích hợp Leaflet và tìm kiếm địa chỉ
Trong file `index.html`:
```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bản đồ Số Tuyến Metro 3 Hà Nội - Tra cứu vùng lún</title>
  <!-- Thư viện Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <!-- Bootstrap 5 CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <style>
    #map { height: calc(100vh - 60px); width: 100%; }
    .search-panel { position: absolute; top: 75px; left: 15px; z-index: 1000; width: 340px; }
    .legend-box { position: absolute; bottom: 25px; right: 15px; z-index: 1000; background: white; padding: 12px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }
  </style>
</head>
<body>
  <!-- Thanh điều hướng Header -->
  <nav class="navbar navbar-dark bg-primary px-3">
    <a class="navbar-brand fw-bold" href="#">🚇 METRO LINE 3 HÀ NỘI - BẢN ĐỒ THEO DÕI AN TOÀN ĐÀO HẦM</a>
    <button class="btn btn-outline-light btn-sm" onclick="showFeedbackModal()">Gửi phản ánh nứt lún</button>
  </nav>

  <!-- Khung tra cứu vị trí nhà dân -->
  <div class="search-panel bg-white p-3 rounded shadow">
    <h6 class="fw-bold text-primary mb-2">🔍 Tra cứu nhà bạn có an toàn?</h6>
    <div class="input-group mb-2">
      <input type="text" id="addressInput" class="form-control" placeholder="Nhập địa chỉ (vd: 12 Kim Mã)...">
      <button class="btn btn-primary" onclick="searchAddress()">Tìm</button>
    </div>
    <button class="btn btn-sm btn-outline-success w-100" onclick="locateUser()">📍 Dùng vị trí hiện tại của tôi</button>
    <div id="resultBox" class="mt-2 text-muted small"></div>
  </div>

  <!-- Bản đồ Leaflet -->
  <div id="map"></div>

  <!-- Thư viện JavaScript -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://unpkg.com/@turf/turf@6/turf.min.js"></script>
  <script src="js/main.js"></script>
</body>
</html>
```

#### 3.3. Thuật toán kiểm tra vị trí nhà dân (Lookup Algorithm)
Khi người dùng bấm vào một vị trí trên bản đồ hoặc tìm kiếm địa chỉ, hàm JavaScript sẽ đo khoảng cách vuông góc từ điểm đó đến đường tim hầm:
```javascript
// Đo khoảng cách từ tọa độ nhà người dân (userPoint) đến đường tim hầm (metroLine)
function checkHouseSafety(userLat, userLng) {
    var pt = turf.point([userLng, userLat]);
    var distanceInMeters = turf.pointToLineDistance(pt, metroLineGeoJSON, {units: 'meters'});
    
    var statusText = "";
    var alertClass = "";
    
    if (distanceInMeters <= 15) {
        statusText = "⚠️ NHÀ BẠN NẰM TRONG VÙNG GIÁM SÁT ĐẶC BIỆT (<15m tính từ tim hầm). " +
                     "Độ lún dự báo có thể nhận thấy. Dự án đã lắp đặt mốc quan trắc và có bảo hiểm công trình 100%.";
        alertClass = "alert-danger";
    } else if (distanceInMeters <= 35) {
        statusText = "🟡 NHÀ BẠN NẰM TRONG VÙNG ẢNH HƯỞNG PHỄU LÚN (15m - 35m). " +
                     "Độ lún rất nhỏ, hầu như không ảnh hưởng kết cấu móng. Cần quan sát vết nứt sơn tường định kỳ.";
        alertClass = "alert-warning";
    } else if (distanceInMeters <= 50) {
        statusText = "🟢 NHÀ BẠN NẰM Ở VÙNG ĐỆM AN TOÀN (35m - 50m). " +
                     "Biến dạng nền đất không đáng kể.";
        alertClass = "alert-info";
    } else {
        statusText = "✅ NHÀ BẠN NẰM HOÀN TOÀN NGOÀI VÙNG ẢNH HƯỞNG THI CÔNG (>50m). Hoàn toàn an tâm!";
        alertClass = "alert-success";
    }
    
    // Hiển thị kết quả ra giao diện
    document.getElementById("resultBox").innerHTML = 
        "<div class='alert " + alertClass + " mt-2 p-2'>" +
        "<strong>Khoảng cách đến tim hầm: " + Math.round(distanceInMeters) + " mét</strong><br>" +
        statusText + "</div>";
}
```

---

### PHẦN 4: HƯỚNG DẪN BIÊN KỊCH CỐT TRUYỆN STORYMAP (DÀNH CHO SV1 & SV3)

Truyền thông khoa học thành công là khi một bà cụ 70 tuổi ở phố Cát Linh hay một bạn học sinh cấp 3 đọc vào đều hiểu và cảm thấy an tâm. Kịch bản StoryMap gồm 4 màn:

* **Màn 1: Vì sao Thủ đô cần Metro ngầm?**
  - Trực quan hóa hình ảnh ùn tắc giao thông giờ cao điểm trên đường Kim Mã, Giảng Võ.
  - Bản đồ toàn cảnh 10 tuyến đường sắt đô thị theo Quy hoạch Thủ đô, nhấn mạnh vai trò xương sống của Tuyến số 3.

* **Màn 2: Cận cảnh hai "chú robot khổng lồ" TBM Thần Tốc và Táo Bạo**
  - Đồ họa giải thích: Đường kính $6{,}30\,\text{m}$, nặng hơn 850 tấn, đào đất đến đâu lắp vỏ hầm bê tông dày 30cm đến đó.
  - Video hoạt hình 3D ngắn giải thích nguyên lý cân bằng áp lực đất (EPB): Áp lực vữa cân bằng chính xác với áp lực đất và nước ngầm, giúp giữ cho lòng đất không bị sụp đổ.

* **Màn 3: Vì sao mặt đất lại có hiện tượng lún nhẹ?**
  - Giải thích hiện tượng mất thể tích đất ($V_L \approx 1\%$) bằng hình ảnh chiếc bánh xốp.
  - Phễu lún Peck được vẽ dưới dạng hình chuông úp ngược, chỉ rõ: Lún lớn nhất ở ngay tim hầm và triệt tiêu dần khi ra xa ngoài $35\,\text{m}$.
  - Giới thiệu hệ thống quan trắc tự động (hàng nghìn lăng kính phản xạ gắn trên tường nhà dọc phố) hoạt động 24/7 để báo động sớm.

* **Màn 4: Đồng hành cùng dự án - Hướng dẫn tự kiểm tra và phản ánh**
  - Hướng dẫn người dân kiểm tra vết nứt nhà cũ bằng cách dán miếng băng dính giấy ghi ngày tháng.
  - Sơ đồ liên hệ nhanh: Số điện thoại Ban chỉ huy công trường từng ga, đường dây nóng UBND Phường.

---

### PHẦN 5: THIẾT KẾ MÔ-ĐUN THAM VẤN PPGIS VÀ ĐÁNH GIÁ TRẢI NGHIỆM SUS

#### 5.1. Bảng hỏi tham vấn cộng đồng (Tích hợp Google Forms hoặc Form trên WebGIS)
Gồm 5 câu hỏi cốt lõi:
1. Bạn đang sinh sống/làm việc tại số nhà hoặc khu vực nào?
2. Trước khi xem bản đồ này, bạn có biết vị trí hầm Metro đi qua gần nhà mình không? (Có / Không)
3. Sau khi tra cứu trên bản đồ, bạn cảm thấy mức độ an tâm của mình thế nào? (Thang điểm 1 đến 5)
4. Bạn có nhận thấy hiện tượng rung chấn hay vết nứt mới xuất hiện gần đây không? (Nếu có, vui lòng tải ảnh đính kèm)
5. Bạn có đề xuất gì để Ban Quản lý dự án cung cấp thông tin tốt hơn đến tổ dân phố?

#### 5.2. Thang đo tiêu chuẩn đánh giá hệ thống SUS (System Usability Scale)
Cho 30–50 người dùng thử bản đồ số và chấm điểm từ 1 (Rất không đồng ý) đến 5 (Rất đồng ý) cho 10 nhận định:
1. Tôi nghĩ rằng tôi sẽ thích sử dụng bản đồ số này thường xuyên khi tuyến hầm đang thi công.
2. Tôi thấy bản đồ này quá phức tạp, không cần thiết.
3. Tôi thấy bản đồ rất dễ sử dụng và tra cứu.
4. Tôi nghĩ rằng tôi cần có chuyên gia công nghệ hướng dẫn mới dùng được bản đồ này.
5. Các tính năng trên bản đồ được tích hợp rất tốt.
6. Tôi thấy có quá nhiều điểm mâu thuẫn/khó hiểu trên trang web.
7. Tôi nghĩ mọi người sẽ học được cách sử dụng bản đồ này rất nhanh chóng.
8. Tôi thấy thao tác trên bản đồ rất cồng kềnh, bất tiện.
9. Tôi cảm thấy rất tự tin khi tự mình tra cứu địa chỉ trên bản đồ.
10. Tôi phải học thêm rất nhiều điều mới trước khi có thể sử dụng thành thạo bản đồ này.  
*(Điểm SUS tổng kết $> 68$ điểm chứng minh sản phẩm đạt chuẩn khả dụng quốc tế).*

---

### PHẦN 6: XUẤT BẢN MIỄN PHÍ VÀ QUẢNG BÁ SẢN PHẨM

1. **Đưa mã nguồn lên GitHub:**  
   Tạo tài khoản GitHub tại [github.com](https://github.com), tạo kho lưu trữ mới đặt tên: `metro3-hanoi-webgis`.
2. **Kích hoạt GitHub Pages (Miễn phí 100%):**  
   Vào `Settings` $\to$ `Pages` $\to$ chọn nhánh `main` $\to$ Bấm `Save`.  
   Sau 1 phút, trang web sẽ có đường link trực tuyến công khai: `https://[ten-tai-khoan].github.io/metro3-hanoi-webgis`.
3. **Tạo mã QR chia sẻ cho người dân:**  
   Vào trang [qr-code-generator.com](https://www.qr-code-generator.com) dán đường link web để tạo mã QR. In mã QR này lên áp phích thử nghiệm hoặc gửi vào các nhóm Zalo tổ dân phố để thu thập ý kiến tham vấn.
