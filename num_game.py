import random

li = list(range(10))
cp = random.choices(li, k=4)


guess = 'N'
while guess == 'N':
    choice = input('enter the numbers: \n').split()
    for i in choice:
        if int(i) in cp:
            if choice.index(i) == cp.index(int(i)):
                print('C', end=' ')
                guess = 'Y'
            else:
                print('P', end=' ')
                guess = 'N'
        else:
            print('X', end=' ')
            guess = 'N'
    print()

print('Wow you found the answers')