import openpyxl
book =openpyxl.load_workbook("/home/bridgeit/Downloads/gnani.xlsx")
sheet=book.active
cell=sheet.cell(row=1,column=2)
print(cell.value)