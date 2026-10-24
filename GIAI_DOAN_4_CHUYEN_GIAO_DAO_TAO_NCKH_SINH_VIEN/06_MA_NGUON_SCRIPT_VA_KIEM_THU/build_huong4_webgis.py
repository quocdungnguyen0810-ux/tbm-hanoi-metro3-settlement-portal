# -*- coding: utf-8 -*-
"""
Script tạo trọn bộ dữ liệu GeoJSON và ứng dụng WebGIS Prototype
cho NCKHSV Hướng 4 (WebGIS/StoryMap) tại:
NCKH_SV_2026_Huong4_WebGIS_StoryMap/05_WEBGIS_PROTOTYPE
"""

import os
import json
import math

OUTPUT_DIR = r"d:\OneDrive\NCKH\NCKH 2027\T2027\TBM_ĐTM\NCKH_SV_2026_Huong4_WebGIS_StoryMap\05_WEBGIS_PROTOTYPE"
DATA_DIR = os.path.join(OUTPUT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 1. DỮ LIỆU CÁC GA NGẦM (S9 -> S12)
stations_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "id": "S09",
                "name": "Ga Kim Mã (S9)",
                "chainage": "Km 8+400",
                "depth_m": 18.5,
                "role": "Giếng phóng 2 máy đào hầm TBM (Điểm xuất phát)",
                "status": "Đang vận hành giếng phóng TBM",
                "location_desc": "Đối diện Đền Voi Phục và Công viên Thủ Lệ, Q. Ba Đình"
            },
            "geometry": {"type": "Point", "coordinates": [105.8192, 21.0315]}
        },
        {
            "type": "Feature",
            "properties": {
                "id": "S10",
                "name": "Ga Cát Linh (S10)",
                "chainage": "Km 9+500",
                "depth_m": 16.8,
                "role": "Ga trung chuyển kết nối Tuyến số 2A Cát Linh - Hà Đông",
                "status": "Đang đào đất tầng hầm B1, thi công bản đỉnh",
                "location_desc": "Nút giao Cát Linh - Giảng Võ - Hào Nam, Q. Đống Đa"
            },
            "geometry": {"type": "Point", "coordinates": [105.8295, 21.0286]}
        },
        {
            "type": "Feature",
            "properties": {
                "id": "S11",
                "name": "Ga Văn Miếu (S11)",
                "chainage": "Km 10+600",
                "depth_m": 15.5,
                "role": "Ga ngầm phục vụ khách du lịch khu di tích lịch sử",
                "status": "Đang thi công tường dẫn và tường vây D-wall",
                "location_desc": "Đường Quốc Tử Giám, trước cổng Văn Miếu, Q. Đống Đa"
            },
            "geometry": {"type": "Point", "coordinates": [105.8368, 21.0264]}
        },
        {
            "type": "Feature",
            "properties": {
                "id": "S12",
                "name": "Ga Hà Nội (S12)",
                "chainage": "Km 11+800",
                "depth_m": 17.2,
                "role": "Ga ngầm trung tâm & Giếng tiếp nhận 2 máy TBM (Điểm đích)",
                "status": "Đang thi công hố đào giếng thu hồi khiên đào",
                "location_desc": "Phố Trần Hưng Đạo, trước cổng Ga Hà Nội, Q. Hoàn Kiếm"
            },
            "geometry": {"type": "Point", "coordinates": [105.8415, 21.0238]}
        }
    ]
}

with open(os.path.join(DATA_DIR, "stations.geojson"), "w", encoding="utf-8") as f:
    json.dump(stations_data, f, ensure_ascii=False, indent=2)

# 2. DỮ LIỆU TIM TUYẾN HẦM ĐÔI (LINESTRING)
# Tọa độ tim tuyến đi uốn lượn theo hành lang Kim Mã - Cát Linh - Quốc Tử Giám - Trần Hưng Đạo
line_coords = [
    [105.8192, 21.0315], # S9
    [105.8220, 21.0308], # Kim Mã đoạn qua hồ Giảng Võ
    [105.8250, 21.0301], # Kim Mã - Cát Linh
    [105.8295, 21.0286], # S10 Cát Linh
    [105.8335, 21.0275], # Cát Linh - Quốc Tử Giám
    [105.8368, 21.0264], # S11 Văn Miếu
    [105.8390, 21.0250], # Quốc Tử Giám - Trần Hưng Đạo
    [105.8415, 21.0238]  # S12 Ga Hà Nội
]

metro_line_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "id": "LINE_3_UG",
                "name": "Tuyến ngầm Metro 3 (S9 - S12)",
                "length_km": 4.0,
                "tunnel_type": "Hầm đôi song song (Twin TBM Tunnels)",
                "diameter_m": 6.30,
                "depth_m": "15 - 18 m",
                "tbm_names": "TBM 1 (Thần Tốc) & TBM 2 (Táo Bạo)"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": line_coords
            }
        }
    ]
}

with open(os.path.join(DATA_DIR, "metro_line.geojson"), "w", encoding="utf-8") as f:
    json.dump(metro_line_data, f, ensure_ascii=False, indent=2)

# 3. TẠO CÁC VÙNG ĐỆM LÚN THEO GIẢI TÍCH PECK (15M, 35M, 50M)
# Chuyển đổi mét sang độ: tại vĩ độ 21°N:
# 1 độ vĩ = 110,750 m -> delta_lat = d / 110750
# 1 độ kinh = 110750 * cos(21°) = 103,390 m -> delta_lng = d / 103390
def create_buffer_polygon(coords, dist_m):
    delta_lat = dist_m / 110750.0
    delta_lng = dist_m / 103390.0
    
    left_side = []
    right_side = []
    
    for i in range(len(coords)):
        # Tính vector hướng tiếp tuyến
        if i == 0:
            dx = coords[1][0] - coords[0][0]
            dy = coords[1][1] - coords[0][1]
        elif i == len(coords) - 1:
            dx = coords[i][0] - coords[i-1][0]
            dy = coords[i][1] - coords[i-1][1]
        else:
            dx = coords[i+1][0] - coords[i-1][0]
            dy = coords[i+1][1] - coords[i-1][1]
            
        # Chuẩn hóa vector tiếp tuyến theo mét
        vx = dx * 103390.0
        vy = dy * 110750.0
        norm = math.sqrt(vx*vx + vy*vy)
        if norm == 0: norm = 1.0
        ux = vx / norm
        uy = vy / norm
        
        # Pháp tuyến vuông góc (nx, ny) = (-uy, ux)
        nx = -uy
        ny = ux
        
        # Điểm lệch trái và phải
        p_left = [coords[i][0] + (nx * dist_m) / 103390.0, coords[i][1] + (ny * dist_m) / 110750.0]
        p_right = [coords[i][0] - (nx * dist_m) / 103390.0, coords[i][1] - (ny * dist_m) / 110750.0]
        
        left_side.append(p_left)
        right_side.append(p_right)
        
    polygon = left_side + right_side[::-1] + [left_side[0]]
    return polygon

poly_15m = create_buffer_polygon(line_coords, 15.0)
poly_35m = create_buffer_polygon(line_coords, 35.0)
poly_50m = create_buffer_polygon(line_coords, 50.0)

settlement_zones_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "zone_id": "ZONE_50M",
                "name": "Vùng đệm mở rộng (35m - 50m)",
                "buffer_m": 50,
                "s_max": "< 3 mm",
                "alert_level": "Xanh (An toàn)",
                "color": "#198754",
                "desc": "Khu vực nền đất hoàn toàn ổn định, độ lún không đáng kể."
            },
            "geometry": {"type": "Polygon", "coordinates": [poly_50m]}
        },
        {
            "type": "Feature",
            "properties": {
                "zone_id": "ZONE_35M",
                "name": "Vùng phễu lún ảnh hưởng chính (15m - 35m)",
                "buffer_m": 35,
                "s_max": "3 - 10 mm",
                "alert_level": "Vàng (Cần theo dõi)",
                "color": "#ffc107",
                "desc": "Nằm trong phạm vi phễu lún Peck (2.5i - 3i). Độ lún nhỏ nhưng cần quan sát vết nứt định kỳ đối với nhà móng nông."
            },
            "geometry": {"type": "Polygon", "coordinates": [poly_35m]}
        },
        {
            "type": "Feature",
            "properties": {
                "zone_id": "ZONE_15M",
                "name": "Vùng giám sát đặc biệt (0m - 15m)",
                "buffer_m": 15,
                "s_max": "> 10 - 15 mm",
                "alert_level": "Đỏ (Ưu tiên giám sát cao nhất)",
                "color": "#dc3545",
                "desc": "Trực diện nóc hầm đôi TBM. Dự án bố trí mốc quan trắc lún tự động 24/7 và cam kết bảo hiểm công trình 100%."
            },
            "geometry": {"type": "Polygon", "coordinates": [poly_15m]}
        }
    ]
}

with open(os.path.join(DATA_DIR, "settlement_zones.geojson"), "w", encoding="utf-8") as f:
    json.dump(settlement_zones_data, f, ensure_ascii=False, indent=2)

# 4. DỮ LIỆU ĐIỂM NHẠY CẢM (DI TÍCH, TRƯỜNG HỌC, CHUNG CƯ CŨ)
sensitive_points_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "id": "POI_01",
                "name": "Đền Voi Phục (Trấn Tây Thăng Long)",
                "type": "Di tích lịch sử văn hóa",
                "distance_to_tunnel_m": 25.0,
                "mitigation": "Khoan cọc chắn chấn động & lắp đặt mốc quan trắc độ nghiêng"
            },
            "geometry": {"type": "Point", "coordinates": [105.8185, 21.0318]}
        },
        {
            "type": "Feature",
            "properties": {
                "id": "POI_02",
                "name": "Khu tập thể Giảng Võ / Cát Linh",
                "type": "Chung cư cũ lắp ghép tấm lớn 5 tầng",
                "distance_to_tunnel_m": 14.2,
                "mitigation": "Ưu tiên giám sát lún tự động 24/7 và mua bảo hiểm công trình"
            },
            "geometry": {"type": "Point", "coordinates": [105.8278, 21.0292]}
        },
        {
            "type": "Feature",
            "properties": {
                "id": "POI_03",
                "name": "Trường THCS Cát Linh",
                "type": "Công trình giáo dục",
                "distance_to_tunnel_m": 28.5,
                "mitigation": "Đào hầm vào ca đêm tránh ảnh hưởng giờ học sinh đến trường"
            },
            "geometry": {"type": "Point", "coordinates": [105.8305, 21.0289]}
        },
        {
            "type": "Feature",
            "properties": {
                "id": "POI_04",
                "name": "Văn Miếu - Quốc Tử Giám",
                "type": "Di tích quốc gia đặc biệt",
                "distance_to_tunnel_m": 38.0,
                "mitigation": "Kiểm soát áp lực vữa TBM tối đa, giữ biến dạng mặt đất < 2mm"
            },
            "geometry": {"type": "Point", "coordinates": [105.8355, 21.0272]}
        },
        {
            "type": "Feature",
            "properties": {
                "id": "POI_05",
                "name": "Ga Hà Nội (Toà nhà chính)",
                "type": "Công trình kiến trúc di sản giao thông",
                "distance_to_tunnel_m": 18.0,
                "mitigation": "Gia cố móng cọc xi măng đất jet-grouting đáy giếng đào"
            },
            "geometry": {"type": "Point", "coordinates": [105.8410, 21.0242]}
        }
    ]
}

with open(os.path.join(DATA_DIR, "sensitive_points.geojson"), "w", encoding="utf-8") as f:
    json.dump(sensitive_points_data, f, ensure_ascii=False, indent=2)

print("All GeoJSON layers generated successfully!")

# 5. TẠO FILE index.html CHO BẢN MẪU WEBGIS HOÀN CHỈNH
html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bản đồ số Tuyến Metro 3 Hà Nội - Tra cứu vùng lún & Tham vấn cộng đồng</title>
  <!-- Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <!-- Bootstrap 5 CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    body, html { height: 100%; margin: 0; padding: 0; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    #navbar { height: 60px; z-index: 1050; }
    #map { height: calc(100vh - 60px); width: 100%; position: relative; }
    
    /* Search & Check Box Panel */
    .floating-panel {
      position: absolute;
      top: 75px;
      left: 15px;
      z-index: 1000;
      width: 360px;
      max-width: 90vw;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.18);
      border: 1px solid rgba(0,0,0,0.08);
      padding: 16px;
    }
    
    /* Legend Box */
    .legend-panel {
      position: absolute;
      bottom: 25px;
      right: 15px;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.95);
      border-radius: 10px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.15);
      padding: 12px 16px;
      font-size: 13px;
      max-width: 280px;
    }
    .legend-item { display: flex; align-items: center; margin-bottom: 6px; }
    .legend-color { width: 20px; height: 14px; border-radius: 3px; margin-right: 8px; display: inline-block; }
    
    /* StoryMap Drawer */
    #storyDrawer {
      position: absolute;
      top: 60px;
      right: -420px;
      width: 400px;
      max-width: 85vw;
      height: calc(100vh - 60px);
      background: #ffffff;
      z-index: 1020;
      box-shadow: -4px 0 20px rgba(0,0,0,0.15);
      transition: right 0.35s ease;
      overflow-y: auto;
      padding: 20px;
    }
    #storyDrawer.active { right: 0; }
    
    /* Station marker icon */
    .station-marker {
      background: #0d6efd;
      color: white;
      border: 2px solid white;
      border-radius: 50%;
      text-align: center;
      line-height: 24px;
      font-size: 12px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.4);
    }
  </style>
</head>
<body>

  <!-- Top Navigation Bar -->
  <nav id="navbar" class="navbar navbar-expand-lg navbar-dark bg-dark px-3 shadow">
    <div class="container-fluid">
      <a class="navbar-brand fw-bold text-warning d-flex align-items-center" href="#">
        <i class="fa-solid fa-train-subway me-2"></i>
        <span>METRO HÀ NỘI LINE 3 • BẢN ĐỒ AN TOÀN ĐÀO HẦM</span>
      </a>
      <div class="d-flex gap-2">
        <button class="btn btn-outline-warning btn-sm" onclick="toggleStoryDrawer()">
          <i class="fa-solid fa-book-open me-1"></i> Câu chuyện TBM
        </button>
        <button class="btn btn-danger btn-sm" onclick="openFeedbackModal()">
          <i class="fa-solid fa-bullhorn me-1"></i> Gửi phản ánh nứt lún
        </button>
      </div>
    </div>
  </nav>

  <!-- Floating Search & Safety Check Panel -->
  <div class="floating-panel">
    <div class="d-flex justify-content-between align-items-center mb-2">
      <h6 class="fw-bold text-primary mb-0"><i class="fa-solid fa-magnifying-glass-location me-1"></i> Tra cứu an toàn nhà bạn</h6>
      <span class="badge bg-primary">Peck (1969)</span>
    </div>
    <p class="text-muted small mb-2">Nhập số nhà hoặc bấm trực tiếp vị trí nhà bạn trên bản đồ để kiểm tra khoảng cách đến tim hầm.</p>
    
    <div class="input-group mb-2">
      <input type="text" id="addressInput" class="form-control form-control-sm" placeholder="Nhập địa chỉ (vd: 35 Cát Linh)..." onkeypress="if(event.key==='Enter') searchAddress()">
      <button class="btn btn-primary btn-sm" onclick="searchAddress()"><i class="fa-solid fa-search"></i> Tìm</button>
    </div>
    
    <button class="btn btn-outline-success btn-sm w-100 mb-2" onclick="locateUser()">
      <i class="fa-solid fa-location-crosshairs me-1"></i> Định vị nhà tôi hiện tại
    </button>
    
    <!-- Diagnostic result box -->
    <div id="resultBox" class="mt-2" style="display:none;"></div>
  </div>

  <!-- Map Container -->
  <div id="map"></div>

  <!-- Legend Panel -->
  <div class="legend-panel">
    <div class="fw-bold mb-2 text-dark"><i class="fa-solid fa-layer-group me-1"></i> Chú giải vùng lún Peck</div>
    <div class="legend-item">
      <span class="legend-color" style="background: rgba(220, 53, 69, 0.5); border: 2px solid #dc3545;"></span>
      <span><strong>0 - 15m:</strong> Giám sát đặc biệt</span>
    </div>
    <div class="legend-item">
      <span class="legend-color" style="background: rgba(255, 193, 7, 0.5); border: 2px solid #ffc107;"></span>
      <span><strong>15 - 35m:</strong> Vùng phễu lún chính</span>
    </div>
    <div class="legend-item">
      <span class="legend-color" style="background: rgba(25, 135, 84, 0.4); border: 2px solid #198754;"></span>
      <span><strong>35 - 50m:</strong> Vùng đệm an toàn</span>
    </div>
    <div class="legend-item">
      <span class="legend-color" style="background: #0d6efd; height: 4px;"></span>
      <span><strong>Tim hầm đôi TBM</strong></span>
    </div>
    <div class="legend-item">
      <i class="fa-solid fa-circle-dot text-primary me-2"></i>
      <span><strong>4 Ga ngầm (S9 - S12)</strong></span>
    </div>
  </div>

  <!-- StoryMap Slide-in Drawer -->
  <div id="storyDrawer">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-newspaper me-1"></i> Câu chuyện Metro ngầm</h5>
      <button class="btn btn-close" onclick="toggleStoryDrawer()"></button>
    </div>
    <hr>
    
    <div class="card mb-3 border-0 bg-light">
      <div class="card-body">
        <h6 class="fw-bold text-dark"><i class="fa-solid fa-robot text-danger me-1"></i> 1. Hai cỗ máy TBM khổng lồ</h6>
        <p class="small text-muted mb-1">Máy TBM 1 "Thần Tốc" và TBM 2 "Táo Bạo" có đường kính 6,3m, dài hơn 100m, nặng 850 tấn. Máy đào đất và tự động lắp ráp vỏ hầm bê tông dày 300mm ngay trong lòng đất ở độ sâu 15 - 18m.</p>
        <span class="badge bg-secondary">Công nghệ EPB cân bằng áp lực</span>
      </div>
    </div>

    <div class="card mb-3 border-0 bg-light">
      <div class="card-body">
        <h6 class="fw-bold text-dark"><i class="fa-solid fa-chart-line text-warning me-1"></i> 2. Vì sao mặt đất lại hơi lún?</h6>
        <p class="small text-muted mb-1">Khi đào hầm, thể tích đất mất đi khoảng 0,5% - 2,0% tạo nên một phễu lún có dạng phân bố Gauss (Peck 1969). Lún lớn nhất ở ngay tim hầm và giảm dần về 0 khi cách tim hầm ngoài 35m.</p>
      </div>
    </div>

    <div class="card mb-3 border-0 bg-light">
      <div class="card-body">
        <h6 class="fw-bold text-dark"><i class="fa-solid fa-shield-halved text-success me-1"></i> 3. Dự án bảo vệ bạn thế nào?</h6>
        <p class="small text-muted mb-1">• Lắp đặt hàng trăm lăng kính quan trắc tự động dọc các dãy nhà để cảnh báo sớm.<br>• Phun ép vữa xi măng áp lực cao ngay sau đuôi khiên đào để bù thể tích rỗng.<br>• Mua bảo hiểm rủi ro xây dựng 100% cho các công trình lân cận.</p>
      </div>
    </div>

    <div class="card border-0 bg-light">
      <div class="card-body">
        <h6 class="fw-bold text-dark"><i class="fa-solid fa-phone-volume text-primary me-1"></i> 4. Kênh hỗ trợ khẩn cấp</h6>
        <p class="small text-muted mb-1">Khi thấy hiện tượng nứt tường, kẹt cửa hoặc rung bất thường, bà con gọi ngay đường dây nóng: <strong>1900.xxxx</strong> hoặc bấm nút gửi phản ánh trên bản đồ này.</p>
      </div>
    </div>
  </div>

  <!-- Modal Gửi Phản Ánh Nứt Lún (PPGIS) -->
  <div class="modal fade" id="feedbackModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header bg-danger text-white">
          <h5 class="modal-title"><i class="fa-solid fa-comment-medical me-2"></i> Gửi phản ánh hiện trạng nhà cửa</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <form id="feedbackForm" onsubmit="submitFeedback(event)">
            <div class="mb-2">
              <label class="form-label small fw-bold">Họ và tên (có thể ẩn danh):</label>
              <input type="text" class="form-control form-control-sm" id="fbName" placeholder="Ví dụ: Nguyễn Văn A">
            </div>
            <div class="mb-2">
              <label class="form-label small fw-bold">Số điện thoại liên hệ:</label>
              <input type="text" class="form-control form-control-sm" id="fbPhone" placeholder="09xxxxxxxx">
            </div>
            <div class="mb-2">
              <label class="form-label small fw-bold">Địa chỉ ngôi nhà:</label>
              <input type="text" class="form-control form-control-sm" id="fbAddress" required placeholder="Số nhà, ngõ, đường phố...">
            </div>
            <div class="mb-2">
              <label class="form-label small fw-bold">Mức độ lo lắng của bạn:</label>
              <select class="form-select form-select-sm" id="fbWorry">
                <option value="1">1 - Rất yên tâm, không có vấn đề gì</option>
                <option value="2">2 - Bình thường</option>
                <option value="3" selected>3 - Hơi lo lắng về tiếng ồn / rung chấn</option>
                <option value="4">4 - Lo lắng vì thấy xuất hiện vết nứt mới</option>
                <option value="5">5 - Rất khẩn cấp, cần cán bộ đến kiểm tra ngay</option>
              </select>
            </div>
            <div class="mb-3">
              <label class="form-label small fw-bold">Mô tả hiện tượng quan sát được:</label>
              <textarea class="form-control form-control-sm" id="fbDesc" rows="3" placeholder="Ví dụ: Bức tường tầng 1 giáp ngõ xuất hiện vết nứt xiên dài khoảng 50cm..."></textarea>
            </div>
            <button type="submit" class="btn btn-danger btn-sm w-100"><i class="fa-solid fa-paper-plane me-1"></i> Gửi phản ánh đến Kỹ sư dự án</button>
          </form>
        </div>
      </div>
    </div>
  </div>

  <!-- JavaScript Libraries -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://unpkg.com/@turf/turf@6/turf.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

  <!-- Embedded WebGIS Logic -->
  <script>
    // 1. Khởi tạo bản đồ tại tâm tuyến S9 - S12
    var map = L.map('map', {zoomControl: false}).setView([21.0285, 21.0285 ? 105.8300 : 105.83], 15);
    L.control.zoom({position: 'bottomleft'}).addTo(map);

    // Bản đồ nền: OpenStreetMap & Esri Satellite
    var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap contributors | Metro Line 3 Ha Noi'
    }).addTo(map);

    var esriSat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles © Esri'
    });

    var baseMaps = {
      "Bản đồ Đường phố": osm,
      "Bản đồ Vệ tinh": esriSat
    };
    L.control.layers(baseMaps, null, {position: 'topright'}).addTo(map);

    // Biến lưu trữ dữ liệu
    var metroLineGeoJSON = null;
    var userMarker = null;

    // 2. Tải các lớp dữ liệu GeoJSON
    // 2.1 Vùng đệm lún Peck
    fetch('data/settlement_zones.geojson')
      .then(res => res.json())
      .then(data => {
        L.geoJSON(data, {
          style: function(feature) {
            return {
              color: feature.properties.color,
              weight: 2,
              opacity: 0.8,
              fillColor: feature.properties.color,
              fillOpacity: feature.properties.buffer_m === 15 ? 0.35 : (feature.properties.buffer_m === 35 ? 0.25 : 0.15)
            };
          },
          onEachFeature: function(feature, layer) {
            var p = feature.properties;
            layer.bindPopup(
              "<div style='min-width:200px;'>" +
              "<h6 style='color:" + p.color + "; font-weight:bold; margin-bottom:4px;'>" + p.name + "</h6>" +
              "<p class='small mb-1'><strong>Bán kính:</strong> " + p.buffer_m + " mét tính từ tim hầm</p>" +
              "<p class='small mb-1'><strong>Độ lún dự báo:</strong> " + p.s_max + "</p>" +
              "<p class='small mb-1'><strong>Mức cảnh báo:</strong> " + p.alert_level + "</p>" +
              "<p class='small text-muted mb-0'>" + p.desc + "</p>" +
              "</div>"
            );
          }
        }).addTo(map);
      });

    // 2.2 Tim tuyến hầm đôi
    fetch('data/metro_line.geojson')
      .then(res => res.json())
      .then(data => {
        metroLineGeoJSON = data.features[0];
        L.geoJSON(data, {
          style: {
            color: '#0d6efd',
            weight: 4,
            dashArray: '6, 6',
            opacity: 0.9
          }
        }).addTo(map).bindPopup("<strong>Tuyến hầm đôi Metro 3</strong><br>Đào bằng 2 máy TBM Thần Tốc & Táo Bạo.<br>Độ sâu chôn hầm: 15 - 18m.");
      });

    // 2.3 Các ga ngầm (S9 -> S12)
    fetch('data/stations.geojson')
      .then(res => res.json())
      .then(data => {
        L.geoJSON(data, {
          pointToLayer: function(feature, latlng) {
            return L.circleMarker(latlng, {
              radius: 9,
              fillColor: '#0d6efd',
              color: '#ffffff',
              weight: 3,
              opacity: 1,
              fillOpacity: 1
            });
          },
          onEachFeature: function(feature, layer) {
            var p = feature.properties;
            layer.bindPopup(
              "<div style='min-width:220px;'>" +
              "<h6 class='text-primary fw-bold mb-1'><i class='fa-solid fa-train me-1'></i> " + p.name + "</h6>" +
              "<p class='small mb-1'><strong>Vị trí:</strong> " + p.location_desc + "</p>" +
              "<p class='small mb-1'><strong>Lý trình:</strong> " + p.chainage + " | <strong>Độ sâu:</strong> " + p.depth_m + "m</p>" +
              "<p class='small mb-1'><strong>Vai trò:</strong> " + p.role + "</p>" +
              "<span class='badge bg-warning text-dark'>" + p.status + "</span>" +
              "</div>"
            );
          }
        }).addTo(map);
      });

    // 2.4 Điểm nhạy cảm di tích / trường học
    fetch('data/sensitive_points.geojson')
      .then(res => res.json())
      .then(data => {
        L.geoJSON(data, {
          pointToLayer: function(feature, latlng) {
            return L.marker(latlng);
          },
          onEachFeature: function(feature, layer) {
            var p = feature.properties;
            layer.bindPopup(
              "<div style='min-width:200px;'>" +
              "<h6 class='text-danger fw-bold mb-1'><i class='fa-solid fa-landmark me-1'></i> " + p.name + "</h6>" +
              "<p class='small mb-1'><strong>Loại hình:</strong> " + p.type + "</p>" +
              "<p class='small mb-1'><strong>Cách tim hầm:</strong> " + p.distance_to_tunnel_m + "m</p>" +
              "<p class='small text-success mb-0'><strong>Bảo vệ:</strong> " + p.mitigation + "</p>" +
              "</div>"
            );
          }
        }).addTo(map);
      });

    // 3. Hàm kiểm tra độ an toàn của ngôi nhà (Check House Safety)
    function evaluateHouseSafety(lat, lng, addressLabel) {
      if (!metroLineGeoJSON) {
        alert("Đang tải dữ liệu tuyến hầm, vui lòng thử lại sau 2 giây...");
        return;
      }
      
      var pt = turf.point([lng, lat]);
      var distance = turf.pointToLineDistance(pt, metroLineGeoJSON, {units: 'meters'});
      var distRounded = Math.round(distance);
      
      var alertHtml = "";
      if (distRounded <= 15) {
        alertHtml = "<div class='alert alert-danger p-2 mb-0'>" +
                    "<strong class='d-block'><i class='fa-solid fa-triangle-exclamation'></i> VÙNG GIÁM SÁT ĐẶC BIỆT (&le;15m)</strong>" +
                    "<span class='small'>Nhà bạn cách tim hầm <strong>" + distRounded + " mét</strong>. Nằm trên đỉnh phễu lún. Dự án đã gắn mốc quan trắc 24/7 và có bảo hiểm 100%.</span>" +
                    "</div>";
      } else if (distRounded <= 35) {
        alertHtml = "<div class='alert alert-warning p-2 mb-0'>" +
                    "<strong class='d-block'><i class='fa-solid fa-circle-exclamation'></i> VÙNG PHỄU LÚN CHÍNH (15m - 35m)</strong>" +
                    "<span class='small'>Nhà bạn cách tim hầm <strong>" + distRounded + " mét</strong>. Độ lún dự báo rất nhỏ (3-10mm), an toàn kết cấu móng. Cần quan sát vết nứt sơn tường định kỳ.</span>" +
                    "</div>";
      } else if (distRounded <= 50) {
        alertHtml = "<div class='alert alert-info p-2 mb-0'>" +
                    "<strong class='d-block'><i class='fa-solid fa-circle-check'></i> VÙNG ĐỆM AN TOÀN (35m - 50m)</strong>" +
                    "<span class='small'>Nhà bạn cách tim hầm <strong>" + distRounded + " mét</strong>. Độ lún <3mm, nền đất ổn định hoàn toàn.</span>" +
                    "</div>";
      } else {
        alertHtml = "<div class='alert alert-success p-2 mb-0'>" +
                    "<strong class='d-block'><i class='fa-solid fa-shield-heart'></i> NGOÀI VÙNG ẢNH HƯỞNG (>50m)</strong>" +
                    "<span class='small'>Nhà bạn cách tim hầm <strong>" + distRounded + " mét</strong>. Nằm ngoài vùng thi công, hoàn toàn yên tâm!</span>" +
                    "</div>";
      }
      
      var box = document.getElementById("resultBox");
      box.style.display = "block";
      box.innerHTML = alertHtml;

      // Cập nhật marker trên bản đồ
      if (userMarker) map.removeLayer(userMarker);
      userMarker = L.marker([lat, lng], {bounceOnAdd: true}).addTo(map);
      userMarker.bindPopup("<strong>Vị trí đã chọn:</strong><br>" + (addressLabel || "Vị trí đã bấm") + "<br>Khoảng cách tim hầm: <strong>" + distRounded + "m</strong>").openPopup();
      map.setView([lat, lng], 17);
    }

    // 4. Bấm trực tiếp trên bản đồ để tra cứu
    map.on('click', function(e) {
      evaluateHouseSafety(e.latlng.lat, e.latlng.lng, "Điểm bạn vừa chọn");
    });

    // 5. Tìm kiếm địa chỉ bằng OpenStreetMap Nominatim API
    function searchAddress() {
      var query = document.getElementById("addressInput").value;
      if (!query) return;
      
      var fullQuery = query + ", Hà Nội, Việt Nam";
      var url = "https://nominatim.openstreetmap.org/search?format=json&q=" + encodeURIComponent(fullQuery);
      
      fetch(url)
        .then(res => res.json())
        .then(results => {
          if (results && results.length > 0) {
            var item = results[0];
            var lat = parseFloat(item.lat);
            var lon = parseFloat(item.lon);
            evaluateHouseSafety(lat, lon, item.display_name);
          } else {
            alert("Không tìm thấy địa chỉ này tại Hà Nội. Vui lòng bấm trực tiếp lên bản đồ!");
          }
        })
        .catch(err => {
          alert("Lỗi kết nối tra cứu địa chỉ. Bạn có thể bấm trực tiếp lên vị trí nhà trên bản đồ!");
        });
    }

    // 6. Định vị vị trí người dùng qua GPS trình duyệt
    function locateUser() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(pos) {
          evaluateHouseSafety(pos.coords.latitude, pos.coords.longitude, "Vị trí GPS của bạn");
        }, function(err) {
          alert("Không thể lấy vị trí hiện tại. Vui lòng cho phép quyền truy cập vị trí trên trình duyệt!");
        });
      } else {
        alert("Trình duyệt không hỗ trợ GPS.");
      }
    }

    // 7. Toggle StoryMap Drawer
    function toggleStoryDrawer() {
      var drawer = document.getElementById("storyDrawer");
      drawer.classList.toggle("active");
    }

    // 8. Modal Phản ánh
    var fbModal = null;
    function openFeedbackModal() {
      if (!fbModal) fbModal = new bootstrap.Modal(document.getElementById('feedbackModal'));
      fbModal.show();
    }

    function submitFeedback(e) {
      e.preventDefault();
      var name = document.getElementById("fbName").value || "Cư dân ẩn danh";
      var addr = document.getElementById("fbAddress").value;
      alert("Cảm ơn " + name + " tại " + addr + "!\nThông tin phản ánh đã được gửi thành công đến Kỹ sư giám sát an toàn dự án Metro số 3.");
      fbModal.hide();
      document.getElementById("feedbackForm").reset();
    }
  </script>
</body>
</html>
"""

with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("WebGIS Prototype HTML generated successfully at:", os.path.join(OUTPUT_DIR, "index.html"))
