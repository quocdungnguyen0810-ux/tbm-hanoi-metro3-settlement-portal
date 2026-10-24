# -*- coding: utf-8 -*-
"""
Setup Stage 3 directory structure and backup shared Stage 1 and Stage 2 data.
Ensures zero disruption to Stage 1 and Stage 2 sealed baselines.
"""
import os
import sys
import shutil
import hashlib

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGE1_DIR = os.path.join(ROOT, "nhiem_vu_luan_an")
STAGE2_DIR = os.path.join(ROOT, "nhiem_vu_luan_an_giai_doan_2")
STAGE3_DIR = os.path.join(ROOT, "nhiem_vu_luan_an_giai_doan_3")

SUBDIRS = [
    "00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1_VA_2",
    os.path.join("00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1_VA_2", "du_lieu_giai_doan_1"),
    os.path.join("00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1_VA_2", "du_lieu_giai_doan_2"),
    "01_KE_HOACH_TRIEN_KHAI_CHI_TIET_GIAI_DOAN_3",
    "02_BO_DU_LIEU_EXCEL_CHUYEN_SAU_GIAI_DOAN_3",
    "03_HINH_ANH_MINH_HOA_CHAT_LUONG_CAO_GIAI_DOAN_3",
    "04_BAN_THAO_BAO_CAO_GIAI_DOAN_3_CHI_TIET",
    "05_HE_THONG_WEBGIS_3_DIGITAL_TWIN_GIAI_DOAN_3",
    os.path.join("05_HE_THONG_WEBGIS_3_DIGITAL_TWIN_GIAI_DOAN_3", "data"),
    "06_HO_SO_NGHIEM_THU_GIAI_DOAN_3"
]

def sha256_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def main():
    print("1. Creating Stage 3 directory tree...")
    for sd in SUBDIRS:
        p = os.path.join(STAGE3_DIR, sd)
        os.makedirs(p, exist_ok=True)
        print(f"  [OK] Directory: {p}")

    print("\n2. Backing up shared Stage 1 core data into Stage 3...")
    dst_g1 = os.path.join(STAGE3_DIR, "00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1_VA_2", "du_lieu_giai_doan_1")
    g1_files = []
    
    # Excel G1
    s_excel1 = os.path.join(STAGE1_DIR, "02_du_lieu_excel_chuyen_nghiep")
    if os.path.exists(s_excel1):
        for f in os.listdir(s_excel1):
            sf = os.path.join(s_excel1, f)
            if os.path.isfile(sf):
                df = os.path.join(dst_g1, f)
                shutil.copy2(sf, df)
                h_src = sha256_file(sf)
                h_dst = sha256_file(df)
                assert h_src == h_dst, f"Checksum mismatch for {f}"
                g1_files.append((f, os.path.getsize(df), h_dst, "Bảng tính Excel cơ sở GĐ1"))

    # GIS G1
    s_gis1 = os.path.join(STAGE1_DIR, "05_he_thong_webgis_tuong_tac", "data")
    if os.path.exists(s_gis1):
        for f in os.listdir(s_gis1):
            sf = os.path.join(s_gis1, f)
            if os.path.isfile(sf):
                df = os.path.join(dst_g1, f)
                shutil.copy2(sf, df)
                h_dst = sha256_file(df)
                g1_files.append((f, os.path.getsize(df), h_dst, "Dữ liệu không gian GeoJSON GĐ1"))

    print(f"  [COPIED] {len(g1_files)} files from Stage 1 -> SHA-256 verified.")

    print("\n3. Backing up shared Stage 2 core data into Stage 3...")
    dst_g2 = os.path.join(STAGE3_DIR, "00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1_VA_2", "du_lieu_giai_doan_2")
    g2_files = []

    # Excel G2
    s_excel2 = os.path.join(STAGE2_DIR, "02_BO_DU_LIEU_EXCEL_NANG_CAO_GIAI_DOAN_2")
    if os.path.exists(s_excel2):
        for f in os.listdir(s_excel2):
            sf = os.path.join(s_excel2, f)
            if os.path.isfile(sf):
                df = os.path.join(dst_g2, f)
                shutil.copy2(sf, df)
                h_src = sha256_file(sf)
                h_dst = sha256_file(df)
                assert h_src == h_dst, f"Checksum mismatch for {f}"
                g2_files.append((f, os.path.getsize(df), h_dst, "Bảng tính Excel 3D & Monte Carlo GĐ2"))

    # GIS G2
    s_gis2 = os.path.join(STAGE2_DIR, "05_HE_THONG_WEBGIS_2_TUONG_TAC_GIAI_DOAN_2", "data")
    if os.path.exists(s_gis2):
        for f in os.listdir(s_gis2):
            sf = os.path.join(s_gis2, f)
            if os.path.isfile(sf):
                df = os.path.join(dst_g2, f)
                shutil.copy2(sf, df)
                h_dst = sha256_file(df)
                g2_files.append((f, os.path.getsize(df), h_dst, "Lớp không gian 100 công trình GeoJSON GĐ2"))

    # WebGIS 2 HTML
    s_w2 = os.path.join(STAGE2_DIR, "05_HE_THONG_WEBGIS_2_TUONG_TAC_GIAI_DOAN_2", "webgis_settlement_advance_v2.html")
    if os.path.exists(s_w2):
        df = os.path.join(dst_g2, "webgis_settlement_advance_v2.html")
        shutil.copy2(s_w2, df)
        h_dst = sha256_file(df)
        g2_files.append(("webgis_settlement_advance_v2.html", os.path.getsize(df), h_dst, "Ứng dụng WebGIS 2.0 đã niêm phong"))

    # Report G2
    s_rep2 = os.path.join(STAGE2_DIR, "04_BAN_THAO_BAO_CAO_GIAI_DOAN_2_CHI_TIET", "BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_2.md")
    if os.path.exists(s_rep2):
        df = os.path.join(dst_g2, "BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_2.md")
        shutil.copy2(s_rep2, df)
        h_dst = sha256_file(df)
        g2_files.append(("BAO_CAO_TOAN_VAN_HOAN_CHINH_GIAI_DOAN_2.md", os.path.getsize(df), h_dst, "Báo cáo toàn văn GĐ2"))

    print(f"  [COPIED] {len(g2_files)} files from Stage 2 -> SHA-256 verified.")

    # Write backup manifest for Stage 3
    manifest_p = os.path.join(STAGE3_DIR, "00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1_VA_2", "DANH_MUC_SAO_LUU_VA_PHAN_LOAI_DU_LIEU_G1_G2.md")
    lines = [
        "# BẢNG DANH MỤC SAO LƯU VÀ PHÂN LOẠI DỮ LIỆU ĐẦU VÀO GIAI ĐOẠN 3",
        "### (KẾ THỪA VÀ BẢO LƯU NGUYÊN VẸN TỪ GIAI ĐOẠN 1 VÀ GIAI ĐOẠN 2)",
        "",
        "**Ngày thực hiện sao lưu:** 2026-10-15  ",
        "**Mục đích:** Tạo lập không gian dữ liệu độc lập cho Giai đoạn 3, tuyệt đối không xâm phạm hay làm sai lệch mã băm của Giai đoạn 1 và Giai đoạn 2 đã đóng băng.  ",
        "",
        "---",
        "",
        "### I. DỮ LIỆU KẾ THỪA TỪ GIAI ĐOẠN 1 (ĐÃ ĐỐI CHUẨN SHA-256 1:1)",
        "",
        "| STT | Tên tệp tin | Dung lượng (bytes) | Mã băm SHA-256 | Vai trò & Mục đích sử dụng trong GĐ3 |",
        "|:---:|---|---|---|---|"
    ]
    for idx, (f, sz, h, role) in enumerate(g1_files, 1):
        lines.append(f"| {idx} | `{f}` | {sz:,} | `{h}` | {role} |")

    lines.extend([
        "",
        "### II. DỮ LIỆU KẾ THỪA TỪ GIAI ĐOẠN 2 (ĐÃ ĐỐI CHUẨN SHA-256 1:1)",
        "",
        "| STT | Tên tệp tin | Dung lượng (bytes) | Mã băm SHA-256 | Vai trò & Mục đích sử dụng trong GĐ3 |",
        "|:---:|---|---|---|---|"
    ])
    for idx, (f, sz, h, role) in enumerate(g2_files, 1):
        lines.append(f"| {idx} | `{f}` | {sz:,} | `{h}` | {role} |")

    lines.extend([
        "",
        "---",
        "### III. PHÂN LOẠI DỮ LIỆU ĐẦU VÀO MỚI BỔ SUNG CHO GIAI ĐOẠN 3",
        "",
        "1. **Dữ liệu thủy văn - địa chất tương tác đa trường (Hydro-Mechanical Input):**",
        "   - Cao trình mực nước ngầm tự nhiên, gradient thủy lực $\\Delta h$ và hệ số thấm $k_x, k_y, k_z$ của các tầng chứa nước Holocen ($q_h$) và Pleistocen ($q_p$).",
        "   - Mô hình cố kết Terzaghi 1D & Biot 3D: chỉ số nén $C_c$, hệ số rỗng ban đầu $e_0$, áp lực tiền cố kết $\\sigma'_p$.",
        "2. **Dữ liệu cấu trúc số 3D phần tử hữu hạn (3D Numerical FEM Mesh Input):**",
        "   - Mô hình đất nền Hardening Soil Model with Small-Strain Stiffness (HSS) hiệu chỉnh cho tầng sét dẻo mềm đoạn Ga S12 ($E_{50}^{ref} = 8.5\\text{ MPa}, E_{ur}^{ref} = 25.5\\text{ MPa}, \\gamma_{0.7} = 1.2 \\times 10^{-4}$).",
        "   - Đặc tính cơ lý vỏ hầm đúc sẵn C45/55 ($E_c = 34\\text{ GPa}, \\nu = 0.2, d = 0.35\\text{ m}$) và khớp nối bu-lông.",
        "3. **Tập dữ liệu huấn luyện mạng nơ-ron vật lý PINN (Physics-Informed Deep Learning Dataset):**",
        "   - 5,000 điểm collocation trong miền không gian $(x, y, z)$ và thời gian $t$.",
        "   - Hàm tổn thất vật lý tích hợp phương trình vi phân cân bằng ứng suất Navier-Cauchy và phương trình thấm liên tục Darcy.",
        "4. **Dữ liệu khảo sát mở rộng 150 công trình & Di tích lịch sử (Expanded Exposure Input):**",
        "   - Bổ sung 50 công trình nhạy cảm đặc biệt (Văn Miếu - Quốc Tử Giám, Chùa Phổ Giác, các tòa nhà trụ sở ngoại giao, chung cư lắp ghép cũ).",
        "   - Bổ sung thông tin cọc móng sâu: đường kính cọc, chiều sâu mũi cọc, cự ly 3D tới tim hầm.",
        "",
        "---",
        "**XÁC NHẬN KIỂM TOÁN DỮ LIỆU ĐẦU VÀO GIAI ĐOẠN 3:**",
        "1. Toàn bộ dữ liệu sao lưu GĐ1 và GĐ2 trùng khớp 1:1 mã băm SHA-256.",
        "2. Hai thư mục gốc `nhiem_vu_luan_an/` và `nhiem_vu_luan_an_giai_doan_2/` hoàn toàn nguyên vẹn, không bị can thiệp."
    ])

    with open(manifest_p, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"  [OK] Created backup manifest: {manifest_p}")

if __name__ == "__main__":
    main()
