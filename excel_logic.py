from openpyxl import Workbook
from openpyxl.styles import Alignment

wb = Workbook()
ws = wb.active

# set column width


def set_column_widths():
    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 50
    ws.column_dimensions['C'].width = 40
    ws.column_dimensions['D'].width = 30
    ws.column_dimensions['E'].width = 30
    ws.column_dimensions['F'].width = 30

# set column names


def set_column_names():
    ws.cell(row=1, column=1, value="S.No")
    ws.cell(row=1, column=2, value="Name")
    ws.cell(row=1, column=3, value="Category")
    ws.cell(row=1, column=4, value="Subscribers")
    ws.cell(row=1, column=5, value="Average Views")
    ws.cell(row=1, column=5, value="Channel Link")


set_column_widths()
set_column_widths()
