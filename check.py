'''with open("C:\\Users\\hp\\Desktop\\csvreader.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)'''
import datetime
import gzip
print datetime.datetime.now()
f_in = open('C:\\Users\\hp\\Desktop\\zips.csv', 'rb')
f_out = gzip.open('C:\\Users\\hp\Desktop\\test\\zips.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()
print datetime.datetime.now()
'''fileHandle = open('C:\\Users\\hp\\Desktop\\zips.csv', 'r')

for line in fileHandle:
    fields = line.split(',')
# prints the second fields value
print fields
print '----------------------'
for line in fileHandle:
    fields = line.split('\n')
    fild = fields.split(',')
# prints the second fields value
print fild
fileHandle.close()'''