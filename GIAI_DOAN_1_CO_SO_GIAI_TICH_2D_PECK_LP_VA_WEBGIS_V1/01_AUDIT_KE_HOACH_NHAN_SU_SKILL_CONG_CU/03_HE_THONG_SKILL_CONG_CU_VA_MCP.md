# HỆ THỐNG SKILL, CÔNG CỤ KỸ THUẬT & MCP SERVER: GIAI_DOAN_1

## 1. Danh mục Skill, MCP Server và Thư viện Kỹ thuật Sử dụng trong Giai đoạn

- MCP parallel-search & exa – Đối chiếu phương trình Loganathan & Poulos (1998) DOI `10.1061/(ASCE)1090-0241(1998)124:9(846)`
- Skill `modern-web-guidance` – Tối ưu giao diện bảng dữ liệu và bản đồ WebGIS v1.0
- Công cụ Tính toán: Python `numpy`, `scipy` (tích phân hình thang bảo toàn thể tích phễu lún)
- Công cụ Bảng tính & Văn bản: `openpyxl` (4 file Excel GĐ1), `python-docx` (`LUAN_AN_HOAN_CHINH_TBM_METRO3_HANOI.docx`)
- Công cụ Đồ họa & GIS: `matplotlib` (7 hình 300 DPI + 4 hình 350 DPI), `Leaflet.js`, `Chart.js`

## 2. Quy chuẩn Vận hành Công cụ & Kiểm thử Độc lập
- Mọi script Python đều tuân thủ chuẩn PEP 8, có Type Hints và kiểm tra ràng buộc vật lý (`validate_physical_plausibility`).
- Các bảng biểu Web HTML đều áp dụng chuẩn `responsive-table` (sticky headers, container queries `@container (width < 600px)`) từ skill `modern-web-guidance`.
- Truy vấn tài liệu học thuật và mốc tiến độ thực tế TBM1/TBM2 qua MCP `parallel-search` và `exa`.
