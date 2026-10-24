# BÁO CÁO THẨM ĐỊNH CỔNG 0 (GATE 0), THIẾT LẬP HỆ THỐNG NHÂN SỰ VÀ BẢN PHẢN BIỆN "GRILL-ME" DỰ ÁN TBM ĐTM HÀ NỘI

**Dự án:** Nghiên cứu đánh giá độ nhạy và dự báo vùng ảnh hưởng lún mặt đất do thi công hầm khiên đào (TBM) trong điều kiện địa chất đô thị Hà Nội bằng phương pháp giải tích kết hợp GIS  
**Phạm vi nghiên cứu:** Đoạn tuyến ngầm S9 (Kim Mã) – S12 (Ga Hà Nội), Tuyến đường sắt đô thị số 3 (Nhổn – Ga Hà Nội)  
**Cơ chế vận hành:** `auto_guarded` | **Chính sách mô hình:** `inherit`  
**Ngày phê duyệt Cổng 0:** 13/10/2026 (UTC+7)  
**Cơ quan chủ trì / Đơn vị kiểm toán:** Ban Điều phối Tác tử & Tổ Kiểm toán Độc lập Dự án TBM–ĐTM  

---

## PHẦN 1: HỆ THỐNG NHÂN SỰ & CƠ CHẾ PHỐI HỢP TÁC TỬ (STAFFING & MULTI-AGENT ARCHITECTURE)

Nhằm đảm bảo tính minh bạch khoa học, liêm chính dữ liệu và tuân thủ tuyệt đối 10 nguyên tắc bất khả xâm phạm tại `AGENTS.md`, dự án thiết lập hệ thống nhân sự đa tác tử chuyên trách với nguyên tắc phân quyền bất đối xứng (Separation of Powers) và kiểm tra chéo độc lập (Maker-Checker).

### 1.1. Danh bạ 10 vai trò chính thức & 2 vai trò có điều kiện

1. **`general_contractor` (Chỉ huy trưởng):** Nắm giữ WBS, đồ thị phụ thuộc (DAG), trạng thái hệ thống `AGENT_STATE.json`, điều phối handoff, kiểm soát việc mở/khóa các Audit Gates. Không được tự ý sửa dữ liệu hoặc tự duyệt audit.
2. **`source_harvester` (Thu thập nguồn):** Tìm kiếm, thu thập tài liệu ĐTM 2013, báo cáo ADB, hồ sơ CP03, bài báo quốc tế; trích xuất văn bản, bảng biểu, hình ảnh mà không làm biến đổi file gốc. File nguồn được băm SHA-256 + Ghi rõ `source_id`, `source_locator` (trang, bảng, hình).
3. **`evidence_auditor` (Kiểm toán chứng cứ):** Kiểm tra độc lập nguồn trích dẫn, bản quyền, tính pháp lý, phân định 7 phân lớp chứng cứ; phát hiện mâu thuẫn số liệu. Có quyền Veto phủ quyết.
4. **`data_engineer` (Kỹ sư dữ liệu):** Chuẩn hóa schema, ràng buộc khoá chính/khoá ngoại, chuyển đổi chuẩn đơn vị SI, quản lý thư mục cách ly `data/quarantine/`, đóng băng baseline Gate 3 với SHA-256 manifest.
5. **`mechanics_reviewer` (Thẩm tra cơ học):** Thẩm định các phương trình giải tích (Peck 1969, Loganathan-Poulos 1998), giả thiết cơ học, kiểm tra thứ nguyên, bảo toàn khối lượng đào, điều kiện biên và giới hạn áp dụng trong đất yếu Hà Nội.
6. **`analytical_modeler` (Mô hình giải tích):** Lập trình tính toán phễu lún Peck và nhánh Loganathan-Poulos (chỉ khi MR phê duyệt); vượt qua kiểm thử tích phân số và trường hợp giới hạn; tuân thủ quy ước lún dương xuống.
7. **`sensitivity_analyst` (Phân tích độ nhạy):** Thiết kế ma trận kịch bản OAT (One-At-A-Time), phân tích bất định (UQ), đánh giá tương quan giữa các tham số $V_L, K, z_0, D$, xác định mức độ nhạy cảm của phễu lún.
8. **`gis_analyst` (Chuyên viên GIS):** Quản lý hệ tọa độ (CRS VN-2000 nội bộ Hà Nội / WGS-84), tuyến hầm, trắc dọc địa chất, tạo buffer vùng ảnh hưởng lún, tích hợp hiện trạng công trình lân cận trên QGIS. Lớp dữ liệu GeoPackage chuẩn CRS, không đo khoảng cách trên kinh vĩ độ (EPSG:4326).
9. **`reporting_editor` (Biên tập báo cáo):** Tổng hợp số liệu, xuất bản biểu bảng, hình ảnh, bài báo khoa học; bảo đảm 100% con số trong báo cáo đều truy nguyên được về nguồn gốc hoặc kịch bản mô phỏng.
10. **`pipeline_engineer` (Kỹ sư hệ thống):** Thiết lập môi trường thực thi, CI/CD, kiểm thử tự động, giải quyết lỗi cú pháp, tương thích thư viện Python 3.13 và orchestration script.
- *Conditional 1 - `numerical_modeler` (Mô hình phần tử hữu hạn/OpenSeesPy):* Khóa mặc định; chỉ kích hoạt khi Cổng 4 chứng minh cần thiết và có đủ dữ liệu.
- *Conditional 2 - `ml_modeler` (Mô hình học máy ML):* Khóa mặc định; chỉ kích hoạt khi có tập dữ liệu quan trắc thực tế độc lập đủ lớn.

### 1.2. Ma trận Trách nhiệm RACI

| Cổng kiểm toán | GC | SH | EA | DE | MR | AM | SA | GA | RE | PE |
|---|---|---|---|---|---|---|---|---|---|---|
| **Gate 0: Khởi tạo, Quản trị & Phản biện Kế hoạch** | **A** | C | **R** | C | **R** | C | C | C | I | C |
| **Gate 1: Toàn vẹn Nguồn thu thập & Trích xuất** | A | **R** | **A** | C | C | I | I | I | I | I |
| **Gate 2: Kiểm soát Vật lý, Địa kỹ thuật & Không gian** | A | C | C | **R** | **A** | I | I | **R** | I | C |
| **Gate 3: Đóng băng Baseline & Mã băm Checksum** | A | I | C | **R/A** | C | I | I | C | I | C |
| **Gate 4: Kiểm chứng Giải tích, Độ nhạy & GIS** | A | I | I | C | **A** | **R** | **R** | **R** | C | C |
| **Gate 5: Báo cáo Khoa học, Khả năng Tái lập 100%** | **A** | I | **A** | C | C | C | C | C | **R** | C |

---

## PHẦN 2: THẨM VẤN PHẢN BIỆN KẾ HOẠCH DỰ ÁN ("GRILL-ME" STRESS-TEST)

1. **Vấn đề ĐTM 2013 & CP03:** Hiện chưa có file gốc cục bộ. Xử lý: **GO có điều kiện** — chỉ chạy kịch bản giải tích trên các mặt cắt học thuật đã thẩm định (ETASR 2024, TCXD 2024); tuyệt đối không bịa số liệu hay công bố dự báo thực địa.
2. **Vấn đề Loganathan & Poulos (1998):** Bị khóa cứng để tránh tình trạng trích dẫn sai lệch, nhầm lẫn gap parameter và ground loss, nhầm bán kính/đường kính. Chỉ mở khóa khi Mechanics Reviewer có memo thẩm định bản gốc 1998.
3. **Vấn đề Mô hình Peck (1969):** Khảo sát dải biến thiên $K \in [0.3; 0.7]$ và $V_L \in [0.5\%; 2.0\%]$. Phân biệt rạch ròi chiều sâu tim hầm $z_0$ và chiều sâu lớp đất phủ $C$. Bắt buộc vượt qua kiểm thử tích phân bảo toàn thể tích với dung sai $< 10^{-6}$.
4. **Vấn đề Nước ngầm & Lún cố kết:** Phân tách rạch ròi lún do đào khiên TBM và lún do hạ áp lực nước ngầm. Tuyệt đối không gộp nước ngầm vào tham số cơ học của Peck khi chưa có mô hình liên kết.
5. **Vấn đề GIS & Tọa độ:** Tuyến hầm và công trình chưa có CRS VN-2000 được kiểm chứng. Cấm tuyệt đối việc gán nguy cơ cho từng ngôi nhà cụ thể; chỉ chạy trên hệ tọa độ sơ đồ trục tuyến (Chainage).
6. **Vấn đề ML & FEM:** Cấm ngụy tạo dữ liệu giả từ công thức rồi huấn luyện AI; chỉ dùng phương pháp giải tích minh bạch làm trọng tâm.

---

## PHẦN 3: BÁO CÁO PHÂN TÍCH ĐÁNH GIÁ CỔNG 0 (GATE 0 AUDIT REPORT)

### Phán quyết Cổng 0: **CONDITIONAL GO (CHẤP THUẬN CÓ ĐIỀU KIỆN)**

- **ĐƯỢC PHÉP:** Nghiên cứu độ nhạy OAT cho phễu lún Peck trên các mặt cắt giả định S9–S10 và BH12 S11–S12; chuẩn hóa cấu trúc dữ liệu schema; xây dựng cấu trúc GIS sơ đồ tuyến.
- **BỊ CHẶN:** Tuyên bố dự báo lún tuyệt đối cho các tòa nhà cụ thể; hiệu chỉnh mô hình khi thiếu quan trắc; lập trình Loganathan-Poulos; triển khai ML/FEM.

---

## PHẦN 4: KẾ HOẠCH HÀNH ĐỘNG WBS (WF-01 ĐẾN WF-20)

- **Gate 1:** WF-01 (Đã hoàn thành), WF-02 (Đã hoàn thành), WF-03 (Đang triển khai với `source_harvester`), WF-04, WF-05.
- **Gate 2:** WF-06, WF-07, WF-08.
- **Gate 3:** WF-09, WF-10, WF-11.
- **Gate 4:** WF-12, WF-13, WF-14, WF-15.
- **Gate 5:** WF-16, WF-17, WF-18, WF-19, WF-20.

---

## PHẦN 5: QUY TRÌNH KIỂM TRA ĐỐI CHIẾU AUDIT & PHẢN HỒI

Mọi dữ liệu phải qua kiểm toán 3 tầng (Schema -> Cơ học -> Pháp lý & Nguồn gốc). Dữ liệu sai lỗi đưa về `data/quarantine/`. Mọi con số bắt buộc kèm metadata: `source_id`, `source_locator`, `value_basis`, `confidence`, `qa_flag`.
