# Voting
# ---------
name =input('Enter your name: ')
age = int(input('Please enter your age: '))

if age >=18:
    print(f'{name}, You are eligible to vote')
else:
    print(f'Sorry {name}, You are not eligible')