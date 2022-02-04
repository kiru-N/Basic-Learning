# Method Overrriding

class Parent:
    def __init__(self):
        print('Parent class Constructor')

    def study(self):
        print('Engineering')

class Child(Parent):
    def __init__(self):
        # super().__init__()
        print('Child class constructor')

    def play(self):
        print('I like kabadi')

    def study(self):
        # super().study()
        print('science')

c =Child()
c.study()
print(isinstance(c,Child))
