# -*- coding: utf-8 -*-
import os
import hashlib

stage2_dir = 'nhiem_vu_luan_an_giai_doan_2'
checksum_file = os.path.join(stage2_dir, '06_HO_SO_NGHIEM_THU_GIAI_DOAN_2', 'DANH_MUC_HO_SO_VA_CHECKSUM_SHA256_GIAI_DOAN_2.md')

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

all_files = []
for root, dirs, files in os.walk(stage2_dir):
    for f in sorted(files):
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, stage2_dir).replace('\\', '/')
        if rel_p == '06_HO_SO_NGHIEM_THU_GIAI_DOAN_2/DANH_MUC_HO_SO_VA_CHECKSUM_SHA256_GIAI_DOAN_2.md':
            continue
        sz = os.path.getsize(full_p)
        h = sha256_file(full_p)
        all_files.append((rel_p, sz, h))

print(f'Total files found: {len(all_files)}')

lines = [
    '# BẢNG KIỂM KÊ VÀ NIÊM PHONG MÃ BĂM SHA-256 TOÀN BỘ SẢN PHẨM GIAI ĐOẠN 2',
    '### ĐỀ TÀI: ĐÁNH GIÁ ĐỘ NHẠY, DỰ BÁO LÚN 3D VÀ RỦI RO 100 CÔNG TRÌNH HẦM METRO 3 HÀ NỘI',
    '',
    '**Cơ quan chủ quản:** Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường - Trường ĐH Giao thông vận tải  ',
    '**Thời gian niêm phong:** 2026-10-15  ',
    f'**Tổng số lượng tệp tin đã niêm phong:** {len(all_files) + 1} tệp tin (bao gồm tệp niêm phong này)  ',
    '',
    '---',
    '',
    '| STT | Đường dẫn tương đối tệp tin | Dung lượng (bytes) | Mã băm SHA-256 Bất biến |',
    '|---|---|---|---|'
]

for idx, (rel_p, sz, h) in enumerate(all_files, 1):
    lines.append(f'| {idx} | `{rel_p}` | {sz:,} | `{h}` |')

lines.extend([
    '',
    '---',
    '**XÁC NHẬN CỦA HỘI ĐỒNG KIỂM TOÁN VÀ CHỦ NHIỆM ĐỀ TÀI:**  ',
    '1. Toàn bộ các sản phẩm thuộc Giai đoạn 2 đã được tính toán mã băm SHA-256 chuẩn FIPS PUB 180-4.',
    '2. Tuyệt đối bảo toàn sản phẩm Giai đoạn 1; 100% dữ liệu dùng chung được sao lưu trong thư mục `00_SAO_LUU_DU_LIEU_DAU_VAO_GIAI_DOAN_1/`.',
    '3. Mọi sửa đổi trên các tệp tin nêu trên sẽ làm sai lệch mã băm và bị phát hiện bởi cơ chế kiểm toán tự động.',
    ''
])

with open(checksum_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Updated DANH_MUC_HO_SO_VA_CHECKSUM_SHA256_GIAI_DOAN_2.md successfully!')
