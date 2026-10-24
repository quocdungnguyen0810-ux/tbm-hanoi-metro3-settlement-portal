# -*- coding: utf-8 -*-
r"""
Fill out the official research proposal form:
'D:\OneDrive\NCKH\NCKH 2027\T2027\Thuyết minh đề tài undefined.docx'
According to UTC regulations, 12 months (01/01/2027 - 31/12/2027),
Product: 01 paper in HĐGSNN scored journal (Tạp chí Giao thông vận tải, max 0.75 pts).
"""
import os
import sys
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

sys.stdout.reconfigure(encoding='utf-8')

DOCX_TEMPLATE = r"D:\OneDrive\NCKH\NCKH 2027\T2027\Thuyết minh đề tài undefined_BACKUP.docx"
DOCX_OUTPUT = r"D:\OneDrive\NCKH\NCKH 2027\T2027\Thuyết minh đề tài undefined.docx"

def set_cell_font(cell, font_name="Times New Roman", size_pt=12, bold=False, italic=False, color=None):
    for p in cell.paragraphs:
        for run in p.runs:
            run.font.name = font_name
            run.font.size = Pt(size_pt)
            run.bold = bold
            run.italic = italic
            if color:
                run.font.color.rgb = color

def add_styled_para(cell, text, font_name="Times New Roman", size_pt=12, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4, space_before=0, line_spacing=1.15):
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
    # remove extra paragraphs if any
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

def fill_proposal():
    doc = docx.Document(DOCX_TEMPLATE)
    t0 = doc.tables[0]
    t1 = doc.tables[1]
    t2 = doc.tables[2]

    # =========================================================================
    # TABLE 0: A. THÔNG TIN CHUNG
    # =========================================================================
    print("Populating Table 0: General Information...")

    # Row 1: Tên đề tài & Mã số
    # Cell 0 has "1. TÊN ĐỀ TÀI\nỨng dụng công nghệ radar giao thoa (InSAR)..." - already good, let's refine
    c_title = t0.rows[1].cells[0]
    c_title.text = ""
    p = add_styled_para(c_title, "1. TÊN ĐỀ TÀI", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=2)
    p = add_styled_para(c_title, "Ứng dụng công nghệ radar giao thoa (InSAR) từ dữ liệu vệ tinh Sentinel-1 giám sát biến dạng bề mặt đất dọc hành lang tuyến Metro số 1 Bến Thành – Suối Tiên.", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=2)
    
    # Cell 1: Mã số do Khoa cấp
    c_code = t0.rows[1].cells[9]
    c_code.text = ""
    add_styled_para(c_code, "2. MÃ SỐ (do Khoa cấp)\n", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Row 2: Thời gian thực hiện
    c_time = t0.rows[2].cells[0]
    c_time.text = ""
    add_styled_para(c_time, "3. THỜI GIAN THỰC HIỆN: 12 tháng\nTừ ngày 01/01/2027 đến ngày 31/12/2027", size_pt=12, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Row 3: Chủ nhiệm đề tài
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

    # Row 4: Header thành viên
    # Row 5: Column headers: TT | Họ và tên | Đơn vị công tác... | Vai trò | Chữ ký
    # We will format Row 5 and we can add member info.
    # Note: Table 0 has 12 columns under the hood due to merges.
    # Let's inspect cells in Row 5:
    # C0: TT, C1: Họ và tên, C3: Đơn vị công tác, C8: Vai trò, C10: Chữ ký

    # Row 8: Mục tiêu đề tài (currently has 'sfáđà')
    c_obj = t0.rows[8].cells[0]
    c_obj.text = ""
    add_styled_para(c_obj, "7. MỤC TIÊU ĐỀ TÀI", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_obj, "7.1. Mục tiêu tổng quát:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_obj, "Nghiên cứu ứng dụng chuỗi công nghệ viễn thám radar giao thoa (InSAR) khai thác chuỗi dữ liệu vệ tinh Sentinel-1 đa thời gian nhằm xây dựng bản đồ số và định lượng trường biến dạng lún bề mặt đất dọc hành lang 500m hai bên tuyến Metro số 1 Bến Thành – Suối Tiên giai đoạn 2019–2026; tích hợp đối chuẩn với số liệu trắc địa thực địa hầm TBM và phân tích tương quan cơ học với điều kiện địa tầng, cung cấp công cụ số phục vụ quản lý và cảnh báo sớm rủi ro an toàn kết cấu tuyến metro trong giai đoạn vận hành thương mại.", size_pt=12, space_after=4)
    add_styled_para(c_obj, "7.2. Mục tiêu cụ thể:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_obj, "1. Thu thập, chuẩn hóa và xây dựng cơ sở dữ liệu chuỗi ảnh radar khẩu độ tổng hợp Sentinel-1 IW SLC (băng C) đa quỹ đạo (Ascending và Descending) giai đoạn 2019–2026 dọc hành lang 19.7 km tuyến Metro số 1 TP.HCM.", size_pt=12, space_after=2)
    add_styled_para(c_obj, "2. Làm chủ quy trình công nghệ xử lý chuỗi thời gian InSAR (kết hợp SNAP, SNAPHU và MintPy); thực hiện phân rã vector chuyển vị 2 chiều (phương thẳng đứng dV và phương ngang Đông–Tây dEW).", size_pt=12, space_after=2)
    add_styled_para(c_obj, "3. Xác định tốc độ chuyển dịch trung bình (mm/năm) và trích xuất chuỗi thời gian lún tích lũy tại các khu vực trọng điểm: đoạn hầm đôi TBM ngầm (Ba Son – Bến Thành), đoạn cầu cạn vượt vùng đất yếu Rạch Văn Thánh và các nhà ga.", size_pt=12, space_after=2)
    add_styled_para(c_obj, "4. Đối chuẩn khoa học kết quả InSAR với chuỗi số liệu quan trắc lún mốc sâu thực địa (Luận án TS. Nguyễn Thạch Bích, 2022); kiểm chứng mức độ tương thích với mô hình phễu lún Peck (1969) và đánh giá rủi ro theo tiêu chuẩn Burland (1995).", size_pt=12, space_after=2)
    add_styled_para(c_obj, "5. Đăng ký và công bố 01 bài báo khoa học trên Tạp chí Giao thông vận tải thuộc danh mục được HĐGSNN tính điểm tối đa 0,75 điểm; hỗ trợ công tác đào tạo sinh viên NCKH.", size_pt=12, space_after=2)

    # Row 9: Nội dung nghiên cứu chính (currently has 'ádfdf')
    c_content = t0.rows[9].cells[0]
    c_content.text = ""
    add_styled_para(c_content, "8. NỘI DUNG NGHIÊN CỨU CHÍNH (Tóm tắt những nội dung nghiên cứu của đề tài)", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_content, "• Nội dung 1: Thu thập tài liệu, chuẩn hóa cơ sở dữ liệu viễn thám radar Sentinel-1, mô hình số độ cao DEM và dữ liệu địa kỹ thuật, bình đồ tuyến Metro số 1 Bến Thành – Suối Tiên.", size_pt=12, space_after=2)
    add_styled_para(c_content, "• Nội dung 2: Nghiên cứu quy trình công nghệ xử lý viễn thám radar giao thoa chuỗi thời gian InSAR đa quỹ đạo (Ascending/Descending), giải pha và phân rã trường biến dạng thẳng đứng.", size_pt=12, space_after=2)
    add_styled_para(c_content, "• Nội dung 3: Đối chuẩn kết quả viễn thám InSAR với chuỗi số liệu quan trắc lún thực tế hầm TBM và phân tích tương quan cơ học với các yếu tố thi công ngầm, địa tầng đất yếu.", size_pt=12, space_after=2)
    add_styled_para(c_content, "• Nội dung 4: Phân tích vùng ảnh hưởng, đánh giá nguy cơ tổn hại kết cấu công trình lân cận theo tiêu chuẩn Burland (1995) và xây dựng bản đồ chuyên đề biến dạng trên nền GIS.", size_pt=12, space_after=2)
    add_styled_para(c_content, "• Nội dung 5: Tổng hợp kết quả, xây dựng báo cáo tổng kết đề tài và công bố bài báo khoa học trên Tạp chí Giao thông vận tải (thuộc danh mục tính điểm của HĐGSNN).", size_pt=12, space_after=2)

    # Row 13: Địa chỉ có thể ứng dụng (currently has 'ádfdf')
    c_addr = t0.rows[13].cells[0]
    c_addr.text = ""
    add_styled_para(c_addr, "9.2. Địa chỉ có thể ứng dụng (ghi cụ thể):", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_addr, "1. Ban Quản lý Đường sắt Đô thị TP. Hồ Chí Minh (MAUR) và Công ty TNHH MTV Đường sắt Đô thị số 1 TP.HCM (HURC1) để hỗ trợ công tác theo dõi, bảo trì kết cấu hạ tầng đường sắt và phát hiện sớm các phễu lún bất thường trong quá trình khai thác thương mại.", size_pt=12, space_after=2)
    add_styled_para(c_addr, "2. Sở Giao thông vận tải TP.HCM, Sở Xây dựng TP.HCM phục vụ công tác quản lý đô thị, cấp phép xây dựng các công trình tiếp giáp hành lang bảo vệ tuyến metro.", size_pt=12, space_after=2)
    add_styled_para(c_addr, "3. Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường, Trường Đại học Giao thông vận tải phục vụ công tác giảng dạy học phần 'Công trình ngầm đô thị', 'Quan trắc địa kỹ thuật', 'Cơ học đất ứng dụng' cho sinh viên đại học và học viên cao học.", size_pt=12, space_after=2)

    # =========================================================================
    # TABLE 1: B. NỘI DUNG CHI TIẾT
    # =========================================================================
    print("Populating Table 1: Detailed Research Content...")

    # Row 1: Mục 10. TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU
    c_sec10 = t1.rows[1].cells[0]
    c_sec10.text = ""
    add_styled_para(c_sec10, "10. TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec10, "10.1. Tình trạng đề tài:   ☐ Mới     ☒ Kế tiếp (tiếp tục hướng nghiên cứu của chính nhóm tác giả)", size_pt=12, bold=True, space_after=4)
    
    add_styled_para(c_sec10, "10.2. Đánh giá tổng quan tình hình nghiên cứu thuộc lĩnh vực của đề tài:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec10, "a) Tình hình nghiên cứu ngoài nước:", size_pt=12, bold=True, italic=True, space_after=2)
    add_styled_para(c_sec10, "Công nghệ radar giao thoa tán xạ ổn định (Persistent Scatterer InSAR - PS-InSAR) do Ferretti và cộng sự (2000, 2001) khởi xướng và phương pháp đường đáy nhỏ (Small Baseline Subset - SBAS-InSAR) do Berardino và cộng sự (2002) phát triển đã tạo nên bước đột phá trong quan trắc biến dạng mặt đất. Kỹ thuật này khắc phục triệt để hiện tượng mất tương quan hình học và suy giảm chất lượng pha do khí quyển, cho phép đạt độ chính xác đo chuyển vị ở mức milimet/năm.", size_pt=12, space_after=2)
    add_styled_para(c_sec10, "Trong lĩnh vực công trình ngầm và metro đô thị, công nghệ InSAR đã được áp dụng rộng rãi tại các đô thị phát triển: Chen và cộng sự (2012, 2021) đã sử dụng TerraSAR-X và Sentinel-1 giám sát mạng lưới metro Thượng Hải, phát hiện mối liên hệ chặt chẽ giữa lún bề mặt với hạ mực nước ngầm và thi công hầm TBM; Standing & Selemetas (2013) tại dự án London Crossrail đã kết hợp dữ liệu InSAR với mô hình phễu lún Gaussian của Peck (1969) để dự báo lún hầm đôi; Yunjun và cộng sự (2019) đã phát triển mã nguồn mở MintPy (Multitemporal InSAR in Python) cho phép giải pha đa chiều và lọc nhiễu khí quyển tự động với độ tin cậy rất cao.", size_pt=12, space_after=4)

    add_styled_para(c_sec10, "b) Tình hình nghiên cứu trong nước:", size_pt=12, bold=True, italic=True, space_after=2)
    add_styled_para(c_sec10, "Tại Việt Nam, các nghiên cứu InSAR đã bước đầu được triển khai để đánh giá sụt lún diện rộng tại đồng bằng sông Cửu Long và TP. Hồ Chí Minh (Phùng Đại Bình, 2018; Lê Văn Nam, 2020; Trần Tuấn Anh, 2021). Tuy nhiên, hầu hết các nghiên cứu này dừng lại ở quy mô vùng địa lý rộng lớn, sử dụng độ phân giải thô và chưa đi sâu vào hành lang công trình hạ tầng giao thông tuyến tính hẹp như đường sắt đô thị.", size_pt=12, space_after=2)
    add_styled_para(c_sec10, "Đối với Tuyến Metro số 1 TP.HCM (Bến Thành – Suối Tiên), công trình Luận án Tiến sĩ Kỹ thuật của tác giả Nguyễn Thạch Bích (2022) tại Trường Đại học Giao thông vận tải đã cung cấp chuỗi số liệu quan trắc lún mốc sâu thực tế rất quý giá trong quá trình khiên đào EPB-TBM thi công qua đoạn Ba Son – Nhà hát Thành phố. Tuy nhiên, quan trắc trắc địa truyền thống chỉ có dữ liệu tại một số mặt cắt rời rạc, không bao quát được toàn bộ 19.7 km tuyến và không có khả năng hồi cứu biến dạng trước và sau thi công. Do đó, việc kế thừa kết quả thực nghiệm địa kỹ thuật của Nguyễn Thạch Bích (2022) để làm chuẩn đối sánh cho công nghệ viễn thám InSAR vệ tinh Sentinel-1 là hướng tiếp cận có tính đột phá và bổ trợ hoàn hảo.", size_pt=12, space_after=4)

    add_styled_para(c_sec10, "10.3. Liệt kê danh mục các công trình nghiên cứu có liên quan trực tiếp:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec10, "1. Berardino, P., Fornaro, G., Lanari, R., & Sansosti, E. (2002). A new algorithm for surface deformation monitoring based on small baseline differential SAR interferograms. IEEE Trans. Geosci. Remote Sens., 40(11), 2375–2383.", size_pt=11, space_after=1)
    add_styled_para(c_sec10, "2. Chen, F., Lin, H., Zhou, W., Hong, T., & Wang, G. (2012). Surface deformation monitoring by InSAR in Shanghai using TerraSAR-X data. Photogrammetric Engineering & Remote Sensing, 78(8), 785–794.", size_pt=11, space_after=1)
    add_styled_para(c_sec10, "3. Ferretti, A., Prati, C., & Rocca, F. (2001). Permanent scatterers in SAR interferometry. IEEE Trans. Geosci. Remote Sens., 39(1), 8–20.", size_pt=11, space_after=1)
    add_styled_para(c_sec10, "4. Nguyễn Thạch Bích (2022). Nghiên cứu thực nghiệm biến dạng đất nền và công trình lân cận do thi công hầm bằng máy khiên đào TBM đoạn tuyến ngầm Metro số 1 Bến Thành – Suối Tiên. Luận án Tiến sĩ Kỹ thuật, Trường Đại học Giao thông vận tải, Hà Nội.", size_pt=11, space_after=1)
    add_styled_para(c_sec10, "5. Phùng Đại Bình (2018). Ứng dụng công nghệ InSAR đa thời gian xác định biến dạng bề mặt đất khu vực TP. Hồ Chí Minh. Tạp chí Khoa học Kỹ thuật Mỏ - Địa chất, 59(2), 45–53.", size_pt=11, space_after=1)
    add_styled_para(c_sec10, "6. Peck, R. B. (1969). Deep excavations and tunneling in soft ground. In Proc. 7th ICSMFE, Mexico City, State-of-the-Art Volume, pp. 225–290.", size_pt=11, space_after=1)
    add_styled_para(c_sec10, "7. Burland, J. B. (1995). Assessment of risk of damage to buildings due to tunnelling and excavations. In Proc. 1st Int. Conf. on Earthquake Geotechnical Engineering, Tokyo, Vol. 3, pp. 1189–1201.", size_pt=11, space_after=1)
    add_styled_para(c_sec10, "8. Yunjun, Z., Fattahi, H., & Amelung, F. (2019). Small baseline InSAR time series analysis: Unwrapping error correction and noise reduction. Computers & Geosciences, 133, 104331.", size_pt=11, space_after=3)

    add_styled_para(c_sec10, "10.4. Những vấn đề KH&CN còn tồn tại và nội dung đặt ra giải quyết:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec10, "• Tồn tại, hạn chế: Các nghiên cứu InSAR trước đây tại TP.HCM chủ yếu chỉ sử dụng một quỹ đạo đơn lẻ (quỹ đạo xuống Descending), dẫn đến chuyển vị thu được chỉ là chuyển vị theo hướng ngắm vệ tinh (Line-of-Sight - LOS), chưa phân rã được thành phần lún thực tế theo phương thẳng đứng. Đồng thời, kết quả InSAR viễn thám thường thiếu sự đối chuẩn thực địa với các mốc đo trắc địa chuẩn và chưa kết nối với mô hình cơ học đất công trình ngầm.", size_pt=12, space_after=2)
    add_styled_para(c_sec10, "• Vấn đề đề tài giải quyết: Kết hợp đồng thời hai quỹ đạo Sentinel-1 (Track 18 Descending và Track 128 Ascending) để giải bài toán phân rã vector 2 chiều (phương đứng dV và phương ngang dEW); liên kết trực tiếp kết quả InSAR với 8 mặt cắt quan trắc lún mốc sâu thực địa của Luận án TS. Nguyễn Thạch Bích (2022) và mô hình phễu lún Peck (1969), từ đó xây dựng bản đồ số phân vùng rủi ro công trình chuẩn hóa theo Burland (1995).", size_pt=12, space_after=4)

    add_styled_para(c_sec10, "10.5. Hướng phát triển tiếp theo của đề tài:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec10, "Nếu đề tài thực hiện thành công, nhóm nghiên cứu sẽ phát triển thành đề tài nghiên cứu cấp Bộ GTVT / Bộ KH&CN hoặc đề tài Quỹ Phát triển KH&CN Quốc gia (NAFOSTED), mở rộng quy mô tích hợp mạng nơ-ron học sâu (Deep Learning / LSTM) dự báo chuỗi thời gian biến dạng lún tự động theo thời gian thực cho toàn bộ các tuyến đường sắt đô thị tại Hà Nội và TP. Hồ Chí Minh.", size_pt=12, space_after=4)

    # Row 2: Mục 11. TÍNH CẤP THIẾT CỦA ĐỀ TÀI
    c_sec11 = t1.rows[2].cells[0]
    c_sec11.text = ""
    add_styled_para(c_sec11, "11. TÍNH CẤP THIẾT CỦA ĐỀ TÀI", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec11, "Tuyến đường sắt đô thị số 1 TP. Hồ Chí Minh (Bến Thành – Suối Tiên) là công trình hạ tầng giao thông trọng điểm quốc gia với tổng chiều dài 19.7 km, đi qua các khu vực đô thị có mật độ dân cư và công trình xây dựng dày đặc. Tuyến gồm 2.6 km đi ngầm bằng công nghệ khiên đào TBM qua trung tâm Quận 1 và 17.1 km cầu cạn trên cao vượt qua các vùng địa chất trầm tích Đệ Tứ ngập nước, có tầng sét yếu hữu cơ dày và sức chịu tải kém (như khu vực Rạch Văn Thánh).", size_pt=12, space_after=2)
    add_styled_para(c_sec11, "Khi tuyến metro chính thức bước vào giai đoạn vận hành thương mại (2024–2026), sự tích tụ tải trọng động của đoàn tàu kết hợp với hiện tượng hạ thấp mực nước ngầm tầng nông và hoạt động xây dựng dày đặc xung quanh có nguy cơ gây ra hiện tượng lún không đều (differential settlement). Lún không đều nếu vượt quá ngưỡng cho phép (15–20 mm) sẽ gây nứt vỡ vỏ hầm, làm sai lệch kích thước hình học đường ray đe dọa trật bánh tàu, hoặc gây rạn nứt kết cấu các công trình di sản lịch sử (Nhà hát Lớn, Khách sạn Continental) và nhà dân lân cận.", size_pt=12, space_after=2)
    add_styled_para(c_sec11, "Tuy nhiên, phương pháp quan trắc trắc địa truyền thống bằng thủy chuẩn hình học độ chính xác cao bộc lộ những nhược điểm lớn: chi phí rất đắt đỏ, mật độ mốc đo thưa thớt, không thể bao quát diện rộng và tần suất đo bị gián đoạn do mật độ giao thông đô thị cao. Do đó, việc ứng dụng công nghệ viễn thám radar giao thoa chuỗi thời gian (InSAR) khai thác nguồn ảnh miễn phí Sentinel-1 của Cơ quan Vũ trụ Châu Âu (ESA) với mật độ hàng nghìn điểm đo/km², độ phủ liên tục không gian và chu kỳ lặp 12 ngày là một giải pháp khoa học công nghệ tiên tiến, đột phá và có tính cấp thiết đặc biệt nhằm đảm bảo an toàn tuyệt đối cho công trình metro.", size_pt=12, space_after=4)

    # Row 3: Mục 12. ĐỐI TƯỢNG, PHẠM VI NGHIÊN CỨU
    c_sec12 = t1.rows[3].cells[0]
    c_sec12.text = ""
    add_styled_para(c_sec12, "12. ĐỐI TƯỢNG, PHẠM VI NGHIÊN CỨU", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec12, "12.1. Đối tượng nghiên cứu:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec12, "Trường biến dạng chuyển vị bề mặt đất (tốc độ lún thẳng đứng mm/năm và chuyển vị ngang) dọc hành lang tuyến đường sắt đô thị và tương tác địa kỹ thuật giữa thi công hầm ngầm/cầu cạn với đất nền bồi tích yếu đô thị.", size_pt=12, space_after=2)
    add_styled_para(c_sec12, "12.2. Phạm vi nghiên cứu:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec12, "• Phạm vi không gian: Toàn bộ hành lang tuyến Metro số 1 Bến Thành – Suối Tiên (19.7 km) và dải đệm quan sát 500m hai bên tim tuyến (tổng diện tích nghiên cứu khoảng 19.85 km²), tập trung trọng điểm vào đoạn ngầm TBM Ba Son – Bến Thành (Km 0+000 – Km 2+600) và đoạn cầu cạn vượt đất yếu Rạch Văn Thánh (Km 2+600 – Km 4+500).", size_pt=12, space_after=2)
    add_styled_para(c_sec12, "• Phạm vi thời gian: Chuỗi dữ liệu viễn thám radar vệ tinh Sentinel-1 từ tháng 01/2019 đến tháng 12/2026. Thời gian thực hiện đề tài từ 01/01/2027 đến 31/12/2027.", size_pt=12, space_after=4)

    # Row 4: Mục 13. CÁCH TIẾP CẬN, PHƯƠNG PHÁP NGHIÊN CỨU
    c_sec13 = t1.rows[4].cells[0]
    c_sec13.text = ""
    add_styled_para(c_sec13, "13. CÁCH TIẾP CẬN, PHƯƠNG PHÁP NGHIÊN CỨU", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec13, "13.1. Cách tiếp cận:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec13, "Đề tài áp dụng cách tiếp cận liên ngành tích hợp (Interdisciplinary Integrated Approach) giữa ba trụ cột: Công nghệ Viễn thám không gian (InSAR) – Hệ thông tin địa lý (GIS) – Cơ học đất và Địa kỹ thuật công trình ngầm. Dữ liệu viễn thám diện rộng đóng vai trò phát hiện và định lượng biến dạng; dữ liệu địa kỹ thuật thực địa đóng vai trò đối chuẩn và giải thích nguyên nhân cơ chế vật lý.", size_pt=12, space_after=2)
    add_styled_para(c_sec13, "13.2. Phương pháp nghiên cứu:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec13, "1. Phương pháp thu thập và tiền xử lý ảnh viễn thám radar: Tải và giải mã chuỗi ảnh radar khẩu độ tổng hợp Sentinel-1 IW SLC băng C từ cổng dữ liệu Copernicus của ESA; nạp dữ liệu quỹ đạo bay chính xác (Precise Orbit Ephemerides).", size_pt=12, space_after=2)
    add_styled_para(c_sec13, "2. Phương pháp giao thoa radar chuỗi thời gian (SBAS-InSAR): Ghép cặp giao thoa kế có đường đáy không gian và thời gian nhỏ (Small Baseline); loại bỏ pha phẳng và pha địa hình bằng mô hình số độ cao Copernicus DEM GLO-30.", size_pt=12, space_after=2)
    add_styled_para(c_sec13, "3. Thuật toán giải pha và khử nhiễu khí quyển: Ứng dụng phần mềm SNAPHU giải pha không gian 3 chiều; sử dụng module mã nguồn mở MintPy để lọc nhiễu pha khí quyển (tropospheric phase delay) và nghịch đảo tìm chuỗi thời gian lún bằng phương pháp bình phương tối thiểu có trọng số (WLS).", size_pt=12, space_after=2)
    add_styled_para(c_sec13, "4. Phương pháp phân rã vector biến dạng 2 chiều (2D Vector Decomposition): Kết hợp đồng thời kết quả giải pha từ quỹ đạo xuống (Track 18) và quỹ đạo lên (Track 128) để tách bạch thành phần chuyển vị thẳng đứng dV và phương ngang dEW.", size_pt=12, space_after=2)
    add_styled_para(c_sec13, "5. Phương pháp đối chuẩn địa kỹ thuật và phân loại rủi ro: So sánh đối sánh kết quả lún InSAR với chuỗi mốc quan trắc thủy chuẩn hình học thực địa tại 8 mặt cắt công trình ngầm; kiểm chứng với mô hình phễu lún Gaussian Peck (1969) và phân loại nguy cơ hư hại công trình theo tiêu chuẩn Burland (1995).", size_pt=12, space_after=4)

    # Row 5: Mục 14.1 Nội dung nghiên cứu chi tiết
    c_sec14 = t1.rows[5].cells[0]
    c_sec14.text = ""
    add_styled_para(c_sec14, "14. NỘI DUNG CHI TIẾT VÀ TIẾN ĐỘ THỰC HIỆN", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec14, "14.1. Nội dung nghiên cứu chi tiết:", size_pt=12, bold=True, space_after=2)
    add_styled_para(c_sec14, "• Nội dung 1: Nghiên cứu tổng quan, thu thập tài liệu và xây dựng cơ sở dữ liệu số hóa.\n- Thu thập tài liệu thiết kế, trắc dọc, bình đồ hướng tuyến, tọa độ 14 nhà ga tuyến Metro số 1.\n- Thu thập hơn 700 cảnh ảnh radar Sentinel-1 IW SLC (2019–2026) cho 2 quỹ đạo bay lên và bay xuống.\n- Thu thập số liệu địa tầng, cơ lý hố khoan và mốc đo lún thực địa từ Luận án TS. Nguyễn Thạch Bích (2022).", size_pt=12, space_after=2)
    add_styled_para(c_sec14, "• Nội dung 2: Xử lý chuỗi thời gian InSAR đa quỹ đạo và phân rã chuyển vị 2D.\n- Tạo cặp giao thoa kế baseline nhỏ, khử pha địa hình bằng Copernicus DEM 30m, giải pha bằng SNAPHU.\n- Lọc nhiễu khí quyển, sửa lỗi giải pha và nghịch đảo chuỗi thời gian bằng MintPy.\n- Phát triển thuật toán ma trận hình học vệ tinh để phân rã chuyển vị thẳng đứng dV và chuyển vị ngang dEW.", size_pt=12, space_after=2)
    add_styled_para(c_sec14, "• Nội dung 3: Đối chuẩn kết quả InSAR với số liệu quan trắc thực địa và phân tích tương quan cơ học.\n- So sánh đối chiếu chuỗi lún InSAR tại các điểm tán xạ ổn định (PS/DS) với mốc lún sâu tại 8 mặt cắt TBM.\n- Đánh giá sai số thống kê (RMSE, MAE, R²) giữa viễn thám và trắc địa mặt đất.\n- Phân tích tương quan giữa biên độ lún với tiến độ khiên đào TBM, áp lực vữa ép và địa tầng sét yếu bùn cát.", size_pt=12, space_after=2)
    add_styled_para(c_sec14, "• Nội dung 4: Phân tích vùng ảnh hưởng, đánh giá nguy cơ tổn hại công trình và xây dựng bản đồ số GIS.\n- Khớp hàm phễu lún Peck (1969) thực địa, xác định hệ số bề rộng phễu lún K và độ dốc mặt đất cực đại.\n- Phân loại cấp độ nguy cơ hư hỏng của các công trình lân cận theo tiêu chuẩn Burland (1995).\n- Xây dựng bản đồ chuyên đề tốc độ lún và các lớp vùng đệm cảnh báo rủi ro trên nền phần mềm QGIS.", size_pt=12, space_after=2)
    add_styled_para(c_sec14, "• Nội dung 5: Tổng kết kết quả, viết báo cáo tổng kết và công bố bài báo khoa học.\n- Biên soạn toàn văn Báo cáo tổng kết đề tài NCKH cấp Trường.\n- Viết và hoàn thiện bài báo khoa học đăng trên Tạp chí Giao thông vận tải (HĐGSNN tính điểm tối đa 0,75 điểm).\n- Nghiệm thu đề tài cấp cơ sở và cấp Trường theo đúng quy định.", size_pt=12, space_after=4)

    # Capture rows 8, 9, 10 before mutating t1
    row_sec15 = t1.rows[8]
    row_sec16 = t1.rows[9]
    row_sec17 = t1.rows[10]

    # Define 5 distinct tasks for schedule sub-table 14.2:
    tasks = [
        ("1", "Nội dung 1: Thu thập, chuẩn hóa cơ sở dữ liệu viễn thám radar Sentinel-1 (2019–2026), bình đồ, trắc dọc và số liệu địa chất, mốc quan trắc Metro 1.", "Bộ CSDL viễn thám & địa chất số hóa chuẩn GIS.", "01/2027 – 03/2027", "ThS. Nguyễn Hải Hà\nKS. Trần Văn Long"),
        ("2", "Nội dung 2: Xử lý chuỗi thời gian InSAR đa quỹ đạo (SNAP-SNAPHU-MintPy) và phân rã trường chuyển vị 2 chiều (thẳng đứng dV và ngang dEW).", "Trường vận tốc lún LOS và bản đồ phân rã chuyển vị 2D (dV, dEW).", "04/2027 – 06/2027", "ThS. Nguyễn Hải Hà\nThS. Lê Văn Nam"),
        ("3", "Nội dung 3: Đối chuẩn kết quả lún InSAR với mốc quan trắc trắc địa thực địa tại 8 mặt cắt TBM; phân tích tương quan cơ học đất và công trình ngầm.", "Báo cáo phân tích đối chuẩn thực địa, chỉ số RMSE, MAE, R².", "07/2027 – 09/2027", "ThS. Nguyễn Hải Hà\nTS. Nguyễn Thạch Bích"),
        ("4", "Nội dung 4: Phân tích phễu lún Peck (1969), đánh giá nguy cơ tổn hại công trình lân cận theo tiêu chuẩn Burland (1995) và thành lập bản đồ số GIS.", "Báo cáo đánh giá rủi ro Burland và bộ bản đồ số chuyên đề phân vùng cảnh báo (Shapefile).", "10/2027 – 11/2027", "ThS. Nguyễn Hải Hà\nThS. Lê Văn Nam"),
        ("5", "Nội dung 5: Viết bài báo khoa học đăng trên Tạp chí Giao thông vận tải (HĐGSNN); tổng hợp báo cáo tổng kết và nghiệm thu đề tài.", "01 Bài báo Tạp chí Giao thông vận tải & Báo cáo tổng kết đề tài.", "11/2027 – 12/2027", "Tập thể nhóm NCKH")
    ]

    import copy
    row_sched = t1.rows[7]
    for col_idx in range(5):
        row_sched.cells[col_idx].text = tasks[0][col_idx]
        set_cell_font(row_sched.cells[col_idx], size_pt=11)
        if col_idx in (0, 3):
            for p in row_sched.cells[col_idx].paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    curr_tr = row_sched._tr
    for task in tasks[1:]:
        new_tr = copy.deepcopy(row_sched._tr)
        tcs = new_tr.xpath('.//w:tc')
        for col_idx in range(5):
            for p in tcs[col_idx].xpath('.//w:p'):
                tcs[col_idx].remove(p)
            new_p = OxmlElement('w:p')
            new_r = OxmlElement('w:r')
            new_t = OxmlElement('w:t')
            new_t.text = task[col_idx]
            new_r.append(new_t)
            new_p.append(new_r)
            tcs[col_idx].append(new_p)
            # Apply styling
            rPr = OxmlElement('w:rPr')
            rFonts = OxmlElement('w:rFonts')
            rFonts.set(qn('w:ascii'), 'Times New Roman')
            rFonts.set(qn('w:hAnsi'), 'Times New Roman')
            rFonts.set(qn('w:cs'), 'Times New Roman')
            sz = OxmlElement('w:sz')
            sz.set(qn('w:val'), '22')  # 11 pt
            rPr.append(rFonts)
            rPr.append(sz)
            new_r.append(rPr)
            if col_idx in (0, 3):
                pPr = OxmlElement('w:pPr')
                jc = OxmlElement('w:jc')
                jc.set(qn('w:val'), 'center')
                pPr.append(jc)
                new_p.append(pPr)
        curr_tr.addnext(new_tr)
        curr_tr = new_tr

    # Row 8: Mục 15. NỘI DUNG NGHIÊN CỨU ỨNG DỤNG VÀ TRIỂN KHAI THỰC NGHIỆM
    c_sec15 = row_sec15.cells[0]
    c_sec15.text = ""
    add_styled_para(c_sec15, "15. NỘI DUNG NGHIÊN CỨU ỨNG DỤNG VÀ TRIỂN KHAI THỰC NGHIỆM", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec15, "• Nội dung ứng dụng và thực nghiệm:\nĐề tài sẽ triển khai thử nghiệm quy trình công nghệ InSAR phân rã 2D trên toàn bộ hành lang 19.7 km tuyến Metro số 1 Bến Thành – Suối Tiên, tập trung kiểm chứng sâu tại 2 khu vực nhạy cảm cao:\n1. Phân đoạn ngầm TBM Ba Son – Bến Thành (Km 0+000 – Km 2+600): Nơi có sự hiện diện của hai đường hầm EPB-TBM song song và nhiều công trình lịch sử nhạy cảm.\n2. Phân đoạn chuyển tiếp và cầu cạn Rạch Văn Thánh (Km 2+600 – Km 4+500): Nơi có địa tầng bùn sét hữu cơ rất dày và tốc độ lún tự nhiên của đất nền khu vực diễn ra nhanh.", size_pt=12, space_after=2)
    add_styled_para(c_sec15, "• Dự kiến rủi ro và giải pháp khắc phục:\n- Rủi ro mất tương quan pha do thảm thực vật hoặc thời tiết mưa rào nhiệt đới: Khắc phục bằng cách chọn lọc thuật toán tán xạ ổn định (PS) ưu tiên trên các kết cấu bê tông, mái tôn, bề mặt đường ray và công trình nhân tạo; áp dụng ngưỡng mạch lạc pha cao (coherence > 0.4).\n- Rủi ro chênh lệch góc chiếu giữa 2 quỹ đạo: Áp dụng thuật toán kiểm soát điều kiện số ma trận (Condition Number CN ≤ 100) để đảm bảo nghiệm phân rã chuyển vị 2D ổn định.", size_pt=12, space_after=4)

    # Row 9: Mục 16. HIỆU QUẢ (GIÁO DỤC ĐÀO TẠO, KINH TẾ - XÃ HỘI)
    c_sec16 = row_sec16.cells[0]
    c_sec16.text = ""
    add_styled_para(c_sec16, "16. HIỆU QUẢ (giáo dục và đào tạo, kinh tế - xã hội)", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec16, "16.1. Hiệu quả đối với giáo dục và đào tạo:\n- Góp phần nâng cao năng lực nghiên cứu khoa học của giảng viên trẻ tại Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường.\n- Cung cấp nguồn tư liệu thực tế, số liệu viễn thám và địa kỹ thuật sinh động phục vụ bài giảng các môn học chuyên ngành: 'Công trình ngầm', 'Quan trắc công trình', 'Tin học ứng dụng trong Địa kỹ thuật'.\n- Trực tiếp hướng dẫn 01–02 sinh viên ngành Kỹ thuật Xây dựng Công trình Giao thông / Địa kỹ thuật thực hiện đồ án tốt nghiệp hoặc tham gia phong trào Sinh viên Nghiên cứu khoa học.", size_pt=12, space_after=2)
    add_styled_para(c_sec16, "16.2. Hiệu quả kinh tế - xã hội:\n- Về kinh tế: Giảm thiểu đáng kể chi phí quan trắc trắc địa truyền thống đắt đỏ; cung cấp giải pháp giám sát diện rộng với chi phí dữ liệu vệ tinh mở hoàn toàn miễn phí.\n- Về xã hội: Hỗ trợ cơ quan quản lý đô thị (MAUR, HURC1, Sở GTVT TP.HCM) phát hiện sớm các nguy cơ lún nứt bất thường, chủ động đưa ra phương án bảo trì dự phòng, ngăn ngừa sự cố kỹ thuật, bảo vệ an toàn tính mạng và tài sản cho hành khách cũng như cư dân sinh sống dọc hành lang metro.", size_pt=12, space_after=4)

    # Row 10: Mục 17. PHƯƠNG THỨC CHUYỂN GIAO KẾT QUẢ VÀ ĐỊA CHỈ ỨNG DỤNG
    c_sec17 = row_sec17.cells[0]
    c_sec17.text = ""
    add_styled_para(c_sec17, "17. PHƯƠNG THỨC CHUYỂN GIAO KẾT QUẢ NGHIÊN CỨU VÀ ĐỊA CHỈ ỨNG DỤNG", size_pt=12, bold=True, space_after=4)
    add_styled_para(c_sec17, "• Phương thức chuyển giao:\n- Chuyển giao trực tiếp kết quả nghiên cứu dưới dạng Báo cáo chuyên đề kỹ thuật và cơ sở dữ liệu số GIS cho Ban Quản lý Đường sắt Đô thị TP.HCM (MAUR).\n- Tổ chức 01 buổi hội thảo khoa học chuyên đề tại Bộ môn để báo cáo kết quả và tập huấn quy trình xử lý ảnh InSAR cho cán bộ, giảng viên và sinh viên quan tâm.\n- Xuất bản công khai bài báo khoa học trên Tạp chí Giao thông vận tải để phổ biến tri thức trong cộng đồng khoa học ngành GTVT và Xây dựng công trình ngầm.\n• Địa chỉ ứng dụng:\n- Ban Quản lý Đường sắt Đô thị TP. Hồ Chí Minh (MAUR).\n- Công ty TNHH MTV Đường sắt Đô thị số 1 TP.HCM (HURC1).\n- Bộ môn Địa kỹ thuật và Không gian ngầm, Khoa Công trình và Môi trường, Trường Đại học Giao thông vận tải.", size_pt=12, space_after=4)

    # =========================================================================
    # TABLE 2: C. QUẢN LÝ & PHÂN BỔ TÀI CHÍNH
    # =========================================================================
    print("Populating Table 2: Financial Management & Budget Allocation...")

    # Financial budget allocation table (25.000.000 VNĐ)
    # Rows 5 to 20:
    # Format of each row:
    # C0: STT, C1: Khoản chi, C2: Thời gian, C3: Tổng kinh phí, C4: Từ NS KHCN, C5: Khác, C6: Ghi chú
    budget_data = [
        # (Row_idx, STT, Item, Time, Total, NS, Khac, Note)
        (5, "I", "Chi công lao động trực tiếp", "Tháng 01–12/2027", "14.000.000", "14.000.000", "0", "Theo quy định"),
        (6, "1.1", "Chi công lao động của cán bộ khoa học, nhân viên kỹ thuật trực tiếp tham gia thực hiện đề tài", "Tháng 01–12/2027", "11.000.000", "11.000.000", "0", "Chủ nhiệm & thành viên"),
        (7, "1.2", "Chi công lao động khác phục vụ triển khai đề tài", "Tháng 03–11/2027", "3.000.000", "3.000.000", "0", "Xử lý số liệu, phụ trợ"),
        (8, "II", "Chi mua vật tư, nguyên, nhiên, vật liệu", "Tháng 01–06/2027", "4.500.000", "4.500.000", "0", ""),
        (9, "", "Chi mua vật tư, tài liệu, tư liệu, số liệu viễn thám, bản đồ chuyên môn, xuất bản phẩm kỹ thuật phục vụ nghiên cứu", "Tháng 01–06/2027", "4.500.000", "4.500.000", "0", "Tư liệu địa kỹ thuật, DEM"),
        (10, "III", "Chi sửa chữa, mua sắm tài sản cố định", "", "0", "0", "0", "Không phát sinh"),
        (11, "IV", "Quản lý chung (5%)", "Tháng 01–12/2027", "1.250.000", "1.250.000", "0", "5% tổng kinh phí đề tài"),
        (12, "V", "Chi khác", "Tháng 01–12/2027", "5.250.000", "5.250.000", "0", ""),
        (13, "5.1", "Công tác phí", "Tháng 04–09/2027", "1.000.000", "1.000.000", "0", "Khảo sát thực địa tuyến"),
        (14, "5.2", "Đoàn ra, đoàn vào", "", "0", "0", "0", "Không phát sinh"),
        (15, "5.3", "Chi trả dịch vụ thuê ngoài phục vụ hoạt động nghiên cứu", "", "0", "0", "0", "Tự thực hiện"),
        (16, "5.4", "Chi điều tra, khảo sát thu thập số liệu", "Tháng 02–05/2027", "1.250.000", "1.250.000", "0", "Khảo sát mốc lún thực địa"),
        (17, "5.5", "Chi văn phòng phẩm, thông tin liên lạc, in ấn tài liệu", "Tháng 01–12/2027", "1.000.000", "1.000.000", "0", "Giấy in, đóng quyển BC"),
        (18, "5.6", "Hội nghị, hội thảo khoa học, đăng bài báo", "Tháng 10–12/2027", "2.000.000", "2.000.000", "0", "Lệ phí đăng bài báo"),
        (19, "5.7", "Chi khác liên quan trực tiếp đến đề tài", "", "0", "0", "0", ""),
        (20, "", "Tổng cộng", "12 tháng", "25.000.000", "25.000.000", "0", "Hai mươi lăm triệu đồng")
    ]

    for r_idx, stt, item, t_time, tot, ns, khac, note in budget_data:
        row = t2.rows[r_idx]
        row.cells[0].text = stt
        row.cells[1].text = item
        row.cells[2].text = t_time
        row.cells[3].text = tot
        row.cells[4].text = ns
        row.cells[5].text = khac
        row.cells[6].text = note

        # Formatting
        is_bold = stt in ["I", "II", "III", "IV", "V"] or item == "Tổng cộng"
        for c_idx in range(7):
            cell = row.cells[c_idx]
            align = WD_ALIGN_PARAGRAPH.RIGHT if c_idx in [3, 4, 5] else (WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT)
            for p in cell.paragraphs:
                p.alignment = align
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                for run in p.runs:
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(11)
                    run.bold = is_bold

    # Row 21: Chữ ký
    c_sig = t2.rows[21].cells[0]
    c_sig.text = ""
    
    # We can layout the signature neatly: Left is Chủ nhiệm đề tài, Right is Hiệu trưởng
    p_sig = c_sig.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(12)
    p_sig.paragraph_format.space_after = Pt(6)
    
    # Add a 2-column signature table inside cell or format nicely
    sig_text_left = "CHỦ NHIỆM ĐỀ TÀI\n(Ký và ghi rõ họ tên)\n\n\n\n\nThS. Nguyễn Hải Hà"
    sig_text_right = "Hà Nội, ngày … tháng … năm 2026\nKT. HIỆU TRƯỞNG\nPHÓ HIỆU TRƯỞNG\n\n\n\n"
    
    # Use runs with tab or add styled paragraph
    add_styled_para(c_sig, "                                                                                                   Hà Nội, ngày … tháng … năm 2026", size_pt=12, italic=True, align=WD_ALIGN_PARAGRAPH.RIGHT)
    p_titles = c_sig.add_paragraph()
    p_titles.paragraph_format.space_after = Pt(60)
    p_titles.paragraph_format.line_spacing = 1.15
    run_l = p_titles.add_run("           CHỦ NHIỆM ĐỀ TÀI                                                                KT. HIỆU TRƯỞNG\n         (Ký và ghi rõ họ tên)                                                              PHÓ HIỆU TRƯỞNG")
    run_l.font.name = "Times New Roman"
    run_l.font.size = Pt(12)
    run_l.bold = True
    
    p_names = c_sig.add_paragraph()
    p_names.paragraph_format.space_after = Pt(12)
    run_n = p_names.add_run("          ThS. Nguyễn Hải Hà")
    run_n.font.name = "Times New Roman"
    run_n.font.size = Pt(12)
    run_n.bold = True

    # Save document
    doc.save(DOCX_OUTPUT)
    print(f"SUCCESS: Successfully populated and saved {DOCX_OUTPUT}!")

if __name__ == "__main__":
    fill_proposal()
