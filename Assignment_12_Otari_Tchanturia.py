############# Question 1
txt = "The wind howled and howled all night long"

def count_word_frequency(sentence):

    words = sentence.split()

    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

print(count_word_frequency(txt))

############# Question 2

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error! Division by zero."
}


def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator in operations:
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Invalid operator.")