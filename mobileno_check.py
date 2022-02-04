import re

def Ismobile(num):
    pattern = re.compile('((91|0)(\d{2,4}))-([1-9]\d{5,8})')
    return pattern.search(num)


num = input('Enter The number: ')
result = Ismobile(num)
print(result.groups())
if result.group(2) == '91':
    if len(result.group(1)) + len(result.group(4)) == 12:
        print('Valid Phone number')
    else:
        print("Invalid Phone number")
elif result.group(2) == '0':
    if len(result.group(1)) + len(result.group(4)) == 11:
        print('Valid Phone number')
    else:
        print("Invalid Phone number")
else:
    print("Invalid Phone number")