# HỆ THỐNG NHÂN SỰ CHUYÊN MÔN & MẠNG LƯỚI TÁC TỬ AI: GIAI_DOAN_1

## 1. Hệ thống Nhân sự Thực hiện (Chủ nhiệm, Thành viên & Đơn vị Phối hợp)

### 1.1. Chủ trì Giai đoạn
- **ThS. Nguyễn Hải Hà (Chủ nhiệm đề tài – Chủ trì cơ học giải tích Peck/LP, đánh giá độ nhạy và biên soạn Luận án/Báo cáo GĐ1)**

### 1.2. Thành viên Nghiên cứu & Phối hợp Thực hiện
- ThS. Lê Anh Đức (Chuẩn hóa địa tầng hố khoan BH12, kiểm tra thông số đất yếu Đệ tứ và đánh giá tổn hại Burland 60 công trình)
- KS. Trần Văn Long (Xây dựng bản đồ số tương tác WebGIS v1.0 Leaflet và xử lý không gian GeoJSON tuyến S9–S12)
- Hội đồng nghiệm thu cấp Bộ môn Địa kỹ thuật & Không gian ngầm (Thẩm định trước nghiệm thu Giai đoạn 1)

## 2. Hệ thống Tác tử AI Chuyên trách (Multi-Agent Guarded System)

### 2.1. Tác tử Chủ trì (Lead Agents)
- `data_engineer (Chuẩn hóa SI, chạy QC vật lý WF-07 và đóng băng Baseline WF-09)`
- `mechanics_reviewer (Thẩm định phương trình giải tích Peck 1969 & Loganathan-Poulos 1998 WF-10)`
- `analytical_modeler (Lập trình `analytical_engine.py` và kiểm thử bảo toàn thể tích 7/7 unit tests WF-11)`
- `sensitivity_analyst (Phân tích độ nhạy OAT 21 kịch bản với VL = 0.5% - 2.0% WF-13)`
- `gis_analyst (Số hóa bình đồ tuyến, 60 công trình dọc S9–S12 và đóng gói WebGIS v1.0 WF-14)`

### 2.2. Tác tử Phối hợp & Kiểm toán (Supporting & Auditing Agents)
- `reporting_editor (Biên soạn 9 chương bản thảo luận án và xuất bản 7 hình vẽ 300–350 DPI)`
- `evidence_auditor (Kiểm toán Gate 2, Gate 3, Gate 4, Gate 5 và lập bảng mã băm SHA-256)`
- `pipeline_engineer (Xây dựng `run_full_pipeline.py` và xuất bản 4 file Excel chuyên nghiệp GĐ1)`
