import json

# Define the Account class
class Account:
    def __init__(self, name, surname, account_number, pin, balance=0):
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
    
    def __str__(self):
        return f"Account Holder: {self.name} {self.surname}\nBalance: {self.balance} GEL"

# Create instances of the Account class
acc1 = Account("otari", "tchanturia", "GE12345", 1234, 5000)
acc2 = Account("mariami", "giorgobiani", "GE54321", 4321, 15000)
acc3 = Account("unknown", "person", "GE67890", 5678, 27000)

# Create a list of accounts
lst = [acc1, acc2, acc3]

# Define a serialization function for JSON serialization
def serialization(object):
    if isinstance(object, Account):
        return {
            "Name": object.name,
            "Surname": object.surname,
            "Account_number": object.account_number,
            "Pin": object.pin,
            "Balance": object.balance
        }
    return object

# Write the list of accounts to a JSON file
with open("accounts.json", "w") as json_file:
    json.dump(lst, json_file, default=serialization, indent=2)

# Define a deserialization function for JSON deserialization
def deserialization(object):
    return Account(object["Name"], object["Surname"], object["Account_number"], object["Pin"], object["Balance"])

# Define a decorator to check account existence and PIN verification
def check_account(func):
    def wrapper(self):
        # Load accounts from the JSON file
        with open("accounts.json", "r") as json_file:
            python_data = json.load(json_file, object_hook=deserialization)
        
        # Check if the account exists and the PIN is correct
        account_found = False
        for account in python_data:
            if account.account_number == self.account_number:
                account_found = True
                if self.pin == account.pin:
                    return func(self, account)
                else:
                    print("Incorrect pin!")
        
        if not account_found:
            print("Account not found!")
    return wrapper

# Define the ATM class
class ATM:
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin

    # Decorate the check_balance method with the check_account decorator
    @check_account
    def check_balance(self, account):
        print(f"Available balance: {account.balance}")

    # Define the withdraw method to withdraw money from the account
    def withdraw(self, amount):
        with open("accounts.json", "r") as json_file:
            python_data = json.load(json_file, object_hook=deserialization)

        # Find the account and perform the withdrawal
        account_found = False
        for account in python_data:
            if account.account_number == self.account_number:
                account_found = True
                if self.pin == account.pin:
                    if amount > account.balance:
                        print("Insufficient funds!")
                    else:
                        account.balance -= amount
                        print(f'Amount withdrawn: {amount}. Remaining balance: {account.balance}')
                        with open("accounts.json", "w") as json_file:
                            json.dump(python_data, json_file, default=serialization, indent=2)
                    break
                else:
                    print("Incorrect pin!")
        if not account_found:
            print("Account not found!")

    # Define the topup method to add money to the account
    def topup(self, amount):
        with open("accounts.json", "r") as json_file:
            python_data = json.load(json_file, object_hook=deserialization)

        # Find the account and perform the top-up
        account_found = False
        for account in python_data:
            if account.account_number == self.account_number:
                account_found = True
                if self.pin == account.pin:
                    account.balance += amount
                    print(f'Top up amount: {amount}. Current balance: {account.balance}')
                    with open("accounts.json", "w") as json_file:
                        json.dump(python_data, json_file, default=serialization, indent=2)
                    break
                else:
                    print("Incorrect pin!")
        if not account_found:
            print("Account not found!")

# Testing the ATM class
log = ATM(input("Enter account number: "), int(input("Enter pin: ")))
log.check_balance()
log.topup(int(input("Enter top-up amount: ")))
log.withdraw(int(input("Enter withdrawal amount: ")))
