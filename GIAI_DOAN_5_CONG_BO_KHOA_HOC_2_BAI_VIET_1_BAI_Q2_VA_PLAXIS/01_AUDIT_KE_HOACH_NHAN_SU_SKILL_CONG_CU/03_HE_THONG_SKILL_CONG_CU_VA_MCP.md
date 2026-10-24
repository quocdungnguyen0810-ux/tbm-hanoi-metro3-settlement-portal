# 03. HỆ THỐNG SKILL, CÔNG CỤ VÀ MCP ĐÃ KÍCH HOẠT — GIAI ĐOẠN 5

1. **Skill `literature-search-openalex` (`C:\Users\ADMIN\.gemini\config\plugins\science\skills\literature_search_openalex\SKILL.md`):**
   - Tra cứu trực tiếp cơ sở dữ liệu học thuật toàn cầu OpenAlex qua `openalex_cli.py`.
   - Đã xác thực các công trình đối chứng cho Metro Hà Nội và hầm TBM: `https://openalex.org/W4391687628` (Nguyen, Bui & Nguyen 2024), `https://openalex.org/W7155201404` (Nguyen 2025), `https://openalex.org/W4415102772` (Bui Trong Le et al. 2025), `https://openalex.org/W4388640090` (Soft Ground Shield Tunnels) và tạp chí mục tiêu Q2 `https://openalex.org/S202628778` (*Geotechnical and Geological Engineering*).
2. **Skill `google-antigravity-sdk` (`C:\Users\ADMIN\.gemini\config\plugins\google-antigravity-sdk\skills\google-antigravity-sdk\SKILL.md`):**
   - Thiết kế kiến trúc điều phối đa tác tử `general_contractor` trong `.agents/agents.json` và định nghĩa Subagent kiểm toán chuyên biệt `publication_mechanics_auditor`.
3. **Skill `uv` & Python Scientific Stack (`numpy`, `scipy.sparse`, `matplotlib`, `openpyxl`, `python-docx`):**
   - Giải hệ phương trình phần tử hữu hạn biến dạng phẳng 2D bằng ma trận thưa `scipy.sparse.linalg.spsolve`, mô phỏng Saltelli-LHS 28.672 mẫu và xuất bản đồng bộ Markdown/Word/Excel/HTML.
