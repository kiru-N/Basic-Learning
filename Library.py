# Library
# ---------

days = int(input('Enter the number of days: '))
if days==0:
    print('No Fine.')
elif 1<=days<=5:
    print(f'Fine amount is {days*0.5} rupees')
elif 5<days<=10:
    print(f'Fine amount is {days * 1} rupees')
elif 10<days<=30:
    print(f'Fine amount is {days * 5} rupees')
elif days>30:
    print('Membership cancelled')
else:
    print('Enter the valid dates')

print('Thank you')