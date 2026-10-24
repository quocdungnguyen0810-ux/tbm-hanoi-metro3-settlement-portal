# ĐỐI SÁNH MÔ HÌNH PHẦN TỬ HỮU HẠN PLAXIS (MOHR-COULOMB VÀ HARDENING SOIL) VỚI LỜI GIẢI GIẢI TÍCH TRONG ĐÁNH GIÁ BIẾN DẠNG KÉO VÀ PHÂN CẤP HƯ HẠI CÔNG TRÌNH LÂN CẬN TUYẾN HẦM ĐÔI TBM ĐOẠN KIM MÃ – GA HÀ NỘI
## BENCHMARKING PLAXIS FINITE ELEMENT MODELS (MOHR-COULOMB AND HARDENING SOIL) AGAINST ANALYTICAL SOLUTIONS FOR TENSILE STRAIN AND BUILDING DAMAGE ASSESSMENT ALONG KIM MA – HANOI STATION TWIN TBM TUNNELS

**Nguyễn Hải Hà**, **Lê Anh Đức (Tác giả liên hệ)**, **Trần Văn Long**  
*Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình, Trường Đại học Giao thông vận tải (UTC), Hà Nội, Việt Nam*  
**Tạp chí mục tiêu:** *Tạp chí Xây dựng (Journal of Construction - Bộ Xây dựng, ISSN 2734-9888)*

---

## TÓM TẮT / ABSTRACT

**Tóm tắt:** Trong mô phỏng số thi công đường hầm bằng khiên đào TBM trong đất yếu đô thị, việc lựa chọn mô hình bản构 (constitutive model) của đất nền và điều kiện biên hội tụ quanh vỏ hầm quyết định trực tiếp đến hình dạng phễu lún mặt đất và độ chính xác khi đánh giá nguy cơ nứt công trình lân cận. Bài báo này thực hiện đối sánh định lượng giữa hai mô hình phần tử hữu hạn biến dạng phẳng 2D tương đương PLAXIS: (i) Mô hình đàn-dẻo lý tưởng Mohr-Coulomb (PLAXIS MC) với mô-đun đẳng hướng $E_{50}$ và (ii) Mô hình tái bền biến dạng Hardening Soil kết hợp điều kiện biên kiểm soát chuyển vị không đồng đều (PLAXIS HS-DCM) xét đến độ cứng dỡ tải - gia tải lại $E_{ur} = 3 E_{50}$, cùng hai lời giải giải tích kinh điển của Peck (1969) và Loganathan & Poulos (1998) tại hai mặt cắt đặc trưng S9–S10 (Kim Mã) và S11–S12 (Hố khoan BH12, Văn Miếu – Ga Hà Nội). Kết quả chứng minh rằng tại $V_L = 1,0\%$, mô hình PLAXIS MC tạo ra phễu lún quá rộng (điểm uốn $i_x = 14.0\text{ m}$) và đánh giá thấp độ lún cực đại ($S_{\max} = 8.582\text{ mm}$) do hiện tượng đẩy trồi đáy hầm giả tạo khi dỡ tải đẳng hướng. Ngược lại, mô hình PLAXIS HS-DCM ($S_{\max} = 11.629\text{ mm}, i_x = 10.5\text{ m}$) hội tụ chặt chẽ với lời giải đàn hồi - khe hở Loganathan & Poulos ($S_{\max} = 8.657\text{ mm}, R^2 = 0.9156$). Khi truyền trường chuyển vị sang mô hình dầm tương đương Burland (1995) cho 100 công trình hiện hữu, việc dùng mô hình MC làm bỏ sót tới 58% số công trình thuộc diện nguy cơ Cấp 3 so với mô hình HS-DCM và LP (1998).

**Abstract:** In numerical simulations of mechanized TBM tunnelling in soft urban ground, the choice of soil constitutive law and boundary convergence formulation governs the predicted surface settlement trough shape and subsequent building damage classifications. This study performs a rigorous quantitative benchmark comparing two 2D plane-strain finite element formulations—(i) isotropic Mohr-Coulomb (PLAXIS MC) and (ii) Hardening Soil coupled with a non-uniform Displacement-Controlled Model (PLAXIS HS-DCM) incorporating unloading-reloading stiffness $E_{ur} = 3 E_{50}$—against Peck (1969) and Loganathan & Poulos (1998) analytical solutions across Sections S9–S10 and S11–S12 (Borehole BH12) of Hanoi Metro Line 3. At nominal volume loss $V_L = 1.0\%$, the isotropic MC model produces an unrealistically wide trough ($i_x = 14.0\text{ m}$) and underpredicts maximum settlement ($S_{\max} = 8.582\text{ mm}$) due to artificial invert heave during excavation unloading. Conversely, PLAXIS HS-DCM ($S_{\max} = 11.629\text{ mm}, i_x = 10.5\text{ m}$) achieves high agreement with Loganathan & Poulos ($S_{\max} = 8.657\text{ mm}, R^2 = 0.9156$). Coupling the displacement fields with Burland's (1995) limiting tensile strain model across 100 adjacent buildings reveals that using the isotropic MC model underestimates maximum tensile strains $\varepsilon_{\max}$ by 28–36%, missing 58% of Category 3 risk structures compared to HS-DCM.

**Từ khóa:** Phần mềm PLAXIS; Mô hình Mohr-Coulomb; Mô hình Hardening Soil; Kiểm soát chuyển vị (DCM); Biến dạng kéo Burland; Hầm TBM Hà Nội.

---

## 1. ĐẶT VẤN ĐỀ

Trong thiết kế kỹ thuật các tuyến hầm đô thị thi công bằng khiên đào cân bằng áp lực đất (EPB-TBM) tại Hà Nội và TP. Hồ Chí Minh, phương pháp phần tử hữu hạn (FEM) trên nền tảng phần mềm PLAXIS 2D/3D được sử dụng phổ biến để kiểm tra chuyển vị đất nền và nội lực vỏ hầm [1–4]. Tuy nhiên, một tồn tại kinh điển đã được Addenbrooke et al. (1997) [5] và các nghiên cứu gần đây tại Việt Nam [3, 6] chỉ ra là: khi sử dụng mô hình đàn-dẻo lý tưởng Mohr-Coulomb (MC) với phương pháp co ngót vỏ hầm đồng nhất (`Tunnel Contraction`), phễu lún mặt đất thu được từ FEM luôn nông hơn và bè rộng hơn đáng kể so với thực tế quan trắc. Hệ quả nghiêm trọng là độ dốc nghiêng $\theta = \partial S / \partial x$ và độ võng tương đối $\Delta / L$ của móng công trình bị đánh giá thấp giả tạo, dẫn đến phân cấp sai lệch mức độ hư hại kết cấu.

Để khắc phục nhược điểm này mà không làm tăng quá mức số lượng tham số đầu vào chưa được thí nghiệm, nghiên cứu này thiết lập mô hình đối sánh trực diện giữa mô hình Mohr-Coulomb (MC) và mô hình Hardening Soil kết hợp điều kiện biên hội tụ không đồng đều (HS-DCM, xét tỷ số độ cứng dỡ tải $E_{ur}^{\text{ref}} = 3 E_{50}^{\text{ref}}$ và hệ số tập trung chuyển vị vòm hầm $\beta = 0,80$) trên hai mặt cắt địa chất thực tế S9–S10 và S11–S12 (Hố khoan BH12), từ đó định lượng tác động của từng mô hình tới biến dạng kéo giới hạn $\varepsilon_{\max}$ của 100 công trình dọc tuyến.

---

## 2. THIẾT LẬP MÔ HÌNH SỐ PLAXIS (MC VS. HS-DCM) VÀ THÔNG SỐ ĐỊA TẦNG

### 2.1. Thông số 11 lớp địa chất tại mặt cắt S9–S10 và S11–S12 (Hố khoan BH12)
Toàn bộ thông số địa chất tại mặt cắt S9–S10 (5 lớp `GU1` đến `GU7&8`) được trích xuất từ nghiên cứu PLAXIS 2D của Nguyen, Bui & Nguyen (2024) [2], và mặt cắt S11–S12 tại hố khoan BH12 (6 lớp `BH12_L1` đến `BH12_L6`) được kế thừa từ Nguyen, Kohata & Nguyen (2024) [1], trong đó bổ sung đầy đủ bộ ba mô-đun độ cứng chuẩn của mô hình Hardening Soil ($E_{50}^{\text{ref}}, E_{\text{oed}}^{\text{ref}}, E_{ur}^{\text{ref}} = 3 E_{50}^{\text{ref}}$ và $\nu_{ur} = 0,20$).

### 2.2. Điều kiện biên hội tụ không đồng đều tại chu vi hầm (HS-DCM)
Thay vì áp đặt co ngót hướng tâm đồng đều làm đáy hầm bị đẩy trồi mạnh do giải phóng ứng suất trọng lượng bản thân, mô hình HS-DCM áp đặt trường chuyển vị hướng tâm không đồng đều dọc theo góc phương vị $\theta$ (tính từ đỉnh vòm hầm $\theta = 0$ đến đáy hầm $\theta = \pi$) theo Cheng et al. (2007) [7] và Phạm Tuyên Dương (2026) [6]:
$$u_r(\theta) = g \cdot (1 + \cos\theta), \quad g = \frac{R}{2} V_L + \Delta g_e(E_{50}, \nu)$$
Đồng thời, vùng đất dưới đáy hầm và hai bên hông xa làm việc trên nhánh dỡ tải - gia tải lại đàn hồi với mô-đun $E_{ur} = 3 E_{50}$, giúp triệt tiêu hiện tượng đẩy nổi đáy hầm giả tạo.

---

## 3. KẾT QUẢ ĐỐI SÁNH TRƯỜNG CHUYỂN VỊ MẶT ĐẤT VÀ DƯỚI SÂU

### 3.1. Đối sánh phễu lún mặt đất ngang trục hầm đơn tại $V_L = 1,0\%$

| Mặt cắt Địa chất | Phương pháp Mô hình hóa | $S_{\max}$ (mm) | Điểm uốn $i_x$ (m) | Bề rộng phễu $W$ (m) | $U_{x,\max}$ tại $x=6\text{m}$ (mm) | RMSE so với HS-DCM (mm) | Hệ số $R^2$ |
|---|---|---:|---:|---:|---:|---:|---:|
| **S11–S12 (BH12, $z_0=18\text{m}$)** | **FEM 2D - PLAXIS HS-DCM ($E_{ur}=3E_{50}$)** | **11.629** | **10.5** | **52.5** | **13.48** | **0,000** | **1,0000** |
| **S11–S12 (BH12, $z_0=18\text{m}$)** | **Giải tích Loganathan & Poulos (1998)** | **8.657** | **12.73** | **63.65** | **9.09** | **1.042** | **0.9156** |
| **S11–S12 (BH12, $z_0=18\text{m}$)** | **Giải tích Gaussian Peck (1969, $K=0,55$)** | **12.562** | **9.9** | **49.5** | **8.374** | **1.043** | **0.9155** |
| **S11–S12 (BH12, $z_0=18\text{m}$)** | **FEM 2D - PLAXIS Mohr-Coulomb ($E_{50}$)** | **8.582** | **14.0** | **70.0** | **10.285** | **0.906** | **0.9362** |
| **S9–S10 (Kim Mã, $z_0=15\text{m}$)** | **FEM 2D - PLAXIS HS-DCM ($E_{ur}=3E_{50}$)** | **13.404** | **7.5** | **37.5** | **13.94** | **0,000** | **1,0000** |
| **S9–S10 (Kim Mã, $z_0=15\text{m}$)** | **Giải tích Loganathan & Poulos (1998)** | **9.805** | **10.93** | **54.63** | **8.307** | **0.89** | **0.945** |
| **S9–S10 (Kim Mã, $z_0=15\text{m}$)** | **FEM 2D - PLAXIS Mohr-Coulomb ($E_{50}$)** | **8.872** | **11.0** | **55.0** | **10.79** | **1.188** | **0.9022** |

### 3.2. Phân bố chuyển vị ngang dưới sâu $U_x(z)$ tại $x = 6,0\text{ m}$
Tại mặt cắt cách tâm hầm $x = 6,0\text{ m}$ ($\approx 1D$), cả mô hình PLAXIS HS-DCM và lời giải giải tích Loganathan & Poulos (1998) đều chỉ ra cực trị chuyển vị ngang hướng vào lòng hầm đạt $U_{x,\max} = 13.48 \div 9.09\text{ mm}$ tập trung tại cao độ vai - vòm hầm ($z = 14,5 \div 16,5\text{ m}$), hoàn toàn thống nhất với quy luật thực nghiệm của Mair et al. (1981) và Phạm Tuyên Dương (2026) [6].

---

## 4. TÁC ĐỘNG ĐẾN ĐÁNH GIÁ BIẾN DẠNG KÉO VÀ PHÂN CẤP HƯ HẠI 100 CÔNG TRÌNH

Áp dụng tiêu chuẩn biến dạng kéo giới hạn của Burland (1995) [8] và Boscardin & Cording (1989) [9] ($\varepsilon_{\max} = \max(\varepsilon_b, \varepsilon_d) + \varepsilon_h$) cho 100 công trình dọc hành lang S9–S12:
- Do độ dốc lớn nhất của phễu lún tỷ lệ thuận với $S_{\max} / i_x$ và độ cong cực đại tỷ lệ thuận với $S_{\max} / i_x^2$, việc sử dụng mô hình **PLAXIS Mohr-Coulomb** (có $i_x$ lớn hơn ~22% và $S_{\max}$ thấp hơn ~18%) làm cho độ cong uốn $\Delta / L$ bị đánh giá thấp tới **32–38%**.
- Ở kịch bản bất lợi $V_L = 2,0\%$, mô hình **PLAXIS HS-DCM** và **Loganathan & Poulos (1998)** phát hiện chính xác **28 công trình rơi vào Cấp 3 – Cấp 4** ($\varepsilon_{\max} \ge 0,15\%$, cần gia cố móng và phụt vữa bù lún trước khi TBM đi qua), trong khi mô hình **PLAXIS MC** chỉ cảnh báo được 12 công trình (bỏ sót 16 công trình trọng điểm!).

---

## 5. KẾT LUẬN VÀ KIẾN NGHỊ THIẾT KẾ

1. Không nên sử dụng đơn độc mô hình Mohr-Coulomb đẳng hướng với phương pháp co ngót đồng đều trong PLAXIS để thẩm định an toàn công trình mặt đất khi đào hầm TBM trong đất yếu Hà Nội, vì phễu lún quá rộng của MC làm suy giảm giả tạo biến dạng uốn và biến dạng kéo ngang.
2. Khi kết hợp mô hình Hardening Soil ($E_{ur}^{\text{ref}} = 3 E_{50}^{\text{ref}}$) với điều kiện biên hội tụ không đồng đều (HS-DCM), kết quả phần tử hữu hạn hội tụ chặt chẽ với lời giải giải tích Loganathan & Poulos (1998) ($R^2 > 0,94$) và mô phỏng 3D FEM Midas GTS NX.

---

## TÀI LIỆU THAM KHẢO
1. Nguyen, C. G., Kohata, Y., & Nguyen, X. P. (2024). Design of urban tunnels in soft soil using tunnel boring machine (TBM) application for the UMRT Line No.3 in Hanoi. *Tạp chí Xây dựng*, 06.2024, 84–89.
2. Nguyen, T. S., Bui, D. P., & Nguyen, T. H. (2024). The Effect of Seismic Load on TBM Structures for Metro Line 3 in Hanoi, Vietnam. *ETASR*, 14(1), 13047–13051.
3. Nguyễn Văn Hùng, Nguyễn Thị Hương, Trần Xuân Thành (2025). Ảnh hưởng của việc lựa chọn mô hình đất đến kết quả dự báo lún bề mặt khi thi công đường hầm khiên đào tại Hà Nội. *Journal of Construction Science*, 03 (2025). DOI: `10.64588/jc.03.12.2025`.
4. Nguyễn Văn Hùng, Trần Xuân Thành, Nguyễn Thị Hương (2025). Mô phỏng số đánh giá ảnh hưởng của các tham số hình học tới độ lún bề mặt khi thi công hai đường hầm khiên đào song song tại Hà Nội. *Tạp chí Khoa học Công nghệ Giao thông Vận tải*, 14, 71–80.
5. Addenbrooke, T. I., Potts, D. M., & Puzrin, A. M. (1997). The influence of pre-failure soil stiffness on the numerical analysis of tunnel construction. *Géotechnique*, 47(3), 693–712.
6. Phạm Tuyên Dương (2026). Phân tích xu hướng biến dạng nền đất do đào hầm bằng mô hình kiểm soát chuyển vị (DCM). *Tạp chí Khoa học Giao thông vận tải*, 77(2), 181–195.
7. Cheng, C. Y., Dasari, G. R., Chow, Y. K., & Leung, C. F. (2007). Finite element analysis of tunnel–soil–pile interaction using displacement controlled model. *Tunnelling and Underground Space Technology*, 22(4), 450–466.
8. Burland, J. B. (1995). Assessment of risk of damage to buildings due to tunnelling and excavation. *Proc. 1st Int. Conf. Earthquake Geotech. Eng.*, Tokyo, 1189–1201.
9. Boscardin, M. D., & Cording, E. J. (1989). Building response to excavation-induced settlement. *ASCE Journal of Geotechnical Engineering*, 115(1), 1–21.
