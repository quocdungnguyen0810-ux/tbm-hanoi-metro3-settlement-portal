# Bộ dữ liệu nền TBM–lún mặt đất, Metro Nhổn–Ga Hà Nội

Ngày rà soát: 2026-10-12.

## Phạm vi và trạng thái

Bộ tài liệu trong `research/` tổng hợp hồ sơ công khai của ADB/Hà Nội/Bộ GTVT và số liệu địa kỹ thuật công bố cho đoạn ngầm S9–S12. Mọi bản ghi giữ nguồn gốc, phạm vi không gian và loại chứng cứ. Không điền giá trị vào chỗ thiếu và không coi giả định mô hình là quan trắc hiện trường.

## Kết quả chính có thể sử dụng ngay

- **S9–S10 (ETASR 2024):** 6 đơn vị gồm backfill, GU1, GU3&4, GU5_a, GU5_b và GU7&8; có dải/giá trị trung bình chiều dày, SPT và bảng tham số Hardening Soil. Mực nước ngầm được báo cáo ở **10–12 m dưới mặt đất**, nhưng không gắn với một hố khoan định danh.
- **BH12, đoạn S11–S12 (Tạp chí Xây dựng 06/2024):** 6 lớp với chiều dày lần lượt **2,0; 10,3; 12,7; 11,9; 15,0; 8,1 m**. Ranh giới độ sâu trong CSV là phép cộng dồn và được gắn nhãn `derived_cumulative`.
- **Nước ngầm BH12:** mức **−6 m** chỉ là đầu vào mô hình, được gắn nhãn `model_assumption`; không trộn với quan trắc 10–12 m tại S9–S10.
- **Kiểm tra chéo toàn Line 3:** Giao et al. (2020) dùng 17 hố khoan trên Km 9+900–22+400. Dữ liệu này mang nhãn `regional_crosscheck`, không tự động gán cho S9–S12 khi chưa có ánh xạ hố khoan–lý trình.
- **Hồ sơ chính thức:** ADB xác nhận dự án 40080-013, EIA cập nhật tháng 8/2013, EIA/EA dự thảo tháng 8/2010, RRP tháng 3/2011 và các báo cáo giám sát. Chưa tìm thấy PDF ĐTM hoặc toàn văn báo cáo khả thi được lập chỉ mục công khai trên `mt.gov.vn` hay `hanoi.gov.vn` trong đợt rà soát này.

## Cấu trúc đầu ra

- `research/official_docs_findings.md`, `research/official_docs.csv`: hồ sơ chính thức, URL, trạng thái truy cập và kết quả âm.
- `research/academic_findings.md`: diễn giải có trang/bảng/hình và cảnh báo chất lượng.
- `research/stratigraphy_raw.csv`: 18 bản ghi địa tầng S9–S10, BH12/S11–S12 và kiểm tra chéo toàn tuyến.
- `research/data_dictionary.md`: khóa, kiểu dữ liệu, quy tắc GIS và QA.
- `research/templates/`: 9 bảng CSV rỗng để nhập dữ liệu khảo sát, TBM, quan trắc lún, công trình và tham số giải tích.
- `research/sources/`: PDF/metadata Crossref dùng để kiểm chứng.
- `research/figures/conceptual_framework_tbm_gis.png`: sơ đồ khái niệm.

## Quy tắc sử dụng cho mô hình độ nhạy

1. Chỉ dùng `direct_text` hoặc `direct_table` làm giá trị nền; giữ `derived_cumulative` trong phân tích bất định.
2. Tách `tunnelling_induced` khỏi `groundwater_consolidation`.
3. Không nội suy không gian khi thiếu tọa độ/lý trình hố khoan; cần bổ sung logs khảo sát CP03 và hệ tọa độ gốc.
4. Với khoảng giá trị, giữ `min`, `max`, `mean` và nguồn; không thay bằng một giá trị duy nhất trước khi xác định phân phối độ nhạy.
5. Giữ nguyên bất nhất BH12: đỉnh lớp sét mềm là 12,3 m theo cộng dồn Bảng 2 nhưng câu văn ghi 12,7 m.

## Khoảng trống ưu tiên

- PDF gốc EIA cập nhật 2013 và số trang các bảng/hình địa chất.
- Báo cáo khảo sát địa chất/thiết kế kỹ thuật CP03, đặc biệt tọa độ và logs hố khoan S9–S12.
- Chuỗi vận hành TBM theo vòng đào: áp lực gương, grout, tốc độ tiến, mô-men, khối lượng đào và mất thể tích.
- Quan trắc lún theo thời gian, mốc đo và khoảng cách ngang tới tim hầm.
- Cao độ mực nước theo piezometer và thời điểm đo.
