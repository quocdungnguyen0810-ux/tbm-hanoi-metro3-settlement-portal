# -*- coding: utf-8 -*-
"""
Script tạo các file văn bản chính (.docx, .xlsx) tương ứng với các file markdown (.md)
trong thư mục NCKH_SV_2026_QuanLyDoThi phục vụ nghiên cứu khoa học sinh viên.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

WORKSPACE = r"d:\OneDrive\NCKH\NCKH 2027\T2027\TBM_ĐTM\NCKH_SV_2026_QuanLyDoThi"

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), 'CCCCCC')
        tblBorders.append(border)
    tblPr.append(tblBorders)

def format_run(run, font_name="Times New Roman", size_pt=12, bold=False, italic=False, color_rgb=(0,0,0)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

# ==========================================
# 1. TẠO FILE 01_DE_CUONG_THUYET_MINH_NCKHSV.docx
# ==========================================
def create_docx_proposal():
    doc = Document()
    
    # Page setup: Standard A4
    for section in doc.sections:
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(0.79)
        
    # Title
    p_header = doc.add_paragraph()
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_header.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO / TRƯỜNG ĐẠI HỌC\n")
    format_run(r1, size_pt=11, bold=True)
    r2 = p_header.add_run("KHOA / BỘ MÔN QUẢN LÝ ĐÔ THỊ & CÔNG TRÌNH\n")
    format_run(r2, size_pt=11, bold=True, color_rgb=(0, 51, 102))
    r3 = p_header.add_run("-------------------------------------\n\n")
    format_run(r3, size_pt=10, bold=False)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_main_title = p_title.add_run("THUYẾT MINH ĐỀ TÀI NGHIÊN CỨU KHOA HỌC CỦA SINH VIÊN\nNĂM HỌC 2026 – 2027\n")
    format_run(r_main_title, size_pt=15, bold=True, color_rgb=(0, 51, 153))
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("TÊN ĐỀ TÀI:\n\"ĐÁNH GIÁ MỨC ĐỘ TỔN THƯƠNG CỦA NHÀ Ở DÂN CƯ MÓNG NÔNG\nVÀ ĐỀ XUẤT GIẢI PHÁP QUẢN LÝ RỦI RO ĐÔ THỊ DỌC HÀNH LANG THI CÔNG HẦM METRO LINE 3\n(ĐOẠN KIM MÃ – CÁT LINH – VĂN MIẾU)\"\n")
    format_run(r_sub, size_pt=13, bold=True, color_rgb=(180, 0, 0))

    # General info table
    table_info = doc.add_table(rows=6, cols=2)
    table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_info)
    info_data = [
        ("Mã số đề tài:", "SV-2026-QLDT-01"),
        ("Lĩnh vực nghiên cứu:", "Quản lý Đô thị / Đánh giá Tác động Môi trường & Quản lý Xây dựng"),
        ("Thời gian thực hiện:", "08 tháng (Từ tháng 11/2026 đến tháng 06/2027)"),
        ("Giảng viên hướng dẫn:", "TS. Nguyễn Hải Hà (Chủ nhiệm Đề tài T2027 TBM_ĐTM)"),
        ("Đơn vị chủ trì:", "Bộ môn Quản lý Đô thị & Công trình"),
        ("Nhóm sinh viên thực hiện:", "1. SV1 (Trưởng nhóm - Thể chế & Báo cáo tổng hợp)\n2. SV2 (Khảo sát Hiện trạng kỹ thuật & Bảng kiểm móng/nứt)\n3. SV3 (Điều tra Xã hội học Đô thị & Thống kê SPSS)\n4. SV4 (Không gian số WebGIS & Cẩm nang Infographic)")
    ]
    for row_idx, (k, v) in enumerate(info_data):
        row = table_info.rows[row_idx]
        row.cells[0].width = Inches(2.2)
        row.cells[1].width = Inches(4.5)
        p0 = row.cells[0].paragraphs[0]
        r0 = p0.add_run(k)
        format_run(r0, size_pt=11, bold=True)
        set_cell_background(row.cells[0], "F2F2F2")
        
        p1 = row.cells[1].paragraphs[0]
        r1 = p1.add_run(v)
        format_run(r1, size_pt=11, bold=False)

    doc.add_paragraph("\n")
    
    # Content sections
    sections_content = [
        ("PHẦN I: TÍNH CẤP THIẾT VÀ TỔNG QUAN VẤN ĐỀ NGHIÊN CỨU", [
            ("1.1. Tính cấp thiết của đề tài:", 
             "• Tuyến đường sắt đô thị số 3 Hà Nội (Nhổn - Ga Hà Nội) đang triển khai thi công 4 km đoạn ngầm (S9 - S12) bằng công nghệ khiên đào EPB-TBM hiện đại.\n"
             "• Hành lang tuyến đi qua khu vực nội đô lịch sử với mật độ nhà ở dạng 'nhà ống' móng nông rất dày đặc, xây dựng qua nhiều thời kỳ, có độ nhạy cảm cao với biến dạng lún chênh lệch.\n"
             "• Dưới góc độ Quản lý Đô thị và Đánh giá tác động môi trường - xã hội (EIA/SIA), việc đánh giá mức độ tổn thương thực tế của nhà dân, lắng nghe tâm tư và xây dựng quy trình giám sát 3 bên (Chủ đầu tư - UBND Phường - Người dân) là khoảng trống nghiên cứu cấp bách có ý nghĩa dân sinh sâu sắc."),
            ("1.2. Tổng quan tình hình nghiên cứu:",
             "• Nghiên cứu quốc tế chuẩn hóa phương pháp đánh giá hư hại công trình bởi Burland (1995), Mair et al. (1996), Son & Cording (2005) dựa trên tương quan độ lún, biến dạng ngang và cấp hư hại.\n"
             "• Đề tài NCKHSV này kế thừa trực tiếp kết quả tính toán cơ học phễu lún Peck (1969) và Loganathan & Poulos (1998) với dải đệm nguy cơ ±35m từ Đề tài lớn T2027 để triển khai đánh giá thực tế quản lý đô thị.")
        ]),
        ("PHẦN II: MỤC TIÊU, ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU", [
            ("2.1. Mục tiêu nghiên cứu:",
             "• Mục tiêu 1: Khảo sát, lập cơ sở dữ liệu hiện trạng kỹ thuật của 80-100 công trình nhà móng nông dải ±35m đoạn S9-S11.\n"
             "• Mục tiêu 2: Điều tra xã hội học đánh giá nhận thức, mức độ lo lắng và sinh kế của 100 hộ dân.\n"
             "• Mục tiêu 3: Lập bản đồ số WebGIS trực quan hóa mức độ tổn thương công trình theo các kịch bản lún.\n"
             "• Mục tiêu 4: Đề xuất Bộ cẩm nang quy trình quản lý rủi ro đô thị cấp cơ sở và cơ chế giám sát hiện trường."),
            ("2.2. Đối tượng và phạm vi nghiên cứu:",
             "• Đối tượng: Hiện trạng kết cấu nhà ở móng nông; nhận thức cộng đồng dân cư; cơ chế quản lý trật tự đô thị và bồi thường thiệt hại.\n"
             "• Không gian: Hành lang dải đệm ±35m tim hầm từ Ga S9 Kim Mã qua Ga S10 Cát Linh đến Ga S11 Văn Miếu.\n"
             "• Thời gian: Dữ liệu thực địa thu thập từ tháng 12/2026 đến tháng 03/2027.")
        ]),
        ("PHẦN III: PHƯƠNG PHÁP NGHIÊN CỨU VÀ TỔ CHỨC THỰC HIỆN", [
            ("3.1. Hệ thống phương pháp liên ngành:",
             "1. Phương pháp kế thừa khoa học: Tiếp nhận mô hình phễu lún từ Đề tài lớn T2027.\n"
             "2. Phương pháp khảo sát điền dã bằng Bảng kiểm (Checklist Field Survey): Ghi nhận 10 thông số mặt đứng ngoài vỉa hè.\n"
             "3. Phương pháp điều tra xã hội học: Bảng hỏi cấu trúc 15 câu (Google Forms kết hợp phiếu giấy kẹp bìa).\n"
             "4. Phương pháp Bản đồ học số (WebGIS): Leaflet.js và Google My Maps số hóa tọa độ WGS84.\n"
             "5. Phương pháp phân tích thể chế: Rà soát Nghị định 06/2021/NĐ-CP, Thông tư 10/2021/TT-BXD, Luật Thủ đô 2024."),
            ("3.2. Cấu trúc nội dung 4 chương:",
             "• Chương 1: Tổng quan dự án Metro Line 3 và Khung lý thuyết quản lý rủi ro nhà ở móng nông.\n"
             "• Chương 2: Đặc điểm không gian kiến trúc và Đánh giá mức độ tổn thương nhà ở đoạn S9-S11.\n"
             "• Chương 3: Thực trạng nhận thức cộng đồng và Tác động xã hội - sinh kế do thi công hầm.\n"
             "• Chương 4: Đề xuất giải pháp quản lý rủi ro đô thị, Bản đồ WebGIS và Cẩm nang ứng phó.")
        ]),
        ("PHẦN IV: DỰ KIẾN SẢN PHẨM VÀ KẾ HOẠCH BÀN GIAO", [
            ("4.1. Danh mục sản phẩm đầu ra:",
             "1. Báo cáo tổng kết toàn văn: Dày 50-60 trang, chuẩn format NCKHSV cấp Trường.\n"
             "2. Bản đồ số WebGIS tương tác: Host trên GitHub Pages, tra cứu trực quan đa tầng dữ liệu.\n"
             "3. Sổ tay Cẩm nang Infographic 8 trang: 'An tâm cùng tuyến Metro ngầm Thủ đô'.\n"
             "4. Bài báo khoa học sinh viên: Đăng Kỷ yếu Hội thảo Khoa học Sinh viên cấp Trường/Phân hiệu."),
            ("4.2. Chữ ký cam kết thực hiện:",
             "Nhóm 4 sinh viên cam kết tuân thủ nghiêm ngặt tiến độ, bảo đảm an toàn thực địa và tuyệt đối trung thực trong nghiên cứu khoa học.")
        ])
    ]
    
    for sec_title, subsections in sections_content:
        p_sec = doc.add_paragraph()
        r_sec = p_sec.add_run(sec_title)
        format_run(r_sec, size_pt=13, bold=True, color_rgb=(0, 51, 102))
        
        for sub_title, text_body in subsections:
            p_sub = doc.add_paragraph()
            r_sub = p_sub.add_run(sub_title)
            format_run(r_sub, size_pt=12, bold=True)
            
            p_body = doc.add_paragraph()
            r_body = p_body.add_run(text_body)
            format_run(r_body, size_pt=11)
            p_body.paragraph_format.line_spacing = 1.25
            
    # Signatures block
    doc.add_paragraph("\n")
    sig_table = doc.add_table(rows=2, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    cell_gv = sig_table.rows[0].cells[0]
    p_gv = cell_gv.paragraphs[0]
    p_gv.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rgv1 = p_gv.add_run("GIẢNG VIÊN HƯỚNG DẪN\n(TỔNG THẦU KHOA HỌC)\n\n\n\n\n")
    format_run(rgv1, size_pt=11, bold=True)
    rgv2 = p_gv.add_run("TS. Nguyễn Hải Hà")
    format_run(rgv2, size_pt=11, bold=True)
    
    cell_sv = sig_table.rows[0].cells[1]
    p_sv = cell_sv.paragraphs[0]
    p_sv.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rsv1 = p_sv.add_run("ĐẠI DIỆN NHÓM SINH VIÊN\n(TRƯỞNG NHÓM - SV1)\n\n\n\n\n")
    format_run(rsv1, size_pt=11, bold=True)
    rsv2 = p_sv.add_run("Sinh viên đại diện nhóm")
    format_run(rsv2, size_pt=11, bold=True)
    
    out_path = os.path.join(WORKSPACE, "01_DE_CUONG_THUYET_MINH_NCKHSV.docx")
    doc.save(out_path)
    print(f"-> Đã tạo: {out_path}")

# ==========================================
# 2. TẠO FILE 02_KE_HOACH_TRIEN_KHAI_CHI_TIET_VA_PHAN_CONG.docx
# ==========================================
def create_docx_plan():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(0.79)
        
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("KẾ HOẠCH TRIỂN KHAI CHI TIẾT VÀ MA TRẬN PHÂN CÔNG RACI\nĐỀ TÀI NCKHSV QUẢN LÝ ĐÔ THỊ (METRO LINE 3 S9–S11)\n")
    format_run(r_title, size_pt=14, bold=True, color_rgb=(0, 51, 153))
    
    # RACI Table
    p_raci = doc.add_paragraph()
    r_raci = p_raci.add_run("I. MA TRẬN PHÂN CÔNG TRÁCH NHIỆM RACI (11 GÓI CÔNG VIỆC)")
    format_run(r_raci, size_pt=12, bold=True, color_rgb=(0, 51, 102))
    
    raci_rows = [
        ("STT", "Gói công việc (WBS)", "SV1 (Trưởng nhóm)", "SV2 (Hiện trạng)", "SV3 (Xã hội học)", "SV4 (GIS/Đồ họa)", "GVHD (Tổng thầu)"),
        ("1", "Hoàn thiện Thuyết minh & Đề cương chi tiết", "R / A", "C", "C", "C", "Phê duyệt (Gate 1)"),
        ("2", "Rà soát cơ chế pháp lý, TCVN & Đề tài T2027", "R", "C", "I", "I", "Hướng dẫn nguồn"),
        ("3", "Thiết kế Bảng kiểm (Checklist) khảo sát nhà ở", "C", "R / A", "C", "I", "Hiệu đính kỹ thuật"),
        ("4", "Thiết kế Phiếu điều tra xã hội học (15 câu)", "C", "C", "R / A", "I", "Phê duyệt nội dung"),
        ("5", "Khảo sát thực địa điền dã (80–100 công trình)", "Giám sát an toàn", "R (Kỹ thuật)", "C (Hỗ trợ)", "C (Chụp ảnh)", "Giám sát từ xa"),
        ("6", "Phát phiếu điều tra người dân (100 phiếu)", "C", "C", "R (Chính)", "C (Hỗ trợ)", "Cấp thư giới thiệu"),
        ("7", "Làm sạch & Phân tích số liệu khảo sát", "C", "R (Dữ liệu nhà)", "R (Dữ liệu dân)", "C", "Kiểm tra thống kê"),
        ("8", "Xây dựng Bản đồ số WebGIS / Google My Maps", "I", "C (Tọa độ)", "C", "R / A", "Đánh giá trực quan"),
        ("9", "Thiết kế Cẩm nang Infographic ứng phó rủi ro", "C (Nội dung)", "C (Kỹ thuật)", "C (Truyền thông)", "R / A", "Phê duyệt xuất bản"),
        ("10", "Soạn thảo Báo cáo toàn văn NCKH (4 chương)", "R / A", "R (Chương 2)", "R (Chương 3)", "R (Chương 4)", "Phản biện & Sửa chữa"),
        ("11", "Thiết kế Slide & Luyện tập bảo vệ đề tài", "C", "C", "C", "R (Thiết kế)", "Tổ chức báo cáo thử")
    ]
    
    table_raci = doc.add_table(rows=len(raci_rows), cols=7)
    table_raci.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_raci)
    
    col_widths = [Inches(0.4), Inches(2.2), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.8), Inches(1.1)]
    for r_idx, row_data in enumerate(raci_rows):
        row = table_raci.rows[r_idx]
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            p = cell.paragraphs[0]
            if c_idx in [0, 2, 3, 4, 5]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            if r_idx == 0:
                format_run(r, size_pt=10, bold=True, color_rgb=(255, 255, 255))
                set_cell_background(cell, "003366")
            else:
                format_run(r, size_pt=9.5, bold=("R" in val or "Gate" in val))
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F9F9F9")

    doc.add_paragraph("\n")
    p_gate = doc.add_paragraph()
    r_gate = p_gate.add_run("II. HỆ THỐNG 4 CỔNG KIỂM SOÁT CHẤT LƯỢNG (AUDIT GATES)")
    format_run(r_gate, size_pt=12, bold=True, color_rgb=(0, 51, 102))
    
    gates = [
        ("Cổng 1 (Gate 1 - Tuần 4): Phê duyệt Công cụ & Đề cương", "Nghiệm thu bản Thuyết minh chính thức, Bảng kiểm checklist 10 tiêu chí và Bảng hỏi điều tra 15 câu đã tinh chỉnh."),
        ("Cổng 2 (Gate 2 - Tuần 11): Nghiệm thu Dữ liệu Thô", "Tối thiểu 80-100 phiếu checklist nhà ở có tọa độ và ảnh đối chứng; 100 phiếu điều tra dân cư hợp lệ; bộ file Excel sạch."),
        ("Cổng 3 (Gate 3 - Tuần 18): Nghiệm thu Sản phẩm Số & Cẩm nang", "Bản đồ WebGIS hoạt động trơn tru trên GitHub Pages có bộ lọc tương tác; Sổ tay Infographic 8 trang thiết kế hoàn chỉnh."),
        ("Cổng 4 (Gate 4 - Tuần 28): Nghiệm thu Toàn văn & Diễn tập bảo vệ", "Báo cáo 50-60 trang không lỗi chính tả, trích dẫn APA chuẩn; Slide 20 trang chỉn chu; nhóm bảo vệ thử đạt yêu cầu.")
    ]
    for g_title, g_desc in gates:
        p = doc.add_paragraph()
        r1 = p.add_run(f"• {g_title}: ")
        format_run(r1, size_pt=11, bold=True)
        r2 = p.add_run(g_desc)
        format_run(r2, size_pt=11)

    out_path = os.path.join(WORKSPACE, "02_KE_HOACH_TRIEN_KHAI_CHI_TIET_VA_PHAN_CONG.docx")
    doc.save(out_path)
    print(f"-> Đã tạo: {out_path}")

# ==========================================
# 3. TẠO FILE 03_SO_TAY_HUONG_DAN_KY_THUAT_CHO_SINH_VIEN.docx
# ==========================================
def create_docx_handbook():
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(0.79)
        
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("SỔ TAY HƯỚNG DẪN KỸ THUẬT VÀ PHƯƠNG PHÁP NGHIÊN CỨU\nDÀNH CHO SINH VIÊN NĂM THỨ NHẤT NGÀNH QUẢN LÝ ĐÔ THỊ\n")
    format_run(r_title, size_pt=14, bold=True, color_rgb=(0, 51, 153))
    
    parts = [
        ("PHẦN 1: HƯỚNG DẪN DÀNH CHO SV2 – BẢNG KIỂM KHẢO SÁT HIỆN TRẠNG NHÀ Ở",
         "1. Nhận diện loại móng từ vỉa hè qua 4 chỉ báo gián tiếp:\n"
         "  - Nhà trước 1990: Tường gạch chịu lực dày 220-330mm, vôi vữa cũ -> Móng nông gạch/đá hoặc móng cọc tre (vùng đất yếu Kim Mã - Cát Linh).\n"
         "  - Nhà 1990-2005: Khung BTCT 3-4 tầng -> Móng băng BTCT hoặc móng bè nông.\n"
         "  - Nhà sau 2005: 4-6 tầng dạng ống hiện đại, có thang máy -> Bắt buộc móng cọc bê tông sâu.\n"
         "2. Tiêu chí phân biệt vết nứt co ngót vữa và vết nứt do lún TBM:\n"
         "  - Nứt co ngót: Chân chim, mạng nhện, bề rộng mảnh <0.5mm, không kẹt cửa, chỉ ở lớp vữa ngoài.\n"
         "  - Nứt lún kết cấu do TBM: Vết nứt xiên 45° từ góc cửa sổ hướng về tim hầm, nứt bậc thang mạch vữa, nứt chữ V tách 2 nhà, kẹt lệch khuôn cửa, lún vênh nền gạch.\n"
         "3. Phân biệt Vùng uốn lõm (Sagging, d <= 12m) chịu nén và Vùng uốn vồng (Hogging, 12m < d <= 35m) chịu kéo ngang xé rách chân tường."),
        
        ("PHẦN 2: HƯỚNG DẪN DÀNH CHO SV3 – BẢNG HỎI ĐIỀU TRA XÃ HỘI HỌC 15 CÂU",
         "• Nguyên tắc đạo đức nghiên cứu: Ẩn danh tuyệt đối, mã hóa ID, tự nguyện tham gia.\n"
         "• Cấu trúc 4 nhóm câu hỏi: (1) Nhân khẩu & Sinh kế đô thị; (2) Nhận thức & Kênh thông tin dự án Metro; (3) Cảm nhận rung chấn, hiện trạng nứt và thang đo lo lắng Likert 1-5; (4) Nhu cầu hỗ trợ, cơ chế bồi thường và nguyện vọng cộng đồng.\n"
         "• Giờ vàng tiếp cận: 14h30 - 16h30 với hộ kinh doanh; 18h30 - 20h00 với hộ dân ở; kết hợp Zalo Tổ dân phố."),
        
        ("PHẦN 3: HƯỚNG DẪN DÀNH CHO SV4 – BẢN ĐỒ SỐ WEBGIS VÀ CẨM NANG INFOGRAPHIC",
         "• Giải pháp Bản đồ số tiếp cận lai: Google My Maps dùng nội bộ tác chiến; WebGIS Leaflet.js host trên GitHub Pages phục vụ báo cáo với bộ lọc tương tác và pop-up công trình.\n"
         "• Đồng bộ GPS WGS84: Định dạng thập phân (21.0315, 105.8192), mã định danh S9_KM_001 liên kết ảnh đối chứng.\n"
         "• Thiết kế Sổ tay Infographic 8 trang trên Canva: Phong cách Flat Design, tông màu Xanh Metro và Cam San hô; 'bình dân hóa' thuật ngữ TBM và phễu lún Peck cánh chim.\n"
         "• Poster A0 và Slide thuyết trình: Tích hợp 2 mã QR trải nghiệm trực tiếp WebGIS và tải Cẩm nang PDF."),
        
        ("PHẦN 4: HƯỚNG DẪN DÀNH CHO SV1 – TỔNG HỢP VĂN PHONG VÀ KHUNG THỂ CHẾ",
         "• Cơ sở pháp lý: Điều 44-45 Nghị định 06/2021/NĐ-CP (sự cố công trình và thỏa thuận bồi thường), Thông tư 10/2021/TT-BXD, Luật Thủ đô 2024.\n"
         "• Thẩm quyền UBND Phường: Tiếp nhận đơn, lập biên bản trong 24-48h, đóng vai trò trọng tài trung gian hòa giải 3 bên.\n"
         "• Văn phong khoa học khách quan, quản lý 4 mốc Audit Gates nghiêm ngặt.")
    ]
    
    for p_title_text, p_body_text in parts:
        p_sec = doc.add_paragraph()
        r_sec = p_sec.add_run(p_title_text)
        format_run(r_sec, size_pt=12, bold=True, color_rgb=(0, 51, 102))
        
        p_body = doc.add_paragraph()
        r_body = p_body.add_run(p_body_text)
        format_run(r_body, size_pt=11)
        p_body.paragraph_format.line_spacing = 1.25
        
    out_path = os.path.join(WORKSPACE, "03_SO_TAY_HUONG_DAN_KY_THUAT_CHO_SINH_VIEN.docx")
    doc.save(out_path)
    print(f"-> Đã tạo: {out_path}")

# ==========================================
# 4. TẠO FILE EXCEL: 02_KE_HOACH_VA_TIEN_DO_GANTT.xlsx
# ==========================================
def create_xlsx_plan():
    wb = openpyxl.Workbook()
    
    # Sheet 1: Timeline & Gantt
    ws_gantt = wb.active
    ws_gantt.title = "Ke_Hoach_Tien_Do_Gantt"
    
    font_header = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
    fill_header = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    fill_gate = PatternFill(start_color="FFE599", end_color="FFE599", fill_type="solid")
    font_bold = Font(name="Times New Roman", size=10, bold=True)
    font_norm = Font(name="Times New Roman", size=10)
    thin_border = Border(
        left=Side(style='thin', color='CCCCCC'),
        right=Side(style='thin', color='CCCCCC'),
        top=Side(style='thin', color='CCCCCC'),
        bottom=Side(style='thin', color='CCCCCC')
    )
    
    headers_gantt = ["STT", "Nội dung gói công việc (WBS)", "Người chủ trì", "Tháng bắt đầu", "Tháng kết thúc", "Số tuần", "Sản phẩm bàn giao", "Trạng thái"]
    ws_gantt.append(headers_gantt)
    for col_idx in range(1, len(headers_gantt)+1):
        cell = ws_gantt.cell(row=1, column=col_idx)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    gantt_data = [
        (1, "Khởi động dự án, tiếp nhận dữ liệu nền T2027", "SV1, GVHD", "11/2026", "11/2026", 2, "Hồ sơ đề cương chi tiết", "Đã hoàn thành"),
        (2, "Thiết kế Bảng kiểm hiện trạng và Bảng hỏi 15 câu", "SV2, SV3", "11/2026", "12/2026", 3, "Phiếu checklist và Google Form", "Đã phê duyệt (Gate 1)"),
        (3, "CỔNG 1 (GATE 1): Phê duyệt công cụ & Thuyết minh", "GVHD", "12/2026", "12/2026", 0, "Biên bản nghiệm thu Gate 1", "ĐẠT (PASSED)"),
        (4, "Khảo sát thực địa nhà ở dải ±35m (80-100 nhà)", "SV2, SV4", "12/2026", "01/2027", 5, "100 phiếu checklist + ảnh GPS", "Đang chuẩn bị"),
        (5, "Điều tra xã hội học 100 hộ dân và hộ kinh doanh", "SV3, SV1", "12/2026", "01/2027", 5, "100 phiếu điều tra hợp lệ", "Đang chuẩn bị"),
        (6, "CỔNG 2 (GATE 2): Nghiệm thu bộ dữ liệu thô", "GVHD, SV1", "01/2027", "01/2027", 0, "Bộ dữ liệu Excel sạch", "Chưa đến hạn"),
        (7, "Phân tích số liệu SPSS và Đánh giá tổn thương nhà", "SV2, SV3", "02/2027", "03/2027", 4, "Báo cáo thống kê & Biểu đồ", "Chưa đến hạn"),
        (8, "Xây dựng Bản đồ WebGIS Leaflet & Google My Maps", "SV4", "02/2027", "03/2027", 4, "Link WebGIS GitHub Pages", "Chưa đến hạn"),
        (9, "Thiết kế Sổ tay Infographic Cẩm nang ứng phó", "SV4, SV1", "02/2027", "03/2027", 4, "Ấn phẩm Sổ tay PDF 8 trang", "Chưa đến hạn"),
        (10, "CỔNG 3 (GATE 3): Nghiệm thu Bản đồ & Cẩm nang", "GVHD", "03/2027", "03/2027", 0, "Bản đồ số live + File in Cẩm nang", "Chưa đến hạn"),
        (11, "Viết bản thảo Báo cáo toàn văn NCKH (4 chương)", "SV1, Nhóm", "03/2027", "04/2027", 5, "Bản thảo báo cáo 50 trang", "Chưa đến hạn"),
        (12, "Viết bài báo gửi Kỷ yếu Hội thảo Sinh viên", "SV1, SV3", "04/2027", "05/2027", 3, "Bài báo khoa học hoàn chỉnh", "Chưa đến hạn"),
        (13, "Thiết kế Slide 20 trang và Poster A0 bảo vệ", "SV4", "05/2027", "05/2027", 2, "Bộ slide PPTX + Poster A0", "Chưa đến hạn"),
        (14, "CỔNG 4 (GATE 4): Báo cáo thử & Nghiệm thu chính thức", "Hội đồng, GVHD", "06/2027", "06/2027", 0, "Bảo vệ chính thức đạt Xuất sắc", "Mục tiêu phấn đấu")
    ]
    for row_idx, r_data in enumerate(gantt_data, start=2):
        ws_gantt.append(r_data)
        is_gate = "CỔNG" in str(r_data[1])
        for col_idx in range(1, len(r_data)+1):
            cell = ws_gantt.cell(row=row_idx, column=col_idx)
            cell.font = font_bold if is_gate else font_norm
            if is_gate:
                cell.fill = fill_gate
            cell.border = thin_border
            if col_idx in [1, 4, 5, 6, 8]:
                cell.alignment = Alignment(horizontal="center", vertical="center")

    # Sheet 2: RACI Matrix
    ws_raci = wb.create_sheet(title="Ma_Tran_RACI")
    headers_raci = ["STT", "Nhiệm vụ nghiên cứu", "SV1 (Trưởng nhóm)", "SV2 (Hiện trạng)", "SV3 (Xã hội học)", "SV4 (GIS/Đồ họa)", "GVHD (Tổng thầu)"]
    ws_raci.append(headers_raci)
    for col_idx in range(1, len(headers_raci)+1):
        cell = ws_raci.cell(row=1, column=col_idx)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    raci_table_data = [
        (1, "Hoàn thiện Thuyết minh & Đề cương chi tiết", "R / A", "C", "C", "C", "Phê duyệt"),
        (2, "Rà soát khung thể chế, pháp lý & TCVN", "R", "C", "I", "I", "Định hướng"),
        (3, "Thiết kế Bảng kiểm (Checklist) khảo sát nhà", "C", "R / A", "C", "I", "Hiệu đính"),
        (4, "Thiết kế Phiếu điều tra xã hội học 15 câu", "C", "C", "R / A", "I", "Phê duyệt"),
        (5, "Tác nghiệp điền dã khảo sát nhà ở (80-100 nhà)", "An toàn", "R (Kỹ thuật)", "C (Hỗ trợ)", "C (Chụp ảnh)", "Bảo trợ"),
        (6, "Phát phiếu điều tra cư dân (100 phiếu)", "C", "C", "R (Chính)", "C (Hỗ trợ)", "Cấp giấy"),
        (7, "Làm sạch & Phân tích số liệu khảo sát", "C", "R (Nhà ở)", "R (Dân cư)", "C", "Kiểm tra"),
        (8, "Xây dựng Bản đồ số WebGIS / My Maps", "I", "C (Tọa độ)", "C", "R / A", "Đánh giá"),
        (9, "Thiết kế Sổ tay Infographic Cẩm nang", "C (Nội dung)", "C (Kỹ thuật)", "C (Truyền thông)", "R / A", "Phê duyệt"),
        (10, "Soạn thảo Báo cáo toàn văn NCKH 4 chương", "R / A", "R (Ch. 2)", "R (Ch. 3)", "R (Ch. 4)", "Phản biện"),
        (11, "Thiết kế Slide 20 trang & Tập dượt bảo vệ", "C", "C", "C", "R (Thiết kế)", "Tổ chức thử")
    ]
    for r_idx, r_data in enumerate(raci_table_data, start=2):
        ws_raci.append(r_data)
        for c_idx in range(1, len(r_data)+1):
            cell = ws_raci.cell(row=r_idx, column=c_idx)
            cell.font = font_norm
            cell.border = thin_border
            if c_idx in [1, 3, 4, 5, 6, 7]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            if "R" in str(r_data[c_idx-1]):
                cell.font = font_bold
                cell.fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")

    # Auto column width
    for ws in [ws_gantt, ws_raci]:
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

    out_path = os.path.join(WORKSPACE, "02_KE_HOACH_VA_TIEN_DO_GANTT.xlsx")
    wb.save(out_path)
    print(f"-> Đã tạo: {out_path}")

# ==========================================
# 5. TẠO FILE EXCEL: 04_BIEU_MAU_THU_THAP_DU_LIEU_THUC_DIA.xlsx
# ==========================================
def create_xlsx_templates():
    wb = openpyxl.Workbook()
    
    font_header = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
    fill_blue = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    fill_green = PatternFill(start_color="385723", end_color="385723", fill_type="solid")
    font_norm = Font(name="Times New Roman", size=10)
    thin_border = Border(
        left=Side(style='thin', color='CCCCCC'),
        right=Side(style='thin', color='CCCCCC'),
        top=Side(style='thin', color='CCCCCC'),
        bottom=Side(style='thin', color='CCCCCC')
    )
    
    # Sheet 1: Checklist Nha O
    ws_house = wb.active
    ws_house.title = "Checklist_80_100_Nha_O"
    headers_house = [
        "Mã công trình", "Số nhà & Tên đường", "Phường", "Quận", 
        "Vĩ độ (Lat WGS84)", "Kinh độ (Long WGS84)", "Khoảng cách tim hầm d (m)", "Phân vùng phễu lún",
        "Số tầng", "Mặt tiền ước tính (m)", "Dạng kết cấu", "Ước tính loại móng",
        "Hiện trạng vết nứt", "Bề rộng vết nứt w (mm)", "Cấp độ Burland (0-5)", "Mục đích sử dụng",
        "Tên file ảnh mặt đứng", "Ghi chú hiện trường"
    ]
    ws_house.append(headers_house)
    for col_idx in range(1, len(headers_house)+1):
        cell = ws_house.cell(row=1, column=col_idx)
        cell.font = font_header
        cell.fill = fill_blue
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    sample_houses = [
        ("S9_KM_001", "Số 285 Kim Mã", "Kim Mã", "Ba Đình", 21.03152, 105.81945, 8.5, "Uốn lõm (Sagging)", 3, 3.8, "Khung BTCT gạch", "Móng băng BTCT", "Nứt chân chim nhẹ", 0.3, "Cấp 1", "Ở + Buôn bán tạp hóa", "S9_KM_001_matdung.jpg", "Cách tim hầm 8.5m"),
        ("S9_KM_002", "Số 287 Kim Mã", "Kim Mã", "Ba Đình", 21.03158, 105.81958, 14.2, "Uốn vồng (Hogging)", 2, 4.2, "Tường gạch chịu lực", "Móng gạch/cọc tre cũ", "Nứt góc cửa sổ xiên", 1.8, "Cấp 2", "Cho thuê quán ăn", "S9_KM_002_matdung.jpg", "Nhà cũ trước 1990"),
        ("S10_CL_001", "Số 12 Cát Linh", "Cát Linh", "Đống Đa", 21.02891, 105.82845, 18.0, "Uốn vồng (Hogging)", 4, 3.5, "Khung BTCT gạch", "Móng băng nông", "Nứt khe tiếp giáp", 2.5, "Cấp 2", "Ở thuần túy", "S10_CL_001_matdung.jpg", "Sát vách nhà số 14"),
        ("S11_QTC_001", "Số 45 Quốc Tử Giám", "Văn Miếu", "Đống Đa", 21.02672, 105.83412, 28.5, "Rìa phễu lún", 5, 5.0, "Khung BTCT hiện đại", "Móng cọc ép sâu", "Không có vết nứt", 0.0, "Cấp 0", "Khách sạn mini", "S11_QTC_001_matdung.jpg", "Nhà xây năm 2018")
    ]
    for r_idx, r_data in enumerate(sample_houses, start=2):
        ws_house.append(r_data)
        for c_idx in range(1, len(r_data)+1):
            cell = ws_house.cell(row=r_idx, column=c_idx)
            cell.font = font_norm
            cell.border = thin_border
            if c_idx in [1, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
                
    # Sheet 2: Dieu Tra Xa Hoi Hoc
    ws_social = wb.create_sheet(title="KhaoSat_XaHoiHoc_100Dan")
    headers_social = [
        "Mã phiếu", "Tên đường/Phường", "Khoảng cách d (m)", "Thời gian cư trú",
        "Hình thức sử dụng", "Phụ thuộc kinh tế tầng 1", "Nắm thông tin TBM", "Kênh thông tin chính",
        "Độ minh bạch thông tin (1-5)", "Cảm nhận rung chấn", "Biểu hiện nhà nứt", "Mức độ lo lắng (Likert 1-5)",
        "Tác động lớn nhất", "Biết quy trình bồi thường", "Hình thức hỗ trợ mong muốn", "Ghi chú ý kiến dân"
    ]
    ws_social.append(headers_social)
    for col_idx in range(1, len(headers_social)+1):
        cell = ws_social.cell(row=1, column=col_idx)
        cell.font = font_header
        cell.fill = fill_green
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    sample_social = [
        ("P_KM_001", "Kim Mã (Ba Đình)", 8.5, "Trên 15 năm", "Ở + Tự kinh doanh", "Hoàn toàn phụ thuộc", "Có nghe nói, không rõ", "Hàng xóm nói chuyện", 2, "Thỉnh thoảng rung nhẹ đêm", "Nứt vữa trát góc", 4, "Lo nứt nhà + Giảm khách", "Chỉ biết báo tổ trưởng", "Phát Sổ tay + Họp dân", "Mong Ban dự án hỗ trợ đo lún"),
        ("P_KM_002", "Kim Mã (Ba Đình)", 14.2, "5-15 năm", "Thuê kinh doanh", "Hoàn toàn phụ thuộc", "Hoàn toàn nắm rõ", "Báo đài, mạng xã hội", 3, "Chưa từng cảm nhận", "Không có", 2, "Ùn tắc do rào chắn", "Biết đường dây nóng", "Cung cấp bản đồ trực tuyến", "Cần đẩy nhanh tiến độ"),
        ("P_CL_001", "Cát Linh (Đống Đa)", 18.0, "Trên 15 năm", "Ở thuần túy", "Không phụ thuộc", "Chưa từng nghe", "Chưa nhận thông tin", 1, "Chưa cảm nhận", "Nứt khe tiếp giáp", 5, "An toàn nứt lún nhà", "Hoàn toàn không biết", "Phát Cẩm nang + Số hotline", "Rất lo vì nhà cổ móng yếu")
    ]
    for r_idx, r_data in enumerate(sample_social, start=2):
        ws_social.append(r_data)
        for c_idx in range(1, len(r_data)+1):
            cell = ws_social.cell(row=r_idx, column=c_idx)
            cell.font = font_norm
            cell.border = thin_border
            if c_idx in [1, 3, 4, 9, 10, 12]:
                cell.alignment = Alignment(horizontal="center", vertical="center")

    for ws in [ws_house, ws_social]:
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 3, 14)

    out_path = os.path.join(WORKSPACE, "04_BIEU_MAU_THU_THAP_DU_LIEU_THUC_DIA.xlsx")
    wb.save(out_path)
    print(f"-> Đã tạo: {out_path}")

if __name__ == "__main__":
    print("Bắt đầu tạo các file định dạng chính (.docx, .xlsx)...")
    create_docx_proposal()
    create_docx_plan()
    create_docx_handbook()
    create_xlsx_plan()
    create_xlsx_templates()
    print("Hoàn tất 100% tất cả các file định dạng chính!")
