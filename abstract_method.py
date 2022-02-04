# Abstraction
# ------------

from abc import *
from random import randint
import datetime as dt


class RBI(ABC):
    @abstractmethod
    def CreateAccount(self):
        pass


class SBI(RBI):
    def __init__(self, name, accountNo=None):
        self.name = name
        self.accountNo = accountNo

    def CreateAccount(self):
        year = dt.date.today()
        self.accountNo = year.strftime('%Y') + str(randint(10, 100))
        return f'Welcome {self.name} and your account is created. Your account no is {self.accountNo}'


Bank = input('Enter your bank name: ')
Name = input('Enter your name: ')
CName = globals()[Bank.upper()]
User1 = CName(Name)
print(User1.CreateAccount())
