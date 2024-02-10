############# Question 1


text = input("Enter text: ")

if text.replace(" ", "") == text.replace(" ", "")[::-1]:
    print("The text entered is a palindrome.")
else:
    print("The text entered is not a palindrome.")



############# Question 2

text_ascii = input("Enter text: ")

ascii_sequence = [ord(char) for char in text_ascii]

print(ascii_sequence)