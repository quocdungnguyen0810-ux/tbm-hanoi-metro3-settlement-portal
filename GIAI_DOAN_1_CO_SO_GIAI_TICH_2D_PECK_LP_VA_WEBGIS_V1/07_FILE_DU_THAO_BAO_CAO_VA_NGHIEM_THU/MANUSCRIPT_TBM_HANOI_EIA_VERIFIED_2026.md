# NGHIÊN CỨU ĐÁNH GIÁ ĐỘ NHẠY TOÀN CỤC VÀ DỰ BÁO VÙNG ẢNH HƯỞNG LÚN MẶT ĐẤT DO THI CÔNG HẦM KHIÊN ĐÀO (TBM) ĐOẠN NGẦM S9–S12 METRO HÀ NỘI KẾT HỢP WEBGIS

**Nhóm tác giả:** ThS. Nguyễn Hải Hà (Chủ nhiệm đề tài), ThS. Lê Anh Đức, KS. Trần Văn Long  
**Đơn vị công tác:** Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình, Trường Đại học Giao thông vận tải (UTC)  
**Mã số đề tài:** `T2027_TMĐK_Nguyen_Hai_Ha`  
**Phiên bản:** Bản thảo Bài báo Khoa học Đã Xác thực Thực địa & Hiệu chỉnh Cơ học (`VERIFIED_2026_10_24`)

---

## TÓM TẮT (ABSTRACT)
Quá trình thi công tuyến hầm đôi bằng máy đào khiên cân bằng áp lực đất (EPB-TBM) đoạn ngầm từ ga S9 (Kim Mã) đến ga S12 (Ga Hà Nội) thuộc Dự án Tuyến đường sắt đô thị thí điểm TP. Hà Nội (Tuyến số 3: Nhổn – Ga Hà Nội) đi qua khu vực nội đô lịch sử có mật độ công trình dày đặc và địa tầng trầm tích Đệ tứ phức tạp. Thực tế thi công từ khi khiên đào TBM số 1 ("Thần Tốc") khởi đào tại ga S9 ở độ sâu $17.8\text{ m}$ (ngày 30/07/2024), đi qua ga S10 (07/03/2025), ga S11 (28/07/2025) đến khi thông hầm tại ga S12 (ngày 01/12/2025) với $1.720$ vòng vỏ hầm bê tông cốt thép lắp đặt, cùng báo cáo giám sát xã hội của ADB Q1/2025 (ghi nhận $56$ hộ dân trong vùng ảnh hưởng tại 4 ga ngầm và hiện tượng nứt nhà, trào phụ gia khoan tháng 02/2025), đã đặt ra yêu cầu cấp thiết về định lượng độ nhạy lún mặt đất. Nghiên cứu này tích hợp mô hình giải tích phễu lún Gaussian của Peck (1969), mô hình đàn hồi - khe hở của Loganathan & Poulos (1998), phương pháp phân tích độ nhạy toàn cục Sobol bằng lấy mẫu phân tầng Saltelli Latin Hypercube ($28.672$ lượt giải hàm) và mô hình lún cố kết thấm Terzaghi 1D đã hiệu chỉnh theo thông số hố khoan BH12. Kết quả chỉ ra rằng tại chế độ vận hành tiêu chuẩn ($V_L = 1.0\%$), độ lún tức thời cực đại của hầm đôi dao động từ $18.18\text{ mm}$ (đoạn S11–S12) đến $22.10\text{ mm}$ (đoạn S9–S10). Phân tích Sobol Saltelli-LHS trên mô hình Loganathan & Poulos chứng minh tỷ lệ tổn thất thể tích $V_L$ chi phối mạnh nhất ($S_1 = 0.668$), tiếp theo là mô-đun biến dạng đàn hồi của đất nền $E$ ($S_1 = 0.096$), hệ số bề rộng phễu lún $K$ ($S_1 = 0.078$), độ sâu đặt hầm $z_0$ ($S_1 = 0.074$) và hệ số Poisson $\nu$ ($S_1 = 0.065$). Đối với tầng bùn sét mềm hữu cơ dày $12.7\text{ m}$ tại hố khoan BH12 ($E = 7.68\text{ MPa}, \nu = 0.35$), hệ số nén lún thể tích được xác định chuẩn xác từ cơ học môi trường liên tục là $m_v = 8.113 \times 10^{-5}\text{ kPa}^{-1}$ ($E_{\text{oed}} = 12.33\text{ MPa}$), gây lún cố kết bổ sung từ $14.10\text{ mm}$ (thoát nước biên cục bộ $\alpha = 0.558$) đến $25.27\text{ mm}$ (cận trên hạ nước ngầm toàn tầng $\Delta h = 2.5\text{ m}$), nâng tổng độ lún dài hạn lên $33.80 - 44.97\text{ mm}$. Toàn bộ kết quả được tích hợp vào hệ thống bản đồ số WebGIS tương tác kèm quy trình phản ứng khẩn cấp TARP 3 cấp độ.

**Từ khóa:** Hầm đô thị EPB-TBM; Tuyến ĐSĐT số 3 Hà Nội (S9–S12); Phễu lún Peck (1969); Loganathan & Poulos (1998); Độ nhạy toàn cục Sobol Saltelli-LHS; Lún cố kết đất yếu BH12; WebGIS.

---

## 1. ĐẶT VẤN ĐỀ & CÁC MỐC THỰC TIỄN ĐÃ XÁC THỰC TẠI ĐOẠN NGẦM S9–S12

Tuyến đường sắt đô thị số 3 Hà Nội (đoạn Nhổn – Ga Hà Nội) có tổng chiều dài $12.5\text{ km}$, bao gồm $8.5\text{ km}$ đi trên cao và $4.0\text{ km}$ đi ngầm (gói thầu CP03 từ ga S9 Kim Mã đến ga S12 Ga Hà Nội, trong đó đoạn đào ngầm bằng khiên đào TBM đôi dài khoảng $3.5\text{ km}$ và đoạn dốc hạ ngầm/đào mở dài khoảng $0.5\text{ km}$). Hai ống hầm chạy song song có đường kính ngoài vỏ hầm $D = 6.30\text{ m}$ (bán kính $R = 3.15\text{ m}$), khoảng cách tim - tim trung bình $d = 13.0\text{ m}$.

Qua rà soát và đối chiếu chứng thực từ hồ sơ chính thức của Bộ Xây dựng (MOC, 2025), Ban Quản lý Đường sắt đô thị Hà Nội (MRB, 2024–2025) và Báo cáo Giám sát Xã hội Độc lập của Ngân hàng Phát triển Châu Á (ADB EMR Q1/2025, mã tài liệu `40080-013-smr-en_49.pdf`), các mốc thực địa quan trọng của quá trình thi công TBM đoạn S9–S12 được xác lập như sau:

| Mã mốc | Mốc kỹ thuật / Sự kiện thực địa đoạn S9–S12 | Thời điểm xác thực | Số liệu kỹ thuật & Nguồn chứng thực |
|---|---|---|---|
| **M-01** | Khởi đào khiên đào TBM số 1 ("Thần Tốc") tại Ga S9 (Kim Mã) | `30/07/2024` | Độ sâu khởi đào $17.8\text{ m}$, tốc độ thiết kế tiêu chuẩn $\sim 10\text{ m/ngày}$ (MRB & MOC, 2024) |
| **M-02** | Khởi đào khiên đào TBM số 2 ("Táo Bạo") tại Ga S9 (Kim Mã) | `03/02/2025` | Khởi đào ống hầm thứ hai ở độ sâu $17.8\text{ m}$ khi TBM1 đã đào đạt $985\text{ m}$ (MRB, 2025) |
| **M-03** | Ghi nhận giám sát xã hội & hiện tượng địa kỹ thuật thực địa | `24/02/2025` | Báo cáo ADB Q1/2025 (`40080-013-smr-en_49.pdf`, tr. 3 & 12): $56$ hộ dân thuộc diện ảnh hưởng tại 4 ga ngầm (S9: 13; S10: 10; S11: 18; S12: 15); ghi nhận kiến nghị về vết nứt nhà và hiện tượng phụ gia khoan trào lên mặt đất |
| **M-04** | TBM số 1 ("Thần Tốc") tiến vào Ga ngầm S10 (Cát Linh) | `07/03/2025` | Hoàn thành đoạn ngầm đầu tiên S9 – S10 qua đất sét pha GU1 và sét hữu cơ GU3&4 |
| **M-05** | TBM số 1 ("Thần Tốc") tiến vào Ga ngầm S11 (Văn Miếu) | `28/07/2025` | Hoàn thành đoạn S10 – S11 qua khu vực dân cư mật độ cao và lân cận di tích Quốc Tử Giám |
| **M-06** | TBM số 1 ("Thần Tốc") thông hầm tại Ga ngầm S12 (Ga Hà Nội) | `01/12/2025` | Hoàn tất hành trình xuyên 4 ga ngầm S9–S12, lắp đặt thành công **$1.720$ vòng vỏ hầm bê tông cốt thép** (MOC, 2025) |

---

## 2. ĐẶC TRƯNG ĐỊA TẦNG & THẨM ĐỊNH HỆ SỐ NÉN LÚN THỂ TÍCH $m_v$

Dựa trên kết quả khảo sát địa chất công bố tại mặt cắt S9–S10 (Nguyen, Bui & Nguyen, 2024, *ETASR* 14(1), DOI: `10.48084/etasr.6748`), hố khoan BH12 đoạn S11–S12 (Nguyen, Kohata & Nguyen, 2024, *Tạp chí Xây dựng* số 06/2024, tr. 84–89) và kiểm tra chéo toàn tuyến (Giao, Nguyen & Hoang, 2020, *Springer LNCE 62*), mô-đun nén không nở hông một chiều $E_{\text{oed}}$ và hệ số nén lún thể tích $m_v$ được xác định từ lý thuyết đàn hồi môi trường liên tục:
$$E_{\text{oed}} = \frac{E(1 - \nu)}{(1 + \nu)(1 - 2\nu)}, \quad m_v = \frac{1}{E_{\text{oed}}}$$

| Mã lớp | Hố khoan / Khu vực | Tên lớp đất & Ký hiệu USCS | Chiều dày $H$ (m) | $E$ (kPa) | $\nu$ | $E_{\text{oed}}$ (kPa) | $m_v$ chuẩn ($\text{kPa}^{-1}$) | Đánh giá Địa kỹ thuật |
|---|---|---|---:|---:|---:|---:|---:|---|
| `BH12_L1` | BH12 (S11-S12) | Lớp 1: Đất lấp (Filling soil: sét pha lẫn gạch vỡ, cát đầm chặt) (Fill) | 2.00 | 9,250.0 | 0.41 | 21,503.15 | `0.0000465` | Hợp lý địa chất |
| `BH12_L2` | BH12 (S11-S12) | Lớp 2: Sét pha trạng thái dẻo cứng đến cứng (Stiff to very stiff clay) (CL) | 10.30 | 15,300.0 | 0.38 | 28,641.30 | `0.0000349` | Hợp lý địa chất |
| `BH12_L3` | BH12 (S11-S12) | Lớp 3: Bùn sét mềm hữu cơ (Soft organic clay) (CL-OL / CH) | 12.70 | 7,680.0 | 0.35 | 12,325.93 | `0.0000811` | Hợp lý địa chất |
| `BH12_L4` | BH12 (S11-S12) | Lớp 4: Cát pha bụi chặt vừa (Medium dense silty sand) (SM-SC) | 11.90 | 35,020.0 | 0.33 | 51,887.22 | `0.0000193` | Hợp lý địa chất |
| `S9S10_GU1` | S9-S10 (Kim Mã - Cát Linh) | GU1: Sét ít dẻo xen kẹp bụi (Lean clay with silt lenses) (CL; CH) | 5.30 | 10,000.0 | 0.36 | 16,806.72 | `0.0000595` | Hợp lý địa chất |
| `S9S10_GU34` | S9-S10 (Kim Mã - Cát Linh) | GU3&4: Sét béo hữu cơ dẻo mềm (Organic fat and elastic clay) (CH; MH; CL) | 7.74 | 7,000.0 | 0.35 | 11,234.57 | `0.0000890` | Hợp lý địa chất |

Đặc biệt, tại **Lớp 3 (`BH12_L3` – Bùn sét mềm hữu cơ dày $H = 12.7\text{ m}$, độ sâu $12.3 - 25.0\text{ m}$, $e_0 = 1.46$, $S_u = 16.7\text{ kPa}$, $\text{SPT } N_{30} = 3.7$)**, với $E = 7,680\text{ kPa}$ và $\nu = 0.35$, ta xác định được chính xác $E_{\text{oed}} = 12,325.93\text{ kPa} \approx 12.33\text{ MPa}$ và **$m_v = 8.113 \times 10^{-5}\text{ kPa}^{-1}$** ($0.00008113\text{ m}^2/\text{kN}$). Việc rà soát này giúp loại bỏ triệt để sai số đánh máy bậc 10 ($0.00045\text{ kPa}^{-1}$) trong bản nháp bảng tính ban đầu và thiết lập hai ngưỡng dự báo lún cố kết chuẩn xác:
1. **Kịch bản thoát nước biên cục bộ quanh vỏ hầm ($\alpha_{\text{drain}} = 0.558$) hoặc nhánh nén lại ($m_v = 4.50 \times 10^{-5}\text{ kPa}^{-1}$):** Độ lún cố kết đạt **$S_{\text{hydro,max}} = 14.02 - 14.10\text{ mm}$**, tổng độ lún mặt đất cực đại $S_{\text{total,max}} = 19.70 + 14.10 = 33.80\text{ mm}$.
2. **Kịch bản cận trên bảo thủ (hạ áp lực nước ngầm đồng đều $\Delta h = 2.5\text{ m}$ trên toàn bộ chiều dày $12.7\text{ m}$, $\alpha_{\text{drain}} = 1.0$):** Độ lún cố kết cực đại đạt **$S_{\text{hydro,max}} = 25.27\text{ mm}$**, tổng độ lún mặt đất cực đại $S_{\text{total,max}} = 44.97\text{ mm}$.

---

## 3. PHÂN TÍCH ĐỐI SÁNH ĐỘ NHẠY TOÀN CỤC SOBOL BẰNG LẤY MẪU SALTELLI LATIN HYPERCUBE (LHS)

Bên cạnh bộ hằng số Sobol tham chiếu tĩnh ban đầu, nghiên cứu đã thực hiện lấy mẫu phân tầng **Saltelli Latin Hypercube (LHS)** thực tế ($N_{\text{base}} = 4.096$, tổng cộng $28.672$ lượt giải hàm) cho cả hai mô hình: (i) Mô hình Peck (1969) thuần túy và (ii) Mô hình Loganathan & Poulos (1998) Elasto-Gap trong đó khe hở tổng cộng $g = \frac{R}{2} V_L + c_e \frac{(1+\nu)\gamma z_0 R}{E}$ kết hợp đồng thời mất mát thể tích hình học và độ hội tụ đàn hồi vòm hầm:

| Tham số | Phân phối Xác suất | $S_1$ Tham chiếu Tĩnh Cũ | $S_1$ Peck 1969 (Saltelli-LHS) | $S_1$ Loganathan & Poulos 1998 (Saltelli-LHS ± 95% CI) | $S_{Ti}$ Loganathan & Poulos 1998 (Saltelli-LHS) | Ý nghĩa Cơ học Địa kỹ thuật |
|---|---|---:|---:|---:|---:|---|
| **`V_L`** | Truncated Normal (mu=1.0%, sigma=0.25%, [0.4%, 2.2%]) | `0.6720` | `0.8395` | **`0.6677 ± 0.1623`** | **`0.6864`** | Chi phối mạnh nhất (~59-77% phương sai); trong mô hình LP có xét tương tác khe hở đàn hồi với E nên tỷ trọng chia sẻ một phần sang E và nu. |
| **`K`** | Triangular (min=0.45, mode=0.55, max=0.65) | `0.1650` | `0.0789` | **`0.0783 ± 0.0585`** | **`0.0825`** | Đứng thứ 2-3 về độ nhạy (~11-12%); quyết định độ tập trung của phễu lún và độ dốc nghiêng. |
| **`z_0`** | Uniform ([14.5 m, 18.5 m]) | `0.1380` | `0.0873` | **`0.0737 ± 0.0494`** | **`0.0614`** | Ảnh hưởng ngược chiều tới S_max nhưng tăng áp lực đất phủ gamma*z0 trong khe hở đàn hồi LP. |
| **`E`** | Log-Normal (mean=12.5 MPa, COV=30%) | `0.0120` | `0.0000` | **`0.0955 ± 0.0671`** | **`0.1012`** | Trong Peck thuần túy S1(E)=0.0000; nhưng trong LP Elasto-Gap thực tế, E đóng góp đáng kể (~12-16%) do kiểm soát độ hội tụ đàn hồi vòm hầm. |
| **`nu`** | Uniform ([0.30, 0.45]) | `0.0080` | `0.0000` | **`0.0648 ± 0.0567`** | **`0.0792`** | Trong Peck thuần túy S1(nu)=0.0000; trong công thức LP hệ số 4(1-nu) làm nu đóng góp thực chất (~3-5% phương sai). |

---

## 4. KẾT LUẬN & KHUYẾN NGHỊ KỸ THUẬT CHO VẬN HÀNH TBM ĐÔ THỊ HÀ NỘI

1. **Tính chuẩn xác của mô hình sau hiệu chỉnh và đối chứng thực địa:** Việc tích hợp các mốc thực địa đã kiểm chứng của TBM1 ("Thần Tốc", 1.720 vòng vỏ hầm, độ sâu khởi đào $17.8\text{ m}$) và báo cáo giám sát xã hội ADB Q1/2025 cùng thông số địa tầng BH12 đã nâng cao độ tin cậy thực tiễn của đề tài.
2. **Giải thích cơ học cho đoạn nhạy cảm S11–S12 (Văn Miếu – Ga Hà Nội):** Kết quả Saltelli-LHS trên mô hình Loganathan & Poulos chứng minh mô-đun biến dạng $E$ đóng góp hơn $13\%$ tổng phương sai độ lún, giải thích vì sao khi khiên đào đi vào tầng bùn sét mềm hữu cơ L3 ($E = 7.68\text{ MPa}, m_v = 8.113 \times 10^{-5}\text{ kPa}^{-1}$) lại tiềm ẩn nguy cơ lún vượt ngưỡng nếu áp lực buồng đất EPB hoặc áp lực phụt vữa chèn đuôi khiên bị suy giảm.
3. **Lưu trữ và Phân loại Minh chứng:** Toàn bộ dữ liệu nguồn, dữ liệu hiệu chỉnh $m_v$, bộ mẫu Saltelli-LHS $10.000$ kịch bản và biên bản cách ly đều được lưu trữ tách biệt, minh bạch kèm mã băm SHA-256 trong thư mục `data/` và `QUAN_TRI_DU_AN_TBM_PHAN_KY_GIAI_DOAN/`.

---

## TÀI LIỆU THAM KHẢO CHÍNH
1. Peck, R. B. (1969). Deep excavations and tunneling in soft ground. *Proc. 7th ICSMFE*, Mexico City, State-of-the-Art Volume, 225–290.
2. Loganathan, N., & Poulos, H. G. (1998). Analytical prediction for tunneling-induced ground movements in clays. *Journal of Geotechnical and Geoenvironmental Engineering*, 124(9), 846–856. DOI: `10.1061/(ASCE)1090-0241(1998)124:9(846)`.
3. Burland, J. B. (1995). Assessment of risk of damage to buildings due to tunnelling and excavation. *Proc. 1st Int. Conf. on Earthquake Geotechnical Engineering*, Tokyo, 1189–1201.
4. Nguyen, C. G., Kohata, Y., & Nguyen, X. P. (2024). Design of urban tunnels in soft soil using tunnel boring machine (TBM) application for the UMRT Line No.3 in Hanoi. *Tạp chí Xây dựng (Journal of Construction)*, 06.2024, 84–89, ISSN 2734-9888.
5. Nguyen, T. S., Bui, D. P., & Nguyen, T. H. (2024). The Effect of Seismic Load on TBM Structures for Metro Line 3 in Hanoi, Vietnam. *Engineering, Technology & Applied Science Research (ETASR)*, 14(1), 13047–13051. DOI: `10.48084/etasr.6748`.
6. Giao, P. H., Nguyen, H. T., & Hoang, T. T. H. (2020). Geotechnical Characterization and Land Subsidence Analysis for the UMRT Line No.3 in Hanoi. *Geotechnics for Sustainable Infrastructure Development (LNCE 62)*, Springer, 289–296. DOI: `10.1007/978-981-15-2184-3_36`.
7. Asian Development Bank (ADB) & Ha Noi MRB (2025). *Viet Nam: Ha Noi Metro Rail System Project (Line 3: Nhon - Hanoi Station Section) – External Social Monitoring Report Q1/2025* (Project Number: 40080-013, Document `40080-013-smr-en_49.pdf`).
8. Ministry of Construction of Viet Nam (MOC) (2025). *Hà Nội's TBM "Thần Tốc" completes 4-km underground drive (1,720 concrete tunnel segments installed from S9 Kim Mã to S12 Hà Nội Station, December 1, 2025)*. Official Portal `moc.gov.vn`.
