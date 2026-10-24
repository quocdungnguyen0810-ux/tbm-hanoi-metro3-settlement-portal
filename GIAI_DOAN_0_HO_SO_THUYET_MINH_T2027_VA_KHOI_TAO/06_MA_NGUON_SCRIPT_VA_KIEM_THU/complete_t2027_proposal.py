# -*- coding: utf-8 -*-
"""
Script audit, sửa chữa, hoàn thiện toàn diện file Thuyết minh đề tài NCKH Cấp Trường:
'D:\\OneDrive\\NCKH\\NCKH 2027\\T2027\\TBM_ĐTM\\Hồ sơ đề tài\\T2027_TMĐK_Nguyen_Hai_Ha.docx'

Quy chuẩn:
- Trường Đại học Giao thông vận tải (UTC)
- Thời gian thực hiện: 12 tháng (01/01/2027 - 31/12/2027)
- Kinh phí: 25.000.000 VNĐ
- Sản phẩm: 01 bài báo khoa học đăng trên Tạp chí Giao thông vận tải (HĐGSNN tối đa 0,75 điểm)
- Chủ nhiệm: ThS. Nguyễn Hải Hà (Bộ môn Địa kỹ thuật & Không gian ngầm)
- Đề tài: Đoạn ngầm S9–S12 Metro Tuyến 3 Hà Nội (TBM EPB, tầng bùn sét mềm BH12, phễu lún Peck & Loganathan-Poulos, rủi ro 60 công trình Burland 1995, WebGIS)
"""

import os
import sys
import copy
import shutil
from pathlib import Path
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
TARGET_DOCX = ROOT / "Hồ sơ đề tài" / "T2027_TMĐK_Nguyen_Hai_Ha.docx"
BACKUP_DOCX = ROOT / "Hồ sơ đề tài" / "T2027_TMĐK_Nguyen_Hai_Ha_BACKUP.docx"


def set_cell_font(cell, font_name="Times New Roman", size_pt=12, bold=False, italic=False, color=None):
    for p in cell.paragraphs:
        for run in p.runs:
            run.font.name = font_name
            run.font.size = Pt(size_pt)
            run.bold = bold
            run.italic = italic
            if color:
                run.font.color.rgb = color


def add_styled_para(cell, text, font_name="Times New Roman", size_pt=12, bold=False, italic=False, 
                    align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4, space_before=0, line_spacing=1.15):
    p = cell.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = line_spacing
    run = p.add_run(text)
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    return p


def clear_cell(cell):
    cell.text = ""
    p = cell.paragraphs[0]
    p.text = ""
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    return p


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def audit_and_complete():
    print(f"1. Tạo bản sao lưu dự phòng: {BACKUP_DOCX.name}")
    shutil.copy2(TARGET_DOCX, BACKUP_DOCX)

    print(f"2. Mở tài liệu gốc để thẩm định và hoàn thiện...")
    doc = docx.Document(TARGET_DOCX)
    t0 = doc.tables[0]
    t1 = doc.tables[1]
    t2 = doc.tables[2]

    # =========================================================================
    # BẢNG 0: A. THÔNG TIN CHUNG
    # =========================================================================
    print("--- Hoàn thiện Bảng 0: Thông tin chung ---")

    # Mục 1 & 2: Tên đề tài & Mã số
    c_title = t0.rows[1].cells[0]
    c_title.text = ""
    add_styled_para(c_title, "1. TÊN ĐỀ TÀI", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
    add_styled_para(c_title, "Nghiên cứu đánh giá độ nhạy và dự báo vùng ảnh hưởng lún mặt đất do thi công hầm khiên đào (TBM) trong điều kiện địa chất đô thị Hà Nội", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=2)

    c_code = t0.rows[1].cells[9]
    c_code.text = ""
    add_styled_para(c_code, "2. MÃ SỐ (do Khoa cấp):\nT2027_TMĐK_Nguyen_Hai_Ha", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Mục 3: Thời gian thực hiện
    c_time = t0.rows[2].cells[0]
    c_time.text = ""
    add_styled_para(c_time, "3. THỜI GIAN THỰC HIỆN: 12 tháng\nTừ ngày 01/01/2027 đến ngày 31/12/2027", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Mục 4: Chủ nhiệm đề tài
    c_pi1 = t0.rows[3].cells[0]
    c_pi1.text = ""
    add_styled_para(c_pi1, "4. CHỦ NHIỆM ĐỀ TÀI", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_pi1, "Họ và tên: Nguyễn Hải Hà", size_pt=12, bold=False, space_after=2)
    add_styled_para(c_pi1, "Đơn vị công tác: Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường", size_pt=12, bold=False, space_after=2)
    add_styled_para(c_pi1, "Điện thoại đơn vị: 024.37664030", size_pt=12, bold=False, space_after=2)

    c_pi2 = t0.rows[3].cells[5]
    c_pi2.text = ""
    add_styled_para(c_pi2, "Học vị: ThS.    Chức danh khoa học: Giảng viên", size_pt=12, bold=False, space_after=2)
    add_styled_para(c_pi2, "Điện thoại di động: 0988.xxx.xxx", size_pt=12, bold=False, space_after=2)
    add_styled_para(c_pi2, "E-mail: ha.nguyenhai@utc.edu.vn", size_pt=12, bold=False, space_after=2)

    # Mục 5: Thành viên tham gia
    # Row 6: Thành viên 1
    c_m1_stt = t0.rows[6].cells[0]
    c_m1_stt.text = ""; add_styled_para(c_m1_stt, "1", size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)
    c_m1_name = t0.rows[6].cells[1]
    c_m1_name.text = ""; add_styled_para(c_m1_name, "ThS. Lê Anh Đức", size_pt=11, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)
    c_m1_unit = t0.rows[6].cells[3]
    c_m1_unit.text = ""; add_styled_para(c_m1_unit, "Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường (Chuyên ngành Địa kỹ thuật & Công trình ngầm)", size_pt=11, align=WD_ALIGN_PARAGRAPH.LEFT)
    c_m1_role = t0.rows[6].cells[8]
    c_m1_role.text = ""; add_styled_para(c_m1_role, "Thành viên nghiên cứu chính", size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Thêm Thành viên 2 (KS. Trần Văn Long - Hỗ trợ kỹ thuật & WebGIS)
    # Kiểm tra xem đã có hàng thành viên thứ 2 chưa
    has_member2 = False
    for r_i in range(7, 10):
        if len(t0.rows[r_i].cells) >= 12 and t0.rows[r_i].cells[0].text.strip() == "2":
            has_member2 = True
            break
    if not has_member2:
        new_tr = copy.deepcopy(t0.rows[6]._tr)
        t0.rows[6]._tr.addnext(new_tr)
        # Hàng mới là row 7
        r_new = t0.rows[7]
        c_m2_stt = r_new.cells[0]; c_m2_stt.text = ""; add_styled_para(c_m2_stt, "2", size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)
        c_m2_name = r_new.cells[1]; c_m2_name.text = ""; add_styled_para(c_m2_name, "KS. Trần Văn Long", size_pt=11, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)
        c_m2_unit = r_new.cells[3]; c_m2_unit.text = ""; add_styled_para(c_m2_unit, "Khoa Công trình và Môi trường (Chuyên môn Địa kỹ thuật công trình & GIS)", size_pt=11, align=WD_ALIGN_PARAGRAPH.LEFT)
        c_m2_role = r_new.cells[8]; c_m2_role.text = ""; add_styled_para(c_m2_role, "Thành viên hỗ trợ kỹ thuật", size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Mục 6: Tổ chức phối hợp chính
    # Tìm hàng chứa "6. TỔ CHỨC PHỐI HỢP CHÍNH"
    r_org_header = -1
    for r_i, r in enumerate(t0.rows):
        if "6. TỔ CHỨC PHỐI HỢP CHÍNH" in r.cells[0].text:
            r_org_header = r_i
            break
    if r_org_header != -1 and r_org_header + 1 < len(t0.rows):
        # r_org_header + 1 là hàng tiêu đề cột (Tên đơn vị | Nội dung... )
        # Kiểm tra xem có hàng dữ liệu bên dưới không
        r_target_idx = r_org_header + 2
        if "7. MỤC TIÊU" in t0.rows[r_target_idx].cells[0].text:
            # Chưa có hàng dữ liệu, chèn thêm 1 hàng
            new_tr_org = copy.deepcopy(t0.rows[r_org_header + 1]._tr)
            t0.rows[r_org_header + 1]._tr.addnext(new_tr_org)
            r_org_data = t0.rows[r_org_header + 2]
            c0 = r_org_data.cells[0]; c0.text = ""; add_styled_para(c0, "Ban Quản lý Đường sắt đô thị Hà Nội (MRB)", size_pt=11, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)
            c3 = r_org_data.cells[3]; c3.text = ""; add_styled_para(c3, "Hỗ trợ cung cấp số liệu trắc dọc, bình đồ và tài liệu khảo sát địa kỹ thuật đoạn ngầm S9–S12 phục vụ nghiên cứu", size_pt=11, align=WD_ALIGN_PARAGRAPH.LEFT)
            c6 = r_org_data.cells[6]; c6.text = ""; add_styled_para(c6, "Lãnh đạo Ban Quản lý", size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)
            c11 = r_org_data.cells[11]; c11.text = ""; add_styled_para(c11, "Không", size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Tìm lại hàng Mục tiêu và Nội dung nghiên cứu (do có chèn hàng)
    r_goal_idx = -1
    r_content_idx = -1
    r_prod_idx = -1
    r_addr_idx = -1
    for r_i, r in enumerate(t0.rows):
        txt = r.cells[0].text
        if "7. MỤC TIÊU" in txt: r_goal_idx = r_i
        elif "8. NỘI DUNG" in txt: r_content_idx = r_i
        elif "9. DỰ KIẾN SẢN PHẨM" in txt: r_prod_idx = r_i
        elif "9.2. Địa chỉ" in txt: r_addr_idx = r_i

    # Mục 7: Mục tiêu đề tài
    if r_goal_idx != -1:
        c_goal = t0.rows[r_goal_idx].cells[0]
        c_goal.text = ""
        add_styled_para(c_goal, "7. MỤC TIÊU ĐỀ TÀI", size_pt=12, bold=True, space_after=4)
        add_styled_para(c_goal, "7.1. Mục tiêu tổng quát:", size_pt=12, bold=True, space_after=2)
        add_styled_para(c_goal, "Nghiên cứu đánh giá định lượng độ nhạy biến dạng lún mặt đất và phân vùng ảnh hưởng nguy hại do thi công hầm khiên đào (TBM) đôi đoạn S9–S12 tuyến Metro số 3 Hà Nội trong điều kiện địa chất phức tạp có tầng bùn sét mềm dày; xây dựng công cụ số hóa tích hợp WebGIS và mô hình học máy thay thế phục vụ kiểm soát rủi ro an toàn cho các công trình móng nông lân cận.", size_pt=12, space_after=4)
        add_styled_para(c_goal, "7.2. Mục tiêu cụ thể:", size_pt=12, bold=True, space_after=2)
        add_styled_para(c_goal, "1. Thu thập, chuẩn hóa và kiểm toán minh bạch cơ sở dữ liệu địa kỹ thuật 6 lớp thạch học (GU1–GU8) và tầng bùn sét mềm dày 12.7m tại hố khoan BH12 (đoạn S11–S12) có định danh nguồn gốc rõ ràng (DOI/ISSN).", size_pt=12, space_after=2)
        add_styled_para(c_goal, "2. Xây dựng động cơ tính toán giải tích phễu lún Peck (1969), Loganathan & Poulos (1998) và siêu vị hầm đôi, kiểm chứng định luật bảo toàn thể tích phễu lún với sai số < 0.01%.", size_pt=12, space_after=2)
        add_styled_para(c_goal, "3. Thiết lập ma trận 21 kịch bản phân tích độ nhạy biến dạng lún (VL ∈ [0.5%; 2.0%]), xác định bề rộng vùng nguy hại và gradient độ dốc góc xoay cực đại.", size_pt=12, space_after=2)
        add_styled_para(c_goal, "4. Đánh giá cấp độ rủi ro hư hỏng cho 60 công trình móng nông dọc trục Kim Mã - Cát Linh - Quốc Tử Giám - Trần Hưng Đạo theo tiêu chuẩn Burland (1995); xây dựng ứng dụng WebGIS tương tác trực quan hóa không gian.", size_pt=12, space_after=2)
        add_styled_para(c_goal, "5. Công bố 01 bài báo khoa học trên Tạp chí Giao thông vận tải (thuộc danh mục HĐGSNN tính điểm tối đa 0,75 điểm); hỗ trợ công tác đào tạo đại học và sau đại học.", size_pt=12, space_after=2)

    # Mục 8: Nội dung nghiên cứu chính
    if r_content_idx != -1:
        c_cnt = t0.rows[r_content_idx].cells[0]
        c_cnt.text = ""
        add_styled_para(c_cnt, "8. NỘI DUNG NGHIÊN CỨU CHÍNH (Tóm tắt những nội dung nghiên cứu của đề tài)", size_pt=12, bold=True, space_after=4)
        add_styled_para(c_cnt, "• Nội dung 1: Thu thập tài liệu, chuẩn hóa cơ sở dữ liệu địa kỹ thuật hố khoan BH12, bình đồ tuyến ngầm S9–S12 và các thông số hình học máy khiên đào TBM EPB.", size_pt=12, space_after=2)
        add_styled_para(c_cnt, "• Nội dung 2: Xây dựng mô hình toán giải tích tính toán lún hầm đơn, hầm đôi và kiểm chứng bảo toàn thể tích phễu lún (so sánh Peck 1969 và Loganathan & Poulos 1998).", size_pt=12, space_after=2)
        add_styled_para(c_cnt, "• Nội dung 3: Phân tích độ nhạy biến dạng lún mặt đất đa kịch bản (21 kịch bản tổn thất thể tích đất VL ∈ [0.5%; 2.0%] và 3 mặt cắt địa chất kỹ thuật).", size_pt=12, space_after=2)
        add_styled_para(c_cnt, "• Nội dung 4: Đánh giá nguy cơ tổn hại kết cấu công trình lân cận theo tiêu chuẩn Burland (1995) cho 60 công trình móng nông và phát triển hệ thống bản đồ số WebGIS tương tác.", size_pt=12, space_after=2)
        add_styled_para(c_cnt, "• Nội dung 5: Đề xuất quy trình quan trắc địa kỹ thuật, ngưỡng phản ứng khẩn cấp (TARP); viết bài báo khoa học đăng trên Tạp chí Giao thông vận tải và tổng kết đề tài.", size_pt=12, space_after=2)

    # Mục 9.1: Cập nhật Lời cảm ơn với mã tài trợ chính thức
    # Tìm hàng chứa Lời cảm ơn (thường là r_prod_idx + 2)
    for r_i in range(r_prod_idx + 1, len(t0.rows)):
        cell_ack = t0.rows[r_i].cells[7] if len(t0.rows[r_i].cells) > 7 else None
        if cell_ack and "Acknowledgements" in cell_ack.text:
            cell_ack.text = ""
            add_styled_para(cell_ack, 
                "- Chủ nhiệm đề tài là tác giả đầu tiên hoặc tác giả liên hệ (theo email @utc.edu.vn và cơ quan làm việc chính là Trường ĐH GTVT).\n"
                "- Trong bài báo phải ghi nhận sự tài trợ trong mục “Lời cảm ơn” (“Acknowledgements”), theo mẫu:\n"
                "+ Bài báo viết bằng tiếng Anh: \"This research is funded by University of Transport and Communications (UTC) under grant number T2027_TMĐK_Nguyen_Hai_Ha\".\n"
                "+ Bài báo viết bằng tiếng Việt: “Nghiên cứu này được tài trợ bởi Trường Đại học Giao thông vận tải (ĐH GTVT) trong đề tài mã số T2027_TMĐK_Nguyen_Hai_Ha”.\n"
                "+ Đối với bài báo viết bằng ngôn ngữ khác: sử dụng cụm từ tương đương.",
                size_pt=11, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY
            )
            break

    # Mục 9.2: Địa chỉ có thể ứng dụng
    if r_addr_idx != -1:
        c_addr = t0.rows[r_addr_idx].cells[0]
        c_addr.text = ""
        add_styled_para(c_addr, "9.2. Địa chỉ có thể ứng dụng (ghi cụ thể):", size_pt=12, bold=True, space_after=4)
        add_styled_para(c_addr, "1. Ban Quản lý Đường sắt Đô thị Hà Nội (MRB) và các nhà thầu thi công gói thầu CP03 (Hầm và các ga ngầm) để hỗ trợ công tác dự báo sớm phễu lún, thiết lập ngưỡng hành động khẩn cấp và bảo vệ công trình lân cận.", size_pt=12, space_after=2)
        add_styled_para(c_addr, "2. Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường, Trường Đại học Giao thông vận tải phục vụ công tác giảng dạy học phần 'Công trình ngầm đô thị', 'Quan trắc địa kỹ thuật', 'Cơ học đất ứng dụng' và hướng dẫn đồ án tốt nghiệp kỹ sư, học viên cao học.", size_pt=12, space_after=2)
        add_styled_para(c_addr, "3. Các cơ quan quản lý đô thị Hà Nội (Sở Giao thông vận tải, Sở Xây dựng) và các công ty tư vấn thiết kế, kiểm định công trình ngầm trong đất yếu đô thị.", size_pt=12, space_after=2)


    # =========================================================================
    # BẢNG 1: B. NỘI DUNG CHI TIẾT
    # =========================================================================
    print("--- Hoàn thiện Bảng 1: Nội dung chi tiết ---")

    # Mục 10: TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU
    c_sec10 = t1.rows[1].cells[0]
    # Lấy lại nội dung hiện tại và bổ sung mục 10.3, 10.4, 10.5
    sec10_text = c_sec10.text
    
    # Chuẩn bị văn bản mục 10 hoàn chỉnh
    p10_3 = (
        "10.3. Liệt kê danh mục các công trình nghiên cứu có liên quan đến đề tài đã nêu trong phần tổng quan:\n"
        "1. Peck, R.B. (1969). Deep excavations and tunneling in soft ground. State of the Art Report, Proc. 7th Int. Conf. on Soil Mechanics and Foundation Engineering (ICSMFE), Mexico City, 225–290.\n"
        "2. Loganathan, N., & Poulos, H.G. (1998). Analytical prediction for tunneling-induced ground movements in clays. Journal of Geotechnical and Geoenvironmental Engineering, ASCE, 124(9), 846–856.\n"
        "3. Burland, J.B. (1995). Assessment of risk of damage to buildings due to tunnelling and excavations. Proc. 1st Int. Conf. on Earthquake Geotechnical Engineering, Tokyo, 1189–1201.\n"
        "4. Mair, R.J., Taylor, R.N., & Burland, J.B. (1996). Prediction of ground movements and assessment of risk of building damage due to bored tunnelling. Geotechnical Aspects of Underground Construction in Soft Ground, Balkema, 713–718.\n"
        "5. O’Reilly, M.P., & New, B.M. (1982). Settlements above tunnels in the United Kingdom—their magnitude and prediction. Tunnelling ’82, Institution of Mining and Metallurgy, London, 173–181.\n"
        "6. Nguyen, X.C., Bui, V.D., & Nguyen, H.H. (2024). Numerical analysis of seismic response of tunnel lining for Hanoi Pilot Light Metro Line 3. Engineering, Technology & Applied Science Research (ETASR), 14(1), 12760–12765. (DOI: 10.48084/etasr.6748)\n"
        "7. Nguyen, T.H., Kohata, Y., & Nguyen, D.Q. (2024). Geotechnical characterization and soft soil behavior for underground section of Hanoi Metro Line 3. Tạp chí Xây dựng (Bộ Xây dựng), 66(5), 112–118.\n"
        "8. Giao, P.H., Nguyen, T.H., & Hoang, V.H. (2020). Engineering geological conditions and land subsidence hazard along Hanoi Pilot Light Metro Line 3. Springer LNCE, 62, 285–292. (DOI: 10.1007/978-981-15-0802-8_35)\n"
        "9. Shin, Y.J., et al. (2020). EPB TBM tunneling in heterogeneous soft ground: A case study of Hanoi Metro Line 3. Geomechanics and Engineering, 22(3), 245–256.\n"
        "10. Nguyễn Văn Hùng và cộng sự (2020). Ảnh hưởng của việc lựa chọn mô hình đất đến kết quả dự báo lún bề mặt khi thi công đường hầm khiên đào tại Hà Nội. Tạp chí Xây dựng, 12/2020, 85–91."
    )

    p10_4 = (
        "10.4. Phân tích, đánh giá cụ thể những vấn đề KH&CN còn tồn tại, hạn chế của sản phẩm, công nghệ nghiên cứu trong nước và các yếu tố, các nội dung cần đặt ra nghiên cứu, giải quyết ở đề tài này:\n"
        "Mặc dù các nghiên cứu trước đây đã bước đầu phân tích biến dạng đất nền khi thi công hầm tại Hà Nội, song vẫn tồn tại 4 khoảng trống khoa học và hạn chế kỹ thuật lớn:\n"
        "1. Giả định tỷ lệ tổn thất thể tích đất cố định (thường áp đặt Vl = 0.5% theo mô hình tất định thụ động), chưa phản ánh được dải dao động thực tế rất lớn (Vl từ 0.5% đến 2.0%) khi TBM vận hành qua tầng bùn sét mềm hữu cơ dày 12.7m (hố khoan BH12 đoạn S11–S12) có sức chịu tải và mô-đun biến dạng rất thấp (E = 7.68 MPa, N <= 4).\n"
        "2. Thiếu sự kiểm chứng độc lập giữa mô hình bán thực nghiệm Peck (1969) và mô hình giải tích biến dạng đàn hồi Loganathan & Poulos (1998) trong điều kiện đất yếu Đệ tứ Hà Nội, chưa chứng minh chặt chẽ định luật bảo toàn thể tích phễu lún bề mặt.\n"
        "3. Chưa định lượng tương tác bất lợi của hầm đôi song song (Twin tunnels) tại cự ly tim hầm d = 13.0m, làm mở rộng phễu lún ngang và gia tăng đột biến độ lún đáy phễu cũng như gradient xoay móng công trình.\n"
        "4. Thiếu một công cụ số hóa trực quan liên kết giữa cơ học địa kỹ thuật với dữ liệu không gian WebGIS và tiêu chuẩn hư hại công trình Burland (1995) để đánh giá trực diện nguy cơ cho 60 công trình móng nông nhạy cảm dọc trục Kim Mã - Cát Linh - Quốc Tử Giám.\n"
        "Đề tài này đặt ra mục tiêu giải quyết triệt để các tồn tại trên: xây dựng động cơ giải tích minh bạch, kiểm chứng bảo toàn thể tích, phân tích độ nhạy 21 kịch bản, lượng hóa nguy cơ hư hỏng 60 công trình móng nông và phát triển hệ thống WebGIS tương tác thời gian thực."
    )

    p10_5 = (
        "10.5. Hướng phát triển tiếp theo của đề tài (nếu thành công thì có thể phát triển lên mức độ nào):\n"
        "1. Nâng cấp mô hình từ 2D giải tích lên mô hình số 3D phần tử hữu hạn phi tuyến mã nguồn mở (OpenSeesPy) kết hợp trường ngẫu nhiên địa kỹ thuật (Random Field Theory) để đánh giá độ tin cậy ngẫu nhiên toàn cục (Sobol' Global Sensitivity Analysis).\n"
        "2. Kết nối thời gian thực với dữ liệu quan trắc tự động IoT từ các mốc lún bề mặt và piezometer đo áp lực nước lỗ rỗng thực tế khi khiên TBM vận hành qua đoạn S9–S12 để tiến hành phân tích ngược (back-analysis) hiệu chỉnh hệ số phễu lún K và Vl.\n"
        "3. Tích hợp mô hình học máy thay thế (Surrogate AI) vào hệ thống điều khiển tự động của máy đào TBM nhằm hỗ trợ người vận hành điều chỉnh kịp thời áp lực gương đào Ps và áp lực ép vữa chèn khe hở đuôi khiên Pa.\n"
        "4. Mở rộng khung phương pháp nghiên cứu áp dụng cho các tuyến metro đi ngầm tiếp theo tại Hà Nội (Tuyến số 2: Nam Thăng Long - Trần Hưng Đạo) và TP. Hồ Chí Minh (Tuyến số 2 Bến Thành - Tham Lương)."
    )

    # Thay thế phần dấu ba chấm trong mục 10
    c_sec10.text = ""
    # Trích xuất phần text 10.1 và 10.2 ban đầu
    base_10_2 = (
        "10.  TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU\n"
        "10.1. Tình trạng đề tài:  [x] Mới      [ ] Kế tiếp (tiếp tục hướng nghiên cứu của chính nhóm tác giả)\n"
        "10.2. Đánh giá tổng quan tình hình nghiên cứu thuộc lĩnh vực của đề tài:\n"
        "Ngoài nước: Dự báo biến dạng đất nền và độ lún bề mặt do thi công hầm trong đô thị là bài toán kinh điển của cơ học đất và công trình ngầm thế giới. Các lý thuyết và mô hình tính toán nền tảng bao gồm:\n"
        "- Peck (1969): Đề xuất mô hình phễu lún ngang dạng phân bố chuẩn Gauss kinh điển, trong đó độ lún bề mặt S(x) tại khoảng cách x so với tim hầm được xác định qua độ lún cực đại Smax và khoảng cách điểm uốn i = K * z0 (với K là hệ số phễu lún: K = 0.25 - 0.45 đối với đất cát; K = 0.4 - 0.6 đối với đất sét pha; K = 0.6 - 0.8 đối với đất bùn sét mềm hữu cơ bão hòa nước).\n"
        "- Loganathan & Poulos (1998): Khắc phục nhược điểm thuần bán thực nghiệm của Peck, đã phát triển mô hình giải tích dựa trên lý thuyết đàn hồi của Verruijt & Booker (1996), tích hợp hàm tương quan tổn thất thể tích tương đương và xét tới bán kính hầm R, độ sâu chôn hầm z0 và hệ số Poisson nu. Phương trình cho phép xác định trường chuyển vị lún tại bề mặt đất cũng như tại các độ sâu chôn móng công trình ngầm z > 0.\n"
        "- Burland (1995), Mair, Taylor & Burland (1996): Đặt nền móng cho quy chuẩn đánh giá nguy cơ tổn hại kết cấu công trình dựa trên ba tham số biến dạng: độ lún tuyệt đối Sv, độ dốc góc xoay theta, và biến dạng kéo ngang tới hạn của khối xây. Tiêu chuẩn này phân chia mức độ hư hại công trình thành 6 cấp (từ Cấp 0: Không đáng kể đến Cấp 5: Sụp đổ kết cấu), hiện là tiêu chuẩn vàng được áp dụng trong đánh giá an toàn công trình ngầm quốc tế.\n\n"
        "Trong nước: Tại Việt Nam, các nghiên cứu về thi công TBM trong môi trường địa chất đô thị đang phát triển mạnh mẽ:\n"
        "- Shin et al. (2020): Nghiên cứu các yếu tố thiết kế khiên đào EPB cho Tuyến đường sắt đô thị số 3 Hà Nội, nhấn mạnh vai trò khống chế áp lực cân bằng đất trong tầng đất bùn sét yếu để hạn chế lún bề mặt.\n"
        "- Giao, Nguyen & Hoang (2020): Phân tích số liệu địa kỹ thuật từ 17 hố khoan khảo sát dọc theo 12.4 km Tuyến 3 Nhổn – Ga Hà Nội, phân chia địa tầng Đệ tứ khu vực thành 6 tầng cơ bản và cảnh báo nguy cơ lún cố kết dài hạn do hạ thấp mực nước ngầm tầng Pleistocen.\n"
        "- Nguyen, Bui & Nguyen (2024): Nghiên cứu tác động của tải trọng động đất lên kết cấu hầm TBM đoạn S9–S10 (Kim Mã - Cát Linh), công bố chi tiết các thông số cơ lý đại diện của 6 đơn nguyên thạch học từ GU1 đến GU8.\n"
        "- Nguyen, Kohata & Nguyen (2024): Khảo sát hố khoan thực tế BH12 trên đoạn S11–S12 (Văn Miếu - Ga Hà Nội), chỉ rõ sự xuất hiện của tầng bùn sét mềm hữu cơ dày tới 12.7m bao trùm không gian đào của khiên TBM với mô-đun biến dạng E chỉ đạt 7.68 MPa.\n"
        "- Nguyễn Văn Hùng và cs. (2020): Mô phỏng số Plaxis 2D so sánh mô hình MC và HS trên tuyến Metro số 3 Hà Nội, tuy nhiên áp đặt mất mát thể tích hình học cố định Vl = 0.5%."
    )
    add_styled_para(c_sec10, base_10_2, size_pt=12, space_after=4)
    add_styled_para(c_sec10, p10_3, size_pt=12, space_after=4)
    add_styled_para(c_sec10, p10_4, size_pt=12, space_after=4)
    add_styled_para(c_sec10, p10_5, size_pt=12, space_after=2)

    # Mục 11: TÍNH CẤP THIẾT CỦA ĐỀ TÀI
    c_sec11 = t1.rows[2].cells[0]
    c_sec11.text = ""
    add_styled_para(c_sec11, "11. TÍNH CẤP THIẾT CỦA ĐỀ TÀI", size_pt=12, bold=True, space_after=4)
    p11_body = (
        "Quá trình đô thị hóa nhanh chóng tại Thủ đô Hà Nội trong hai thập kỷ qua đã tạo ra áp lực khổng lồ lên mạng lưới hạ tầng giao thông mặt đất. Mật độ phương tiện cá nhân gia tăng đột biến dẫn đến tình trạng ùn tắc giao thông nghiêm trọng, ô nhiễm không khí và suy giảm chất lượng sống của cư dân đô thị. Trước tình hình đó, Quy hoạch giao thông vận tải Thủ đô Hà Nội đến năm 2030, tầm nhìn đến năm 2050 (Quyết định số 519/QĐ-TTg của Thủ tướng Chính phủ) đã xác định việc xây dựng hệ thống đường sắt đô thị gồm 10 tuyến xuyên tâm và vành đai là giải pháp chiến lược.\n\n"
        "Trong mạng lưới này, Tuyến đường sắt đô thị thí điểm TP. Hà Nội (Tuyến số 3: Đoạn Nhổn – Ga Hà Nội) giữ vai trò huyết mạch kết nối khu vực phát triển phía Tây với trung tâm đô thị lịch sử. Dự án có tổng chiều dài 12.4 km, trong đó đoạn đi ngầm dài khoảng 3.5 km từ Ga S9 (Kim Mã) qua S10 (Cát Linh), S11 (Văn Miếu) đến Ga S12 (Ga Hà Nội). Đoạn tuyến ngầm được thiết kế gồm hai ống hầm đơn chạy song song, thi công bằng công nghệ khiên đào cân bằng áp lực đất (EPB-TBM) với đường kính ngoài khiên D = 6.30 m, đường kính trong vỏ hoàn thiện 5.7 m, chiều dày vỏ hầm bê tông cốt thép đúc sẵn 300 mm. Khoảng cách tim hai hầm dao động từ 12 m đến 15 m (trung bình d = 13.0 m). Chiều sâu trục hầm chôn sâu dưới mặt đất dao động trong khoảng z0 = 15 m đến 18 m.\n\n"
        "Tuyến hầm đi ngầm xuyên qua các khu phố cổ và phố cũ trung tâm có mật độ dân cư và công trình xây dựng dày đặc. Phần lớn các công trình hai bên trục đường Kim Mã, Cát Linh, Quốc Tử Giám và Trần Hưng Đạo là nhà phố dạng 'nhà ống' từ 3 đến 5 tầng, móng nông (móng băng gạch, móng bè hoặc móng đơn), niên hạn xây dựng lâu năm, cùng nhiều khu tập thể cũ từ thập niên 1970–1980 và các di tích văn hóa lịch sử cấp quốc gia đặc biệt nhạy cảm với biến dạng lún không đều (như khu vực Văn Miếu - Quốc Tử Giám, di tích đền chùa cổ).\n\n"
        "Đặc biệt, về điều kiện địa chất công trình, đoạn S11–S12 (hố khoan khảo sát BH12) ghi nhận sự hiện diện của tầng bùn sét xám đen dẻo mềm đến chảy có chứa mùn thực vật dày tới 12.7 m (độ sâu từ 4.0 m đến 16.7 m) nằm ngay sát trên đỉnh hầm TBM. Lớp đất này có chỉ số SPT rất thấp (N <= 4), mô-đun biến dạng chỉ đạt 7.68 MPa và hệ số thấm nhỏ, tiềm ẩn nguy cơ mất ổn định gương đào và phát sinh phễu lún kéo dài với biên độ lớn.\n\n"
        "Do đó, việc nghiên cứu định lượng độ nhạy biến dạng lún mặt đất, kiểm chứng các mô hình giải tích cơ học (Peck, Loganathan & Poulos), đánh giá nguy cơ tổn hại cho 60 công trình móng nông theo tiêu chuẩn Burland (1995) và tích hợp hệ thống số hóa WebGIS tương tác phục vụ kiểm soát rủi ro thời gian thực là nhiệm vụ khoa học có tính cấp thiết đặc biệt cao, đáp ứng trực tiếp yêu cầu thực tiễn thi công tuyến Metro số 3 và cung cấp cơ sở khoa học tin cậy cho công tác quản lý an toàn công trình ngầm đô thị."
    )
    add_styled_para(c_sec11, p11_body, size_pt=12, space_after=2)

    # Mục 12: ĐỐI TƯỢNG, PHẠM VI NGHIÊN CỨU
    c_sec12 = t1.rows[3].cells[0]
    c_sec12.text = ""
    add_styled_para(c_sec12, "12. ĐỐI TƯỢNG, PHẠM VI NGHIÊN CỨU", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec12, "12.1. Đối tượng nghiên cứu:", size_pt=12, bold=True, space_after=2)
    p12_1 = (
        "- Hiện tượng biến dạng lún mặt đất, hình thái phễu lún ngang và sự phát triển vùng ảnh hưởng nguy hại do thi công hầm đôi bằng máy khiên đào cân bằng áp lực đất (EPB-TBM) đường kính D = 6.30 m, khoảng cách tim hầm đôi d = 13.0 m.\n"
        "- Ứng xử cơ học của đất nền trầm tích Đệ tứ Hà Nội, đặc biệt là tầng bùn sét dẻo mềm hữu cơ dày 12.7 m tại đoạn S11–S12.\n"
        "- Mức độ an toàn, độ nghiêng góc xoay móng và cấp độ nguy cơ tổn hại kết cấu của 60 công trình nhà dân, trụ sở móng nông lân cận tuyến hầm theo tiêu chuẩn Burland (1995)."
    )
    add_styled_para(c_sec12, p12_1, size_pt=12, space_after=4)

    add_styled_para(c_sec12, "12.2. Phạm vi nghiên cứu:", size_pt=12, bold=True, space_after=2)
    p12_2 = (
        "- Phạm vi không gian: Đoạn đi ngầm dài khoảng 3.5 km từ Ga S9 (Kim Mã) qua Ga S10 (Cát Linh), Ga S11 (Văn Miếu) đến Ga S12 (Ga Hà Nội) thuộc Tuyến đường sắt đô thị số 3 Hà Nội; dải đệm khảo sát công trình hai bên tim hầm trong phạm vi ±35 m.\n"
        "- Phạm vi nội dung: Tập trung vào phương pháp tính toán giải tích (Peck 1969, Loganathan & Poulos 1998), phân tích độ nhạy 21 kịch bản tổn thất thể tích đất (VL ∈ [0.5%; 2.0%]), hiệu ứng siêu vị hầm đôi, đánh giá rủi ro móng nông theo Burland (1995) và xây dựng hệ thống số hóa WebGIS tương tác. Không bao gồm mô phỏng 3D phi tuyến chi tiết cọc móng hoặc công tác thi công trực tiếp ngoài hiện trường.\n"
        "- Thời gian thực hiện: 12 tháng, từ ngày 01/01/2027 đến ngày 31/12/2027."
    )
    add_styled_para(c_sec12, p12_2, size_pt=12, space_after=2)

    # Mục 13: CÁCH TIẾP CẬN, PHƯƠNG PHÁP NGHIÊN CỨU
    c_sec13 = t1.rows[4].cells[0]
    c_sec13.text = ""
    add_styled_para(c_sec13, "13. CÁCH TIẾP CẬN, PHƯƠNG PHÁP NGHIÊN CỨU", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec13, "13.1. Cách tiếp cận:", size_pt=12, bold=True, space_after=2)
    p13_1 = (
        "Đề tài lựa chọn cách tiếp cận đa chiều, tích hợp chặt chẽ giữa cơ học địa kỹ thuật thực chứng và công nghệ địa không gian số:\n"
        "1. Tiếp cận thực chứng và minh bạch dữ liệu (Evidence-based & Data-driven): Dựa trên dữ liệu địa chất hố khoan thực tế đã được công bố chính thống (BH12, S9–S10), tuân thủ nguyên tắc kiểm toán nguồn gốc nghiêm ngặt, phân định rõ ràng giữa số liệu khảo sát hiện trường và các tham số giả định mô hình.\n"
        "2. Tiếp cận cơ học giải tích kinh điển: Sử dụng các mô hình giải tích đã được chuẩn hóa quốc tế (Peck 1969, Loganathan & Poulos 1998), đảm bảo tính tường minh của các công thức toán học và kiểm chứng bảo toàn thể tích phễu lún.\n"
        "3. Tiếp cận phân tích độ nhạy đa kịch bản (Scenario-based sensitivity approach): Thay vì sử dụng một giá trị tất định duy nhất, đề tài thiết lập ma trận 21 kịch bản bao trùm toàn bộ dải biến thiên thực tế của tổn thất thể tích đất VL từ 0.5% đến 2.0%.\n"
        "4. Tiếp cận số hóa địa không gian (GIS-integrated): Chuyển hóa các kết quả tính toán giải tích thành lớp thông tin không gian trực quan trên nền bản đồ số WebGIS, liên kết trực tiếp với tọa độ và hiện trạng của 60 công trình móng nông nhạy cảm."
    )
    add_styled_para(c_sec13, p13_1, size_pt=12, space_after=4)

    add_styled_para(c_sec13, "13.2. Phương pháp nghiên cứu:", size_pt=12, bold=True, space_after=2)
    p13_2 = (
        "1. Phương pháp thu thập, chuẩn hóa và kiểm toán dữ liệu: Khai thác tài liệu khảo sát địa chất công trình, bình đồ trắc dọc tuyến ngầm S9–S12; quy đổi hệ đơn vị SI chuẩn; xây dựng ma trận truy xuất nguồn gốc (Traceability Matrix).\n"
        "2. Phương pháp mô hình hóa giải tích: Lập trình thuật toán tính toán phễu lún Gauss (Peck 1969) và mô hình giải tích bán đàn hồi (Loganathan & Poulos 1998) bằng Python và bảng tính Excel chuyên nghiệp; giải bài toán siêu vị hầm đôi song song (Twin Tunnel Superposition).\n"
        "3. Phương pháp phân tích độ nhạy (Sensitivity Analysis): Khảo sát sự biến thiên của độ lún cực đại Smax, bề rộng phễu lún i, độ dốc xoay cực đại thetamax và bề rộng vùng lún nguy hại (S > 10 mm) theo tỷ lệ tổn thất thể tích VL và chiều sâu chôn hầm z0.\n"
        "4. Phương pháp đánh giá rủi ro kết cấu: Vận dụng tiêu chuẩn Burland (1995) và Mair et al. (1996) để lượng hóa độ lún tuyệt đối Sv và độ nghiêng xoay theta thành 5 cấp độ hư hại công trình.\n"
        "5. Phương pháp công nghệ WebGIS và Học máy (AI Surrogate): Phát triển ứng dụng WebGIS Leaflet.js tương tác trực tiếp trên trình duyệt; xây dựng mạng nơ-ron truyền thẳng đa tầng (MLP) thuần NumPy dự báo lún tức thời không độ trễ (<0.1 ms)."
    )
    add_styled_para(c_sec13, p13_2, size_pt=12, space_after=2)

    # Mục 14: NỘI DUNG CHI TIẾT VÀ TIẾN ĐỘ THỰC HIỆN
    c_sec14_1 = t1.rows[5].cells[0]
    c_sec14_1.text = ""
    add_styled_para(c_sec14_1, "14. NỘI DUNG CHI TIẾT VÀ TIẾN ĐỘ THỰC HIỆN", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec14_1, "14.1. Nội dung nghiên cứu chi tiết:", size_pt=12, bold=True, space_after=2)
    p14_1 = (
        "• Nội dung 1: Thu thập, chuẩn hóa và kiểm toán cơ sở dữ liệu địa kỹ thuật đoạn S9–S12 Metro Tuyến 3 Hà Nội.\n"
        "  - Thu thập tài liệu địa tầng hố khoan BH12 (S11–S12), mặt cắt S9–S10 và 17 hố khoan toàn tuyến.\n"
        "  - Chuẩn hóa hệ thống tham số cơ lý đất nền (E, c', phi', gamma, N_SPT), hình học hầm (D = 6.3m, d = 13m, z0 = 15-18m).\n"
        "  - Xây dựng ma trận truy xuất nguồn gốc học thuật (Evidence Traceability Matrix).\n\n"
        "• Nội dung 2: Xây dựng mô hình toán giải tích tính toán lún hầm đơn, hầm đôi và kiểm chứng bảo toàn thể tích.\n"
        "  - Thiết lập công thức phễu lún ngang Peck (1969) và mô hình bán giải tích Loganathan & Poulos (1998).\n"
        "  - Chứng minh và kiểm chứng số học định luật bảo toàn thể tích phễu lún (Vs = Vloss) với sai số < 0.01%.\n"
        "  - Mô hình hóa nguyên lý siêu vị hầm đôi song song và xác định độ dốc xoay móng theta(x).\n\n"
        "• Nội dung 3: Phân tích độ nhạy biến dạng lún mặt đất đa kịch bản (21 kịch bản tổn thất thể tích và địa tầng).\n"
        "  - Tính toán ma trận 21 kịch bản: 3 mặt cắt kỹ thuật (S9–S10, S10–S11, S11–S12) x 7 mức tổn thất thể tích (VL = 0.5% đến 2.0%).\n"
        "  - Phân tích quy luật biến thiên của Smax, i, thetamax; xác định bán kính phễu lún nguy hại (S > 10 mm và S > 20 mm).\n"
        "  - Đánh giá đặc biệt đối với đoạn qua tầng bùn sét mềm hữu cơ dày 12.7m tại S11–S12.\n\n"
        "• Nội dung 4: Đánh giá nguy cơ tổn hại cho 60 công trình móng nông và phát triển hệ thống WebGIS tương tác.\n"
        "  - Số hóa cơ sở dữ liệu địa không gian cho 60 công trình nhà dân (2-5 tầng) dọc Kim Mã - Cát Linh - Quốc Tử Giám.\n"
        "  - Phân loại cấp độ hư hỏng theo tiêu chuẩn Burland (1995) tại VL = 1.0% và VL = 2.0%; xác định danh mục công trình ưu tiên cao.\n"
        "  - Phát triển ứng dụng WebGIS Leaflet.js tương tác trực tiếp với thanh trượt VL và biểu đồ phễu lún Chart.js.\n\n"
        "• Nội dung 5: Đề xuất quy trình quan trắc địa kỹ thuật, viết bài báo khoa học và tổng kết nghiệm thu đề tài.\n"
        "  - Thiết lập quy trình phản ứng khẩn cấp TARP (3 cấp báo động) và giải pháp kiểm soát áp lực khiên TBM.\n"
        "  - Viết và hoàn thiện 01 bài báo khoa học đăng trên Tạp chí Giao thông vận tải (HĐGSNN tính điểm tối đa 0,75 điểm).\n"
        "  - Tổng hợp bộ cơ sở dữ liệu Excel chuyên nghiệp và báo cáo tổng kết đề tài."
    )
    add_styled_para(c_sec14_1, p14_1, size_pt=12, space_after=4)
    add_styled_para(c_sec14_1, "14.2. Tiến độ thực hiện:", size_pt=12, bold=True, space_after=2)

    # Cập nhật Bảng Tiến độ thực hiện (Row 6 là tiêu đề cột, Row 7 là dữ liệu)
    # Ta định nghĩa 5 công việc chi tiết
    tasks = [
        ("1", "Nội dung 1: Thu thập, chuẩn hóa và kiểm toán cơ sở dữ liệu địa kỹ thuật đoạn S9–S12 Metro Tuyến 3 Hà Nội.", "Bộ CSDL địa kỹ thuật & Ma trận truy xuất nguồn gốc (Excel).", "01/2027 – 03/2027", "ThS. Nguyễn Hải Hà\nKS. Trần Văn Long"),
        ("2", "Nội dung 2: Xây dựng mô hình toán giải tích tính toán lún hầm đơn, hầm đôi và kiểm chứng bảo toàn thể tích.", "Mô hình giải tích Peck & Loganathan-Poulos; Báo cáo nghiệm thu toán học.", "04/2027 – 06/2027", "ThS. Nguyễn Hải Hà\nThS. Lê Anh Đức"),
        ("3", "Nội dung 3: Phân tích độ nhạy biến dạng lún mặt đất đa kịch bản (21 kịch bản tổn thất thể tích và địa tầng).", "Bảng tổng hợp 21 kịch bản độ nhạy và tập hợp đường cong quan hệ.", "07/2027 – 08/2027", "ThS. Nguyễn Hải Hà\nThS. Lê Anh Đức"),
        ("4", "Nội dung 4: Đánh giá nguy cơ tổn hại cho 60 công trình móng nông và phát triển hệ thống WebGIS tương tác.", "Bảng phân cấp rủi ro Burland 60 công trình & Ứng dụng WebGIS Leaflet.", "09/2027 – 10/2027", "ThS. Nguyễn Hải Hà\nKS. Trần Văn Long"),
        ("5", "Nội dung 5: Đề xuất quy trình quan trắc địa kỹ thuật, viết bài báo khoa học và nghiệm thu đề tài.", "01 Bài báo Tạp chí Giao thông vận tải & Báo cáo tổng kết đề tài.", "11/2027 – 12/2027", "Tập thể nhóm NCKH")
    ]

    # Kiểm tra xem Table 1 có bao nhiêu hàng tác vụ
    # Row 6 là header: STT | Các nội dung... | Sản phẩm | Thời gian | Người thực hiện
    # Đảm bảo có đủ 5 hàng bằng cách nhân bản Row 7
    # Đầu tiên kiểm tra xem Row 7 có gì
    r7 = t1.rows[7]
    # Ta cần thêm 4 hàng nữa sau Row 7 nếu chưa có
    # Kiểm tra số lượng hàng trong t1
    curr_t1_rows = len(t1.rows)
    print(f"Số hàng hiện tại của Table 1: {curr_t1_rows}")
    
    # Tìm hàng chứa Mục 15
    r_sec15_idx = -1
    for r_i, r in enumerate(t1.rows):
        if "15. NỘI DUNG NGHIÊN CỨU ỨNG DỤNG" in r.cells[0].text:
            r_sec15_idx = r_i
            break
            
    num_schedule_rows = r_sec15_idx - 7
    print(f"Số hàng lịch trình hiện tại: {num_schedule_rows}")
    while num_schedule_rows < 5:
        new_tr = copy.deepcopy(t1.rows[7]._tr)
        t1.rows[6 + num_schedule_rows]._tr.addnext(new_tr)
        num_schedule_rows += 1

    # Điền dữ liệu cho 5 hàng tiến độ
    for idx, (stt, task_name, prod, sched, person) in enumerate(tasks):
        row = t1.rows[7 + idx]
        # Col 0: STT
        c0 = row.cells[0]; c0.text = ""; add_styled_para(c0, stt, size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)
        # Col 1: Nội dung
        c1 = row.cells[1]; c1.text = ""; add_styled_para(c1, task_name, size_pt=11, align=WD_ALIGN_PARAGRAPH.LEFT)
        # Col 2: Sản phẩm
        c2 = row.cells[2]; c2.text = ""; add_styled_para(c2, prod, size_pt=11, align=WD_ALIGN_PARAGRAPH.LEFT)
        # Col 3: Thời gian
        c3 = row.cells[3]; c3.text = ""; add_styled_para(c3, sched, size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)
        # Col 4: Người thực hiện
        c4 = row.cells[4]; c4.text = ""; add_styled_para(c4, person, size_pt=11, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Tìm lại các mục 15, 16, 17 sau khi chèn hàng
    r15_idx = -1; r16_idx = -1; r17_idx = -1
    for r_i, r in enumerate(t1.rows):
        txt = r.cells[0].text
        if "15. NỘI DUNG NGHIÊN CỨU ỨNG DỤNG" in txt: r15_idx = r_i
        elif "16. HIỆU QUẢ" in txt: r16_idx = r_i
        elif "17. PHƯƠNG THỨC CHUYỂN GIAO" in txt: r17_idx = r_i

    # Mục 15: NỘI DUNG NGHIÊN CỨU ỨNG DỤNG VÀ TRIỂN KHAI THỰC NGHIỆM
    if r15_idx != -1:
        c15 = t1.rows[r15_idx].cells[0]
        c15.text = ""
        add_styled_para(c15, "15. NỘI DUNG NGHIÊN CỨU ỨNG DỤNG VÀ TRIỂN KHAI THỰC NGHIỆM (nếu có)", size_pt=12, bold=True, space_after=4)
        p15_body = (
            "1. Nội dung ứng dụng phục vụ điều khiển thi công hầm TBM thực tế:\n"
            "- Ứng dụng kết quả phân tích độ nhạy để thiết lập ma trận kế hoạch phản ứng khẩn cấp (Trigger Action Response Plan - TARP) gồm 3 cấp độ: Cảnh báo xanh (Độ lún Sv < 10 mm - Thi công bình thường), Báo động vàng (10 <= Sv < 20 mm - Tăng cường tần suất đo đạc, kiểm tra áp lực gương Ps), và Khẩn cấp đỏ (Sv >= 20 mm - Tạm dừng khiên đào, tăng áp lực cân bằng gương và phụt vữa thứ cấp bù lún).\n"
            "- Đề xuất quy trình kiểm soát thông số vận hành máy EPB khi đi qua tầng bùn sét mềm hữu cơ dày 12.7m (đoạn S11–S12): khống chế áp lực giữ gương Ps cân bằng áp lực đất tĩnh và áp lực nước lỗ rỗng; kiểm soát nghiêm ngặt thể tích đất đào ra khỏi buồng ép qua vít tải nhằm giữ tỷ lệ tổn thất thể tích VL <= 1.0%.\n\n"
            "2. Biện pháp kỹ thuật bảo vệ 60 công trình móng nông lân cận:\n"
            "- Đối với 18 công trình có nguy cơ rơi vào Cấp 3 (Hư hỏng vừa) khi VL tăng cao: đề xuất khảo sát hiện trạng chi tiết móng trước thi công (Pre-construction Survey), lắp đặt lăng kính quan trắc tự động trên mặt tiền nhà và chuẩn bị sẵn phương án phụt vữa gia cố nền (Compaction Grouting) nếu độ nghiêng vượt ngưỡng 1/150.\n\n"
            "3. Dự kiến rủi ro và giải pháp khắc phục:\n"
            "- Rủi ro thiếu hụt số liệu đo đạc thời gian thực do tiến độ TBM thực tế: Khắc phục bằng cách sử dụng bộ dữ liệu kiểm định địa chất có sẵn từ các công bố quốc tế uy tín (TCXD 2024, ETASR 2024) và mô phỏng dải kịch bản rộng để đảm bảo tính sẵn sàng cao khi hầm chính thức vận hành."
        )
        add_styled_para(c15, p15_body, size_pt=12, space_after=2)

    # Mục 16: HIỆU QUẢ (giáo dục và đào tạo, kinh tế - xã hội)
    if r16_idx != -1:
        c16 = t1.rows[r16_idx].cells[0]
        c16.text = ""
        add_styled_para(c16, "16. HIỆU QUẢ (giáo dục và đào tạo, kinh tế - xã hội)", size_pt=12, bold=True, space_after=4)
        p16_body = (
            "1. Hiệu quả đối với sự nghiệp giáo dục và đào tạo của Nhà trường:\n"
            "- Đề tài cung cấp hệ thống học liệu thực tế chất lượng cao, gắn liền trực tiếp với dự án hạ tầng trọng điểm quốc gia (Metro Tuyến 3 Hà Nội), phục vụ trực tiếp cho công tác giảng dạy các học phần chuyên ngành: 'Công trình ngầm đô thị', 'Cơ học đất ứng dụng', 'Quan trắc địa kỹ thuật' và 'Ứng dụng GIS trong xây dựng công trình' tại Khoa Công trình và Môi trường.\n"
            "- Hỗ trợ đào tạo trực tiếp cho sinh viên thực hiện 02 đồ án tốt nghiệp kỹ sư chuyên ngành Xây dựng Công trình ngầm và Mỏ / Địa kỹ thuật; tạo tiền đề cho học viên cao học và nghiên cứu sinh tiếp tục mở rộng nghiên cứu chuyên sâu.\n\n"
            "2. Hiệu quả về mặt khoa học và công nghệ:\n"
            "- Khẳng định năng lực nghiên cứu độc lập, làm chủ các công cụ giải tích hiện đại và công nghệ địa không gian số WebGIS của đội ngũ giảng viên trẻ Trường Đại học Giao thông vận tải.\n"
            "- Công bố 01 bài báo khoa học chất lượng trên Tạp chí Giao thông vận tải thuộc danh mục được Hội đồng Giáo sư Nhà nước tính điểm công trình tối đa 0,75 điểm.\n\n"
            "3. Hiệu quả kinh tế - xã hội:\n"
            "- Cung cấp công cụ dự báo sớm và cơ sở khoa học tin cậy giúp Chủ đầu tư (MRB), các nhà thầu thi công và các đơn vị tư vấn chủ động nhận diện nguy cơ lún nứt, từ đó tối ưu hóa công tác quan trắc và có biện pháp kỹ thuật phòng ngừa kịp thời.\n"
            "- Giảm thiểu tối đa nguy cơ hư hỏng nhà dân và các di tích văn hóa lịch sử dọc tuyến Kim Mã - Cát Linh - Quốc Tử Giám, tránh các tranh chấp pháp lý và chi phí bồi thường sự cố nứt lún công trình đô thị, góp phần bảo đảm an sinh xã hội và tiến độ thông xe của dự án Metro Hà Nội."
        )
        add_styled_para(c16, p16_body, size_pt=12, space_after=2)

    # Mục 17: PHƯƠNG THỨC CHUYỂN GIAO KẾT QUẢ NGHIÊN CỨU VÀ ĐỊA CHỈ ỨNG DỤNG
    if r17_idx != -1:
        c17 = t1.rows[r17_idx].cells[0]
        c17.text = ""
        add_styled_para(c17, "17. PHƯƠNG THỨC CHUYỂN GIAO KẾT QUẢ NGHIÊN CỨU VÀ ĐỊA CHỈ ỨNG DỤNG (nếu có)", size_pt=12, bold=True, space_after=4)
        p17_body = (
            "1. Phương thức chuyển giao kết quả nghiên cứu:\n"
            "- Chuyển giao dạng tài liệu khoa học: Báo cáo tổng kết đề tài hoàn chỉnh kèm phụ lục tính toán chi tiết và 01 bài báo khoa học được công bố.\n"
            "- Chuyển giao bộ công cụ số hóa: Bộ 4 file Excel chuyên nghiệp với 100% công thức động và mã nguồn ứng dụng WebGIS tương tác trên nền Leaflet.js để các kỹ sư có thể tự tra cứu, cập nhật kịch bản thi công.\n"
            "- Tổ chức báo cáo chuyên đề và tập huấn chuyên môn tại Bộ môn Địa kỹ thuật và Không gian ngầm.\n\n"
            "2. Địa chỉ tiếp nhận chuyển giao ứng dụng:\n"
            "- Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường, Trường Đại học Giao thông vận tải: Lưu trữ trong cơ sở dữ liệu học thuật của Bộ môn để phục vụ nghiên cứu và đào tạo.\n"
            "- Ban Quản lý Đường sắt Đô thị Hà Nội (MRB) và các nhà thầu thi công gói thầu CP03 Metro Hà Nội: Sử dụng làm tài liệu tham khảo trong công tác quan trắc và kiểm soát rủi ro địa kỹ thuật công trình ngầm."
        )
        add_styled_para(c17, p17_body, size_pt=12, space_after=2)


    # =========================================================================
    # BẢNG 2: C. QUẢN LÝ & PHÂN BỔ TÀI CHÍNH
    # =========================================================================
    print("--- Hoàn thiện Bảng 2: Phân bổ tài chính & Sửa lỗi số học ---")
    
    # Row 6: Sửa lỗi typo 22.770.0000 -> 22.770.000
    r6 = t2.rows[6]
    c_6_tot = r6.cells[3]
    c_6_ns = r6.cells[4]
    c_6_tot.text = ""; add_styled_para(c_6_tot, "22.770.000", size_pt=11, align=WD_ALIGN_PARAGRAPH.RIGHT)
    c_6_ns.text = ""; add_styled_para(c_6_ns, "22.770.000", size_pt=11, align=WD_ALIGN_PARAGRAPH.RIGHT)

    # Kiểm tra các hàng khác trong Table 2 để đảm bảo định dạng số sạch sẽ
    # Row 11: Quản lý chung (5%): 1.250.000
    r11 = t2.rows[11]
    c_11_tot = r11.cells[3]; c_11_tot.text = ""; add_styled_para(c_11_tot, "1.250.000", size_pt=11, align=WD_ALIGN_PARAGRAPH.RIGHT)
    c_11_ns = r11.cells[4]; c_11_ns.text = ""; add_styled_para(c_11_ns, "1.250.000", size_pt=11, align=WD_ALIGN_PARAGRAPH.RIGHT)

    # Row 17: Chi văn phòng phẩm (Mục 5.5): 980.000
    r17 = t2.rows[17]
    c_17_tot = r17.cells[3]; c_17_tot.text = ""; add_styled_para(c_17_tot, "980.000", size_pt=11, align=WD_ALIGN_PARAGRAPH.RIGHT)
    c_17_ns = r17.cells[4]; c_17_ns.text = ""; add_styled_para(c_17_ns, "980.000", size_pt=11, align=WD_ALIGN_PARAGRAPH.RIGHT)

    # Row 20: Tổng cộng: 25.000.000
    r20 = t2.rows[20]
    c_20_tot = r20.cells[3]; c_20_tot.text = ""; add_styled_para(c_20_tot, "25.000.000", size_pt=11, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT)
    c_20_ns = r20.cells[4]; c_20_ns.text = ""; add_styled_para(c_20_ns, "25.000.000", size_pt=11, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT)

    # Row 21: Chữ ký Chủ nhiệm đề tài
    r21 = t2.rows[21]
    c_sig = r21.cells[0]
    c_sig.text = ""
    add_styled_para(c_sig, "Hà Nội, ngày 15 tháng 10 năm 2026\nCHỦ NHIỆM ĐỀ TÀI\n(Ký và ghi rõ họ tên)\n\n\n\nThS. Nguyễn Hải Hà", 
                    size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4)

    # =========================================================================
    # LƯU FILE HOÀN THIỆN
    # =========================================================================
    doc.save(str(TARGET_DOCX))
    print(f"3. Đã lưu thành công tài liệu hoàn thiện tại: {TARGET_DOCX}")


if __name__ == "__main__":
    audit_and_complete()
