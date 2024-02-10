############# Question 1

def anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

string1 = input("Enter first word: ")
string2 = input("Enter second word: ")
result = anagram("listen", "silent")
print(f"This is anagram: {result}")



############# Question 2

def number_of_character(text, character):
    count = 0
    for i in text:
        if i == character:
            count += 1
    return count

text = input("Enter text: ")
character = input("Enter character: ")

print(number_of_character(text, character))



############# Question 3

def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    if n == 0:
        return fibonacci_sequence

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

num = int(input("Enter number: "))
print(generate_fibonacci(num))