# BẢN GHI CHÚ KHOA HỌC: ĐỐI CHIẾU HỌC THUẬT, ĐÁNH GIÁ TÍNH MỚI VÀ CHIẾN LƯỢC TRÁNH TRÙNG LẶP CHO ĐỀ TÀI CẤP TRƯỜNG & BÀI BÁO TRONG NƯỚC

**Đơn vị:** Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường, Trường Đại học Giao thông vận tải  
**Người phụ trách:** TS. Nguyễn Hải Hà  
**Đối tượng áp dụng:** Đề tài NCKH Cấp Trường (UTC) & Bài báo khoa học trong nước (Tạp chí Giao thông vận tải)

---

## I. MỤC ĐÍCH BẢN GHI CHÚ
Bản ghi chú này làm rõ ranh giới học thuật, khẳng định tính độc lập và tính mới tuyệt đối của đề tài nghiên cứu cấp Trường dự kiến so với các công bố khoa học tiêu biểu đã có trong nước; đồng thời đề xuất khung lập luận phần **Tổng quan nghiên cứu (Literature Review)** để biến các công bố đi trước thành bệ phóng khoa học vững chắc.

---

## II. ĐỐI CHIẾU CHI TIẾT CÁC CÔNG BỐ TIÊU BIỂU TRONG NƯỚC

### 1. Công bố 1: TS. Nguyễn Anh Thư et al. (2019)
- **Tên bài báo:** *Phân tích độ nhạy của các yếu tố ảnh hưởng đến lún mặt đất do đào hầm bằng khiên đào trong đất yếu* (Kỷ yếu Hội nghị / Tạp chí chuyên ngành, 2019).
- **Phương pháp tiếp cận:**
  - Sử dụng phương pháp **phân tích độ nhạy cục bộ truyền thống (Local Sensitivity Analysis - OAT / One-At-a-Time)**.
  - Sử dụng phần mềm thương mại **Plaxis**.
  - Giữ cố định hầu hết các biến số, lần lượt tăng/giảm từng thông số hình học ($D, H$) hoặc đất nền ($c, \varphi$) để quan sát mức độ thay đổi của độ lún mặt đất.
- **Hạn chế học thuật & Khoảng trống:**
  - Phương pháp OAT không xét đến tương tác phi tuyến đa biến giữa các lớp đất với nhau và giữa đất nền với tải trọng thi công.
  - Mô hình mang tính tất định (deterministic), không phản ánh bản chất biến thiên ngẫu nhiên không gian thực tế của đất trầm tích trẻ ngậm nước TP.HCM.

### 2. Công bố 2: TS. Nguyễn Văn Hùng et al. (Tạp chí Xây dựng, 12/2020 - 2025)
- **Tên bài báo:** *Ảnh hưởng của việc lựa chọn mô hình đất đến kết quả dự báo lún bề mặt khi thi công đường hầm khiên đào tại Hà Nội* (Tạp chí Xây dựng, 12/2020).
- **Đối tượng & Địa bàn nghiên cứu:**
  - Tuyến ĐSĐT Thí điểm TP. Hà Nội, Tuyến số 3 (Nhổn - Ga Hà Nội).
  - Địa tầng trầm tích Đệ tứ Hà Nội: cát pha, sét pha, cuội sỏi ($GU1s, GU3\&4, GU5, GU7\&8$).
- **Phương pháp mô phỏng:**
  - Mô hình số Plaxis 2D so sánh ứng xử giữa mô hình Mohr-Coulomb (MC) và Hardening Soil (HS).
  - Áp dụng giả định mất mát thể tích định trước (**$V_l = 0.5\%$**, co ngót hình học đồng nhất xung quanh chu vi hầm).
- **Hạn chế học thuật & Khoảng trống:**
  - Thiết kế tất định thuần túy, không lượng hóa độ bất định của thông số cơ lý.
  - Giả định mất mát thể tích $V_l = 0.5\%$ là biến dạng hình học thụ động, chưa mô phỏng cơ chế cơ học tiếp xúc chủ động của máy EPB TBM (áp lực giữ gương đào $P_s$, áp lực ép vữa chèn khe hở đuôi khiên $P_a$).

---

## III. BẢNG MA TRẬN ĐỐI CHIẾU HỌC THUẬT TRỰC DIỆN

| Tiêu chí so sánh | Nguyễn Anh Thư et al. (2019) | Nguyễn Văn Hùng et al. (2020) | Đề tài Nhóm nghiên cứu (Đề xuất) |
| :--- | :--- | :--- | :--- |
| **Địa bàn & Địa tầng** | Đất yếu TP.HCM (tổng quát) | Hà Nội (Metro 3: Nhổn - Ga HN) | TP.HCM (Metro 1: CP1b, bùn sét $Ac2$ & cát $As1/2$) |
| **Công cụ mô phỏng** | Plaxis 2D (Phần mềm đóng) | Plaxis 2D (Phần mềm đóng) | **OpenSeesPy (Mã nguồn mở Python)** |
| **Phương pháp tiếp cận** | Tất định, biến thiên đơn biến (OAT) | Tất định, so sánh mô hình MC & HS | **Ngẫu nhiên (Stochastic), Toàn cục (GSA)** |
| **Mô phỏng thi công** | Biến thiên hình học/tải trọng đơn giản | Áp đặt co ngót thể tích $V_l = 0.5\%$ | **Mô phỏng cơ học động: Áp lực gương $P_s$ & vữa $P_a$** |
| **Khả năng mở rộng AI** | Rất khó, không tự động hóa được | Không khả thi trong môi trường GUI | **Tự động hóa hoàn toàn, sinh dữ liệu lớn cho AI & MCS** |

---

## IV. BỐN ĐIỂM KHÁC BIỆT CỐT LÕI TẠO NÊN TÍNH MỚI TUYỆT ĐỐI

1. **Công cụ mã nguồn mở OpenSeesPy (Khắc phục hạn chế của Plaxis):**
   - Viết code Python thuần túy, làm chủ 100% thuật toán giải phi tuyến ma trận độ cứng.
   - Cho phép tự động hóa lặp hàng nghìn kịch bản mô phỏng ngẫu nhiên mà không cần thao tác bấm chuột thủ công.
2. **Cơ chế thi công cơ học động lực học (Khắc phục giả định $V_l$ thụ động):**
   - Mô phỏng trực tiếp áp lực giữ gương đào $P_s$ và áp lực ép vữa chèn khe hở đuôi khiên $P_a$ bám sát số liệu giám sát thực tế từ máy EPB TBM Gói thầu CP1b (Metro 1 TP.HCM).
3. **Phân tích độ nhạy ngẫu nhiên toàn cục (Global Sensitivity Analysis - GSA):**
   - Vượt qua phương pháp đơn biến OAT bằng phương pháp phân tích độ nhạy dựa trên phương sai (Sobol' Indices / Morris Method).
   - Đánh giá tương tác ngẫu nhiên giữa các chỉ tiêu cơ lý đất nền ($COV = 15\% \div 30\%$) với thông số vận hành máy.
4. **Địa tầng trầm tích trẻ TP.HCM & Số liệu thực địa CP1b:**
   - Tập trung giải quyết bài toán mâu thuẫn mô đun của lớp cát ngậm nước $As1/As2$ nằm dưới lớp bùn sét $Ac2$ dày của TP.HCM, đối chiếu trực tiếp với quan trắc lún thực địa Km0+700.

---

## V. ĐỀ XUẤT TIÊU ĐỀ ĐỀ TÀI VÀ BÀI BÁO TRONG NƯỚC

- **Tên Đề tài NCKH Cấp Trường (UTC):**  
  > *"Nghiên cứu đánh giá độ nhạy ngẫu nhiên của biến dạng lún mặt đất khi đào hầm TBM tuyến Metro số 1 TP.HCM trên nền tảng phần tử hữu hạn mã nguồn mở."*
- **Tên Bài báo Khoa học Trong nước (Tạp chí Giao thông vận tải):**  
  > *"Đánh giá độ nhạy toàn cục của độ lún mặt đất theo các thông số vận hành khiên đào và địa tầng ngẫu nhiên bằng OpenSeesPy: Áp dụng cho Metro số 1 TP.HCM."*

---

## VI. CHIẾN LƯỢC VIẾT PHẦN TỔNG QUAN (LITERATURE REVIEW)

Để biến hai nghiên cứu trước thành bệ phóng học thuật, cấu trúc lập luận trong bản thuyết minh và bài báo sẽ được xây dựng như sau:

1. **Ghi nhận đóng góp của nghiên cứu tiền bối:**
   > *"Các nghiên cứu gần đây trong nước đã bước đầu phân tích ứng xử của đất nền khi đào hầm metro, chẳng hạn như nghiên cứu của Nguyễn Văn Hùng và cộng sự (2020) đã chứng minh tầm quan trọng của mô hình đất phi tuyến tại tuyến Metro số 3 Hà Nội..."*
2. **Chỉ ra khoảng trống học thuật cần lấp đầy:**
   > *"Tuy nhiên, việc áp đặt mất mát thể tích hình học $V_l$ cố định chưa mô tả được tương tác cơ học chủ động giữa áp lực gương đào $P_s$ và áp lực ép vữa $P_a$. Mặt khác, nghiên cứu của Nguyễn Anh Thư và cộng sự (2019) về đào hầm trong đất yếu TP.HCM đã đánh giá độ nhạy theo phương pháp đơn biến (OAT), chưa phản ánh được tính biến thiên ngẫu nhiên đồng thời và tính phi tuyến đa biến của các chỉ tiêu cơ lý..."*
3. **Khẳng định tính mới và đóng góp của nghiên cứu hiện tại:**
   > *"Để khắc phục triệt để các hạn chế trên, nghiên cứu này xây dựng khung phân tích độ nhạy ngẫu nhiên toàn cục (Global Sensitivity Analysis) trên nền tảng mã nguồn mở OpenSeesPy, kết nối trực tiếp thông số vận hành thực tế của máy TBM tại Gói thầu CP1b Metro số 1 TP.HCM với phân phối ngẫu nhiên địa kỹ thuật."*

---

## VII. LỘ TRÌNH KẾT NỐI HỌC THUẬT

```
[Đề tài Cấp Trường UTC] (2D OpenSeesPy + Độ nhạy Sobol')
             │
             ├──► [01 Bài báo Tạp chí GTVT] (Minh chứng năng lực)
             │
             ▼
[Thuyết minh NAFOSTED 2027-2029] (Mô hình 3D + Trường ngẫu nhiên)
             │
             ├──► [Nâng cấp Bài 2 - Q1] (OpenSeesPy + AI Surrogate + 100k MCS)
             │
             └──► [Bài 4 Độc lập - Q1] (Độ tin cậy RESS/Structural Safety)
```
