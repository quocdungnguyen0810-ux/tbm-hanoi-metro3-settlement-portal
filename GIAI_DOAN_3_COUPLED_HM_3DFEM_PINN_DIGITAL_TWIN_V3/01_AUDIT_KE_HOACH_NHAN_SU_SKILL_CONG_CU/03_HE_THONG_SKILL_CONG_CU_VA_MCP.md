# HỆ THỐNG SKILL, CÔNG CỤ KỸ THUẬT & MCP SERVER: GIAI_DOAN_3

## 1. Danh mục Skill, MCP Server và Thư viện Kỹ thuật Sử dụng trong Giai đoạn

- MCP parallel-search – Xác thực dữ liệu giám sát xã hội ADB Q1/2025 (56 hộ dân bị ảnh hưởng dọc S9–S12, hiện tượng phụ gia phun lên mặt đất tháng 02/2025)
- Skill `modern-web-guidance` & `generative_ui` – Thiết kế giao diện bảng điều khiển TARP và báo cáo kiểm toán tương tác
- Công cụ Kiểm toán tự động: `audit_artifacts.py`, `project_stage_organizer.py` (quét công thức Excel, GeoJSON provenance, SHA-256)
- Công cụ Tính toán & Đồ họa: `numpy`, `openpyxl` (5 workbook GĐ3), `matplotlib` (7 hình 300 DPI `FIG_15`–`FIG_21`)

## 2. Quy chuẩn Vận hành Công cụ & Kiểm thử Độc lập
- Mọi script Python đều tuân thủ chuẩn PEP 8, có Type Hints và kiểm tra ràng buộc vật lý (`validate_physical_plausibility`).
- Các bảng biểu Web HTML đều áp dụng chuẩn `responsive-table` (sticky headers, container queries `@container (width < 600px)`) từ skill `modern-web-guidance`.
- Truy vấn tài liệu học thuật và mốc tiến độ thực tế TBM1/TBM2 qua MCP `parallel-search` và `exa`.
