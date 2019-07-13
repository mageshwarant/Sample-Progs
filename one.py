# import Second
# first = "one"
# second ="two"
# maintain(first)
# maintain(second)

mylist = ["Magesh", 2, 3, 4, 5]

print(mylist)

myfile = open("maegsh1.txt", "w")

for i in mylist:
    myfile.write(str(i) + "\n")

myfile.close()


myfile = open("maegsh1.txt", "r")

print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())


import xlrd as xl

xl.open_workbook("")