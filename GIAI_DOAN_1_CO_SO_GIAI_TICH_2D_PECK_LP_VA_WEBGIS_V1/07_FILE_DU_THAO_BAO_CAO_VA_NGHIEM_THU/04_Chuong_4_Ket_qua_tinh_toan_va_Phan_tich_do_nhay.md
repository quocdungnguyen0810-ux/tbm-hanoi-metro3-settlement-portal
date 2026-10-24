# CHƯƠNG 4: KẾT QUẢ TÍNH TOÁN VÀ PHÂN TÍCH ĐỘ NHẠY BIẾN DẠNG MẶT ĐẤT

---

## 4.1. KẾT QUẢ TÍNH TOÁN TẠI KỊCH BẢN THI CÔNG TIÊU CHUẨN ($V_L = 1.0\%$)

Trong điều kiện thi công khiên đào EPB-TBM được kiểm soát chặt chẽ theo đúng quy trình công nghệ (duy trì áp lực cân bằng đất trong khoang đào ổn định và bơm vữa chèn đuôi khiên kịp thời), tỷ lệ tổn thất thể tích đất thiết kế thường được khống chế ở mức $V_L = 1.0\%$ (tương đương lượng tổn thất thể tích đất $V_{\text{loss}} = 0.312\text{ m}^3/\text{m}$ chiều dài hầm).

Áp dụng các phương trình giải tích đã chứng minh ở Chương 2 với đường kính ngoài khiên đào $D = 6.30\text{ m}$ và cự ly tim hầm đôi $d = 13.0\text{ m}$, kết quả tính toán độ lún bề mặt tại 3 mặt cắt đại diện được tổng hợp trong Bảng 4.1:

<br>

**Bảng 4.1: Kết quả tính toán biến dạng phễu lún tại kịch bản tiêu chuẩn ($V_L = 1.0\%$)**

| Mặt cắt đại diện | $z_0$ (m) | $K$ | $i$ (m) | $S_{\max}$ Hầm đơn Peck (mm) | $S_{\max}$ Hầm đôi Peck (mm) | $S_{\max}$ Hầm đơn LP (mm) | Độ dốc cực đại $\theta_{\max}$ ($10^{-3}$ rad) | Bề rộng vùng lún $>5\text{ mm}$ (m) | Cấp độ rủi ro (Burland 1995) |
|---|---|---|---|---|---|---|---|---|---|
| **S9–S10 (Kim Mã - Cát Linh)** | 15.0 | 0.50 | 7.50 | 16.58 | **22.78** | 17.20 | 1.341 | 23.23 | **Cấp 2 (Nhẹ / Slight)** |
| **S10–S11 (Cát Linh - Văn Miếu)** | 16.5 | 0.55 | 9.08 | 13.70 | **21.21** | 15.39 | 0.916 | 25.77 | **Cấp 2 (Nhẹ / Slight)** |
| **S11–S12 (Văn Miếu - Ga Hà Nội)** | 18.0 | 0.60 | 10.80 | 11.51 | **19.21** | 13.67 | 0.647 | 27.90 | **Cấp 1 (Rất nhẹ / Very Slight)** |

### Phân tích so sánh giữa các mặt cắt:
1. **Biên độ lún cực đại ($S_{\max}$):**
   - Độ lún cực đại của hầm đôi xuất hiện tại trục đối xứng ($x = 0$) chính giữa hai hầm.
   - Đoạn S9–S10 có chiều sâu chôn hầm nông hơn ($z_0 = 15.0\text{ m}$) và hệ số phễu lún hẹp hơn ($K = 0.50 \implies i = 7.5\text{ m}$) nên có độ lún cực đại lớn nhất: $S_{\max} = 22.78\text{ mm}$.
   - Đoạn S11–S12 chôn sâu hơn ($z_0 = 18.0\text{ m}$) nhưng do nằm trong tầng bùn sét mềm hữu cơ ($K = 0.60 \implies i = 10.8\text{ m}$), năng lượng giải phóng ứng suất được phân tán rộng hơn sang hai bên, làm độ lún đỉnh giảm xuống còn $19.21\text{ mm}$.
2. **Độ dốc mặt đất ($\theta_{\max}$):**
   - Mặc dù độ lún đỉnh của đoạn S11–S12 không quá lớn, nhưng đoạn S9–S10 lại có độ dốc cực đại lớn nhất ($\theta_{\max} = 1.341 \times 10^{-3}\text{ rad} \approx 1/745$). Đây là yếu tố nguy hiểm đối với các dãy nhà ống móng nông dọc đường Kim Mã, đòi hỏi phải theo dõi sát biến dạng nghiêng lệch móng.
3. **Phạm vi vùng ảnh hưởng:**
   - Vùng ảnh hưởng lún có ý nghĩa ($S(x) > 5\text{ mm}$) mở rộng dần từ $23.2\text{ m}$ tại S9–S10 lên tới $27.9\text{ m}$ tại S11–S12 (mỗi bên cách tim tuyến gần $14\text{ m}$).

---

## 4.2. MA TRẬN PHÂN TÍCH ĐỘ NHẠY 21 KỊCH BẢN TỔN THẤT THỂ TÍCH ĐẤT

Do tính bất định cao của địa tầng bồi tích Hà Nội và nguy cơ mất áp gương đào khi gặp dị vật chướng ngại vật ngầm hoặc túi bùn loãng, một ma trận phân tích độ nhạy toàn diện gồm **21 kịch bản** đã được thiết lập. Ma trận khảo sát 7 mức tổn thất thể tích đất:
$$V_L \in \{0.50\%; \, 0.75\%; \, 1.00\%; \, 1.25\%; \, 1.50\%; \, 1.75\%; \, 2.00\%\}$$
kết hợp trên 3 mặt cắt kỹ thuật đại diện.

Toàn bộ kết quả tính toán chi tiết được trình bày trong Bảng 4.2:

<br>

**Bảng 4.2: Bảng tổng hợp 21 kịch bản độ nhạy lún hầm đôi TBM (Đoạn S9–S12)**

| Mã KB | Đoạn tuyến | $z_0$ (m) | $K$ | $i$ (m) | $V_L$ (%) | $V_{\text{loss}}$ ($\text{m}^3/\text{m}$) | $S_{\max}$ Đơn (mm) | $S_{\max}$ Đôi (mm) | $S_{\max}$ LP (mm) | Độ dốc $\theta_{\max}$ ($10^{-3}$) | Bề rộng lún $>5\text{ mm}$ (m) | Cấp độ rủi ro (Burland 1995) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SC-01** | S9–S10 | 15.0 | 0.50 | 7.50 | 0.50% | 0.156 | 8.29 | **11.39** | 8.60 | 0.670 | 15.09 | Cấp 1 (Rất nhẹ) |
| **SC-02** | S9–S10 | 15.0 | 0.50 | 7.50 | 0.75% | 0.234 | 12.44 | **17.08** | 12.90 | 1.006 | 20.25 | Cấp 1 (Rất nhẹ) |
| **SC-03** | S9–S10 | 15.0 | 0.50 | 7.50 | 1.00% | 0.312 | 16.58 | **22.78** | 17.20 | 1.341 | 23.23 | Cấp 2 (Nhẹ) |
| **SC-04** | S9–S10 | 15.0 | 0.50 | 7.50 | 1.25% | 0.390 | 20.73 | **28.47** | 21.50 | 1.676 | 25.30 | Cấp 2 (Nhẹ) |
| **SC-05** | S9–S10 | 15.0 | 0.50 | 7.50 | 1.50% | 0.468 | 24.87 | **34.17** | 25.80 | 2.011 | 26.87 | **Cấp 3 (Vừa phải / Nguy hại)** |
| **SC-06** | S9–S10 | 15.0 | 0.50 | 7.50 | 1.75% | 0.545 | 29.02 | **39.86** | 30.10 | 2.347 | 28.13 | **Cấp 3 (Vừa phải / Nguy hại)** |
| **SC-07** | S9–S10 | 15.0 | 0.50 | 7.50 | 2.00% | 0.623 | 33.16 | **45.56** | 34.40 | 2.682 | 29.18 | **Cấp 4 (Nặng / Severe)** |
| **SC-08** | S10–S11 | 16.5 | 0.55 | 9.08 | 0.50% | 0.156 | 6.85 | **10.60** | 7.70 | 0.458 | 14.41 | Cấp 1 (Rất nhẹ) |
| **SC-09** | S10–S11 | 16.5 | 0.55 | 9.08 | 0.75% | 0.234 | 10.28 | **15.90** | 11.55 | 0.687 | 21.79 | Cấp 1 (Rất nhẹ) |
| **SC-10** | S10–S11 | 16.5 | 0.55 | 9.08 | 1.00% | 0.312 | 13.70 | **21.21** | 15.39 | 0.916 | 25.77 | Cấp 2 (Nhẹ) |
| **SC-11** | S10–S11 | 16.5 | 0.55 | 9.08 | 1.25% | 0.390 | 17.13 | **26.51** | 19.24 | 1.145 | 28.48 | Cấp 2 (Nhẹ) |
| **SC-12** | S10–S11 | 16.5 | 0.55 | 9.08 | 1.50% | 0.468 | 20.56 | **31.81** | 23.09 | 1.374 | 30.52 | **Cấp 3 (Vừa phải / Nguy hại)** |
| **SC-13** | S10–S11 | 16.5 | 0.55 | 9.08 | 1.75% | 0.545 | 23.98 | **37.11** | 26.94 | 1.603 | 32.14 | **Cấp 3 (Vừa phải / Nguy hại)** |
| **SC-14** | S10–S11 | 16.5 | 0.55 | 9.08 | 2.00% | 0.623 | 27.41 | **42.41** | 30.79 | 1.832 | 33.48 | **Cấp 3 (Vừa phải / Nguy hại)** |
| **SC-15** | S11–S12 | 18.0 | 0.60 | 10.80 | 0.50% | 0.156 | 5.76 | **9.61** | 6.84 | 0.323 | 11.47 | Cấp 0 (Không đáng kể) |
| **SC-16** | S11–S12 | 18.0 | 0.60 | 10.80 | 0.75% | 0.234 | 8.64 | **14.41** | 10.25 | 0.485 | 22.58 | Cấp 1 (Rất nhẹ) |
| **SC-17** | S11–S12 | 18.0 | 0.60 | 10.80 | 1.00% | 0.312 | 11.51 | **19.21** | 13.67 | 0.647 | 27.90 | Cấp 1 (Rất nhẹ) |
| **SC-18** | S11–S12 | 18.0 | 0.60 | 10.80 | 1.25% | 0.390 | 14.39 | **24.02** | 17.09 | 0.808 | 31.41 | Cấp 2 (Nhẹ) |
| **SC-19** | S11–S12 | 18.0 | 0.60 | 10.80 | 1.50% | 0.468 | 17.27 | **28.82** | 20.51 | 0.970 | 34.01 | Cấp 2 (Nhẹ) |
| **SC-20** | S11–S12 | 18.0 | 0.60 | 10.80 | 1.75% | 0.545 | 20.15 | **33.63** | 23.92 | 1.132 | 36.06 | **Cấp 3 (Vừa phải / Nguy hại)** |
| **SC-21** | S11–S12 | 18.0 | 0.60 | 10.80 | 2.00% | 0.623 | 23.03 | **38.43** | 27.34 | 1.293 | 37.75 | **Cấp 3 (Vừa phải / Nguy hại)** |

---

## 4.3. ĐỒ THỊ ĐƯỜNG CONG ĐỘ NHẠY VÀ XÁC ĐỊNH NGƯỠNG NGUY HẠI

Các quy luật nhạy cảm của biến dạng lún mặt đất theo sự biến thiên của tỷ lệ tổn thất thể tích đất $V_L$ được trực quan hóa trên Hình 4.1:

<br>

<div align="center">

![Hình 4.1: Đồ thị phân tích độ nhạy biến dạng mặt đất theo dải tổn thất thể tích VL (0.5% – 2.0%)](../03_hinh_anh_minh_hoa_chat_luong_cao/FIG_04_Sensitivity_Curves_Smax_Slope.png)

*Hình 4.1: Đồ thị phân tích độ nhạy biến dạng mặt đất theo dải tổn thất thể tích VL (0.5% – 2.0%)*

</div>

<br>

### Các kết luận rút ra từ phân tích độ nhạy:
1. **Quan hệ tuyến tính đồng dạng:**
   Độ lún cực đại của cả hầm đơn và hầm đôi biến thiên hoàn toàn tuyến tính với tỷ lệ tổn thất thể tích $V_L$. Độ dốc đường thẳng phụ thuộc vào chiều sâu $z_0$ và hệ số $K$.
   Hệ số góc của đường nhạy cảm $S_{\max} - V_L$ tại các đoạn tuyến:
   - Đoạn S9–S10: $\Delta S_{\max} / \Delta V_L \approx 22.78\text{ mm} / 1.0\% = 2.278\text{ mm} / 0.1\%$ tổn thất thể tích.
   - Đoạn S10–S11: $\Delta S_{\max} / \Delta V_L \approx 21.21\text{ mm} / 1.0\% = 2.121\text{ mm} / 0.1\%$ tổn thất thể tích.
   - Đoạn S11–S12: $\Delta S_{\max} / \Delta V_L \approx 19.21\text{ mm} / 1.0\% = 1.921\text{ mm} / 0.1\%$ tổn thất thể tích.

2. **Ngưỡng rủi ro nguy hại bước ngoặt ($V_L = 1.5\%$):**
   - Khi $V_L \le 1.0\%$, độ lún của tất cả các mặt cắt đều khống chế dưới $23\text{ mm}$, độ dốc góc xoay $\theta_{\max} < 1.35 \times 10^{-3} < 1/500$. Toàn bộ công trình nằm trong vùng an toàn hoặc chỉ chịu tác động nhẹ (Cấp 0 – Cấp 2).
   - Tuy nhiên, ngay khi $V_L$ chạm ngưỡng $1.5\%$, độ lún cực đại tại S9–S10 vọt lên $34.17\text{ mm}$ và độ dốc đạt $2.011 \times 10^{-3} > 1/500$ (vượt ngưỡng gây nứt tường vữa trát của Burland).
   - Khi xảy ra sự cố nghiêm trọng ($V_L = 2.0\%$), độ lún cực đại hầm đôi vượt từ $38.4\text{ mm}$ đến $45.6\text{ mm}$, đẩy kết cấu công trình vào cấp nguy cơ Cấp 3 và Cấp 4 (nứt toác dầm sàn, hư hại đường ống).

3. **Mở rộng bán kính phễu lún tại vùng bùn sét S11–S12:**
   Tại đoạn S11–S12, mặc dù $S_{\max}$ nhỏ hơn đoạn S9–S10 nhưng bề rộng vùng lún $>5\text{ mm}$ mở rộng rất xa, đạt tới $37.75\text{ m}$ (khi $V_L = 2.0\%$). Điều này đồng nghĩa với việc các công trình nằm cách tim đường Quốc Tử Giám tới gần $20\text{ m}$ vẫn nằm trong diện bị ảnh hưởng biến dạng.

---

## 4.4. ĐÁNH GIÁ, PHẢN BIỆN VÀ GHI CHÚ AUDIT CỦA CHƯƠNG 4

> **Ghi chú Kiểm toán Khoa học (Audit Note 4.1):**
> - **Đối chiếu bảng tính Excel:** Toàn bộ công thức tính toán 21 kịch bản trên được liên kết động trong sheet `Bang_21_Kich_Ban_Tong_Hop` của file [TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx](../02_du_lieu_excel_chuyen_nghiep/TBM_SETTLEMENT_ANALYTICAL_ENGINE.xlsx). Khi người dùng thay đổi giá trị $V_L$ hoặc $K$, toàn bộ các giá trị $S_{\max}$, độ dốc và bề rộng vùng lún sẽ tự động cập nhật theo thời gian thực.
> - `==[GIẢ THIẾT TÍNH TOÁN: Trong phân tích siêu vị hầm đôi, cự ly tim hầm d được giả định cố định là 13.0m cho toàn tuyến. Trong thực tế thi công, cự ly d có thể thu hẹp xuống 12.0m khi tiếp cận họng đón ga và mở rộng ra 15.0m ở đoạn tuyến thẳng. Khi d thu hẹp, độ lún cực đại tại tâm trục đối xứng x=0 sẽ tăng thêm khoảng 5-8%. Cần nạp tọa độ tim hầm thực tế vào mô hình khi tiến hành quan trắc mốc lún.]==`
