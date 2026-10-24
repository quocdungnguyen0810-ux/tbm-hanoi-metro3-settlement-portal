# -*- coding: utf-8 -*-
"""
Script xây dựng trọn bộ hệ thống WebGIS tương tác giám sát lún và rủi ro công trình
đoạn S9–S12 Metro Tuyến 3 Hà Nội, phục vụ nghiệm thu Bộ môn Địa kỹ thuật & Không gian ngầm.
"""

import json
import math
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "nhiem_vu_luan_an" / "05_he_thong_webgis_tuong_tac"
DATA_DIR = OUT_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 1. Trục tọa độ các ga ngầm S9–S12 (WGS-84)
# S9 (Ga Kim Mã): Km 8.400 -> [21.0315, 105.8142]
# S10 (Ga Cát Linh): Km 9.400 -> [21.0281, 105.8278]
# S11 (Ga Văn Miếu): Km 10.400 -> [21.0264, 105.8361]
# S12 (Ga Hà Nội): Km 11.500 -> [21.0242, 105.8423]

STATIONS = [
    {"id": "S9", "name": "Ga S9 - Kim Mã", "lat": 21.0315, "lng": 105.8142, "km": 8.400, "z0": 15.0, "type": "Ga ngầm trung chuyển"},
    {"id": "S10", "name": "Ga S10 - Cát Linh", "lat": 21.0281, "lng": 105.8278, "km": 9.400, "z0": 16.5, "type": "Ga ngầm kết nối Tuyến 2A"},
    {"id": "S11", "name": "Ga S11 - Văn Miếu", "lat": 21.0264, "lng": 105.8361, "km": 10.400, "z0": 18.0, "type": "Ga ngầm khu vực di tích"},
    {"id": "S12", "name": "Ga S12 - Ga Hà Nội", "lat": 21.0242, "lng": 105.8423, "km": 11.500, "z0": 18.0, "type": "Ga ngầm trung tâm đường sắt quốc gia"}
]

# Hàm tính toán tọa độ theo lý trình km và khoảng cách lệch tim offset_m
def get_coords_at_chainage_and_offset(km, offset_m):
    # Xác định đoạn tim hầm
    if km <= STATIONS[1]["km"]:
        st_a, st_b = STATIONS[0], STATIONS[1]
    elif km <= STATIONS[2]["km"]:
        st_a, st_b = STATIONS[1], STATIONS[2]
    else:
        st_a, st_b = STATIONS[2], STATIONS[3]
    
    # Tỷ lệ nội suy u
    span_km = st_b["km"] - st_a["km"]
    u = (km - st_a["km"]) / span_km if span_km > 0 else 0.0
    u = max(0.0, min(1.0, u))
    
    base_lat = st_a["lat"] + u * (st_b["lat"] - st_a["lat"])
    base_lng = st_a["lng"] + u * (st_b["lng"] - st_a["lng"])
    
    # Vector chỉ phương đoạn hầm (đổi sang mét xấp xỉ tại Hà Nội ~21 độ vĩ Bắc)
    # 1 độ vĩ ~ 110,800 m, 1 độ kinh ~ 103,800 m
    dx_m = (st_b["lng"] - st_a["lng"]) * 103800.0
    dy_m = (st_b["lat"] - st_a["lat"]) * 110800.0
    length_m = math.sqrt(dx_m**2 + dy_m**2)
    
    if length_m == 0:
        return base_lat, base_lng
    
    # Vector pháp tuyến đơn vị quay phải 90 độ (phía Phải = dương, phía Trái = âm)
    # T = (dx/L, dy/L) -> N = (dy/L, -dx/L)
    nx = dy_m / length_m
    ny = -dx_m / length_m
    
    offset_east_m = offset_m * nx
    offset_north_m = offset_m * ny
    
    bld_lat = base_lat + offset_north_m / 110800.0
    bld_lng = base_lng + offset_east_m / 103800.0
    
    return bld_lat, bld_lng


def main():
    print("Bắt đầu xây dựng hệ thống WebGIS tương tác...")
    
    # 2. Đọc file Excel 60 công trình
    excel_path = ROOT / "nhiem_vu_luan_an" / "02_du_lieu_excel_chuyen_nghiep" / "TBM_BUILDING_RISK_EXPOSURE.xlsx"
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    ws = wb['Danh_Muc_60_Cong_Trinh']
    
    buildings = []
    building_features = []
    
    for r in range(5, 65):
        bld_id = ws.cell(r, 2).value
        name = ws.cell(r, 3).value
        km = float(ws.cell(r, 4).value)
        section = ws.cell(r, 5).value
        offset = float(ws.cell(r, 6).value)
        structure = ws.cell(r, 7).value
        floors = int(ws.cell(r, 8).value) if ws.cell(r, 8).value else 3
        foundation = ws.cell(r, 9).value
        s_10 = float(ws.cell(r, 10).value)
        theta_10 = float(ws.cell(r, 11).value)
        risk_10 = ws.cell(r, 12).value
        s_20 = float(ws.cell(r, 13).value)
        risk_20 = ws.cell(r, 14).value
        priority = ws.cell(r, 15).value
        
        bld_lat, bld_lng = get_coords_at_chainage_and_offset(km, offset)
        
        bld_data = {
            'id': bld_id,
            'name': name,
            'km': km,
            'section': section,
            'offset': offset,
            'structure': structure,
            'floors': floors,
            'foundation': foundation,
            's_10': s_10,
            'theta_10': theta_10,
            'risk_10': risk_10,
            's_20': s_20,
            'risk_20': risk_20,
            'priority': priority,
            'lat': round(bld_lat, 6),
            'lng': round(bld_lng, 6)
        }
        buildings.append(bld_data)
        
        # Tạo polygon mô phỏng mặt bằng nhà (~14m x 16m)
        w_lat = 0.00007
        w_lng = 0.00008
        poly = [
            [bld_lng - w_lng, bld_lat - w_lat],
            [bld_lng + w_lng, bld_lat - w_lat],
            [bld_lng + w_lng, bld_lat + w_lat],
            [bld_lng - w_lng, bld_lat + w_lat],
            [bld_lng - w_lng, bld_lat - w_lat]
        ]
        
        building_features.append({
            "type": "Feature",
            "properties": bld_data,
            "geometry": {
                "type": "Polygon",
                "coordinates": [poly]
            }
        })
        
    print(f"Đã nạp và định vị {len(buildings)} công trình.")
    
    # 3. Xuất GeoJSON Các Ga và Tuyến hầm
    station_features = []
    for st in STATIONS:
        station_features.append({
            "type": "Feature",
            "properties": {
                "id": st["id"],
                "name": st["name"],
                "km": st["km"],
                "z0": st["z0"],
                "type": st["type"]
            },
            "geometry": {
                "type": "Point",
                "coordinates": [st["lng"], st["lat"]]
            }
        })
    
    stations_geojson = {
        "type": "FeatureCollection",
        "name": "hanoi_metro3_stations_s9_s12",
        "features": station_features
    }
    (DATA_DIR / "stations_wgs84.geojson").write_text(json.dumps(stations_geojson, indent=2, ensure_ascii=False), encoding="utf-8")
    
    # Tuyến hầm đôi
    center_coords = [[st["lng"], st["lat"]] for st in STATIONS]
    # Hầm Bắc (offset +6.5m) và Hầm Nam (offset -6.5m)
    north_coords = []
    south_coords = []
    for st in STATIONS:
        n_lat, n_lng = get_coords_at_chainage_and_offset(st["km"], 6.5)
        s_lat, s_lng = get_coords_at_chainage_and_offset(st["km"], -6.5)
        north_coords.append([round(n_lng, 6), round(n_lat, 6)])
        south_coords.append([round(s_lng, 6), round(s_lat, 6)])
        
    alignment_features = [
        {
            "type": "Feature",
            "properties": {"name": "Tuyến hầm đôi TBM - Tim tuyến thiết kế", "diameter_m": 6.3, "color": "#1e3c72"},
            "geometry": {"type": "LineString", "coordinates": center_coords}
        },
        {
            "type": "Feature",
            "properties": {"name": "Ống hầm TBM Phải (Bắc)", "diameter_m": 6.3, "color": "#0056b3"},
            "geometry": {"type": "LineString", "coordinates": north_coords}
        },
        {
            "type": "Feature",
            "properties": {"name": "Ống hầm TBM Trái (Nam)", "diameter_m": 6.3, "color": "#0056b3"},
            "geometry": {"type": "LineString", "coordinates": south_coords}
        }
    ]
    alignment_geojson = {
        "type": "FeatureCollection",
        "name": "hanoi_metro3_alignment_s9_s12",
        "features": alignment_features
    }
    (DATA_DIR / "alignment_wgs84.geojson").write_text(json.dumps(alignment_geojson, indent=2, ensure_ascii=False), encoding="utf-8")
    
    # Xuất GeoJSON 60 công trình
    buildings_geojson = {
        "type": "FeatureCollection",
        "name": "buildings_exposure_60_s9_s12",
        "features": building_features
    }
    (DATA_DIR / "buildings_exposure_60.geojson").write_text(json.dumps(buildings_geojson, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Đã xuất thành công 3 file GeoJSON.")
    
    # 4. Tạo file HTML WebGIS tương tác hoàn chỉnh
    generate_interactive_webgis_html(buildings)
    
    # 5. Tạo file hướng dẫn sử dụng WebGIS
    create_webgis_user_guide()
    
    print("Hoàn tất xây dựng gói WebGIS!")


def generate_interactive_webgis_html(buildings):
    buildings_json_str = json.dumps(buildings, ensure_ascii=False)
    stations_json_str = json.dumps(STATIONS, ensure_ascii=False)
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hệ thống WebGIS Giám sát & Dự báo Lún TBM Metro Tuyến 3 Hà Nội (S9–S12)</title>
    <!-- Leaflet CSS & JS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
    <style>
        :root {{
            --primary: #1e3c72;
            --primary-dark: #122549;
            --secondary: #2a5298;
            --accent: #e74c3c;
            --bg-panel: rgba(255, 255, 255, 0.96);
            --border-color: #d1d8e0;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0; padding: 0;
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
            background: #f4f6f9;
            color: #2c3e50;
            overflow: hidden;
        }}
        #app {{ display: flex; height: 100vh; width: 100vw; position: relative; }}
        #map {{ flex: 1; height: 100%; z-index: 1; }}
        
        /* Top Navigation Header */
        .top-header {{
            position: absolute;
            top: 12px;
            left: 60px;
            z-index: 1000;
            background: var(--bg-panel);
            backdrop-filter: blur(8px);
            padding: 8px 18px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            border-left: 5px solid var(--primary);
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        .top-header h1 {{
            margin: 0; font-size: 15px; font-weight: 700; color: var(--primary);
            letter-spacing: 0.3px;
        }}
        .top-header .subtitle {{
            font-size: 12px; color: #7f8c8d; font-weight: 500;
        }}
        
        /* Control Sidebar / Floating Panel */
        .sidebar {{
            position: absolute;
            top: 12px;
            right: 12px;
            bottom: 12px;
            width: 400px;
            z-index: 1000;
            background: var(--bg-panel);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.8);
        }}
        
        .sidebar-header {{
            padding: 14px 18px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .sidebar-header h2 {{ margin: 0; font-size: 14px; font-weight: 600; }}
        .sidebar-header .badge-mode {{
            background: rgba(255,255,255,0.25);
            padding: 3px 8px; border-radius: 12px; font-size: 11px;
        }}
        
        .sidebar-content {{
            flex: 1;
            padding: 14px 18px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}
        
        .card {{
            background: #ffffff;
            border-radius: 8px;
            padding: 12px 14px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
            border: 1px solid var(--border-color);
        }}
        .card-title {{
            font-size: 12px; font-weight: 700; color: var(--primary);
            text-transform: uppercase; margin-bottom: 10px;
            display: flex; align-items: center; gap: 6px;
        }}
        
        /* Slider & Controls */
        .form-group {{ margin-bottom: 10px; }}
        .form-group label {{
            display: flex; justify-content: space-between;
            font-size: 12px; font-weight: 600; margin-bottom: 5px;
        }}
        .form-control {{
            width: 100%; padding: 6px 10px; border-radius: 5px;
            border: 1px solid #ccc; font-size: 12px;
        }}
        .slider-val {{
            color: var(--accent); font-weight: 700; font-size: 13px;
        }}
        
        /* KPI Metrics Grid */
        .metrics-grid {{
            display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
        }}
        .metric-box {{
            background: #f8f9fa; border-radius: 6px; padding: 8px 10px;
            border-left: 3px solid var(--secondary);
        }}
        .metric-box .label {{ font-size: 11px; color: #6c757d; font-weight: 500; }}
        .metric-box .value {{ font-size: 16px; font-weight: 700; color: var(--primary); margin-top: 2px; }}
        
        /* Chart container */
        .chart-container {{
            position: relative; height: 160px; width: 100%;
        }}
        
        /* Building list table */
        .table-container {{
            max-height: 180px; overflow-y: auto; font-size: 11px;
            border: 1px solid #e9ecef; border-radius: 4px;
        }}
        .bld-table {{
            width: 100%; border-collapse: collapse;
        }}
        .bld-table th {{
            position: sticky; top: 0; background: #e9ecef;
            padding: 6px; text-align: left; font-weight: 600;
        }}
        .bld-table td {{
            padding: 5px 6px; border-bottom: 1px solid #f1f2f6; cursor: pointer;
        }}
        .bld-table tr:hover {{ background: #f1f5f9; }}
        
        /* Risk Badges */
        .risk-badge {{
            display: inline-block; padding: 2px 6px; border-radius: 4px;
            font-size: 10px; font-weight: 700; color: white; text-align: center;
        }}
        .risk-c0 {{ background-color: #28a745; }}
        .risk-c1 {{ background-color: #17a2b8; }}
        .risk-c2 {{ background-color: #ffc107; color: #212529 !important; }}
        .risk-c3 {{ background-color: #fd7e14; }}
        .risk-c4 {{ background-color: #dc3545; }}
        
        /* Legend */
        .legend-box {{
            display: flex; flex-wrap: wrap; gap: 8px; font-size: 11px;
        }}
        .legend-item {{ display: flex; align-items: center; gap: 4px; }}
        .legend-color {{
            width: 12px; height: 12px; border-radius: 2px; display: inline-block;
        }}
        
        /* Station Marker Custom Icon */
        .station-icon {{
            background: #d9534f; color: white; border: 2px solid white;
            border-radius: 50%; text-align: center; font-weight: bold;
            font-size: 11px; line-height: 22px; width: 26px; height: 26px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.4);
        }}
    </style>
</head>
<body>
    <div id="app">
        <!-- Bản đồ Leaflet -->
        <div id="map"></div>
        
        <!-- Tiêu đề Header -->
        <div class="top-header">
            <div>
                <h1>METRO TUYẾN 3 HÀ NỘI (ĐOẠN S9–S12) | HỆ THỐNG WEBGIS GIÁM SÁT LÚN TBM</h1>
                <div class="subtitle">Đề tài Luận án Tiến sĩ / Thạc sĩ | Bộ môn Địa kỹ thuật & Không gian ngầm - UTC</div>
            </div>
        </div>
        
        <!-- Bảng điều khiển Sidebar -->
        <div class="sidebar">
            <div class="sidebar-header">
                <h2><i class="fa-solid fa-layer-group"></i> TRUNG TÂM DỰ BÁO LÚN TBM</h2>
                <span class="badge-mode">Peck (1969) & Burland (1995)</span>
            </div>
            
            <div class="sidebar-content">
                <!-- Điều khiển Kịch bản -->
                <div class="card">
                    <div class="card-title"><i class="fa-solid fa-sliders"></i> Kịch bản Vận hành & Địa chất</div>
                    <div class="form-group">
                        <label>
                            <span>Tổn thất thể tích (V<sub>L</sub>):</span>
                            <span class="slider-val" id="vl-text">1.00%</span>
                        </label>
                        <input type="range" id="vl-slider" min="0.5" max="2.0" step="0.1" value="1.0" class="form-control">
                    </div>
                    
                    <div class="form-group">
                        <label>Mặt cắt địa chất phân tích:</label>
                        <select id="section-select" class="form-control">
                            <option value="S9_S10">S9–S10: Kim Mã - Cát Linh (z0=15.0m, K=0.50)</option>
                            <option value="S10_S11">S10–S11: Cát Linh - Văn Miếu (z0=16.5m, K=0.55)</option>
                            <option value="S11_S12" selected>S11–S12: Văn Miếu - Ga HN (z0=18.0m, K=0.60, Bùn sét)</option>
                        </select>
                    </div>
                </div>
                
                <!-- Chỉ số KPI Kết quả tính -->
                <div class="card">
                    <div class="card-title"><i class="fa-solid fa-chart-pie"></i> Thông số Phễu lún tức thời</div>
                    <div class="metrics-grid">
                        <div class="metric-box">
                            <div class="label">Lún cực đại S<sub>max</sub>:</div>
                            <div class="value" id="kpi-smax">22.1 mm</div>
                        </div>
                        <div class="metric-box">
                            <div class="label">Bề rộng phễu lún i:</div>
                            <div class="value" id="kpi-i">10.8 m</div>
                        </div>
                        <div class="metric-box">
                            <div class="label">Độ dốc cực đại θ<sub>max</sub>:</div>
                            <div class="value" id="kpi-theta">1.24 ‰</div>
                        </div>
                        <div class="metric-box">
                            <div class="label">Vùng nguy hại (S>10mm):</div>
                            <div class="value" id="kpi-w10">±13.6 m</div>
                        </div>
                    </div>
                </div>
                
                <!-- Đồ thị Phễu lún ngang -->
                <div class="card">
                    <div class="card-title"><i class="fa-solid fa-chart-line"></i> Phân bố Lún Ngang S(x)</div>
                    <div class="chart-container">
                        <canvas id="troughChart"></canvas>
                    </div>
                </div>
                
                <!-- Danh sách 60 Công trình -->
                <div class="card">
                    <div class="card-title" style="justify-content: space-between;">
                        <span><i class="fa-solid fa-building"></i> Danh mục 60 Công trình</span>
                        <select id="filter-risk" style="font-size: 11px; padding: 2px 4px;">
                            <option value="ALL">Tất cả cấp</option>
                            <option value="C2_C3">Cấp 2 & 3 (Cần quan sát)</option>
                            <option value="PRIORITY">Ưu tiên cao</option>
                        </select>
                    </div>
                    <div class="table-container">
                        <table class="bld-table" id="bld-table">
                            <thead>
                                <tr>
                                    <th>Mã</th>
                                    <th>Khoảng cách</th>
                                    <th>Lún Sv</th>
                                    <th>Cấp Burland</th>
                                </tr>
                            </thead>
                            <tbody id="bld-tbody">
                                <!-- Dữ liệu nạp bằng Javascript -->
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <!-- Chú giải phân cấp rủi ro -->
                <div class="card">
                    <div class="card-title"><i class="fa-solid fa-shield-halved"></i> Chú giải Tiêu chuẩn Burland (1995)</div>
                    <div class="legend-box">
                        <div class="legend-item"><span class="legend-color" style="background:#28a745;"></span> Cấp 0: Không đáng kể (&lt;10mm)</div>
                        <div class="legend-item"><span class="legend-color" style="background:#17a2b8;"></span> Cấp 1: Rất nhẹ (10-15mm)</div>
                        <div class="legend-item"><span class="legend-color" style="background:#ffc107;"></span> Cấp 2: Nhẹ (15-25mm)</div>
                        <div class="legend-item"><span class="legend-color" style="background:#fd7e14;"></span> Cấp 3: Vừa (25-50mm)</div>
                        <div class="legend-item"><span class="legend-color" style="background:#dc3545;"></span> Cấp 4: Nghiêm trọng (&ge;50mm)</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Dữ liệu nạp từ Python backend
        const RAW_BUILDINGS = {buildings_json_str};
        const STATIONS = {stations_json_str};
        
        // Khởi tạo bản đồ Leaflet
        const map = L.map('map', {{
            center: [21.0280, 105.8280],
            zoom: 15,
            zoomControl: false
        }});
        L.control.zoom({{ position: 'bottomleft' }}).addTo(map);
        
        // Lớp bản đồ nền (Basemaps)
        const cartoVoyager = L.tileLayer('https://{{s}}.basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}{{r}}.png', {{
            attribution: '&copy; CARTO &copy; OpenStreetMap',
            maxZoom: 19
        }}).addTo(map);
        
        const osm = L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            attribution: '&copy; OpenStreetMap contributors'
        }});
        
        const esriSat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
            attribution: '&copy; Esri &copy; Maxar'
        }});
        
        // Vẽ Tuyến hầm ngầm (Twin tunnels)
        const stationCoords = STATIONS.map(s => [s.lat, s.lng]);
        const tunnelCenterLine = L.polyline(stationCoords, {{
            color: '#1e3c72', weight: 6, opacity: 0.85, dashArray: '10, 8'
        }}).addTo(map);
        tunnelCenterLine.bindPopup("<b>Tuyến hầm đôi TBM EPB Tuyến 3 (S9–S12)</b><br>Đường kính đào D = 6.30 m<br>Chiều dài đi ngầm: ~3.5 km");
        
        // Vẽ Các Ga ngầm S9 - S12
        const stationLayer = L.layerGroup().addTo(map);
        STATIONS.forEach(st => {{
            const divIcon = L.divIcon({{
                className: 'station-div',
                html: `<div class="station-icon">${{st.id}}</div>`,
                iconSize: [26, 26],
                iconAnchor: [13, 13]
            }});
            const marker = L.marker([st.lat, st.lng], {{ icon: divIcon }}).addTo(stationLayer);
            marker.bindPopup(`<b>${{st.name}}</b><br>Lý trình: Km ${{st.km.toFixed(3)}}<br>Độ sâu đỉnh hầm z0: ${{st.z0}} m<br>Đặc điểm: ${{st.type}}`);
        }});
        
        // Layer chứa các vùng đệm phễu lún và các công trình
        const bufferLayer = L.layerGroup().addTo(map);
        const buildingsLayer = L.layerGroup().addTo(map);
        
        // Điều khiển Layer
        const baseMaps = {{ "Bản đồ Đô thị (Voyager)": cartoVoyager, "OpenStreetMap": osm, "Ảnh Vệ tinh (Esri)": esriSat }};
        const overlayMaps = {{ "Tuyến hầm TBM": tunnelCenterLine, "Ga ngầm S9-S12": stationLayer, "Vùng đệm lún": bufferLayer, "60 Công trình": buildingsLayer }};
        L.control.layers(baseMaps, overlayMaps, {{ position: 'topleft' }}).addTo(map);
        
        // Khởi tạo đồ thị Chart.js
        const ctx = document.getElementById('troughChart').getContext('2d');
        const troughChart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: [],
                datasets: [{{
                    label: 'Độ lún S(x) (mm)',
                    data: [],
                    borderColor: '#1e3c72',
                    backgroundColor: 'rgba(30, 60, 114, 0.2)',
                    fill: true,
                    tension: 0.35,
                    borderWidth: 2,
                    pointRadius: 0
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{
                        reverse: true,
                        title: {{ display: true, text: 'Lún (mm)', font: {{ size: 10 }} }},
                        suggestedMax: 25,
                        suggestedMin: 0
                    }},
                    x: {{
                        title: {{ display: true, text: 'Khoảng cách x (m)', font: {{ size: 10 }} }}
                    }}
                }},
                plugins: {{
                    legend: {{ display: false }},
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                return 'Lún: ' + context.parsed.y.toFixed(2) + ' mm';
                            }}
                        }}
                    }}
                }}
            }}
        }});
        
        // Hàm tính toán tham số cơ học Peck
        function calculateTroughParams(vl_percent, sectionKey) {{
            const D = 6.30;
            const At = Math.PI * D * D / 4.0;
            let z0 = 18.0;
            let K = 0.60;
            
            if (sectionKey === 'S9_S10') {{
                z0 = 15.0; K = 0.50;
            }} else if (sectionKey === 'S10_S11') {{
                z0 = 16.5; K = 0.55;
            }} else {{
                z0 = 18.0; K = 0.60;
            }}
            
            const i = K * z0;
            const Vloss = (vl_percent / 100.0) * At;
            const Smax = (Vloss / (Math.sqrt(2 * Math.PI) * i)) * 1000.0; // mm
            const theta_max = (Smax / (Math.exp(0.5) * i)); // mm/m (hay 10^-3)
            
            // Bán kính vùng lún S > 10 mm
            let w10 = 0.0;
            if (Smax > 10.0) {{
                w10 = i * Math.sqrt(2.0 * Math.log(Smax / 10.0));
            }}
            
            return {{ D, At, z0, K, i, Smax, theta_max, w10 }};
        }}
        
        // Hàm phân cấp Burland (1995)
        function getBurlandRisk(Sv_mm, theta_rad_1000) {{
            if (Sv_mm < 10.0 && theta_rad_1000 < 2.0) {{
                return {{ code: 'C0', name: 'Cấp 0 (Không đáng kể)', color: '#28a745' }};
            }} else if (Sv_mm < 15.0 && theta_rad_1000 < 3.33) {{
                return {{ code: 'C1', name: 'Cấp 1 (Rất nhẹ)', color: '#17a2b8' }};
            }} else if (Sv_mm < 25.0 && theta_rad_1000 < 6.67) {{
                return {{ code: 'C2', name: 'Cấp 2 (Nhẹ)', color: '#ffc107' }};
            }} else if (Sv_mm < 50.0 && theta_rad_1000 < 13.33) {{
                return {{ code: 'C3', name: 'Cấp 3 (Vừa)', color: '#fd7e14' }};
            }} else {{
                return {{ code: 'C4', name: 'Cấp 4 (Nghiêm trọng)', color: '#dc3545' }};
            }}
        }}
        
        // Cập nhật toàn bộ hệ thống
        function updateModel() {{
            const vl = parseFloat(document.getElementById('vl-slider').value);
            document.getElementById('vl-text').innerText = vl.toFixed(2) + '%';
            
            const section = document.getElementById('section-select').value;
            const params = calculateTroughParams(vl, section);
            
            // Cập nhật KPI
            document.getElementById('kpi-smax').innerText = params.Smax.toFixed(1) + ' mm';
            document.getElementById('kpi-i').innerText = params.i.toFixed(1) + ' m';
            document.getElementById('kpi-theta').innerText = params.theta_max.toFixed(2) + ' ‰';
            document.getElementById('kpi-w10').innerText = params.w10 > 0 ? ('±' + params.w10.toFixed(1) + ' m') : '0 m';
            
            // Cập nhật Đồ thị phễu lún
            const xLabels = [];
            const yData = [];
            for (let x = -35; x <= 35; x += 1) {{
                xLabels.push(x);
                const s = params.Smax * Math.exp(-(x * x) / (2.0 * params.i * params.i));
                yData.push(s.toFixed(2));
            }}
            troughChart.data.labels = xLabels;
            troughChart.data.datasets[0].data = yData;
            troughChart.update();
            
            // Cập nhật hiển thị 60 Công trình trên bản đồ và trong bảng
            renderBuildings(params);
        }}
        
        const buildingMarkers = {{}};
        
        function renderBuildings(params) {{
            buildingsLayer.clearLayers();
            const filterVal = document.getElementById('filter-risk').value;
            const tbody = document.getElementById('bld-tbody');
            tbody.innerHTML = '';
            
            RAW_BUILDINGS.forEach(b => {{
                // Tính độ lún Sv và độ dốc theta theo tham số hiện hành
                const x = b.offset;
                const sv = params.Smax * Math.exp(-(x * x) / (2.0 * params.i * params.i));
                const theta = (Math.abs(x) / (params.i * params.i)) * sv; // mm/m hay 10^-3
                const risk = getBurlandRisk(sv, theta);
                
                // Lọc danh sách
                let passFilter = true;
                if (filterVal === 'C2_C3' && (risk.code !== 'C2' && risk.code !== 'C3' && risk.code !== 'C4')) {{
                    passFilter = false;
                }}
                if (filterVal === 'PRIORITY' && b.priority !== 'ƯU TIÊN CAO') {{
                    passFilter = false;
                }}
                
                // Vẽ mặt bằng công trình (polygon)
                const w_lat = 0.00007;
                const w_lng = 0.00008;
                const bounds = [
                    [b.lat - w_lat, b.lng - w_lng],
                    [b.lat + w_lat, b.lng + w_lng]
                ];
                
                const rect = L.rectangle(bounds, {{
                    color: risk.color,
                    weight: 2,
                    fillColor: risk.color,
                    fillOpacity: 0.7
                }}).addTo(buildingsLayer);
                
                const popupContent = `
                    <div style="font-size:12px; line-height:1.4;">
                        <h4 style="margin:0 0 6px 0; color:#1e3c72; border-bottom:1px solid #ccc; padding-bottom:3px;">
                            ${{b.id}} - ${{b.name}}
                        </h4>
                        <b>Lý trình:</b> Km ${{b.km.toFixed(3)}} (${{b.section}})<br>
                        <b>Khoảng cách tim hầm:</b> ${{b.offset > 0 ? ('+' + b.offset.toFixed(1) + ' m (Phải)') : (b.offset.toFixed(1) + ' m (Trái)')}}<br>
                        <b>Kết cấu:</b> ${{b.structure}} (${{b.floors}} tầng)<br>
                        <b>Loại móng:</b> ${{b.foundation}}<br>
                        <hr style="margin:4px 0; border:none; border-top:1px dashed #eee;">
                        <b>Độ lún dự báo Sv:</b> <span style="font-size:13px; font-weight:bold; color:${{risk.color}};">${{sv.toFixed(2)}} mm</span><br>
                        <b>Độ dốc móng θ:</b> ${{theta.toFixed(3)}} &times; 10<sup>-3</sup><br>
                        <b>Phân cấp rủi ro Burland:</b> <span class="risk-badge" style="background:${{risk.color}};">${{risk.name}}</span><br>
                        <b>Ưu tiên bảo vệ:</b> <b>${{b.priority}}</b>
                    </div>
                `;
                rect.bindPopup(popupContent);
                buildingMarkers[b.id] = rect;
                
                // Thêm vào bảng danh mục nếu vượt qua bộ lọc
                if (passFilter) {{
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td><strong>${{b.id}}</strong></td>
                        <td>${{b.offset.toFixed(1)}} m</td>
                        <td style="font-weight:bold; color:${{risk.color}};">${{sv.toFixed(1)}} mm</td>
                        <td><span class="risk-badge" style="background:${{risk.color}};">${{risk.code}}</span></td>
                    `;
                    tr.onclick = function() {{
                        map.flyTo([b.lat, b.lng], 18);
                        rect.openPopup();
                    }};
                    tbody.appendChild(tr);
                }}
            }});
        }}
        
        // Lắng nghe sự kiện
        document.getElementById('vl-slider').addEventListener('input', updateModel);
        document.getElementById('section-select').addEventListener('change', updateModel);
        document.getElementById('filter-risk').addEventListener('change', function() {{
            const vl = parseFloat(document.getElementById('vl-slider').value);
            const section = document.getElementById('section-select').value;
            const params = calculateTroughParams(vl, section);
            renderBuildings(params);
        }});
        
        // Khởi động mô hình lần đầu
        updateModel();
    </script>
</body>
</html>
"""
    webgis_file = OUT_DIR / "webgis_settlement_map.html"
    webgis_file.write_text(html, encoding="utf-8")
    print(f"Đã tạo file WebGIS HTML tại: {webgis_file}")


def create_webgis_user_guide():
    guide_content = """# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG WEBGIS TƯƠNG TÁC GIÁM SÁT LÚN TBM
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
   - **Thanh trượt Tổn thất Thể tích $V_L$ ($0.5\\% \\div 2.0\\%$):** Kéo thanh trượt để quan sát phễu lún và nguy cơ công trình thay đổi tức thời (Real-time).
   - **Chọn mặt cắt địa chất:** Lựa chọn giữa S9–S10 (Kim Mã, $z_0=15\\text{ m}$), S10–S11 (Cát Linh, $z_0=16.5\\text{ m}$) và S11–S12 (Văn Miếu, $z_0=18.0\\text{ m}$, tầng bùn sét dày $12.7\\text{ m}$).
   - **Bảng chỉ số KPI:** Tự động tính toán $S_{\\max}$, bề rộng phễu lún $i$, độ dốc cực đại $\\theta_{\\max}$ và bán kính vùng ảnh hưởng nguy hại ($S > 10\\text{ mm}$).
   - **Đồ thị Phễu lún ngang:** Trực quan hóa hình học mặt cắt lún ngang $S(x)$ trong dải $\\pm 35\\text{ m}$.
4. **Tra cứu và kiểm tra 60 Công trình:**
   - Nhấp vào bất kỳ hình chữ nhật công trình nào trên bản đồ để mở Popup hiển thị đầy đủ: Mã công trình, Tên địa chỉ, Lý trình, Khoảng cách tim hầm, Kết cấu, Số tầng, Loại móng, Độ lún tính toán, Độ nghiêng góc xoay $\\theta$, Cấp rủi ro Burland và Mức độ ưu tiên bảo vệ.
   - Nhấp vào hàng tương ứng trong bảng danh mục phía dưới sidebar để tự động zoom (FlyTo) đến vị trí công trình trên bản đồ.

---

### III. QUY CHUẨN MÀU SẮC RỦI RO (BURLAND 1995)
- **Màu Xanh lá (Cấp 0):** Không đáng kể ($S_v < 10\\text{ mm}, \\theta < 2.0 \\times 10^{-3}$).
- **Màu Xanh lơ (Cấp 1):** Rất nhẹ ($10 \\le S_v < 15\\text{ mm}$).
- **Màu Vàng (Cấp 2):** Nhẹ ($15 \\le S_v < 25\\text{ mm}$, xuất hiện vết nứt chân chim).
- **Màu Cam (Cấp 3):** Trung bình ($25 \\le S_v < 50\\text{ mm}$, nứt kết cấu, cần gia cố hoặc quan trắc đặc biệt).
- **Màu Đỏ (Cấp 4):** Nghiêm trọng ($S_v \\ge 50\\text{ mm}$, nguy cơ mất an toàn kết cấu).
"""
    (OUT_DIR / "HUONG_DAN_SU_DUNG_WEBGIS.md").write_text(guide_content, encoding="utf-8")
    print("Đã tạo tài liệu HUONG_DAN_SU_DUNG_WEBGIS.md.")


if __name__ == "__main__":
    main()
