############# Question 1

def check_positive(func):
    def wrapper(number):
        if number < 0:
            raise ValueError("Number must be positive!")
        else:
            result = func(number)
            return result
    return wrapper

@check_positive
def return_value(value):
    return value

print(return_value(5))



############# Question 2

class Functor:
    def __init__(self, func):
        self.func = func


    def __call__(self, num):
        if num < 0:
            raise ValueError("Number must be positive!")
        else: 
            return self.func(num)


def return_value(value):
    return value

my_func = Functor(return_value)

print(my_func(3))



############# Question 3

def commission(func):
    def wrapper(balance, tran_amount):
        tran_amount += 1
        if balance < tran_amount:
            return "Not enough balance!"
        else: 
            return func(balance, tran_amount)
    return wrapper

@commission
def transaction(balance, tran_amount):
    balance -= tran_amount
    return f"Balance is {balance}."

print(transaction(100, 5))