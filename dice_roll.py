# Dice Roll

from random import randint as diceroll
print('Game Starts')
roll_again = True
while roll_again:
    print('Dice value: ', diceroll(1, 6))
    roll = input('Roll again(Y/N)? ')
    if roll.lower() =='y':
        roll_again = True
    else:
        roll_again = False