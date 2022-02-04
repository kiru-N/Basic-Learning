cont = 'Y'
print(' Basic Calculator ')
print('------------------')
print(''' operations:
        1  --> Addition
        2  --> Subtraction
        3  --> Multiplication
        4  --> Division
        5  --> Modulus
        6 --> Power operator
        7 --> Floor Division ''')

while cont.upper() == 'Y':
    num1 = float(input('Enter the number: '))
    operator = int(input('Enter your choice: '))
    num2 = float(input('Enter the number: '))
    if operator == 1:
        result = num1 + num2
    elif operator == 2:
        result = num1 - num2
    elif operator == 3:
        result = num1 * num2
    elif operator == 4:
        result = num1 / num2
    elif operator == 7:
        result = num1 // num2
    elif operator == 5:
        result = num1 % num2
    elif operator == 6:
        result = num1 ** num2
    else:
        print('Enter the valid choice(1~7):')

    print(f'{num1} {operator} {num2} = {result}')
    cont = input('Do you want to try again?(Y/N): ')