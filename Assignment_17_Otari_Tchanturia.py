from multipledispatch import dispatch

class Person:
    def __init__(self, name, deposit=1000, loan=0):
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
            raise TypeError("Wrong Person!")
        else:
            self.owner = owner
        self.status = "For Sale"
    
    def __str__(self):
        return f"House price: {self.price}, Owner: {self.owner.name}, Status: {self.status}"
    
    @dispatch(Person)
    def sell(self, home_buyer):
        self.owner.deposit += self.price
        home_buyer.deposit -= self.price
        self.owner = home_buyer
        self.status = "Sold"
        print(f'This house has been bought for {self.price} dollars by {self.owner.name}')
    
    @dispatch(Person, int)
    def sell(self, home_buyer, loan_amount):
        self.owner.deposit += self.price
        home_buyer.loan += loan_amount
        self.owner = home_buyer
        self.status = "Sold by Loan"
        print(f'This house has been bought by loan for {self.price} dollars by {self.owner.name}')


seller = Person("otari")
buyer = Person("irakli")
home = House("GE1234", 600, seller)

print(seller)
print(buyer)
print(home)

home.sell(buyer, 700)

print(seller)
print(buyer)
print(home)