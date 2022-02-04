# Random module - Guessing a number

num = random.randint(1, 10)
print(num)
guess = int(input('Guess a number (1~10): '))
while True:
    if guess == num:
        print('You are a genius!!')
        break
    elif guess > num:
        print('Your guess is higher')
    else:
        print('Your guess is lower')
    guess = int(input('Guess a number again(1~10): '))