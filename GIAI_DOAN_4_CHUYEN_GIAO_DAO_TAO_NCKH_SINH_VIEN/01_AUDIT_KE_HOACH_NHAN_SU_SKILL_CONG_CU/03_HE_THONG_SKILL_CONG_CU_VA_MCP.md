# HỆ THỐNG SKILL, CÔNG CỤ KỸ THUẬT & MCP SERVER: GIAI_DOAN_4

## 1. Danh mục Skill, MCP Server và Thư viện Kỹ thuật Sử dụng trong Giai đoạn

- Skill `modern-web-guidance` – Tối ưu giao diện StoryMap tương tác cho sinh viên
- Công cụ Python: `openpyxl` (biểu mẫu khảo sát thực địa & Gantt chart), `python-docx` (6 tài liệu đề cương & sổ tay)
- Công cụ WebGIS StoryMap: `Leaflet.js`, HTML5/CSS3 (`05_WEBGIS_PROTOTYPE/index.html`)

## 2. Quy chuẩn Vận hành Công cụ & Kiểm thử Độc lập
- Mọi script Python đều tuân thủ chuẩn PEP 8, có Type Hints và kiểm tra ràng buộc vật lý (`validate_physical_plausibility`).
- Các bảng biểu Web HTML đều áp dụng chuẩn `responsive-table` (sticky headers, container queries `@container (width < 600px)`) từ skill `modern-web-guidance`.
- Truy vấn tài liệu học thuật và mốc tiến độ thực tế TBM1/TBM2 qua MCP `parallel-search` và `exa`.
