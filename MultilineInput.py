# multi-line input
para=[]
print('Enter the details: ')
while True:
    value = input()
    if value:
        para.append(value)
    else:
        break

print('\n'.join(para))