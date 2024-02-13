class Person:
    def __init__(self, name, deposit = 1000, loan = 0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"


class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        if not isinstance(owner, Person):
            raise TypeError("Wrong person")
        else: self.owner = owner
        self.status = "for sale"
    
    def sell(self, buyer):
        print(f'{buyer}')


seller = Person("seller")
buyer = Person("buyer")
home = House("GE1234", 1200, seller)

print(home.status)
print(home.owner)
