############# Question 1

num_list = [100,20,30,50,5323,3321,22,56,700,90,10]

def sum_list(number_list):
    sum = 0
    for i in number_list:
        sum += i
    return sum

print(sum_list(num_list))


############# Question 2

def sum_digits(num):
    if len(str(num)) == 1:
        return num
    else:
        return num%10 + sum_digits(num//10)

print(sum_digits(int(input("Enter digit: "))))


############# Question 3

def reverse(text):
    if len(text) == 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])

print(reverse(input("Enter text: ")))

############# Question 4

def fibonachi(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fibonachi(num-1)

print(fibonachi(int(input("Enter number: "))))