############# Question 1

num = int(input("Enter positive number"))

while num > 0:
    print(num)
    num -= 1


############# Question 2

total_sum = 0
text = input("Enter number or sum: ")

while text != "sum":
    if float(text) > 0:
        total_sum += float(text)
    text = input("Enter number or sum: ")

print(total_sum)

############# Question 3

import random

life = 5

num = random.randint(1, 100)

user_num = int(input("Guess number between 1 and 100: "))
life -= 1

while life > 0:
    if num == user_num:
        print("You won!")
        break
    else:
        if user_num > num:
            print("Your number is higher.")
        else: print("Your number is lower.")
    print(f"You have left {life} tries!")
    life -= 1
    user_num = int(input("Try again: "))
else: print("You lost.")