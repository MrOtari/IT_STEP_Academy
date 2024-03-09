### ATM

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




### Hangman

# List of words for the game
word_list = ["python", "hangman", "program", "computer", "keyboard", "monitor", "mouse", "printer", "scanner"]

# Function to choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Function to initialize the display word with underscores
def initialize_display_word(word):
    return "_" * len(word)

# Function to update the display word with correctly guessed letters
def update_display_word(word, display_word, letter):
    updated_display_word = ""
    for i in range(len(word)):
        if word[i] == letter:
            updated_display_word += letter
        else:
            updated_display_word += display_word[i]
    return updated_display_word

# Main function to run the Hangman game
def hangman():
    word = choose_word(word_list)
    display_word = initialize_display_word(word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")
    print(display_word)

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            display_word = update_display_word(word, display_word, guess)
            print(display_word)
            if "_" not in display_word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", word)
            else:
                print(display_word)

# Run the game
hangman()