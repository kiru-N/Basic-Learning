# User defined Exception
# ------------------------

class InsufficientBalanceException(Exception):
    def __init__(self):
    #     self.message = 'Insufficient Balance'
        pass

try:
    balance =1000
    amount = int(input('Enter the amount: '))
except ValueError:
    print('Enter a valid number')
else:
    try:
        if amount > balance:
            raise InsufficientBalanceException
    except InsufficientBalanceException:
        print('Please check your balance')
    else:
        balance -= amount
        print('The remaining balance is ', balance)
finally:
    print('Thank you!!')