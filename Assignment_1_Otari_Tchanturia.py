############# Question 1

num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))
num3 = int(input("Enter the third whole number: "))

total_sum = num1 + num2 + num3

print(f"The sum of {num1}, {num2}, and {num3} is: {total_sum}")


############# Question 2

lenght = float(input("Enter the the length of the side of the cube: "))

V = lenght**3
S = 6*lenght**2

print(f"V = {V} and S = {S}")


####    ######### Question 3

screen = float(input("Enter the price of screen: "))
sys_block = float(input("Enter the price of system block: "))
keyboard = float(input("Enter the price of keyboard: "))
mouse = float(input("Enter the price of mouse: "))

sum_price = screen + sys_block + keyboard + mouse

print(f"Price of all components is {sum_price}")