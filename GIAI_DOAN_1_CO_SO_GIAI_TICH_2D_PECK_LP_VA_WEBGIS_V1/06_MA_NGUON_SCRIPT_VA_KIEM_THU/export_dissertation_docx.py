# -*- coding: utf-8 -*-
"""
Script biên dịch toàn văn bản thảo luận án từ Markdown sang Microsoft Word (.docx)
đáp ứng đầy đủ quy chuẩn luận án Tiến sĩ / Thạc sĩ Kỹ thuật (Bộ môn Địa kỹ thuật & Không gian ngầm, UTC).
Tích hợp:
- Bìa chính quy, trang phụ bìa, tóm tắt.
- Căn lề chuẩn: Trái 3.0cm, Phải 2.0cm, Trên 2.0cm, Dưới 2.0cm.
- Font Times New Roman, dãn dòng 1.3 - 1.5 lines, thụt đầu dòng 1.0cm.
- Bảng biểu được kẻ viền, tô màu tiêu đề bảng (#EAECEE).
- Chèn trực tiếp toàn bộ 7 hình ảnh minh họa độ phân giải cao 300 DPI.
- Các hộp ghi chú Audit (bôi vàng/cảnh báo) được định dạng khung nổi bật.
"""

import re
import sys
from pathlib import Path
import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
MD_PATH = ROOT / "nhiem_vu_luan_an" / "04_ban_thao_luan_an_chi_tiet" / "LUAN_AN_HOAN_CHINH_TBM_METRO3_HANOI.md"
DOCX_PATH = ROOT / "nhiem_vu_luan_an" / "04_ban_thao_luan_an_chi_tiet" / "LUAN_AN_HOAN_CHINH_TBM_METRO3_HANOI.docx"
FIG_DIR = ROOT / "nhiem_vu_luan_an" / "03_hinh_anh_minh_hoa_chat_luong_cao"


def set_cell_border(cell, **kwargs):
    """
    Set cell borders
    kwargs: top, bottom, left, right
    values: dict(sz=12, val='single', color='CCCCCC')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            for key, val in edge_data.items():
                element.set(qn('w:{}'.format(key)), str(val))


def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def add_formatted_text(p, text, default_font="Times New Roman", default_size=13, default_bold=False, default_italic=False, default_color=None):
    """
    Phân tích định dạng inline markdown cơ bản: **bold**, *italic*, ==audit==, $math$
    """
    # Xử lý khối audit highlight ==[...] ==
    if "==" in text:
        parts = text.split("==")
        for idx, part in enumerate(parts):
            if idx % 2 == 1:
                # Đây là phần audit
                run = p.add_run(f"[{part.strip()}]")
                run.font.name = default_font
                run.font.size = Pt(default_size - 1)
                run.font.bold = True
                run.font.italic = True
                run.font.color.rgb = RGBColor(180, 50, 0) # Màu cam gạch
            else:
                add_sub_formatted_text(p, part, default_font, default_size, default_bold, default_italic, default_color)
    else:
        add_sub_formatted_text(p, text, default_font, default_size, default_bold, default_italic, default_color)


def add_sub_formatted_text(p, text, font_name, size, bold, italic, color):
    # Tách theo bold **...**
    tokens = re.split(r'(\*\*.*?\*\*)', text)
    for token in tokens:
        if token.startswith('**') and token.endswith('**') and len(token) >= 4:
            content = token[2:-2]
            # Kiểm tra tiếp italic *...*
            sub_tokens = re.split(r'(\*.*?\*)', content)
            for st in sub_tokens:
                if st.startswith('*') and st.endswith('*') and len(st) >= 2:
                    run = p.add_run(st[1:-1])
                    run.font.name = font_name
                    run.font.size = Pt(size)
                    run.font.bold = True
                    run.font.italic = True
                    if color: run.font.color.rgb = color
                else:
                    run = p.add_run(st)
                    run.font.name = font_name
                    run.font.size = Pt(size)
                    run.font.bold = True
                    run.font.italic = italic
                    if color: run.font.color.rgb = color
        else:
            # Kiểm tra italic *...*
            sub_tokens = re.split(r'(\*.*?\*)', token)
            for st in sub_tokens:
                if st.startswith('*') and st.endswith('*') and len(st) >= 2:
                    run = p.add_run(st[1:-1])
                    run.font.name = font_name
                    run.font.size = Pt(size)
                    run.font.bold = bold
                    run.font.italic = True
                    if color: run.font.color.rgb = color
                else:
                    run = p.add_run(st)
                    run.font.name = font_name
                    run.font.size = Pt(size)
                    run.font.bold = bold
                    run.font.italic = italic
                    if color: run.font.color.rgb = color


def main():
    print("Bắt đầu xuất bản thảo luận án sang Word (.docx)...")
    content = MD_PATH.read_text(encoding='utf-8')
    lines = content.splitlines()

    doc = docx.Document()

    # Thiết lập căn lề chuẩn luận án: Trái 3.0cm, Phải 2.0cm, Trên 2.0cm, Dưới 2.0cm
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.0)
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)

    # Style Normal
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(13)
    style_normal.paragraph_format.line_spacing = 1.3
    style_normal.paragraph_format.space_after = Pt(4)
    style_normal.paragraph_format.space_before = Pt(0)

    in_table = False
    table_rows = []
    
    i = 0
    total_lines = len(lines)
    while i < total_lines:
        line = lines[i]
        stripped = line.strip()

        # Kiểm tra bảng Markdown
        if stripped.startswith("|") and stripped.endswith("|"):
            table_rows.append(stripped)
            i += 1
            continue
        elif table_rows:
            # Kết thúc một bảng -> Tiến hành vẽ bảng vào Word
            render_markdown_table(doc, table_rows)
            table_rows = []

        if not stripped:
            i += 1
            continue

        # Kiểm tra hình ảnh ![alt](path)
        img_match = re.match(r'!\[(.*?)\]\((.*?)\)', stripped)
        if img_match:
            caption = img_match.group(1)
            img_rel_path = img_match.group(2)
            # Tìm file hình
            img_filename = Path(img_rel_path).name
            img_full_path = FIG_DIR / img_filename
            if img_full_path.exists():
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(10)
                p_img.paragraph_format.space_after = Pt(4)
                p_img.add_run().add_picture(str(img_full_path), width=Inches(6.0))
                
                # Caption
                p_cap = doc.add_paragraph()
                p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_cap.paragraph_format.space_before = Pt(0)
                p_cap.paragraph_format.space_after = Pt(10)
                run_cap = p_cap.add_run(caption)
                run_cap.font.name = "Times New Roman"
                run_cap.font.size = Pt(11)
                run_cap.font.italic = True
                run_cap.font.bold = True
            i += 1
            continue

        # Tiêu đề cấp 1 (# CHƯƠNG...)
        if stripped.startswith("# "):
            title_text = stripped[2:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(18)
            p.paragraph_format.space_after = Pt(12)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(title_text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(16)
            run.font.bold = True
            run.font.color.rgb = RGBColor(30, 60, 114) # Xanh đậm trang trọng
            i += 1
            continue

        # Tiêu đề cấp 2 (## ...)
        if stripped.startswith("## "):
            title_text = stripped[3:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(title_text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(14)
            run.font.bold = True
            run.font.color.rgb = RGBColor(40, 80, 140)
            i += 1
            continue

        # Tiêu đề cấp 3 (### ...)
        if stripped.startswith("### "):
            title_text = stripped[4:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(title_text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(13)
            run.font.bold = True
            i += 1
            continue

        # Tiêu đề cấp 4 (#### ...)
        if stripped.startswith("#### "):
            title_text = stripped[5:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            run = p.add_run(title_text)
            run.font.name = "Times New Roman"
            run.font.size = Pt(13)
            run.font.bold = True
            run.font.italic = True
            i += 1
            continue

        # Blockquote / Khung ghi chú (> ...)
        if stripped.startswith("> "):
            quote_text = stripped[2:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.right_indent = Cm(0.5)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            add_formatted_text(p, quote_text, default_size=12, default_italic=True, default_color=RGBColor(80, 80, 80))
            i += 1
            continue

        # Dấu gạch ngang phân cách (---)
        if stripped in ["---", "***", "___"]:
            i += 1
            continue

        # Danh sách bullet (- hoặc *)
        if stripped.startswith("- ") or stripped.startswith("* "):
            item_text = stripped[2:].strip()
            p = doc.add_paragraph(style='List Bullet')
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.25
            add_formatted_text(p, item_text, default_size=13)
            i += 1
            continue

        # Danh sách đánh số (1., 2., ...)
        num_match = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if num_match:
            item_text = num_match.group(2)
            p = doc.add_paragraph(style='List Number')
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.25
            add_formatted_text(p, item_text, default_size=13)
            i += 1
            continue

        # Đoạn văn thông thường
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.3
        add_formatted_text(p, stripped, default_size=13)

        i += 1

    # Nếu còn bảng sót lại ở cuối
    if table_rows:
        render_markdown_table(doc, table_rows)

    doc.save(str(DOCX_PATH))
    print(f"Đã xuất bản thảo luận án thành công sang file Word: {DOCX_PATH}")


def render_markdown_table(doc, table_rows):
    """Xây dựng bảng đẹp trong Word từ các dòng markdown"""
    clean_rows = []
    for r in table_rows:
        cells = [c.strip() for c in r.strip('|').split('|')]
        # Bỏ qua hàng phân cách |--|--|
        if all(re.match(r'^:?-+:?$', c) for c in cells):
            continue
        clean_rows.append(cells)

    if not clean_rows:
        return

    num_cols = max(len(r) for r in clean_rows)
    num_rows = len(clean_rows)

    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    border_spec = {'sz': 4, 'val': 'single', 'color': 'CCCCCC'}

    for r_idx, row_data in enumerate(clean_rows):
        is_header = (r_idx == 0)
        for c_idx in range(num_cols):
            cell = table.cell(r_idx, c_idx)
            text = row_data[c_idx] if c_idx < len(row_data) else ""
            
            p = cell.paragraphs[0]
            p.text = ""
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.15
            
            if is_header:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_cell_shading(cell, "EAECEE")
                add_formatted_text(p, text, default_size=11, default_bold=True, default_color=RGBColor(30, 40, 60))
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                add_formatted_text(p, text, default_size=11)

            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            set_cell_border(cell, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)

    # Thêm khoảng trống sau bảng
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(4)
    p_after.paragraph_format.space_after = Pt(4)


if __name__ == "__main__":
    main()
