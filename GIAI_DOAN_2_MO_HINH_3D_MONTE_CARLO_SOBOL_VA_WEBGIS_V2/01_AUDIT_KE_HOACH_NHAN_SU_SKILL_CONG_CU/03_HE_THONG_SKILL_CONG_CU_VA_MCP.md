# HỆ THỐNG SKILL, CÔNG CỤ KỸ THUẬT & MCP SERVER: GIAI_DOAN_2

## 1. Danh mục Skill, MCP Server và Thư viện Kỹ thuật Sử dụng trong Giai đoạn

- MCP parallel-search – Kiểm chứng tốc độ đào TBM thực tế (~10m/ngày, 1.720 vòng vỏ hầm) trên đoạn S9–S12
- Skill `modern-web-guidance` – Thiết kế giao diện bảng điều khiển và bộ lọc công trình trên WebGIS v2.0
- Công cụ Tính toán: Python `numpy`, `scipy.special.erf`, `scipy.stats`
- Công cụ Bảng tính & Đồ họa: `openpyxl` (4 workbook nâng cao GĐ2), `matplotlib` (7 hình 3D & thống kê 300 DPI)
- Công cụ WebGIS: `Leaflet.js`, `Chart.js` (thanh trượt tiến độ Ring 0–2500)

## 2. Quy chuẩn Vận hành Công cụ & Kiểm thử Độc lập
- Mọi script Python đều tuân thủ chuẩn PEP 8, có Type Hints và kiểm tra ràng buộc vật lý (`validate_physical_plausibility`).
- Các bảng biểu Web HTML đều áp dụng chuẩn `responsive-table` (sticky headers, container queries `@container (width < 600px)`) từ skill `modern-web-guidance`.
- Truy vấn tài liệu học thuật và mốc tiến độ thực tế TBM1/TBM2 qua MCP `parallel-search` và `exa`.
