"""Spatial engine and WebGIS Leaflet generator for Gate 4 (WF-14).

Builds WGS-84 GeoJSON layers:
1. S9-S12 Twin Tunnel Alignment
2. Stations S9, S10, S11, S12
3. Settlement trough buffer zones (5mm, 10mm, 20mm)
4. Synthetic building footprints with exposure and risk tags
5. Interactive standalone WebGIS HTML map with Leaflet.js
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "research_outputs" / "2026-10-13_152753"
DATA_DIR = OUT_DIR / "03_processed_data"
TABLE_DIR = OUT_DIR / "06_tables"
DATA_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)

# Station Coordinates (WGS-84: [lng, lat])
STATIONS = [
    {"id": "S9", "name": "Ga S9 - Kim Mã", "coords": [105.8142, 21.0315], "chainage": 0},
    {"id": "S10", "name": "Ga S10 - Cát Linh", "coords": [105.8278, 21.0281], "chainage": 1500},
    {"id": "S11", "name": "Ga S11 - Văn Miếu", "coords": [105.8361, 21.0264], "chainage": 2400},
    {"id": "S12", "name": "Ga S12 - Ga Hà Nội", "coords": [105.8423, 21.0242], "chainage": 3100}
]


def build_alignment_geojson():
    # Stations feature collection
    station_features = []
    for st in STATIONS:
        station_features.append({
            "type": "Feature",
            "properties": {
                "station_id": st["id"],
                "name": st["name"],
                "chainage_m": st["chainage"],
                "type": "underground_station"
            },
            "geometry": {
                "type": "Point",
                "coordinates": st["coords"]
            }
        })
        
    line_coords = [st["coords"] for st in STATIONS]
    
    # Twin tunnel alignment lines (slightly offset ~13m, ~0.00012 deg)
    tunnel_features = [
        {
            "type": "Feature",
            "properties": {"tunnel": "TBM_North", "status": "planned", "diameter_m": 6.3},
            "geometry": {"type": "LineString", "coordinates": line_coords}
        },
        {
            "type": "Feature",
            "properties": {"tunnel": "TBM_South", "status": "planned", "diameter_m": 6.3},
            "geometry": {
                "type": "LineString", 
                "coordinates": [[c[0], c[1] - 0.00012] for c in line_coords]
            }
        }
    ]
    
    geojson = {
        "type": "FeatureCollection",
        "name": "hanoi_metro3_s9_s12_alignment",
        "features": station_features + tunnel_features
    }
    
    path = DATA_DIR / "alignment_wgs84.geojson"
    path.write_text(json.dumps(geojson, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved: {path.name}")
    return geojson


def build_buildings_geojson():
    """Generates synthetic nearby buildings with risk levels for demonstration."""
    import random
    random.seed(42)
    
    features = []
    num_buildings = 60
    
    # Sample along alignment segments
    for i in range(num_buildings):
        t = random.random()
        # Pick random segment between stations
        seg_idx = random.randint(0, len(STATIONS) - 2)
        p1 = STATIONS[seg_idx]["coords"]
        p2 = STATIONS[seg_idx + 1]["coords"]
        
        # Base point on tunnel axis
        base_lng = p1[0] + t * (p2[0] - p1[0])
        base_lat = p1[1] + t * (p2[1] - p1[1])
        
        # Lateral offset distance (m): from -50m to +50m
        offset_m = random.uniform(-45.0, 45.0)
        # In degrees (~111,000 m per deg lat, ~103,000 m per deg lng)
        d_lat = (offset_m / 111000.0) * random.choice([-1, 1])
        d_lng = (offset_m / 103000.0) * random.choice([-1, 1])
        
        b_lng = base_lng + d_lng
        b_lat = base_lat + d_lat
        
        dist_axis = abs(offset_m)
        
        # Calculate synthetic settlement at VL = 1.0% (Smax ~ 20mm, i ~ 9m)
        # S = 20 * exp(-dist^2 / (2 * 9^2))
        settlement_mm = 22.0 * math.exp(-(dist_axis ** 2) / (2.0 * (9.0 ** 2)))
        
        if settlement_mm >= 15.0:
            risk = "Severe"
            color = "#d9534f"
        elif settlement_mm >= 8.0:
            risk = "Moderate"
            color = "#f0ad4e"
        elif settlement_mm >= 3.0:
            risk = "Slight"
            color = "#5bc0de"
        else:
            risk = "Negligible"
            color = "#5cb85c"
            
        # Create a small polygon (~15m x 15m)
        w = 0.00015
        poly_coords = [
            [b_lng - w, b_lat - w],
            [b_lng + w, b_lat - w],
            [b_lng + w, b_lat + w],
            [b_lng - w, b_lat + w],
            [b_lng - w, b_lat - w]
        ]
        
        features.append({
            "type": "Feature",
            "properties": {
                "building_id": f"BLD_{i+1:03d}",
                "name": f"Công trình nhà dân #{i+1}",
                "type": random.choice(["Nhà ống 4-5 tầng", "Chung cư cũ", "Trụ sở cơ quan", "Công trình di tích"]),
                "distance_to_axis_m": round(dist_axis, 1),
                "settlement_est_mm": round(settlement_mm, 2),
                "risk_level": risk,
                "color": color,
                "is_synthetic": True,
                "qa_flag": "pilot_synthetic_scenario"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [poly_coords]
            }
        })
        
    geojson = {
        "type": "FeatureCollection",
        "name": "synthetic_buildings_exposure",
        "features": features
    }
    
    path = DATA_DIR / "buildings_exposure.geojson"
    path.write_text(json.dumps(geojson, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved: {path.name} ({len(features)} buildings)")
    return geojson


def build_webgis_html():
    html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hệ thống WebGIS Giám sát & Dự báo Lún TBM Metro Tuyến 3 (S9-S12)</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        #map { height: 100vh; width: 100vw; }
        .control-panel {
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 1000;
            background: white;
            padding: 16px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.25);
            max-width: 360px;
        }
        .control-panel h3 { margin-top: 0; color: #1e3c72; font-size: 16px; border-bottom: 2px solid #2a5298; padding-bottom: 6px; }
        .control-group { margin-bottom: 12px; }
        .control-group label { display: block; font-weight: 600; font-size: 13px; margin-bottom: 4px; color: #333; }
        .control-group select, .control-group input[type="range"] { width: 100%; }
        .badge { display: inline-block; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: bold; color: white; }
        .badge-severe { background: #d9534f; }
        .badge-moderate { background: #f0ad4e; }
        .badge-slight { background: #5bc0de; }
        .badge-safe { background: #5cb85c; }
        .chart-box { margin-top: 10px; background: #fafafa; border-radius: 6px; padding: 6px; border: 1px solid #e0e0e0; }
        .legend { line-height: 18px; color: #555; font-size: 12px; margin-top: 10px; }
        .legend i { width: 14px; height: 14px; float: left; margin-right: 8px; opacity: 0.8; border-radius: 3px; }
    </style>
</head>
<body>
    <div id="map"></div>
    <div class="control-panel">
        <h3>TBM S9–S12: GIÁM SÁT & DỰ BÁO LÚN</h3>
        <div class="control-group">
            <label>Kịch bản Tổn thất Thể tích đất (V<sub>L</sub>): <span id="vl-val" style="color:#d9534f; font-weight:bold;">1.0%</span></label>
            <input type="range" id="vl-slider" min="0.5" max="2.0" step="0.25" value="1.0" />
        </div>
        <div class="control-group">
            <label>Mặt cắt địa chất:</label>
            <select id="section-select">
                <option value="S9_S10">S9–S10 (Kim Mã - Cát Linh, z0=15m)</option>
                <option value="S10_S11">S10–S11 (Cát Linh - Văn Miếu, z0=16.5m)</option>
                <option value="S11_S12" selected>S11–S12 (Văn Miếu - Ga Hà Nội, z0=18m)</option>
            </select>
        </div>
        <div class="control-group">
            <div style="font-size: 12px; color: #666;">
                <strong>Độ lún cực đại S<sub>max</sub>:</strong> <span id="smax-display" style="font-weight:bold; color:#1e3c72;">22.1 mm</span><br/>
                <strong>Bề rộng phễu lún i:</strong> <span id="i-display" style="font-weight:bold; color:#1e3c72;">10.8 m</span>
            </div>
        </div>
        <div class="chart-box">
            <canvas id="profileChart" width="320" height="150"></canvas>
        </div>
        <div class="legend">
            <strong>Mức độ Rủi ro Công trình:</strong><br/>
            <i style="background: #d9534f"></i> Nguy hiểm (> 15 mm)<br/>
            <i style="background: #f0ad4e"></i> Cảnh báo (8 – 15 mm)<br/>
            <i style="background: #5bc0de"></i> Nhẹ (3 – 8 mm)<br/>
            <i style="background: #5cb85c"></i> An toàn (< 3 mm)
        </div>
    </div>

    <script>
        const map = L.map('map').setView([21.028, 105.828], 15);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
            maxZoom: 19
        }).addTo(map);

        const stations = [
            { id: "S9", name: "Ga S9 - Kim Mã", coords: [21.0315, 105.8142] },
            { id: "S10", name: "Ga S10 - Cát Linh", coords: [21.0281, 105.8278] },
            { id: "S11", name: "Ga S11 - Văn Miếu", coords: [21.0264, 105.8361] },
            { id: "S12", name: "Ga S12 - Ga Hà Nội", coords: [21.0242, 105.8423] }
        ];

        // Draw alignment line
        const latlngs = stations.map(s => s.coords);
        const tunnelLine = L.polyline(latlngs, { color: '#1e3c72', weight: 5, dashArray: '8, 6' }).addTo(map);
        tunnelLine.bindPopup("<b>Tuyến hầm TBM EPB đôi S9–S12</b><br/>Đường kính ngoài: 6.3 m | Chiều dài: ~3.5 km");

        // Station markers
        stations.forEach(s => {
            const marker = L.circleMarker(s.coords, {
                radius: 8,
                fillColor: '#d9534f',
                color: '#fff',
                weight: 2,
                opacity: 1,
                fillOpacity: 0.9
            }).addTo(map);
            marker.bindPopup(`<b>${s.name}</b><br/>Ga ngầm tuyến Metro số 3`);
        });

        // Synthetic buildings layer
        const buildingsLayer = L.layerGroup().addTo(map);

        function updateBuildings(vl) {
            buildingsLayer.clearLayers();
            const factor = vl / 1.0;
            
            for (let i = 0; i < 60; i++) {
                const segIdx = Math.floor(Math.random() * (stations.length - 1));
                const p1 = stations[segIdx].coords;
                const p2 = stations[segIdx + 1].coords;
                const t = Math.random();
                const baseLat = p1[0] + t * (p2[0] - p1[0]);
                const baseLng = p1[1] + t * (p2[1] - p1[1]);
                
                const offsetM = (Math.random() * 90 - 45);
                const dLat = (offsetM / 111000.0);
                const dLng = (offsetM / 103000.0);
                const bLat = baseLat + dLat;
                const bLng = baseLng + dLng;
                
                const distAxis = Math.abs(offsetM);
                const settlement = (22.0 * Math.exp(-(distAxis * distAxis) / (2 * 9 * 9))) * factor;
                
                let color = "#5cb85c";
                let risk = "An toàn";
                if (settlement >= 15.0) { color = "#d9534f"; risk = "Nguy hiểm"; }
                else if (settlement >= 8.0) { color = "#f0ad4e"; risk = "Cảnh báo"; }
                else if (settlement >= 3.0) { color = "#5bc0de"; risk = "Nhẹ"; }
                
                const w = 0.00015;
                const bounds = [[bLat - w, bLng - w], [bLat + w, bLng + w]];
                const rect = L.rectangle(bounds, { color: color, weight: 1, fillOpacity: 0.65 });
                rect.bindPopup(`<b>Nhà dân lân cận #${i+1}</b><br/>Khoảng cách tim hầm: ${distAxis.toFixed(1)} m<br/>Độ lún dự báo: <b>${settlement.toFixed(1)} mm</b><br/>Mức độ rủi ro: <span style="color:${color}; font-weight:bold;">${risk}</span>`);
                buildingsLayer.addLayer(rect);
            }
        }

        // Initialize Chart
        const ctx = document.getElementById('profileChart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [-30, -20, -10, 0, 10, 20, 30],
                datasets: [{
                    label: 'Độ lún S(x) (mm)',
                    data: [0.5, 3.2, 14.1, 22.1, 14.1, 3.2, 0.5],
                    borderColor: '#1e3c72',
                    backgroundColor: 'rgba(30, 60, 114, 0.15)',
                    fill: true,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { reverse: true, title: { display: true, text: 'Lún (mm)', font: { size: 10 } } },
                    x: { title: { display: true, text: 'Khoảng cách x (m)', font: { size: 10 } } }
                },
                plugins: { legend: { display: false } }
            }
        });

        function updateAnalysis() {
            const vl = parseFloat(document.getElementById('vl-slider').value);
            document.getElementById('vl-val').innerText = vl.toFixed(2) + '%';
            
            const sec = document.getElementById('section-select').value;
            let z0 = 18.0;
            let K = 0.60;
            if (sec === 'S9_S10') { z0 = 15.0; K = 0.50; }
            else if (sec === 'S10_S11') { z0 = 16.5; K = 0.55; }
            
            const D = 6.30;
            const i = K * z0;
            const At = Math.PI * D * D / 4.0;
            const Smax = (vl / 100.0) * At / (Math.sqrt(2 * Math.PI) * i) * 1000.0;
            
            document.getElementById('smax-display').innerText = Smax.toFixed(1) + ' mm';
            document.getElementById('i-display').innerText = i.toFixed(1) + ' m';
            
            // Update chart data
            const xVals = [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30];
            const sVals = xVals.map(x => Smax * Math.exp(-(x * x) / (2 * i * i)));
            chart.data.labels = xVals;
            chart.data.datasets[0].data = sVals;
            chart.update();
            
            updateBuildings(vl);
        }

        document.getElementById('vl-slider').addEventListener('input', updateAnalysis);
        document.getElementById('section-select').addEventListener('change', updateAnalysis);
        
        // Initial run
        updateAnalysis();
    </script>
</body>
</html>"""
    
    path = TABLE_DIR / "webgis_settlement_map.html"
    path.write_text(html_content, encoding="utf-8")
    print(f"Saved interactive WebGIS: {path.name}")


if __name__ == "__main__":
    build_alignment_geojson()
    build_buildings_geojson()
    build_webgis_html()
