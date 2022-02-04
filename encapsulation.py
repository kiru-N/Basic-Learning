# Encapsulation
# -------------

class Test:
    a =10
    _b =20
    __c =30
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

emp1  = Test('Neer',3000)
print(emp1.name)
print(emp1.a)
print(emp1._b)
print(emp1._Test__c)
print(emp1._Test__salary)
