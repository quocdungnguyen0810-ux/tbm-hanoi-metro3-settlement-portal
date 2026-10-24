# BẢN GHI NHỚ THẨM TRA CƠ HỌC & CÔNG THỨC GIẢI TÍCH (WF-10)
**Tác tử chủ trì:** `mechanics_reviewer`  
**Cổng kiểm toán:** Gate 3 (Baseline Freeze)  
**Ngày thực hiện:** 2026-10-14  

---

## 1. Thẩm tra Mô hình Cơ sở Peck (1969)
1. **Dạng phương trình:**
   $$S(x) = S_{\max} \exp\left(-\frac{x^2}{2i^2}\right)$$
   với $i = K \cdot z_0$ là khoảng cách từ tim hầm đến điểm uốn phễu lún.
2. **Bảo toàn thể tích (Mass/Volume Balance):**
   $$V_s = \int_{-\infty}^{\infty} S(x) dx = \sqrt{2\pi} \cdot i \cdot S_{\max}$$
   Thể tích tổn thất đất lý thuyết:
   $$V_{\text{loss}} = V_L \cdot A_t = V_L \cdot \frac{\pi D^2}{4}$$
   Do đó:
   $$S_{\max} = \frac{V_L \cdot \pi D^2}{4 \sqrt{2\pi} \cdot i} = \frac{V_L \cdot D^2 \sqrt{2\pi}}{8 \cdot i}$$
3. **Độ dốc (Tilt) & Độ cong (Curvature):**
   - Độ dốc bề mặt:
     $$\frac{dS}{dx} = - S_{\max} \frac{x}{i^2} \exp\left(-\frac{x^2}{2i^2}\right)$$
     Giá trị độ dốc cực đại đạt tại điểm uốn $x = \pm i$:
     $$\left|\frac{dS}{dx}\right|_{\max} = \frac{S_{\max}}{i \sqrt{e}} \approx 0.6065 \frac{S_{\max}}{i}$$
   - Độ cong (Curvature):
     $$\frac{d^2 S}{dx^2} = S_{\max} \frac{x^2 - i^2}{i^4} \exp\left(-\frac{x^2}{2i^2}\right)$$

---

## 2. Thẩm tra Mô hình So sánh Loganathan & Poulos (1998)
1. **Dạng phương trình lún mặt đất ($z = 0$):**
   $$S(x) = \epsilon_0 R^2 \cdot \frac{4(1-\nu) z_0}{x^2 + z_0^2} \cdot \exp\left(-\frac{1.38 x^2}{(z_0 + R)^2}\right)$$
   với $R = D/2$, $\epsilon_0 \approx V_L$ (tổn thất đất tương đương), $\nu$ là hệ số Poisson.
2. **Đánh giá & Ràng buộc học thuật:**
   - Mô hình LP không cần giả định trước hệ số $K$, hình dạng phễu tự nhiên thu hẹp khi hầm sâu hơn.
   - Theo quyết định thẩm vấn với người dùng, mô hình được lập trình với cờ cảnh báo `qa_flag: secondary_source_unverified_original`.

## 3. Kết luận
Cả hai phương trình giải tích đã được chuẩn hóa thứ nguyên, quy ước dấu lún dương xuống, sẵn sàng cho việc lập trình tại Gate 4.
