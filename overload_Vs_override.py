"""
Operator overloading means when we use a operator with a user defined methode, its called operator overloading. 
For example:
"""
class Person:
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
    def __gt__(self, other):
        return self.age > other.age

p1 = Person('Sakib', 22, 'Dhaka')
p2 = Person('Mahdfuz', 23, 'Cumilla')

if p1>p2:
    print('Sakib Buro')

else:
    print('Mahfuz Buro')


