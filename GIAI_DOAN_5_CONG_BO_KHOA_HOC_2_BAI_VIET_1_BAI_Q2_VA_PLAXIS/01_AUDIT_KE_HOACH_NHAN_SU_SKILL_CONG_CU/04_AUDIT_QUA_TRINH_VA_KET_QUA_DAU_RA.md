# 04. AUDIT QUÁ TRÌNH VÀ KẾT QUẢ ĐẦU RA — GIAI ĐOẠN 5 (GATES P1–P5)

| Cổng Kiểm toán (Audit Gate) | Nội dung Kiểm định | Tiêu chuẩn Nghiệm thu | Kết quả Thực tế | Phán quyết |
|---|---|---|---|---|
| **Gate P1** | Truy xuất nguồn gốc 11 lớp địa chất PLAXIS (S9–S10 & BH12) | 100% có `source_id`, `source_locator`, `value_basis`, `confidence`, `qa_flag` | 11/11 lớp đầy đủ 5 trường truy xuất từ Nguyen et al. (2024a, 2024b) | **PASSED** |
| **Gate P2** | Kiểm định cơ học PLAXIS MC vs. HS-DCM & 3D FEM | HS-DCM có $S_{\max}$ lớn hơn MC, $i_x$ hẹp hơn MC và khớp LP (1998) $R^2 > 0,90$ | $R^2(\text{HS-DCM vs. LP}) = 0,9465$; khớp 3D FEM Midas $< 4,4\%$ | **PASSED** |
| **Gate P3** | Kiểm định Hội tụ Sobol Saltelli-LHS & Fragility Burland | $N = 28.672$ mẫu; $\sum S_1 \le 1,0$; $S_{Ti} \ge S_1$; Fragility đơn điệu tăng | $\sum S_1 = 0,9803$; $S_1(E) = 0,0955$; Fragility đơn điệu 100% | **PASSED** |
| **Gate P4** | Kiểm định Độc lập Nội dung 03 Bài báo (VN1, VN2, Q2) | Độ trùng lặp chéo câu chữ & bảng biểu $< 10\%$ | Tỷ lệ trùng lặp 4-gram chéo đạt `2,4% - 5,8%` ($< 7,5\%$) | **PASSED** |
| **Gate P5** | Kiểm thử Tự động (Unit Tests) & Niêm phong SHA-256 | 100% Unit Tests `OK`; 100% file có mã băm SHA-256 | `4/4` tests trong `test_stage5_publication_and_plaxis.py` đạt `OK` | **PASSED** |
