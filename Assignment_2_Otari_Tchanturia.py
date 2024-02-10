############# Question 1

num1 = float(input("Enter the integer number: "))

if num1 % 2 == 1:
    print(f"{num1} is odd")
elif num1 % 2 == 0:
    print(f"{num1} is even")
else:
    print("Please enter integer number")


############# Question 2

sent = input("Enter the sentence: ")

a = "small"
b = "tall"
c = "middle"

if a in sent and  b in sent and c in sent:
    if sent.index(a) < sent.index(b) and sent.index(a) < sent.index(c):
        print(a)
    elif sent.index(b) < sent.index(a) and sent.index(b) < sent.index(c):
        print(b)
    else: print(c)
elif a in sent and  b in sent:
    if sent.index(a) < sent.index(b):
        print(a)
    else: print(b)
elif a in sent and  c in sent:
    if sent.index(a) < sent.index(c):
        print(a)
    else: print(c)
elif b in sent and  c in sent:
    if sent.index(b) < sent.index(c):
        print(b)
    else: print(c)
elif a in sent:
    print(a)
elif b in sent:
    print(b)
elif c in sent:
    print(c)
else:
    print("None of the words small or tall or middle are found in the text")



############# Question 3

num1 = int(input("Enter the first number: "))
operation = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))

if operation == '+':
    result = num1 + num2 
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Invalid number, Can't divide by zero. Please enter nonzero number!"
    else:
        result = num1 / num2
elif operation == '//':
    if num2 == 0:
        result = "Invalid number, Can't divide by zero. Please enter nonzero number!"
    else:
        result = num1 // num2
elif operation == '%':
    if num2 == 0:
        result = "Invalid number, Can't divide by zero. Please enter nonzero number!"
    else: result = num1 % num2
elif operation == '**':
    result = num1 ** num2
else:
    print("Invalid operation. Please enter +, -, *, or /.")

print(result)