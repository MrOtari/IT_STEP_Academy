############# Question 1
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f'Amount withdrawn: {amount}. Remaining balance: {self.balance}')
    

    def topup(self, amount):
        self.balance += amount
        print(f'Top up amount: {amount}. Current balance: {self.balance}')


Otari = BankAccount("GE24BG2024", "Otari", 666)
Otari.topup(100)
Otari.topup(50)
Otari.withdraw(666)




############# Question 2

class Student:
    def __init__(self, name, student_id, *args):
        self.name = name
        self.student_id = student_id
        self.courses = list([*args])

    def student_info(self):
        print(f'Students name is {self.name}; Students ID is {self.student_id}.')

    def Student_courses(self):
        print(f'Student courses are {self.courses}')
    
    def add_courses(self, *args):
        for i in range(len(list([*args]))):
            self.courses.append(list([*args])[i])


otari = Student("otari", "1234", "biology", "geometry")

otari.student_info()
otari.Student_courses()

otari.add_courses("math", "physics")
otari.Student_courses()
