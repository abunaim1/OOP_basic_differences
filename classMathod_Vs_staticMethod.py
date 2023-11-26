"""
1. use a decorator @classmethod for classmethod, and @staticmethod.
2. staticmethod does not contain any self but classmethod does.
3. we use staticmethod and classmethod when we need to call a method with the class name just.
4. staticmethod behaves like a regular function, these methods are used to do some utility tasks by taking some parameters. but is defined inside a class for organizational purposes. While, a classmethod takes the class as its first argument, which allows it to modify class-level attributes.
"""
class Bank:
    def __init__(self, name, location, fixed) -> None:
        self.name = name
        self.location = location
        self.fixed = fixed
    
    @classmethod
    def acc(self, id):
        print(f'your bank id: {id}')
    
    def add_balance(self, amount):
        self.fixed += amount 
    
    @staticmethod
    def get_balance(a,b):
        print(a*b)

UCB = Bank('UCB', 'Dhaka', 2000)
UCB.add_balance(3000)
print(Bank.acc(41501656))
Bank.get_balance(20,20)

