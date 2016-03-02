import openpyxl, os

wb = openpyxl.Workbook()
print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet')
print(sheet['A1'].value)

sheet['A1'] = 42
sheet['A2'] = 44

os.chdir('/Users/myfiles')
wb.save('data1.xlsx')
