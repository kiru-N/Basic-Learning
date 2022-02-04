try:
    a = int(input('Enter Number 1: '))
    b = int(input('Enter Number 2: '))
except ValueError:
    print('Please check the number you entered')
else:
    try:
        output = a / b
    except ZeroDivisionError:
        print('The Denominator shouldn\'t be zero')
    else:
        print(output)
finally:
    print('The program completed')