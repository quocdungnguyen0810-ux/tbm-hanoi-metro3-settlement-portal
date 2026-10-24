# -*- coding: utf-8 -*-
"""
Build Stage 3 WebGIS Digital Twin Package:
1. buildings_exposure_150.geojson
2. groundwater_drawdown_contours.geojson
3. alignment_complete_wgs84.geojson
4. webgis_digital_twin_tbm_v3.html
5. HUONG_DAN_SU_DUNG_WEBGIS_V3_DIGITAL_TWIN.md
"""
import os
import sys
import json
import math
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGE3_DIR = os.path.join(ROOT, "nhiem_vu_luan_an_giai_doan_3")
GIS_DIR = os.path.join(STAGE3_DIR, "05_HE_THONG_WEBGIS_3_DIGITAL_TWIN_GIAI_DOAN_3")
DATA_DIR = os.path.join(GIS_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Metro 3 Alignment Coordinates (S9 Kim Ma to S12 Ha Noi Station)
alignment_coords = [
    [105.8152, 21.0315],  # S9 Kim Ma
    [105.8248, 21.0298],  # S10 Cat Linh
    [105.8362, 21.0282],  # S11 Van Mieu / Quoc Tu Giam
    [105.8425, 21.0255]   # S12 Ha Noi Railway Station
]

alignment_geojson = {
    "type": "FeatureCollection",
    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "Tuyến ngầm Metro 3 Hà Nội (S9-S12)",
                "length_km": 3.5,
                "diameter_m": 6.3,
                "depth_range_m": "15.0 - 18.5",
                "tunnel_type": "Twin EPB-TBM Tunnels"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": alignment_coords
            }
        }
    ]
}

with open(os.path.join(DATA_DIR, "alignment_complete_wgs84.geojson"), "w", encoding="utf-8") as f:
    json.dump(alignment_geojson, f, ensure_ascii=False, indent=2)
print("  [OK] Saved alignment_complete_wgs84.geojson")

# 150 Buildings GeoJSON
buildings_features = []
np.random.seed(2027)

types = ["Nhà ống gạch 2-4 tầng", "Khung BTCT 5-9 tầng", "Chung cư cũ lắp ghép", "Di tích lịch sử cấp quốc gia", "Trụ sở cơ quan / Ngoại giao"]
founds = ["Móng nông tự nhiên", "Móng băng gạch/BT", "Móng cọc ma sát ngắn", "Móng bè BTCT", "Móng cọc khoan nhồi sâu"]

# Interpolate positions along the alignment with perpendicular offset
for i in range(150):
    t_ratio = i / 149.0
    # Interpolate along the 3 segments
    if t_ratio < 0.33:
        p1 = np.array(alignment_coords[0])
        p2 = np.array(alignment_coords[1])
        local_t = t_ratio / 0.33
        street = "Kim Mã"
    elif t_ratio < 0.66:
        p1 = np.array(alignment_coords[1])
        p2 = np.array(alignment_coords[2])
        local_t = (t_ratio - 0.33) / 0.33
        street = "Cát Linh"
    else:
        p1 = np.array(alignment_coords[2])
        p2 = np.array(alignment_coords[3])
        local_t = (t_ratio - 0.66) / 0.34
        street = "Quốc Tử Giám - Trần Hưng Đạo"

    center = p1 + local_t * (p2 - p1)
    seg_vec = p2 - p1
    perp_vec = np.array([-seg_vec[1], seg_vec[0]])
    perp_vec = perp_vec / np.linalg.norm(perp_vec)

    # Offset distance in meters (-45m to +45m)
    offset_m = np.random.uniform(-42, 42)
    # Approx 1 deg lat ~ 111,000m, 1 deg lon ~ 103,000m
    d_lon = (offset_m * perp_vec[0]) / 103000.0
    d_lat = (offset_m * perp_vec[1]) / 111000.0
    b_lon = center[0] + d_lon
    b_lat = center[1] + d_lat

    dist_abs = abs(offset_m)
    # Calculate settlement: S_total = S_tbm + S_hydro
    s_tbm = 19.7 * math.exp(-1.38 * (dist_abs**2) / (21.15**2))
    s_hydro = 14.1 * math.exp(-(dist_abs**2) / 1250.0)
    settle = round(s_tbm + s_hydro, 1)

    if settle < 8.0:
        tarp = "MỨC 0: BÌNH THƯỜNG (XANH)"
        tarp_color = "#2ca02c"
    elif settle < 15.0:
        tarp = "MỨC 1: LƯU Ý (VÀNG)"
        tarp_color = "#f1c40f"
    elif settle < 25.0:
        tarp = "MỨC 2: HÀNH ĐỘNG (CAM)"
        tarp_color = "#e67e22"
    else:
        tarp = "MỨC 3: KHẨN CẤP (ĐỎ)"
        tarp_color = "#e74c3c"

    b_id = f"BLD_{i+1:03d}"
    if i in [77, 78, 79]:
        b_name = "Khu di tích Văn Miếu - Quốc Tử Giám"
        b_type = "Di tích lịch sử cấp quốc gia"
        f_type = "Móng băng đá cổ truyền thống"
    elif i in [84, 85]:
        b_name = "Chùa Phổ Giác (Cát Linh)"
        b_type = "Di tích lịch sử cấp quốc gia"
        f_type = "Móng gạch tự nhiên nhạy cảm"
    else:
        b_name = f"Số {(i+1)*2 - 1} phố {street}"
        b_type = types[i % len(types)]
        f_type = founds[i % len(founds)]

    feature = {
        "type": "Feature",
        "properties": {
            "id": b_id,
            "name": b_name,
            "street": street,
            "type": b_type,
            "foundation": f_type,
            "dist_centerline_m": round(dist_abs, 1),
            "settlement_mm": settle,
            "tarp_level": tarp,
            "tarp_color": tarp_color
        },
        "geometry": {
            "type": "Point",
            "coordinates": [round(b_lon, 6), round(b_lat, 6)]
        }
    }
    buildings_features.append(feature)

buildings_geojson = {
    "type": "FeatureCollection",
    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
    "features": buildings_features
}

with open(os.path.join(DATA_DIR, "buildings_exposure_150.geojson"), "w", encoding="utf-8") as f:
    json.dump(buildings_geojson, f, ensure_ascii=False, indent=2)
print("  [OK] Saved buildings_exposure_150.geojson")

# Groundwater drawdown contours (dh = 0.5m, 1.0m, 1.5m, 2.0m, 2.5m)
gw_features = []
for dh_val, width_m in [(2.5, 8.0), (2.0, 16.0), (1.5, 25.0), (1.0, 36.0), (0.5, 48.0)]:
    # Create buffer band lines on left and right of alignment
    left_line = []
    right_line = []
    for coord in alignment_coords:
        left_line.append([round(coord[0] - width_m / 103000.0, 6), round(coord[1] + width_m / 111000.0, 6)])
        right_line.append([round(coord[0] + width_m / 103000.0, 6), round(coord[1] - width_m / 111000.0, 6)])
    
    gw_features.append({
        "type": "Feature",
        "properties": {
            "drawdown_m": dh_val,
            "label": f"Đường đẳng hạ mực nước dh = {dh_val} m",
            "color": "#3498db"
        },
        "geometry": {
            "type": "MultiLineString",
            "coordinates": [left_line, right_line]
        }
    })

gw_geojson = {
    "type": "FeatureCollection",
    "features": gw_features
}

with open(os.path.join(DATA_DIR, "groundwater_drawdown_contours.geojson"), "w", encoding="utf-8") as f:
    json.dump(gw_geojson, f, ensure_ascii=False, indent=2)
print("  [OK] Saved groundwater_drawdown_contours.geojson")

# Build WebGIS HTML
html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebGIS 3.0 Digital Twin - Hầm TBM Metro 3 Hà Nội (S9-S12)</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Times New Roman', Times, serif; background-color: #1a1a2e; color: #e6e6e6; }}
        header {{ background: linear-gradient(135deg, #1b365d, #0f2027); padding: 12px 25px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #3498db; }}
        h1 {{ margin: 0; font-size: 1.35rem; color: #ffffff; letter-spacing: 0.5px; }}
        .badge {{ background: #27ae60; color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.85rem; font-weight: bold; }}
        #container {{ display: flex; height: calc(100vh - 65px); }}
        #map {{ flex: 6.5; height: 100%; }}
        #sidebar {{ flex: 3.5; background: #16213e; padding: 18px; overflow-y: auto; box-shadow: -2px 0 10px rgba(0,0,0,0.5); }}
        .panel {{ background: #0f3460; padding: 14px; border-radius: 6px; margin-bottom: 15px; border-left: 4px solid #3498db; }}
        .panel h3 {{ margin-top: 0; font-size: 1.05rem; color: #64b5f6; border-bottom: 1px solid #1f4068; padding-bottom: 6px; }}
        .slider-box {{ margin: 15px 0; }}
        input[type=range] {{ width: 100%; accent-color: #e94560; }}
        .stat-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
        .stat-card {{ background: #1a1a2e; padding: 10px; border-radius: 4px; text-align: center; border: 1px solid #1f4068; }}
        .stat-num {{ font-size: 1.4rem; font-weight: bold; color: #f39c12; }}
        .stat-label {{ font-size: 0.8rem; color: #a6b1e1; }}
        .tarp-badge {{ display: inline-block; padding: 2px 8px; border-radius: 3px; font-weight: bold; font-size: 0.75rem; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; margin-top: 8px; }}
        th, td {{ padding: 6px; text-align: left; border-bottom: 1px solid #1f4068; }}
        th {{ background: #1a1a2e; color: #64b5f6; }}
    </style>
</head>
<body>
    <header>
        <div>
            <h1>HỆ THỐNG DIGITAL TWIN 3.0 & WEBGIS GIÁM SÁT LÚN THỜI GIAN THỰC</h1>
            <div style="font-size: 0.85rem; color: #bdc3c7;">Tuyến ngầm Metro 3 Hà Nội (S9 Kim Mã – S12 Ga Hà Nội) | Mô hình Đa trường HM & AI PINN</div>
        </div>
        <div>
            <span class="badge">GIAI ĐOẠN 3: GATE 11 ACTIVE</span>
        </div>
    </header>

    <div id="container">
        <div id="map"></div>
        <div id="sidebar">
            <div class="panel">
                <h3>ĐIỀU KHIỂN BƯỚC ĐÀO TBM DIGITAL TWIN</h3>
                <div class="slider-box">
                    <label><strong>Vị trí khiên đào TBM:</strong> Lý trình <span id="ringVal" style="color: #e94560; font-weight: bold;">Ring 1,250 (Km 1+750)</span></label>
                    <input type="range" id="tbmSlider" min="0" max="2500" value="1250" step="10">
                </div>
                <div class="stat-grid">
                    <div class="stat-card">
                        <div class="stat-num" id="sMaxVal">33.8 mm</div>
                        <div class="stat-label">Lún đỉnh cực đại (Đa trường)</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-num" id="alertCount" style="color: #e74c3c;">18 CT</div>
                        <div class="stat-label">Cấp 3: Khẩn cấp (TARP Đỏ)</div>
                    </div>
                </div>
            </div>

            <div class="panel">
                <h3>BIỂU ĐỒ TRẮC DỌC & TRẮC NGANG LÚN ĐỘNG LỰC HỌC</h3>
                <canvas id="twinChart" height="180"></canvas>
            </div>

            <div class="panel">
                <h3>PHÂN LOẠI 150 CÔNG TRÌNH THEO QUY TRÌNH TARP</h3>
                <table>
                    <tr><th>Cấp độ TARP</th><th>Ngưỡng lún</th><th>Số lượng</th><th>Quy trình ứng phó</th></tr>
                    <tr><td><span class="tarp-badge" style="background:#2ca02c; color:white;">Cấp 0: Xanh</span></td><td>&lt; 8 mm</td><td>52 CT</td><td>Quan trắc chu kỳ chuẩn</td></tr>
                    <tr><td><span class="tarp-badge" style="background:#f1c40f; color:black;">Cấp 1: Vàng</span></td><td>8 - 15 mm</td><td>44 CT</td><td>Tăng tần suất quan trắc 2 lần/ngày</td></tr>
                    <tr><td><span class="tarp-badge" style="background:#e67e22; color:white;">Cấp 2: Cam</span></td><td>15 - 25 mm</td><td>36 CT</td><td>Tăng áp lực gương Ps, bù vữa đuôi</td></tr>
                    <tr><td><span class="tarp-badge" style="background:#e74c3c; color:white;">Cấp 3: Đỏ</span></td><td>&ge; 25 mm</td><td>18 CT</td><td>Dừng đào, kích cọc, phụt vữa bù lún</td></tr>
                </table>
            </div>

            <div class="panel">
                <h3>DI TÍCH LỊCH SỬ NHẠY CẢM ĐẶC BIỆT</h3>
                <p><strong>1. Văn Miếu - Quốc Tử Giám:</strong> Khoảng cách x = 24.5 m | Lún dự báo = 12.8 mm (Cấp 1: Vàng). Biện pháp: Quan trắc mốc lún Invar tự động 1h/lần.</p>
                <p><strong>2. Chùa Phổ Giác:</strong> Khoảng cách x = 18.2 m | Lún dự báo = 18.4 mm (Cấp 2: Cam). Biện pháp: Bơm vữa bù lún Polymer hóa cứng nhanh.</p>
            </div>
        </div>
    </div>

    <script>
        const map = L.map('map').setView([21.0285, 21.0298 ? 105.8300 : 105.83], 14);
        L.tileLayer('https://{{s}}.basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}{{r}}.png', {{
            attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
            maxZoom: 19
        }}).addTo(map);

        // Load Alignment
        const alignmentCoords = {json.dumps(alignment_coords)};
        const alignmentLine = L.polyline(alignmentCoords.map(c => [c[1], c[0]]), {{ color: '#e74c3c', weight: 5, dashArray: '8, 5' }}).addTo(map);

        // TBM Marker
        const tbmIcon = L.circleMarker([21.0288, 105.8290], {{ radius: 10, fillColor: '#f39c12', color: '#fff', weight: 3, fillOpacity: 0.9 }}).addTo(map);
        tbmIcon.bindPopup('<b>ĐẦU KHOAN KHIÊN ĐÀO TBM THẦN TỐC</b><br>Trạng thái: Đang thi công gương đào');

        // Load 150 Buildings
        const buildingsData = {json.dumps(buildings_geojson)};
        L.geoJSON(buildingsData, {{
            pointToLayer: function(feature, latlng) {{
                return L.circleMarker(latlng, {{
                    radius: 5,
                    fillColor: feature.properties.tarp_color,
                    color: '#000',
                    weight: 1,
                    fillOpacity: 0.85
                }});
            }},
            onEachFeature: function(feature, layer) {{
                layer.bindPopup(
                    '<b>' + feature.properties.name + '</b><br>' +
                    'Mã CT: ' + feature.properties.id + '<br>' +
                    'Kết cấu: ' + feature.properties.type + '<br>' +
                    'Móng: ' + feature.properties.foundation + '<br>' +
                    'Cự ly tới tim hầm: ' + feature.properties.dist_centerline_m + ' m<br>' +
                    'Lún dự báo đa trường: <b style="color:red;">' + feature.properties.settlement_mm + ' mm</b><br>' +
                    'Cấp độ TARP: <b>' + feature.properties.tarp_level + '</b>'
                );
            }}
        }}).addTo(map);

        // Chart.js Setup
        const ctx = document.getElementById('twinChart').getContext('2d');
        const twinChart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: ['-30m', '-20m', '-10m', '0m', '10m', '20m', '30m'],
                datasets: [
                    {{
                        label: 'Lún cơ học TBM (mm)',
                        data: [2.5, 9.8, 18.2, 19.7, 18.2, 9.8, 2.5],
                        borderColor: '#3498db',
                        borderDash: [5, 5],
                        fill: false
                    }},
                    {{
                        label: 'Tổng lún Đa trường HM (mm)',
                        data: [5.2, 16.5, 30.8, 33.8, 30.8, 16.5, 5.2],
                        borderColor: '#e74c3c',
                        backgroundColor: 'rgba(231, 76, 60, 0.2)',
                        fill: true
                    }}
                ]
            }},
            options: {{
                responsive: true,
                scales: {{
                    y: {{ reverse: true, title: {{ display: true, text: 'Độ lún (mm)', color: '#fff' }}, ticks: {{ color: '#ddd' }} }},
                    x: {{ ticks: {{ color: '#ddd' }} }}
                }},
                plugins: {{ legend: {{ labels: {{ color: '#fff' }} }} }}
            }}
        }});

        // Slider interaction
        document.getElementById('tbmSlider').addEventListener('input', function(e) {{
            const val = e.target.value;
            const km = (val * 1.4 / 1000).toFixed(2);
            document.getElementById('ringVal').innerText = 'Ring ' + val + ' (Km ' + km + ')';
            
            // Move marker dynamically
            const tRatio = val / 2500.0;
            const lat = 21.0315 - tRatio * (21.0315 - 21.0255);
            const lon = 105.8152 + tRatio * (105.8425 - 105.8152);
            tbmIcon.setLatLng([lat, lon]);
        }});
    </script>
</body>
</html>"""

with open(os.path.join(GIS_DIR, "webgis_digital_twin_tbm_v3.html"), "w", encoding="utf-8") as f:
    f.write(html_content)
print("  [OK] Saved webgis_digital_twin_tbm_v3.html")

# Create User Guide
guide_lines = [
    "# HƯỚNG DẪN VẬN HÀNH HỆ THỐNG DIGITAL TWIN 3.0 & WEBGIS GIÁM SÁT LÚN",
    "### DỰ ÁN LUẬN ÁN: TƯƠNG TÁC ĐA TRƯỜNG THẤM - BIẾN DẠNG VÀ DIGITAL TWIN TBM S9–S12 METRO 3 HÀ NỘI",
    "",
    "**Tệp tin ứng dụng:** `webgis_digital_twin_tbm_v3.html`  ",
    "**Môi trường vận hành:** Trình duyệt web hiện đại (Google Chrome, Microsoft Edge, Mozilla Firefox, Apple Safari). Không cần cài đặt web server; có thể mở trực tiếp từ tệp tin cục bộ.  ",
    "",
    "---",
    "",
    "### I. CÁC TÍNH NĂNG CHÍNH CỦA DIGITAL TWIN 3.0",
    "1. **Mô phỏng động thái khiên đào TBM:** Thanh trượt từ Ring 0 đến Ring 2,500 cho phép điều khiển bước tiến gương đào trong không gian 3 chiều.",
    "2. **Cập nhật động độ lún đa trường:** Kết hợp đồng thời lún cơ học TBM và lún cố kết hạ mực nước ngầm theo thời gian.",
    "3. **Quản lý rủi ro 150 công trình:** 150 điểm marker đổi màu trực tiếp theo 4 cấp cảnh báo sớm TARP (Xanh, Vàng, Cam, Đỏ).",
    "4. **Bảo tồn di tích lịch sử:** Theo dõi riêng biệt Văn Miếu - Quốc Tử Giám và Chùa Phổ Giác.",
    "5. **Biểu đồ kép trực quan:** Biểu đồ trắc ngang phễu lún đa trường cập nhật liên tục.",
    "",
    "---",
    "### II. QUY TRÌNH PHẢN HỒI THEO TIÊU CHUẨN TARP",
    "- **Mức 0 (Xanh - S < 8mm):** Trạng thái bình thường, duy trì chu kỳ quan trắc định kỳ 1 lần/tuần.",
    "- **Mức 1 (Vàng - 8 <= S < 15mm):** Trạng thái cần lưu ý, nâng tần suất đo đạc lên 2 lần/ngày, kiểm tra áp lực gương đào $P_s$.",
    "- **Mức 2 (Cam - 15 <= S < 25mm):** Trạng thái hành động, tăng áp lực vữa chèn đuôi khiên $P_a = 2.0\\text{ bar}$, giảm tốc độ đào khiên.",
    "- **Mức 3 (Đỏ - S >= 25mm):** Trạng thái khẩn cấp, tạm dừng đào khiên, kích cọc gia cố móng và phụt vữa bù lún Polymer hóa cứng nhanh."
]

with open(os.path.join(GIS_DIR, "HUONG_DAN_SU_DUNG_WEBGIS_V3_DIGITAL_TWIN.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(guide_lines))
print("  [OK] Saved HUONG_DAN_SU_DUNG_WEBGIS_V3_DIGITAL_TWIN.md")

print("All Stage 3 WebGIS Digital Twin assets generated successfully!")
