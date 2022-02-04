# read an write CSV file
# -----------------------

import csv

file1 = open('C:/Users/NEVIN/Desktop/Kiru/test.csv','w',newline='')
w = csv.writer(file1)
w.writerow(['SID','SNAME','STUDADDRESS'])
count = int(input('Enter students count: '))
for i in range(count):
    sid = input('Enter student id: ')
    sname = input('Enter student name: ')
    saddress = input('Enter Student address: ')
    w.writerow([sid,sname,saddress])
file1 = open('C:/Users/NEVIN/Desktop/Kiru/test.csv','r',newline='')
r = csv.reader(file1)
read1 = list(r)
for i in read1:
    print(i)
