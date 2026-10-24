# TỜ TRÌNH XIN NGHIỆM THU THỬ GIAI ĐOẠN 1
### ĐỀ TÀI LUẬN ÁN TIẾN SĨ / THẠC SĨ KỸ THUẬT

**Kính gửi:**
- Ban Chủ nhiệm Khoa Công trình và Môi trường;
- Ban Chủ nhiệm Bộ môn Địa kỹ thuật và Không gian ngầm;
- Các Thầy/Cô thành viên Hội đồng chuyên môn đánh giá nghiệm thu.

---

### 1. THÔNG TIN CHUNG VỀ ĐỀ TÀI
- **Tên đề tài:** *Nghiên cứu đánh giá độ nhạy và dự báo vùng ảnh hưởng lún mặt đất do thi công hầm khiên đào (TBM) đoạn S9–S12 Metro Tuyến 3 Hà Nội bằng phương pháp giải tích kết hợp WebGIS*.
- **Ngành đào tạo:** Kỹ thuật Xây dựng Công trình Ngầm và Mỏ / Kỹ thuật Địa kỹ thuật (Mã số: 9580204 / 9580211).
- **Cơ sở đào tạo:** Trường Đại học Giao thông vận tải (UTC).
- **Người thực hiện:** Nhóm nghiên cứu & Tác giả Luận án (Phụ trách: TS. Nguyễn Hải Hà & Cộng sự).
- **Đơn vị chuyên môn quản lý:** Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường.

---

### 2. MỤC ĐÍCH VÀ CĂN CỨ TỔ CHỨC NGHIỆM THU THỬ
Căn cứ vào Quy chế đào tạo sau đại học và Kế hoạch thực hiện nghiên cứu khoa học của Bộ môn Địa kỹ thuật và Không gian ngầm;
Nhằm rà soát, đánh giá độc lập tính chuẩn xác về mặt cơ học đất, mô hình toán học giải tích, tính toàn vẹn của dữ liệu địa tầng thực tế và tính khả thi của hệ thống công cụ số hóa trước khi tiến hành nghiệm thu chính thức;
Nhóm nghiên cứu đã hoàn thành toàn bộ khối lượng công việc của **Giai đoạn 1: Xây dựng bộ sản phẩm nghiên cứu cốt lõi** và kính trình Bộ môn tổ chức phiên họp nghiệm thu thử.

---

### 3. TẬP HỢP TRỌN BỘ CÁC SẢN PHẨM BÀN GIAO NỘP KÈM
Trọn bộ sản phẩm nghiệm thu nộp Bộ môn bao gồm 4 cấu phần khoa học đồng bộ và hồ sơ kiểm toán:

1. **Bản thảo luận án chi tiết hoàn chỉnh:**
   - Tập hợp đầy đủ 8 chương, Trang bìa tóm tắt, Tài liệu tham khảo chuẩn mực và Phụ lục ma trận bằng chứng.
   - Định dạng Markdown toàn văn (`LUAN_AN_HOAN_CHINH_TBM_METRO3_HANOI.md`, 113 trang, 93,764 ký tự).
   - Bản in ấn Microsoft Word chuẩn quy định đào tạo sau đại học (`LUAN_AN_HOAN_CHINH_TBM_METRO3_HANOI.docx`, 2.64 MB, căn lề 3-2-2-2 cm, tích hợp bảng biểu và hình vẽ).
2. **Bộ 4 file Excel chuyên nghiệp (Đạt tiêu chuẩn tư vấn quốc tế):**
   - `TBM_HANOI_GEOTECHNICAL_BASELINE.xlsx`: Cơ sở dữ liệu địa chất hố khoan BH12, mặt cắt S9–S10 và tổng hợp 6 đơn nguyên thạch học.
   - `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx`: Động cơ tính toán giải tích Peck (1969) và Loganathan & Poulos (1998), 21 kịch bản và siêu vị hầm đôi.
   - `TBM_BUILDING_RISK_EXPOSURE.xlsx`: Đánh giá chi tiết nguy cơ lún và độ nghiêng cho 60 công trình móng nông theo Burland (1995).
   - `EVIDENCE_TRACEABILITY_AUDIT_MATRIX.xlsx`: Ma trận truy xuất nguồn gốc học thuật, phân định rõ ràng giữa quan trắc thực địa và giả định mô hình.
3. **Hệ thống 7 hình ảnh minh họa khoa học chất lượng cao 300 DPI:**
   - Đạt chuẩn xuất bản tạp chí quốc tế Q1/Scopus và Tạp chí Giao thông vận tải, độ phân giải từ $3000 \times 1650$ đến $4200 \times 1650$ pixels (`FIG_01` đến `FIG_07`).
4. **Hệ thống WebGIS tương tác giám sát và dự báo lún:**
   - Ứng dụng WebGIS độc lập (`webgis_settlement_map.html`), chạy trực tiếp trên trình duyệt web, tích hợp 60 công trình thực tế, thanh trượt $V_L$ thời gian thực, biểu đồ phễu lún Chart.js và các lớp dữ liệu GeoJSON chuẩn WGS-84.
5. **Hồ sơ kiểm toán khoa học và bàn giao (Audit Gates 1–5):**
   - Biên bản kiểm toán xác nhận đã vượt qua 5 cổng kiểm soát chất lượng nghiêm ngặt (Gate 1 đến Gate 5) và Bảng mã băm SHA-256 niêm phong bất biến cho toàn bộ 31 tệp tin.

---

### 4. ĐỀ NGHỊ CỦA NHÓM NGHIÊN CỨU
Kính đề nghị Ban Chủ nhiệm Bộ môn Địa kỹ thuật và Không gian ngầm:
1. Tiếp nhận trọn bộ hồ sơ và sản phẩm nghiên cứu Giai đoạn 1;
2. Phân công các Thầy/Cô phản biện chuyên môn đánh giá chi tiết;
3. Bố trí lịch họp nghiệm thu thử để Nhóm nghiên cứu báo cáo trực tiếp, tiếp thu ý kiến phản biện của các chuyên gia nhằm hoàn thiện hồ sơ trước khi công bố và nghiệm thu cấp Khoa/Trường.

Nhóm nghiên cứu xin trân trọng cảm ơn sự quan tâm, chỉ đạo và giúp đỡ quý báu của các Thầy/Cô trong Bộ môn!

*Hà Nội, ngày 15 tháng 10 năm 2026*

**ĐẠI DIỆN NHÓM NGHIÊN CỨU**  
*(Ký và ghi rõ họ tên)*  


**TS. NGUYỄN HẢI HÀ**
