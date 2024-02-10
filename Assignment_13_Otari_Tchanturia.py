############# Question 1

with open("text.txt", 'w') as file:
    for i in range(1, 1001):
        file.write(f"{i}. This is line number {i}\n")


count = 0

with open("text.txt", 'r') as file:
    for line in file:
        count += 1
print(f'Number of lines in file is {count}!')



############# Question 2

numbers_with_text = {
        2: "two",
        8: "Eight",
        10: "Ten",
        13: "Thirteen",
        17: "Seventeen"}


with open("text_with_names.txt", 'w') as file:
    for i in range(1, 21):
        if i in numbers_with_text:
            file.write(f"{numbers_with_text[i]}\n")
        else:
            file.write(f"This is line {i}\n")

with open("text_with_names.txt", 'r') as file:
    for line in file:
        print(line.strip())




############# Question 3

with open("text1.txt", 'w') as file:
    for i in range(1, 6):
        file.write(f"{i}. This is first text line number {i}\n")

with open("text2.txt", 'w') as file:
    for i in range(1, 11):
        file.write(f"{i}. This is second text line number {i}\n")

with open("text1.txt", 'r') as file1:
        file1_content = file1.readlines()

with open("text2.txt", 'r') as file2:
        file2_content = file2.readlines()

merged_content = file1_content + file2_content

with open("text_merged.txt", 'w') as merged_file:
        merged_file.writelines(merged_content)


with open("text_merged.txt", 'r') as merged_file:
    for line in merged_file:
        print(line.strip())