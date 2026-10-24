# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ PHƯƠNG PHÁP TÍNH TOÁN GIẢI TÍCH

---

## 2.1. CƠ CHẾ BIẾN DẠNG ĐẤT NỀN XUNG QUANH KHIÊN ĐÀO CÂN BẰNG ÁP LỰC ĐẤT (EPB-TBM)

Quá trình thi công hầm bằng khiên đào EPB-TBM trong môi trường địa chất đô thị là một bài toán tương tác phức tạp giữa máy đào, đất nền, nước ngầm và vỏ hầm lắp ghép. Khác với phương pháp đào mở (cut-and-cover) hoặc phương pháp đào ngầm truyền thống (NATM), khiên đào EPB kiểm soát biến dạng đất nền thông qua một buồng áp lực (pressure chamber) kín phía sau gương đào.

### 2.1.1. Các thành phần tổn thất thể tích đất trong chu kỳ thi công TBM
Biến dạng lún bề mặt đất phát sinh chủ yếu do hiện tượng "tổn thất thể tích đất" (ground volume loss), xảy ra qua bốn giai đoạn kế tiếp nhau trong suốt quá trình khiên đào tiến lên:

1. **Tổn thất trước gương đào ($V_{\text{face}}$):**
   Phát sinh khi áp lực đất và áp lực nước ngầm trong khoang đào EPB thấp hơn ứng suất pháp tự nhiên trong đất ($\sigma_0$). Đất nền phía trước gương bị biến dạng dẻo trượt vào buồng đào, gây ra hiện tượng lún sớm (pre-settlement) xuất hiện trước khi mũi khiên đào tới vị trí quan trắc khoảng $(1.0 - 1.5) \cdot z_0$. Ngược lại, nếu áp lực khoang đào quá cao sẽ gây trồi đất (heave).

2. **Tổn thất dọc thân khiên ($V_{\text{shield}}$):**
   Do thân khiên đào có dạng côn nhẹ (tapered shield) thu nhỏ về phía đuôi để giảm ma sát, kết hợp với hiện tượng khiên đào bị lắc lệch (pitching/yawing) khi điều chỉnh hướng lái và việc đào dư (over-cutting) của dao viền. Khoảng trống hình học này khiến đất xung quanh co thắt lại bám vào vỏ ngoài khiên đào.

3. **Tổn thất tại khe hở đuôi khiên ($V_{\text{tail}}$):**
   Đây là thành phần chiếm tỷ trọng lớn nhất (từ 50% đến 70% tổng lượng tổn thất thể tích) trong điều kiện thi công thông thường. Khi các tấm vỏ hầm đúc sẵn (segments) được lắp dựng xong trong lòng khiên và rời khỏi đuôi khiên, tồn tại một khe hở hình xuyến (tail void) giữa đường kính ngoài của khiên đào ($D = 6.30\text{ m}$) và đường kính ngoài của vỏ hầm ($D_{\text{ring}} \approx 6.00\text{ m}$). Khoảng hở này có bề dày khoảng $120 - 150\text{ mm}$. Nếu vữa chèn (backfill grout) không được bơm phụt áp lực cao lấp đầy tức thời, đất yếu xung quanh sẽ sập lún vào khoảng trống này.

4. **Tổn thất do cố kết dài hạn ($V_{\text{consolidation}}$):**
   Sau khi vỏ hầm đã ổn định, ứng suất dư và áp lực nước lỗ rỗng thặng dư sinh ra do quá trình ép gương và xáo động đất sẽ tiêu tán dần theo thời gian, dẫn đến quá trình nén cố kết của các lớp đất sét xung quanh hầm.

> `==[GIẢ THIẾT TÍNH TOÁN: Trong khuôn khổ nghiên cứu này, các mô hình giải tích Peck (1969) và Loganathan & Poulos (1998) tập trung dự báo thành phần **độ lún tức thời không thoát nước** (undrained short-term settlement), bao gồm tổng hợp ba thành phần đầu tiên: $V_{\text{loss}} \approx V_{\text{face}} + V_{\text{shield}} + V_{\text{tail}}$. Biến dạng cố kết dài hạn $V_{\text{consolidation}}$ được tách riêng để không làm sai lệch việc điều khiển thông số vận hành máy TBM.]==`

### 2.1.2. Định nghĩa tỷ lệ tổn thất thể tích đất $V_L$ (Volume Loss Ratio)
Tỷ lệ tổn thất thể tích $V_L$ (đôi khi ký hiệu là $V_{l,\text{ratio}}$) được định nghĩa là tỷ số giữa thể tích đất bị tổn thất trên một đơn vị chiều dài tuyến hầm ($V_{\text{loss}}$, đơn vị $\text{m}^3/\text{m}$) so với diện tích mặt cắt ngang lý thuyết của đường hầm đào ($A_t$, đơn vị $\text{m}^2$):
$$V_L = \frac{V_{\text{loss}}}{A_t} = \frac{V_{\text{loss}}}{\frac{\pi D^2}{4}}$$

Đối với hầm đơn có đường kính ngoài $D = 6.30\text{ m}$, diện tích tiết diện đào lý thuyết là:
$$A_t = \frac{\pi \cdot (6.30)^2}{4} \approx 31.172\text{ m}^2$$

Do đó, lượng tổn thất thể tích đất đơn vị $V_{\text{loss}}$ ứng với các giá trị $V_L$ được xác định bởi:
$$V_{\text{loss}} = V_L \cdot 31.172\text{ m}^3/\text{m}$$

Theo kinh nghiệm thi công khiên đào EPB quốc tế trong điều kiện địa chất đô thị (Mair et al., 1996; Standing & Selemetas, 2013), các mức tổn thất thể tích được phân loại như sau:
- $V_L \le 0.5\%$: Chất lượng thi công xuất sắc, kiểm soát áp lực gương và phụt vữa đuôi khiên hoàn hảo.
- $V_L = 0.5\% - 1.0\%$: Mức kiểm soát tiêu chuẩn đối với đất bồi tích đô thị.
- $V_L = 1.0\% - 1.5\%$: Đất nền yếu có xáo động, áp lực phụt vữa không đồng đều, bắt đầu có nguy cơ ảnh hưởng công trình.
- $V_L = 1.5\% - 2.0\%$: Sự cố đào hầm, mất cân bằng áp lực gương đào hoặc sạt lở cục bộ khe hở đuôi khiên.

---

## 2.2. MÔ HÌNH PHỄU LÚN GAUSSIAN CỦA PECK (1969)

### 2.2.1. Phương trình toán học dạng chuẩn
Peck (1969) đề xuất đường cong lún bề mặt đất tại mặt cắt ngang vuông góc với tim hầm có dạng hàm mật độ phân bố chuẩn Gauss:
$$S(x) = S_{\max} \exp\left(-\frac{x^2}{2i^2}\right)$$

Trong đó:
- $x$: Khoảng cách ngang tính từ trục tim hầm ($x = 0$ tại tim hầm, mang dấu âm về bên trái và dấu dương về bên phải, đơn vị $\text{m}$).
- $S(x)$: Độ lún bề mặt đất tại vị trí có khoảng cách ngang $x$ (đơn vị $\text{mm}$ hoặc $\text{m}$).
- $S_{\max}$: Độ lún cực đại bề mặt, xuất hiện trực diện phía trên tim hầm ($x = 0$).
- $i$: Khoảng cách từ tim hầm đến điểm uốn của đường cong phân bố lún (đơn vị $\text{m}$).

### 2.2.2. Khoảng cách điểm uốn $i$ và hệ số phễu lún $K$
Tại vị trí điểm uốn ($x = \pm i$), đạo hàm bậc hai của hàm lún triệt tiêu ($d^2S/dx^2 = 0$), độ dốc lún đạt giá trị cực đại và độ cong bề mặt đổi dấu (từ vùng uốn võng sang vùng uốn vồng).

Theo công thức bán thực nghiệm được chấp nhận rộng rãi nhất của O'Reilly & New (1982):
$$i = K \cdot z_0$$

trong đó:
- $z_0$: Chiều sâu từ mặt đất tự nhiên đến tâm trục hầm ($\text{m}$).
- $K$: Hệ số bề rộng phễu lún không thứ nguyên, phụ thuộc vào đặc tính cơ lý của các lớp đất nằm từ nóc hầm lên đến mặt đất.

<br>

**Bảng 2.1: Khoảng giá trị hệ số phễu lún $K$ theo các nghiên cứu kinh điển**

| Loại đất chủ đạo phía trên hầm | Khoảng giá trị $K$ (O'Reilly & New, 1982) | Giá trị khuyến nghị (Mair et al., 1993) | Giá trị áp dụng trong luận án |
|---|---|---|---|
| Cát hạt thô, sỏi cuội rời | 0.20 – 0.35 | 0.25 | — |
| Cát mịn, cát pha sét chặt vừa | 0.35 – 0.50 | 0.45 – 0.50 | **0.50 (Mặt cắt S9–S10)** |
| Sét dẻo cứng đến dẻo mềm chuyển tiếp | 0.45 – 0.60 | 0.50 – 0.55 | **0.55 (Mặt cắt S10–S11)** |
| Bùn sét hữu cơ dẻo mềm bão hòa | 0.55 – 0.70 | 0.60 – 0.65 | **0.60 (Mặt cắt S11–S12, BH12)** |

### 2.2.3. Chứng minh toán học định luật bảo toàn thể tích ($V_s = V_{\text{loss}}$)
Trong điều kiện đất nền sét hoặc bùn sét bão hòa nước biến dạng không thoát nước trong thời gian ngắn thi công TBM, hệ số biến đổi thể tích của đất xem như bằng 0 (coi đất là vật liệu không nén được, hệ số Poisson $\nu_u \approx 0.5$). Do đó, tổng thể tích của phễu lún bề mặt đất trên một mét dài hầm ($V_s$) phải đúng bằng lượng tổn thất thể tích đất ngầm ($V_{\text{loss}}$):
$$V_s = V_{\text{loss}}$$

Thể tích phễu lún $V_s$ bằng tích phân diện tích mặt cong lún từ $-\infty$ đến $+\infty$:
$$V_s = \int_{-\infty}^{\infty} S(x) \, dx = \int_{-\infty}^{\infty} S_{\max} \exp\left(-\frac{x^2}{2i^2}\right) dx$$

Đặt biến đổi phụ: $u = \frac{x}{\sqrt{2} \cdot i} \implies dx = \sqrt{2} \cdot i \, du$. Khi đó:
$$V_s = S_{\max} \cdot \sqrt{2} \cdot i \int_{-\infty}^{\infty} e^{-u^2} \, du$$

Sử dụng tích phân Gauss kinh điển: $\int_{-\infty}^{\infty} e^{-u^2} \, du = \sqrt{\pi}$, ta có:
$$V_s = S_{\max} \cdot \sqrt{2} \cdot i \cdot \sqrt{\pi} = \sqrt{2\pi} \cdot i \cdot S_{\max} \approx 2.5066 \cdot i \cdot S_{\max}$$

Cân bằng với thể tích tổn thất đất:
$$\sqrt{2\pi} \cdot i \cdot S_{\max} = V_L \cdot A_t = V_L \cdot \frac{\pi D^2}{4}$$

Từ đó, ta rút ra phương trình giải tích xác định chính xác độ lún cực đại $S_{\max}$ của hầm đơn:
$$S_{\max} = \frac{V_L \cdot \pi D^2}{4 \sqrt{2\pi} \cdot K \cdot z_0} = \frac{\sqrt{2\pi} \cdot V_L \cdot D^2}{8 \cdot K \cdot z_0}$$

> **Ý nghĩa vật lý:** Độ lún cực đại $S_{\max}$ tỷ lệ thuận bậc nhất với tỷ lệ tổn thất thể tích $V_L$ và bình phương đường kính hầm $D^2$, đồng thời tỷ lệ nghịch bậc nhất với hệ số phễu lún $K$ và chiều sâu chôn hầm $z_0$. Khi hầm chôn càng sâu hoặc qua đất càng dẻo ($K$ lớn), $S_{\max}$ sẽ giảm nhưng bề rộng phễu lún sẽ lan rộng ra hai bên.

---

## 2.3. MÔ HÌNH BÁN GIẢI TÍCH LOGANATHAN & POULOS (1998)

Nhằm khắc phục tính thuần kinh nghiệm của Peck, Loganathan & Poulos (1998) đã xây dựng lời giải giải tích dạng đóng (closed-form analytical solution) dựa trên cơ học đàn hồi giải phóng ứng suất xung quanh lỗ khoét tròn trong nửa không gian vô hạn (semi-infinite elastic ground).

### 2.3.1. Phương trình chuyển vị lún tổng quát
Tại một điểm bất kỳ trong khối đất có tọa độ $(x, z)$, chuyển vị thẳng đứng $S_z(x, z)$ do quá trình đào hầm gây ra được xác định bởi:
$$S_z(x, z) = \epsilon_0 R^2 \cdot \left[ \frac{z - z_0}{x^2 + (z - z_0)^2} + \frac{(3 - 4\nu)(z + z_0)}{x^2 + (z + z_0)^2} - \frac{2z [x^2 - (z + z_0)^2]}{(x^2 + (z + z_0)^2)^2} \right] \cdot \exp\left\{ -\left[ \frac{1.38 x^2}{(z_0 + R)^2} + \frac{0.69 z^2}{z_0^2} \right] \right\}$$

Trong đó:
- $R = D/2$: Bán kính ngoài của hầm đào ($R = 3.15\text{ m}$).
- $z_0$: Chiều sâu tim hầm tính từ mặt đất ($\text{m}$).
- $z$: Chiều sâu của điểm cần tính lún ($z = 0$ tại mặt đất tự nhiên; $z > 0$ khi xét đáy móng công trình).
- $\nu$: Hệ số Poisson của môi trường đất nền ($\nu \approx 0.30 - 0.35$).
- $\epsilon_0$: Biến dạng thể tích lỗ rỗng tương đương tại biên hầm (equivalent ground loss ratio at tunnel boundary). Trong điều kiện biến dạng phẳng, $\epsilon_0$ có thể xấp xỉ bằng tỷ số tổn thất thể tích $V_L$.

### 2.3.2. Phương trình lún bề mặt đất ($z = 0$)
Khi xét chuyển vị lún tại bề mặt đất tự nhiên ($z = 0$), phương trình trên được rút gọn thành:
$$S_{\text{LP}}(x) = \epsilon_0 R^2 \cdot \frac{4(1 - \nu) z_0}{x^2 + z_0^2} \cdot \exp\left( -\frac{1.38 x^2}{(z_0 + R)^2} \right)$$

Tại tim hầm ($x = 0$), độ lún bề mặt cực đại theo Loganathan & Poulos là:
$$S_{\text{LP}}(0) = \epsilon_0 R^2 \cdot \frac{4(1 - \nu)}{z_0}$$

### 2.3.3. So sánh đối sánh giữa mô hình Peck và Loganathan & Poulos
Trên Hình 2.1, biên dạng phễu lún ngang của mô hình Peck (1969) và Loganathan & Poulos (1998) được thể hiện đồng thời cho hai mặt cắt đại diện S9–S10 ($z_0=15\text{ m}, K=0.50$) và S11–S12 ($z_0=18\text{ m}, K=0.60$) tại tỷ lệ tổn thất thể tích tiêu chuẩn $V_L = 1.0\%$.

<br>

<div align="center">

![Hình 2.1: So sánh hình học phễu lún giữa mô hình Peck (1969) và Loganathan & Poulos (1998)](../03_hinh_anh_minh_hoa_chat_luong_cao/FIG_02_Peck_vs_LoganathanPoulos_Transverse.png)

*Hình 2.1: So sánh hình học phễu lún giữa mô hình Peck (1969) và Loganathan & Poulos (1998) tại kịch bản VL = 1.0%*

</div>

<br>

**Nhận xét cơ học:**
1. **Tại tâm phễu lún ($x = 0$):** Cả hai mô hình cho kết quả rất tương đồng. Tại đoạn S9–S10, Peck cho $S_{\max} = 16.58\text{ mm}$ trong khi LP cho $17.20\text{ mm}$ (chênh lệch chỉ $+3.7\%$). Tại đoạn S11–S12, Peck cho $S_{\max} = 11.51\text{ mm}$, LP cho $13.67\text{ mm}$ (chênh lệch $+18.7\%$).
2. **Hình thái sườn phễu lún:** Mô hình Peck duy trì dạng phân bố chuẩn với điểm uốn thực nghiệm $i = K z_0$, phản ánh chính xác kinh nghiệm đo đạc hiện trường. Mô hình LP do có số hạng suy giảm mũ bậc hai theo $(z_0+R)^2$ nên có xu hướng dốc hơn tại tâm và suy giảm nhanh hơn khi ra xa tim hầm.

---

## 2.4. NGUYÊN LÝ SIÊU VỊ HẦM ĐÔI (TWIN TUNNEL SUPERPOSITION)

Tuyến Metro số 3 Hà Nội gồm hai ống hầm đơn chạy song song cách nhau một khoảng cách tim hầm $d \approx 13.0\text{ m}$. Đặt gốc tọa độ $x = 0$ tại trục đối xứng chính giữa hai hầm:
- Hầm nhánh Trái (Left Tunnel): Tâm hầm nằm tại tọa độ $x_L = -d/2 = -6.5\text{ m}$.
- Hầm nhánh Phải (Right Tunnel): Tâm hầm nằm tại tọa độ $x_R = +d/2 = +6.5\text{ m}$.

Áp dụng nguyên lý cộng tác dụng tuyến tính (Linear Superposition Principle), độ lún tổng cộng của hầm đôi tại khoảng cách ngang $x$ được xác định bởi:
$$S_{\text{twin}}(x) = S_{\text{left}}(x) + S_{\text{right}}(x) = S_{\max,\text{single}} \left[ \exp\left(-\frac{(x + d/2)^2}{2i^2}\right) + \exp\left(-\frac{(x - d/2)^2}{2i^2}\right) \right]$$

<br>

<div align="center">

![Hình 2.2: Phân bố lún bề mặt hầm đôi TBM và sự phát triển phễu lún theo các kịch bản tổn thất thể tích](../03_hinh_anh_minh_hoa_chat_luong_cao/FIG_03_Twin_Tunnel_Interaction_Profiles.png)

*Hình 2.2: Phân bố lún bề mặt hầm đôi TBM và sự phát triển phễu lún theo các kịch bản tổn thất thể tích*

</div>

<br>

### 2.4.1. Độ dốc mặt đất và độ cong phễu lún
Độ dốc mặt đất (Ground Slope / Tilt, ký hiệu $\theta(x)$) là đạo hàm bậc nhất của hàm lún theo khoảng cách ngang:
$$\theta(x) = \left| \frac{dS(x)}{dx} \right|$$

Đối với hầm đơn:
$$\frac{dS(x)}{dx} = -S_{\max} \frac{x}{i^2} \exp\left(-\frac{x^2}{2i^2}\right) \implies \theta(x) = \frac{|x|}{i^2} S(x)$$

Độ dốc cực đại $\theta_{\max}$ xuất hiện chính xác tại điểm uốn $x = \pm i$:
$$\theta_{\max} = \frac{i}{i^2} S(i) = \frac{1}{i} S_{\max} \exp(-1/2) = \frac{S_{\max}}{i \sqrt{e}} \approx 0.6065 \frac{S_{\max}}{i}$$

Đối với hầm đôi, đạo hàm độ dốc được tính bằng tổng hình học của hai nhánh:
$$\theta_{\text{twin}}(x) = \left| -S_{\max,\text{single}} \left[ \frac{x + d/2}{i^2} \exp\left(-\frac{(x + d/2)^2}{2i^2}\right) + \frac{x - d/2}{i^2} \exp\left(-\frac{(x - d/2)^2}{2i^2}\right) \right] \right|$$

---

## 2.5. TIÊU CHUẨN ĐÁNH GIÁ NGUY CƠ HƯ HỎNG CÔNG TRÌNH THEO BURLAND (1995)

Độ lún đồng đều nhìn chung không gây hư hại kết cấu công trình; nguyên nhân chính gây nứt toác tường, kẹt cửa và gãy dầm là do **lún lệch (differential settlement)**, **độ dốc góc xoay ($\theta$)** và **biến dạng kéo ngang ($\epsilon_h$)**.

Theo tiêu chuẩn phân loại hư hỏng của Burland (1995) và Mair, Taylor & Burland (1996), mức độ rủi ro được chia thành 6 cấp độ:

<br>

**Bảng 2.2: Phân loại cấp độ hư hại công trình theo Burland (1995) và Mair et al. (1996)**

| Cấp hư hỏng | Tên phân loại | Độ lún tuyệt đối $S_v$ (mm) | Độ dốc góc xoay $\theta$ (rad) | Biến dạng kéo ngang $\epsilon_h$ (%) | Bề rộng vết nứt tường ($w$) | Mô tả hư hại điển hình & Biện pháp can thiệp |
|---|---|---|---|---|---|---|
| **Cấp 0** | Không đáng kể (Negligible) | $< 10$ | $< 1/500$ ($< 2.0 \times 10^{-3}$) | $< 0.05\%$ | $< 0.1\text{ mm}$ | Vết nứt chân chim rất nhỏ trên bề mặt lớp trát, không ảnh hưởng thẩm mỹ. Quan trắc định kỳ. |
| **Cấp 1** | Rất nhẹ (Very Slight) | $10 – 20$ | $1/500 – 1/333$ | $0.05\% – 0.075\%$ | $0.1 – 1.0\text{ mm}$ | Vết nứt nhỏ dễ thấy trên lớp vữa trát trong nhà. Sơn trát lại thẩm mỹ sau khi lún ổn định. |
| **Cấp 2** | Nhẹ (Slight) | $20 – 35$ | $1/333 – 1/200$ | $0.075\% – 0.15\%$ | $1.0 – 5.0\text{ mm}$ | Vết nứt mở rộng qua tường gạch, cửa đi/cửa sổ có thể bị kẹt nhẹ. Trát vá nứt, kiểm tra đường ống thoát nước. |
| **Cấp 3** | Vừa phải (Moderate) | $35 – 50$ | $1/200 – 1/100$ | $0.15\% – 0.30\%$ | $5.0 – 15.0\text{ mm}$ | Nứt sâu xuyên tường, nứt dầm nhỏ, nguy cơ rò rỉ đường ống ngầm. Cần gia cố móng, phụt vữa bù lún. |
| **Cấp 4** | Nặng (Severe) | $50 – 75$ | $1/100 – 1/50$ | $> 0.30\%$ | $15.0 – 25.0\text{ mm}$ | Nứt toác khung kết cấu, vỡ tường, sàn bị dốc rõ rệt, rò rỉ đường ống cấp nước/ga. Chống đỡ khẩn cấp. |
| **Cấp 5** | Rất nặng (Very Severe) | $> 75$ | $> 1/50$ ($> 20 \times 10^{-3}$) | $> 0.50\%$ | $> 25.0\text{ mm}$ | Nguy cơ mất ổn định tổng thể, sụp đổ một phần hoặc toàn bộ công trình. Sơ tán khẩn cấp, tháo dỡ. |

---

## 2.6. ĐÁNH GIÁ, PHẢN BIỆN VÀ GHI CHÚ AUDIT CỦA CHƯƠNG 2

> **Ghi chú Kiểm toán Khoa học (Audit Note 2.1):**
> - **Kiểm chứng bảo toàn thể tích:** Công thức giải tích của Peck đã được kiểm tra tính đúng đắn thông qua thuật toán tích phân số trị hình thang (Trapezoidal Rule) trên dải cự ly $x \in [-100\text{ m}; +100\text{ m}]$ với bước lưới $\Delta x = 0.01\text{ m}$ trong mã nguồn `scripts/analytical_engine.py`. Kết quả sai số tích phân số trị so với công thức giải tích là $0.000\%$, đạt chỉ tiêu nghiệm thu Gate 4.
> - **Hiệu ứng che chắn hầm đôi (Shielding / Interaction Effect):** Mô hình siêu vị tuyến tính giả định đất nền có ứng xử đàn hồi tuyến tính. Trong thực tế, việc thi công hầm thứ nhất sẽ làm thay đổi trạng thái ứng suất ban đầu của đất, khiến thể tích tổn thất của hầm thứ hai có thể tăng từ 10% đến 25% nếu đào quá gần (Addenbrooke & Potts, 2001).
> - `==[GIẢ THIẾT TÍNH TOÁN: Khi khoảng cách tim hầm d = 13.0m (tương đương d/D = 13.0 / 6.3 ≈ 2.06), tương tác làm tăng tổn thất của ống hầm đào sau nằm trong khoảng 10-15%. Trong các phân tích độ nhạy tiếp theo, kịch bản VL = 1.5% và 2.0% đã bao trùm đầy đủ sự gia tăng biến dạng do hiệu ứng tương tác này.]==`
