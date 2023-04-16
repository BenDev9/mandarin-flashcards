from docx.enum.table import WD_ALIGN_VERTICAL
from docx.shared import Cm, Pt


def format_card(card):
    return card["Front"], card["Back"]


def format_table(fronts, backs):
    for f_row in fronts.rows:
        f_row.height = Cm(4)

        for cell in f_row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell.paragraphs[0].style.font.size = Pt(30)

    for b_row in backs.rows:
        b_row.height = Cm(4)

        for cell in b_row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell.paragraphs[0].style.font.size = Pt(30)
