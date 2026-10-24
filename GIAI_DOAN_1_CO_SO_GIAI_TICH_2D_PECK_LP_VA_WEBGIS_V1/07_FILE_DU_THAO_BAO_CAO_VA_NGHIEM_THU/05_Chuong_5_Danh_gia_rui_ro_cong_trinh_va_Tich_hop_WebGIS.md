# CHƯƠNG 5: ĐÁNH GIÁ NGUY CƠ HƯ HỎNG CÔNG TRÌNH VÀ TÍCH HỢP HỆ THỐNG WEBGIS

---

## 5.1. KHẢO SÁT HIỆN TRẠNG CÔNG TRÌNH DỌC HÀNH LANG HẦM S9–S12

Tuyến hầm đôi TBM đoạn S9–S12 có chiều dài khoảng $3.5\text{ km}$, chạy ngầm bên dưới các tuyến phố cổ và phố cũ huyết mạch có mật độ xây dựng cao nhất thành phố Hà Nội:
- **Đoạn ga S9 – ga S10:** Đi dưới đường Kim Mã, phố Cát Linh.
- **Đoạn ga S10 – ga S11:** Đi qua nút giao Cát Linh – Giảng Võ, phố Bích Câu, phố Quốc Tử Giám.
- **Đoạn ga S11 – ga S12:** Đi dọc phố Quốc Tử Giám, phố Văn Miếu, rẽ qua đường Phan Bội Châu đến phố Trần Hưng Đạo.

### 5.1.1. Phân loại kết cấu công trình chịu ảnh hưởng
Dọc hành lang hẹp $\pm 35\text{ m}$ tính từ tim tuyến hầm, các công trình xây dựng chủ yếu thuộc 4 nhóm kết cấu đặc trưng:
1. **Nhà ống đô thị (Shophouses):** Chiếm khoảng 65% số lượng công trình. Đặc điểm: chiều ngang hẹp ($3.0 - 5.0\text{ m}$), chiều sâu lớn ($10 - 20\text{ m}$), cao từ 3 đến 5 tầng. Phần lớn sử dụng móng gạch hoặc móng băng nông đặt ở độ sâu $-1.5\text{ m}$ đến $-2.5\text{ m}$ trong tầng đất đắp hoặc sét dẻo cứng mặt. Các nhà xây chen sát vách, chia sẻ tường chung hoặc khe lún hẹp, rất dễ bị biến dạng chéo khi một bên móng bị lún.
2. **Khu tập thể cũ lắp ghép (Old Apartment Blocks):** Xây dựng từ những năm 1970–1980 tại khu vực Kim Mã, Cát Linh. Kết cấu tấm lớn lắp ghép hoặc khung bê tông bán lắp ghép 4–5 tầng, móng bè nông trên nền đất yếu. Các mối nối liên kết sau hơn 40 năm đã xuống cấp và rỉ sét, khả năng chịu lún lệch rất kém.
3. **Trụ sở cơ quan và công trình hỗn hợp hiện đại:** Chiều cao từ 7 đến 15 tầng, sử dụng móng cọc bê tông cốt thép ép hoặc khoan nhồi tựa vào tầng cát cuội sỏi sâu ($>30\text{ m}$). Các công trình này ít chịu ảnh hưởng của lún bề mặt nông nhưng cần kiểm tra lực ma sát âm (negative skin friction) tác dụng lên thân cọc.
4. **Quần thể di tích lịch sử - văn hóa đặc biệt (Di tích Quốc Tử Giám và các đền chùa cổ):** Kết cấu gỗ cổ truyền, tường gạch vôi vữa, móng nông đặt trực tiếp trên nền đất tự nhiên. Đây là đối tượng nhạy cảm tối cao, bắt buộc phải bảo tồn nguyên trạng, không cho phép phát sinh bất kỳ vết nứt nào.

### 5.1.2. Cơ sở dữ liệu số hóa 60 công trình đại diện
Để phục vụ đánh giá định lượng, nhóm nghiên cứu đã tiến hành số hóa không gian và thuộc tính kỹ thuật của **60 công trình đại diện** dọc theo hành lang hầm S9–S12 trong dải đệm $\pm 30\text{ m}$ tính từ trục tim tuyến. Dữ liệu bao gồm: tọa độ địa lý (WGS-84), lý trình tuyến (Km), khoảng cách ngang tới tim hầm ($x_{\text{offset}}$), loại hình kết cấu, số tầng, loại móng và cấp bảo vệ ưu tiên.

Toàn bộ danh mục 60 công trình này được quản lý chi tiết trong file Excel [TBM_BUILDING_RISK_EXPOSURE.xlsx](../02_du_lieu_excel_chuyen_nghiep/TBM_BUILDING_RISK_EXPOSURE.xlsx).

---

## 5.2. ĐÁNH GIÁ NGUY CƠ HƯ HỎNG CÔNG TRÌNH THEO CÁC KỊCH BẢN THI CÔNG

Dựa trên tọa độ và cự ly ngang của từng công trình đối với tim tuyến hầm đôi ($x_{\text{offset}}$), độ lún bề mặt $S_v$ và độ dốc mặt đất $\theta$ tại vị trí móng công trình được tính toán theo mô hình siêu vị hầm đôi tương ứng với 4 mức tổn thất thể tích: $V_L = 0.5\%$, $V_L = 1.0\%$, $V_L = 1.5\%$ và $V_L = 2.0\%$.

Mức độ rủi ro được phân loại theo tiêu chuẩn Burland (1995):
- **Cấp 0 (Không đáng kể / Negligible):** $S_v < 10\text{ mm}, \theta < 1/500$.
- **Cấp 1 (Rất nhẹ / Very Slight):** $10 \le S_v < 20\text{ mm}, 1/500 \le \theta < 1/333$.
- **Cấp 2 (Nhẹ / Slight):** $20 \le S_v < 30\text{ mm}, 1/333 \le \theta < 1/200$.
- **Cấp 3 (Vừa phải / Moderate):** $30 \le S_v < 45\text{ mm}, 1/200 \le \theta < 1/100$.
- **Cấp 4 (Nặng / Severe):** $S_v \ge 45\text{ mm}, \theta \ge 1/100$.

<br>

**Bảng 5.1: Thống kê phân bố cấp độ rủi ro của 60 công trình theo 4 kịch bản tổn thất thể tích**

| Kịch bản tổn thất | Cấp 0 (Không đáng kể) | Cấp 1 (Rất nhẹ) | Cấp 2 (Nhẹ) | Cấp 3 (Vừa phải / Nguy hại) | Cấp 4 (Nặng / Sự cố) | Tổng số công trình có rủi ro Cấp 2 trở lên |
|---|---|---|---|---|---|---|
| **$V_L = 0.5\%$ (Kiểm soát tối ưu)** | **46 (76.7%)** | 14 (23.3%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | **0 (0.0%)** |
| **$V_L = 1.0\%$ (Mức chuẩn vận hành)** | **28 (46.7%)** | **19 (31.7%)** | **13 (21.6%)** | 0 (0.0%) | 0 (0.0%) | **13 (21.6%)** |
| **$V_L = 1.5\%$ (Cảnh báo biến dạng)** | 12 (20.0%) | 18 (30.0%) | 17 (28.3%) | **13 (21.7%)** | 0 (0.0%) | **30 (50.0%)** |
| **$V_L = 2.0\%$ (Sự cố đào hầm)** | 6 (10.0%) | 12 (20.0%) | 16 (26.7%) | **21 (35.0%)** | **5 (8.3%)** | **42 (70.0%)** |

<br>

<div align="center">

![Hình 5.1: Phân bố cấp độ rủi ro hư hỏng của 60 công trình dọc hành lang S9–S12](../03_hinh_anh_minh_hoa_chat_luong_cao/FIG_05_Building_Risk_Zoning_Distribution.png)

*Hình 5.1: Phân bố cấp độ rủi ro hư hỏng của 60 công trình dọc hành lang S9–S12 theo các mức tổn thất thể tích đất*

</div>

<br>

### Nhận định đánh giá chuyên sâu:
1. **Ở kịch bản kiểm soát tốt ($V_L = 0.5\%$):** 100% công trình nằm trong vùng Cấp 0 và Cấp 1, không có bất kỳ công trình nào bị rủi ro nứt tường gạch hay kẹt cửa. Đây là mục tiêu vận hành lý tưởng cần đạt được của nhà thầu thi công EPB-TBM.
2. **Ở kịch bản tiêu chuẩn ($V_L = 1.0\%$):** Khoảng 78.4% số công trình an toàn tuyệt đối (Cấp 0 và 1). Có 13 công trình (21.6%) nằm trực diện sát tim tuyến chịu độ lún từ $20\text{ mm}$ đến $23\text{ mm}$ (Cấp 2: Nhẹ), xuất hiện các vết nứt nhỏ $<1\text{ mm}$ trên tường vôi vữa, cần được theo dõi định kỳ.
3. **Khi xảy ra sự cố ($V_L = 2.0\%$):** Tình hình rủi ro leo thang nghiêm trọng: có tới **42 công trình (70%)** rơi vào cấp hư hại từ Nhẹ đến Nặng. Đặc biệt có 5 công trình nằm sát tim hầm trên đường Kim Mã chịu độ lún vượt quá $44\text{ mm}$ và độ dốc vượt $1/400$, rơi vào Cấp 4 (Severe), đe dọa nứt dầm sàn và mất an toàn kết cấu.

---

## 5.3. PHÁT TRIỂN HỆ THỐNG WEBGIS TƯƠNG TÁC GIÁM SÁT LÚN

Nhằm chuyển giao kết quả nghiên cứu lý thuyết thành công cụ quản trị rủi ro trực quan phục vụ thực địa, một hệ thống bản đồ số WebGIS tương tác đa nền tảng đã được phát triển trên nền tảng thư viện mã nguồn mở **Leaflet.js** (kết hợp GeoJSON và OpenStreetMap/Esri World Imagery).

### 5.3.1. Cấu trúc các lớp dữ liệu không gian trong WebGIS
1. **Lớp tim tuyến hầm đôi (Metro Line 3 Alignments):** Thể hiện hai ống hầm song song với mã màu nổi bật, gắn nhãn lý trình Km và các nhà ga ngầm S9, S10, S11, S12.
2. **Lớp các vành đệm phân vùng ảnh hưởng lún (Settlement Envelopes):**
   - Vùng đệm $S > 5\text{ mm}$ (Bán kính ảnh hưởng mở rộng).
   - Vùng đệm $S > 10\text{ mm}$ (Vùng bắt đầu có biến dạng quan sát được).
   - Vùng đệm $S > 15\text{ mm}$ (Vùng cảnh báo kỹ thuật).
   - Vùng đệm $S > 20\text{ mm}$ (Vùng nguy cơ cao sát tim tuyến).
3. **Lớp 60 đối tượng công trình kiến trúc (Building Risk Layer):**
   Mỗi công trình được thể hiện bằng một điểm đánh dấu (Marker) có màu sắc thay đổi động theo cấp rủi ro:
   - Xanh lá cây: Cấp 0 & 1 (An toàn / Lún nhẹ $<15\text{ mm}$).
   - Vàng cam: Cấp 2 (Cảnh báo theo dõi $15 - 25\text{ mm}$).
   - Đỏ rực: Cấp 3 & 4 (Nguy hiểm cao $>25\text{ mm}$).
   Khi nhấp chuột (click) vào từng công trình, một cửa sổ tương tác (Popup) sẽ hiển thị đầy đủ thông tin: Tên/Địa chỉ, Khoảng cách tới hầm, Độ lún dự báo, Độ nghiêng, Cấp rủi ro và Khuyến cáo gia cố.

Hệ thống WebGIS hoàn chỉnh được đóng gói độc lập trong tập tin `webgis_settlement_map.html` tại thư mục kết quả nghiên cứu, có thể mở trực tiếp trên mọi trình duyệt web (Chrome, Edge, Firefox) hoặc thiết bị di động mà không cần cài đặt phần mềm chuyên ngành GIS phức tạp.

---

## 5.4. ĐÁNH GIÁ, PHẢN BIỆN VÀ GHI CHÚ AUDIT CỦA CHƯƠNG 5

> **Ghi chú Kiểm toán Khoa học (Audit Note 5.1):**
> 1. **Mô hình hóa hình học công trình:**
>    - `==[AUDIT CẦN BỔ SUNG: Dữ liệu 60 công trình hiện tại được số hóa dưới dạng điểm đại diện (Centroid Point) với khoảng cách ngang giả định tương đối dọc theo trục đường Kim Mã, Cát Linh, Quốc Tử Giám. Trước khi máy TBM vận hành thực tế qua từng đoạn, bắt buộc chủ đầu tư phải thực hiện công tác "Khảo sát tình trạng công trình trước thi công" (Pre-construction Condition Survey - PCS) để lập biên bản hiện trạng vết nứt cũ, độ nghiêng ban đầu và kết cấu móng của từng ngôi nhà.]==`
> 2. **Hiệu ứng độ cứng kết cấu (Building Stiffness Effect):**
>    - Mô hình tính toán trong luận án hiện đánh giá theo độ lún bề mặt tự do (greenfield ground settlement). Trong thực tế, các công trình có độ cứng móng lớn (như móng bè hoặc khung bê tông liền khối) sẽ có tác dụng kìm hãm biến dạng uốn của đất nền, làm giảm độ cong thực tế mà tòa nhà phải chịu (Potts & Addenbrooke, 1997; Franzius et al., 2006). Do đó, dự báo greenfield trong nghiên cứu này mang tính an toàn bảo thủ (conservative).
> 3. **Xem dữ liệu chi tiết công trình:**
>    - Toàn bộ bảng dữ liệu và phân tích rủi ro 60 công trình được lưu trữ chuyên nghiệp tại [TBM_BUILDING_RISK_EXPOSURE.xlsx](../02_du_lieu_excel_chuyen_nghiep/TBM_BUILDING_RISK_EXPOSURE.xlsx).
