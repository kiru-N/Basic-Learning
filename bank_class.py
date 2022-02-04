import sys

class Customer:
    bank = 'ICICI Bank'
    def __init__(self,name,accountNo,balance=500):
        self.name = name
        self.accno = accountNo
        self.balance =balance

    def deposit(self,amount):
        self.balance += amount
        print('The total balance in your account is ',self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient Balance')
        else:
            self.balance -= amount
            print('The total balance in your account is ', self.balance)


print(f'Welcome to {Customer.bank}')
name = input('Enter your name: ')
accountNo = int(input('Enter your account number: '))
cust1 = Customer(name,accountNo)
cont = 'Y'
while cont == 'Y':
    print('W - Withdraw , D - Deposit, E - Exit')
    choice = input('Please Enter your valid choice: ')
    if choice == 'W':
        amt = int(input('Amount to withdraw: '))
        cust1.withdraw(amt)
    elif choice == 'D':
        amt = int(input('Amount to Deposit: '))
        cust1.deposit(amt)
    elif choice == 'E':
        sys.exit()
    cont = input('Do you want to continue Y/N: ')