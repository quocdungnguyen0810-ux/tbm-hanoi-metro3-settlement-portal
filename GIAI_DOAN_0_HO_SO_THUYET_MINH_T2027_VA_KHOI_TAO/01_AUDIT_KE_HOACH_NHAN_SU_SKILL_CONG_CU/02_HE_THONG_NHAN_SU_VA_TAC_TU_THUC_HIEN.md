# HỆ THỐNG NHÂN SỰ CHUYÊN MÔN & MẠNG LƯỚI TÁC TỬ AI: GIAI_DOAN_0

## 1. Hệ thống Nhân sự Thực hiện (Chủ nhiệm, Thành viên & Đơn vị Phối hợp)

### 1.1. Chủ trì Giai đoạn
- **ThS. Nguyễn Hải Hà (Chủ nhiệm đề tài – Bộ môn Địa kỹ thuật & Không gian ngầm, Khoa Công trình, Trường ĐH GTVT)**

### 1.2. Thành viên Nghiên cứu & Phối hợp Thực hiện
- ThS. Lê Anh Đức (Thành viên nghiên cứu chính – Bộ môn Địa kỹ thuật & Không gian ngầm, Trường ĐH GTVT)
- KS. Trần Văn Long (Thành viên hỗ trợ kỹ thuật & WebGIS – Khoa Công trình và Môi trường, Trường ĐH GTVT)
- Ban Quản lý Đường sắt đô thị Hà Nội (MRB – Đơn vị phối hợp cung cấp bình đồ, trắc dọc đoạn S9–S12)

## 2. Hệ thống Tác tử AI Chuyên trách (Multi-Agent Guarded System)

### 2.1. Tác tử Chủ trì (Lead Agents)
- `general_contractor (Chỉ huy trưởng điều phối WBS & trạng thái AGENT_STATE.json)`
- `source_harvester (Khai thác tài liệu ADB EIA 2013, báo cáo địa chất & bài báo quốc tế)`
- `evidence_auditor (Kiểm toán hồ sơ thuyết minh T2027 và Gate 1 Source Integrity)`

### 2.2. Tác tử Phối hợp & Kiểm toán (Supporting & Auditing Agents)
- `data_engineer (Thiết kế 9 biểu mẫu CSV chuẩn SI và từ điển dữ liệu Data Dictionary)`
- `reporting_editor (Chuẩn hóa Thuyết minh T2027 theo mẫu Trường ĐH GTVT)`
- `pipeline_engineer (Xây dựng script tự động điền và sửa lỗi thuyết minh .docx)`
