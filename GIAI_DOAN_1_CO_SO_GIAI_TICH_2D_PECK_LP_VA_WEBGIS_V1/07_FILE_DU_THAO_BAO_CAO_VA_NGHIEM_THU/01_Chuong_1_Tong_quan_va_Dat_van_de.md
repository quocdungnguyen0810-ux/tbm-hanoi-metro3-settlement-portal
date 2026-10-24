# CHƯƠNG 1: TỔNG QUAN VÀ ĐẶT VẤN ĐỀ NGHIÊN CỨU

---

## 1.1. BỐI CẢNH PHÁT TRIỂN ĐƯỜNG SẮT ĐÔ THỊ VÀ CÔNG NGHỆ TBM TẠI HÀ NỘI

Quá trình đô thị hóa nhanh chóng tại Thủ đô Hà Nội trong hai thập kỷ qua đã tạo ra áp lực khổng lồ lên mạng lưới hạ tầng giao thông mặt đất. Mật độ phương tiện cá nhân gia tăng đột biến dẫn đến tình trạng ùn tắc giao thông nghiêm trọng, ô nhiễm không khí và suy giảm chất lượng sống của cư dân đô thị. Trước tình hình đó, Quy hoạch giao thông vận tải Thủ đô Hà Nội đến năm 2030, tầm nhìn đến năm 2050 (Quyết định số 519/QĐ-TTg của Thủ tướng Chính phủ) đã xác định việc xây dựng hệ thống đường sắt đô thị (Urban Mass Rapid Transit - UMRT) gồm 10 tuyến xuyên tâm và vành đai là giải pháp chiến lược then chốt.

Trong mạng lưới này, **Tuyến đường sắt đô thị thí điểm TP. Hà Nội (Tuyến số 3: Đoạn Nhổn – Ga Hà Nội)** giữ vai trò huyết mạch kết nối khu vực phát triển phía Tây với trung tâm đô thị lịch sử. Dự án có tổng chiều dài $12.4\text{ km}$, bao gồm:
- **Đoạn đi trên cao:** Dài $8.4\text{ km}$ với 8 ga trên cao (từ ga S1 - Nhổn đến ga S8 - Cầu Giấy), đã hoàn thành công tác thi công và đưa vào vận hành thương mại từ tháng 8/2024.
- **Đoạn đi ngầm (Gói thầu CP03):** Dài khoảng $3.5\text{ km}$ (cộng thêm $0.5\text{ km}$ đoạn dốc chuyển tiếp) với 4 ga ngầm:
  - Ga S9: Kim Mã
  - Ga S10: Cát Linh (nút giao trung chuyển với Tuyến 2A Cát Linh – Hà Đông)
  - Ga S11: Văn Miếu (sát quần thể di tích Quốc Tử Giám)
  - Ga S12: Ga Hà Nội (nút giao kết nối đường sắt quốc gia trên trục Trần Hưng Đạo)

Đoạn ngầm S9–S12 được thiết kế gồm hai ống hầm đơn chạy song song, thi công bằng công nghệ khiên đào cân bằng áp lực đất (Earth Pressure Balance - EPB-TBM) với đường kính ngoài của khiên $D = 6.30\text{ m}$, đường kính trong vỏ hầm hoàn thiện $5.70\text{ m}$, chiều dày vỏ hầm bê tông cốt thép đúc sẵn $300\text{ mm}$. Khoảng cách tim hai hầm dao động từ $12.0\text{ m}$ đến $15.0\text{ m}$ (trung bình lấy $d = 13.0\text{ m}$). Chiều sâu trục hầm chôn sâu dưới mặt đất dao động trong khoảng $z_0 = 15.0\text{ m}$ đến $18.0\text{ m}$.

Tuyến hầm đi ngầm xuyên qua các khu phố cổ và phố cũ trung tâm có mật độ dân cư và công trình xây dựng dày đặc. Phần lớn các công trình hai bên trục đường Kim Mã, Cát Linh, Quốc Tử Giám và Trần Hưng Đạo là nhà phố dạng "nhà ống" từ 3 đến 5 tầng, móng nông (móng băng gạch, móng đơn bê tông), niên hạn xây dựng lâu năm, cùng nhiều khu tập thể cũ từ thập niên 1970–1980 và các di tích văn hóa lịch sử cấp quốc gia đặc biệt nhạy cảm với biến dạng lún không đều.

---

## 1.2. TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU BIẾN DẠNG LÚN DO THI CÔNG HẦM

### 1.2.1. Các nghiên cứu kinh điển và mô hình bán thực nghiệm quốc tế
Dự báo biến dạng đất nền và độ lún bề mặt do thi công hầm trong đất yếu là chủ đề nghiên cứu trọng điểm của cơ học đất và kỹ thuật công trình ngầm trong hơn 50 năm qua.

- **Peck (1969):** Dựa trên quan sát thực nghiệm tại nhiều công trình đường hầm ở Chicago và châu Âu, Ralph B. Peck là người đầu tiên chứng minh rằng mặt cắt ngang của phễu lún bề mặt đất phía trên một đường hầm đơn đào trong điều kiện không thoát nước có dạng phân bố chuẩn (phễu lún Gaussian):
  $$S(x) = S_{\max} \exp\left(-\frac{x^2}{2i^2}\right)$$
  trong đó $S_{\max}$ là độ lún cực đại tại tim hầm, $i$ là khoảng cách ngang từ tim hầm đến điểm uốn của đường cong lún (nơi độ dốc lún đạt giá trị lớn nhất).

- **O'Reilly & New (1982), Mair et al. (1993):** Phân tích dữ liệu đo đạc tại Vương quốc Anh và thiết lập mối quan hệ tuyến tính giữa khoảng cách điểm uốn $i$ và chiều sâu trục hầm $z_0$:
  $$i = K \cdot z_0$$
  với $K$ là hệ số bề rộng phễu lún không thứ nguyên phụ thuộc chặt chẽ vào loại đất: $K \approx 0.25 - 0.45$ đối với đất cát hạt thô; $K \approx 0.40 - 0.60$ đối với đất sét pha cát chặt; và $K \approx 0.60 - 0.70$ đối với đất sét mềm hữu cơ bão hòa nước.

- **Loganathan & Poulos (1998):** Khắc phục nhược điểm thuần bán thực nghiệm của Peck, Loganathan & Poulos đã phát triển mô hình giải tích dựa trên lý thuyết đàn hồi của Verruijt & Booker (1996), tích hợp hàm tương quan tổn thất thể tích tương đương và xét tới kích thước hình học hầm ($R = D/2$), độ sâu chôn hầm $z_0$ và hệ số Poisson của đất nền $\nu$. Phương trình của Loganathan & Poulos cho phép xác định trường chuyển vị lún tại bề mặt đất ($z=0$) cũng như tại các độ sâu chôn móng công trình ngầm ($z > 0$).

- **Burland (1995), Mair, Taylor & Burland (1996):** Đã đặt nền móng cho quy chuẩn đánh giá nguy cơ tổn hại kết cấu công trình dựa trên ba tham số biến dạng: độ lún tuyệt đối $S_v$, độ dốc góc xoay (angular distortion / tilt $\theta = dS/dx$), và biến dạng kéo ngang tới hạn của khối xây $\epsilon_{\text{lim}}$. Tiêu chuẩn này phân chia mức độ hư hại công trình thành 6 cấp (từ Cấp 0: Không đáng kể đến Cấp 5: Sụp đổ kết cấu), hiện là tiêu chuẩn vàng được áp dụng trong đánh giá tác động môi trường các dự án hầm đô thị quốc tế.

### 1.2.2. Các nghiên cứu liên quan đến Metro Hà Nội và TP. Hồ Chí Minh
Tại Việt Nam, các nghiên cứu về thi công TBM trong môi trường địa chất đô thị đang phát triển mạnh mẽ:
- **Shin et al. (2020):** Nghiên cứu các yếu tố thiết kế khiên đào EPB cho Tuyến đường sắt đô thị số 3 Hà Nội, nhấn mạnh vai trò khống chế áp lực cân bằng đất trong tầng đất bùn sét yếu để hạn chế lún bề mặt.
- **Giao, Nguyen & Hoang (2020):** Thu thập và phân tích số liệu địa kỹ thuật từ 17 hố khoan khảo sát dọc theo $12.4\text{ km}$ Tuyến 3 Nhổn – Ga Hà Nội, phân chia địa tầng Đệ tứ khu vực thành 6 tầng cơ bản và cảnh báo nguy cơ lún cố kết dài hạn do hạ thấp mực nước ngầm tầng Pleistocen.
- **Nguyen, Bui & Nguyen (2024):** Nghiên cứu tác động của tải trọng động đất lên kết cấu hầm TBM đoạn S9–S10 (Kim Mã - Cát Linh), công bố chi tiết các thông số cơ lý đại diện của 6 đơn nguyên thạch học từ GU1 đến GU8.
- **Nguyen, Kohata & Nguyen (2024):** Khảo sát hố khoan thực tế BH12 trên đoạn S11–S12 (Văn Miếu - Ga Hà Nội), chỉ rõ sự xuất hiện của tầng bùn sét mềm hữu cơ dày tới $12.7\text{ m}$ bao trùm toàn bộ không gian đào của khiên TBM với mô-đun biến dạng $E$ chỉ đạt $7.68\text{ MPa}$.

---

## 1.3. KHOẢNG TRỐNG TRI THỨC VÀ ĐẶT VẤN ĐỀ (RESEARCH GAPS)

Mặc dù các công trình nêu trên đã cung cấp nhiều mảnh ghép quan trọng, việc quản lý và dự báo rủi ro lún mặt đất cho đoạn ngầm S9–S12 vẫn tồn tại những khoảng trống khoa học và kỹ thuật nghiêm trọng:

1. **Thiếu một bộ cơ sở dữ liệu địa kỹ thuật kiểm định nguồn mở (Verified Open Baseline):**
   Phần lớn các số liệu địa tầng, hố khoan và mực nước ngầm nằm rải rác trong các bài báo độc lập hoặc các báo cáo nội bộ của dự án. Nhiều nghiên cứu khi mô phỏng số đã tự do gán các tham số địa chất giả định mà không ghi nhận rõ nguồn gốc, dẫn đến khó khăn trong việc kiểm chứng và tái lập kết quả khoa học.
   
   > `==[AUDIT CẦN BỔ SUNG: Hiện nay toàn văn hồ sơ khảo sát địa chất giai đoạn thiết kế kỹ thuật (CP03 Geotechnical Survey Report) và tọa độ chính xác của toàn bộ mạng lưới hố khoan chưa được công bố công khai. Nghiên cứu này neo giữ cột địa tầng vào hố khoan BH12 đã được công bố chính thức có kiểm định bởi Nguyen, Kohata & Nguyen (2024) và mặt cắt S9–S10 của Nguyen et al. (2024). Khi có hồ sơ as-built, cần rà soát lại toàn bộ tọa độ hố khoan.]==`

2. **Sự đánh đổi giữa mô hình số 3D phức tạp và phương pháp giải tích minh bạch:**
   Các mô hình phần tử hữu hạn 3D (3D FEM) thường đòi hỏi hàng chục tham số phi tuyến đàn dẻo vốn rất khó xác định chính xác trong đất bồi tích phân lớp phức tạp. Ngược lại, phương pháp giải tích phễu lún Gaussian dựa trên định luật bảo toàn thể tích thể hiện tính minh bạch vật lý tuyệt đối, dễ kiểm soát sai số và cho phép quét độ nhạy hàng nghìn kịch bản trong vài giây. Tuy nhiên, sự kết hợp giữa mô hình Gaussian truyền thống với mô hình bán giải tích Loganathan & Poulos và phân tích độ nhạy có hệ thống cho tuyến Metro Hà Nội chưa từng được công bố toàn diện.

3. **Khoảng trống trong dự báo thời gian thực và quản lý rủi ro địa không gian (GIS):**
   Trong quá trình khiên đào TBM vận hành dưới lòng đường Kim Mã và Cát Linh, người vận hành cần biết ngay lập tức phạm vi phễu lún mở rộng và mức độ rủi ro đối với từng tòa nhà cụ thể tương ứng với thể tích đất đào ra sau mỗi ring vỏ hầm. Việc chạy các phần mềm mô phỏng nặng nề mất hàng giờ là không thể đáp ứng. Do đó, nhu cầu phát triển một **module học máy thay thế (Surrogate AI)** có khả năng suy luận trong phần nghìn giây kết hợp với **hệ thống bản đồ số WebGIS tương tác** là một đòi hỏi kỹ thuật cấp bách.

---

## 1.4. MỤC TIÊU VÀ ĐỐI TƯỢNG NGHIÊN CỨU

### 1.4.1. Mục tiêu tổng quát
Nghiên cứu đánh giá định lượng độ nhạy biến dạng lún mặt đất và phân vùng ảnh hưởng nguy hại do thi công hầm đôi TBM đoạn S9–S12 Tuyến đường sắt đô thị số 3 Hà Nội, xây dựng bộ công cụ tích hợp giải tích – WebGIS – AI phục vụ kiểm soát rủi ro công trình và cung cấp cơ sở khoa học cho công tác quan trắc hiện trường.

### 1.4.2. Mục tiêu cụ thể
1. Thu thập, chuẩn hóa và kiểm toán minh bạch cơ sở dữ liệu địa tầng, cơ lý đất nền và hình học tuyến hầm S9–S12.
2. Xây dựng mô hình toán giải tích tính toán lún hầm đơn và siêu vị hầm đôi, kiểm chứng bảo toàn thể tích và đối sánh giữa mô hình Peck (1969) và Loganathan & Poulos (1998).
3. Thiết lập ma trận phân tích độ nhạy 21 kịch bản tổn thất thể tích đất ($V_L \in [0.5\%; 2.0\%]$), xác định ngưỡng an toàn và vùng ảnh hưởng nguy hại.
4. Xây dựng bản đồ số WebGIS và cơ sở dữ liệu 60 công trình móng nông đại diện dọc tuyến, phân cấp rủi ro hư hại theo tiêu chuẩn Burland (1995).
5. Huấn luyện mô hình mạng nơ-ron Surrogate AI (MLP) dự báo lún tức thời thời gian thực đạt độ chính xác cao ($R^2 > 0.999$).
6. Đề xuất quy trình quan trắc địa kỹ thuật và ngưỡng phản ứng khẩn cấp (TARP) bảo vệ an toàn công trình đô thị.

---

## 1.5. Ý NGHĨA KHOA HỌC VÀ GIÁ TRỊ THỰC TIỄN

- **Ý nghĩa khoa học:**
  - Chứng minh sự tương thích và giới hạn ứng dụng của mô hình giải tích Gaussian và Loganathan & Poulos đối với địa tầng bồi tích Đệ tứ có tầng bùn sét mềm dày bao quanh hầm.
  - Cung cấp phương pháp luận kiểm toán dữ liệu nghiên cứu (Evidence Traceability Protocol) với 5 cổng nghiệm thu (Audit Gates), đảm bảo tính tái lập và chống suy đoán giả tạo trong nghiên cứu kỹ thuật công trình ngầm.
  - Đóng góp giải pháp mô hình hóa Surrogate AI thuần túy (thuật toán tinh gọn không phụ thuộc framework cồng kềnh) để xấp xỉ trường chuyển vị địa kỹ thuật.

- **Giá trị thực tiễn:**
  - Cung cấp cho Ban Quản lý Đường sắt đô thị Hà Nội (MRB) và các nhà thầu thi công gói thầu CP03 một bộ công cụ tính toán nhanh trên Excel và WebGIS để dự báo lún trước mỗi ca đào TBM.
  - Nhận diện sớm các điểm xung yếu dọc tuyến (đoạn qua tầng bùn sét BH12, khu vực gần di tích Văn Miếu) để chủ động lập phương án phụt vữa gia cường hoặc quan trắc đặc biệt.

---

## 1.6. KHUNG PHƯƠNG PHÁP NGHIÊN CỨU TỔNG THỂ

Quy trình nghiên cứu tổng thể của luận án được minh họa trên Hình 1.1, thể hiện sự phối hợp chặt chẽ giữa 5 mô-đun chức năng: Thu thập & Kiểm toán dữ liệu $\rightarrow$ Mô hình hóa giải tích $\rightarrow$ Mô hình Surrogate AI $\rightarrow$ Hệ thống WebGIS $\rightarrow$ Quy trình quan trắc & Phản biện.

<br>

<div align="center">

![Hình 1.1: Khung phương pháp nghiên cứu tổng thể tích hợp Giải tích - WebGIS - AI Surrogate và Audit quan trắc](../03_hinh_anh_minh_hoa_chat_luong_cao/FIG_07_Methodological_Workflow_Framework.png)

*Hình 1.1: Khung phương pháp nghiên cứu tổng thể tích hợp Giải tích - WebGIS - AI Surrogate và Audit quan trắc*

</div>

<br>

---

## 1.7. ĐÁNH GIÁ, PHẢN BIỆN VÀ GHI CHÚ AUDIT CỦA CHƯƠNG 1

> **Ghi chú Kiểm toán Khoa học (Audit Note 1.1):**
> - **Cấp độ tin cậy của phạm vi nghiên cứu:** Rất cao đối với kích thước hình học hầm ($D = 6.30\text{ m}, d \approx 13\text{ m}, z_0 = 15 - 18\text{ m}$) do đã được đối chiếu chéo giữa báo cáo ĐTM chính thức của ADB (2013) và hai bài báo công bố năm 2024.
> - **Điểm cần hiệu chỉnh khi thi công thực tế:** Bình đồ tim tuyến chính xác theo hệ tọa độ VN-2000 kinh tuyến trục $105^\circ$ với tọa độ đỉnh cong (PI) và bán kính cong nằm ngang cần được nạp trực tiếp từ bản vẽ thiết kế thi công (Shop Drawings) khi nhà thầu kích khiên.
> - **Biện pháp khắc phục trong đề tài:** Mô hình hóa trục hầm dưới dạng tuyến hình học tham số hóa, cho phép cập nhật tức thời tọa độ tim tuyến vào file Excel `TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx` và bản đồ WebGIS.
