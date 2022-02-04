# Linear Search

list1 = [1,2,34,6,78,12,45,99,36]

find = int(input('Enter the value to search: '))

if find in list1:
    print(f'Value {find} found at position {list1.index(find)}')
else:
    print(f'Value {find} not found')

stu_count = int(input('Enter the Total number of Student: '))
sub = ('Tamil', 'English', 'Maths', 'Science', 'Social')
report = {}
for cnt in range(stu_count):
    name = input('Enter the student Name %d: ' % (cnt + 1))
    marks = []
    for subject in sub:
        marks.append(int(input('Enter the marks %s: ' % subject)))
    report[name] = marks

print(report)

for name, mark in report.items():
    total = sum(mark)
    avg = total / 5
    print('%s \'s total is %d' % (name, total))
    if total > 175:
        print('%s is passed' % name)
    else:
        print('%s is failed' % name)
