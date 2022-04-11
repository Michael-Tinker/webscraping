
from tkinter import font
import openpyxl as xl
from openpyxl.styles import Font

from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

#create a new excel document
wb = xl.Workbook()

MySheet = wb.active

MySheet.title = "First Sheet"


#alternatively you can create a font object and assign it

fontobject = Font(size=16, bold=True)
MySheet['A1'].font = fontobject
MySheet['B1'].font = fontobject
MySheet['C1'].font = fontobject
MySheet['D1'].font = fontobject
MySheet['E1'].font = fontobject
MySheet['F1'].font = fontobject


table_rows = soup.findAll("tr")


MySheet['A1'] = "Rank"
MySheet['B1'] = "Title"
MySheet['C1'] = "Release Date"
MySheet['D1'] = "Gross"
MySheet['E1'] = "Total Gross"
MySheet['F1'] = "% of Total Gross"


MySheet['C1'].font = fontobject
MySheet['D1'].font = fontobject
MySheet['E1'].font = fontobject
MySheet['F1'].font = fontobject

rownum = 2
for row in table_rows[1:6]:
    #print(row)
    td = row.findAll("td")
    rank = td[0].text.strip()
    release = td[1].text.strip()
    genre = td[2].text
    money_type = td[3].text
    duration = td[4].text
    gross = td[5].text
    gross_num = int(gross.replace(",","").replace("$",""))
    theaters = td[6].text
    total_gross = td[7].text
    total_gross_num = int(total_gross.replace(",","").replace("$",""))
    release_date = td[8].text
    distributor = td[9].text

    #print(rank + " - " + release + " - Gross Total: " + total_gross + "\n")

    MySheet["A" + str(rownum)] = rank
    MySheet["B" + str(rownum)] = release
    MySheet["C" + str(rownum)] = release_date
    MySheet["D" + str(rownum)] = gross
    MySheet["E" + str(rownum)] = total_gross
    MySheet["F" + str(rownum)] = str(round((gross_num/total_gross_num)*100,2)) + "%"

    rownum += 1

ws.column_dimension["A"].width = 5
#30, 25, 16, 20 ,26

#for cell in ws[1:1]:
#    cell.font = header_font

wb.save("PythonToExcel.xlsx")
