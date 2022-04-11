from tkinter import font
import openpyxl as xl
from openpyxl.styles import Font


#create a new excel document
wb = xl.Workbook()

MySheet = wb.active

MySheet.title = "First Sheet"

#create a new worksheet
wb.create_sheet(index=1,title="second sheet")

#write content to a cell
MySheet['A1']='An example of Sum Formula'

#change the font size and italicize
MySheet['A1'].font = Font(name="Times New Roman", size=24, italic=True,bold=True)

#alternatively you can create a font object and assign it

fontobject = Font(name="Times New Roman", size=24, italic=True,bold=True)
MySheet['A1'].font = fontobject

#adding values to cells
MySheet['B2'] = 50
MySheet['B3'] = 75
MySheet['B4'] = 100
MySheet['A5'] = "Total"
MySheet['A5'].font = Font(size=16,bold=True)

MySheet['B5'] = '=SUM(B2:B4)'

#change the column width
MySheet.column_dimensions['A'].width = 25



wb.save("PythonToExcel.xlsx")
