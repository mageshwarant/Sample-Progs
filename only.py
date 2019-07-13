# import Second
# first = "one"
# second ="two"
# maintain(first)
# maintain(second)
#
# mylist = ["Magesh", 2, 3, 4, 5]
#
# print(mylist)
#
# myfile = open("maegsh1.txt", "w")
#
# for i in mylist:
#     myfile.write(str(i) + "\n")
#
# myfile.close()
#
#
# myfile = open("maegsh1.txt", "r")
#
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())
#

import xlrd as xl

reader = xl.open_workbook("C:\\Users\\hp\\Desktop\\Book2.xls")
sheetno = reader.sheet_by_index(0)

print(sheetno.nrows)
print(type(sheetno.ncols))

list = []
for i in range(0,sheetno.nrows):
    list.append(sheetno.cell_value(i,0))

print(len(list))
