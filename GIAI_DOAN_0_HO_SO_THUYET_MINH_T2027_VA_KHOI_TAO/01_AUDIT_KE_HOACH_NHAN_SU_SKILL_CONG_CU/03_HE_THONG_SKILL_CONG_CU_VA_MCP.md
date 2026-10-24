# HỆ THỐNG SKILL, CÔNG CỤ KỸ THUẬT & MCP SERVER: GIAI_DOAN_0

## 1. Danh mục Skill, MCP Server và Thư viện Kỹ thuật Sử dụng trong Giai đoạn

- MCP parallel-search (`web_search`, `web_fetch`) – Đối chiếu thông tin dự án ADB 40080-013 & mốc thông hầm TBM1/TBM2
- MCP exa (`web_search_exa`) – Truy vấn siêu dữ liệu bài báo ASCE / Crossref / OpenAlex
- Skill `literature-search-openalex` – Tra cứu định danh DOI/OpenAlex cho 10 tài liệu tham khảo cốt lõi
- Skill `modern-web-guidance` (`responsive-table`, `accessibility`) – Chuẩn hóa bảng dữ liệu HTML tương tác
- Skill `generative_ui` – Thiết kế giao diện bảng điều khiển kiểm toán trực quan
- Công cụ Python: `python-docx`, `openpyxl`, `hashlib`, `json`, `csv`

## 2. Quy chuẩn Vận hành Công cụ & Kiểm thử Độc lập
- Mọi script Python đều tuân thủ chuẩn PEP 8, có Type Hints và kiểm tra ràng buộc vật lý (`validate_physical_plausibility`).
- Các bảng biểu Web HTML đều áp dụng chuẩn `responsive-table` (sticky headers, container queries `@container (width < 600px)`) từ skill `modern-web-guidance`.
- Truy vấn tài liệu học thuật và mốc tiến độ thực tế TBM1/TBM2 qua MCP `parallel-search` và `exa`.
