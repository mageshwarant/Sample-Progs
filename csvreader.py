'''import csv

with open('C:\\Users\\hp\\Desktop\\zips.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)'''
import gzip
import datetime
import StringIO
import csv
#input = StringIO.StringIO()
print datetime.datetime.now()

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

input_file = gzip.open("C:\\Users\\hp\\Desktop\\test\\1.gz", 'rb')
try:
    input = StringIO(input_file.read())
finally:
    input_file.close()


value = input.getvalue()

#value1 = value.pop()
#v1=value.split("\n")
#print v1
result = [row for row in csv.reader(value.split('\n'), delimiter=',')]
print len(result)
Value1 = result.pop(0)
value2 = result.pop(len(result)-2)
print Value1
print value2
print len(result)

#print value2
#break
#print listen
print datetime.datetime.now()



#print input.read()