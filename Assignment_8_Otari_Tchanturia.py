############# Question 1

lst1 = [1, 2, 3]
lst2 = ["a", "b", "c"]
print(list(zip(lst1, lst2)))

############# Question 2

lst = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(lambda a: a % 2, lst)))


############# Question 3

lst = [1, -2, 3, -4, 5, 6, -7]
print(list(filter(lambda a: a > 0, lst)))


############# Question 4

lst = ["adam", "badam", "faaf", "dam", "ama"]
print(list(filter(lambda a: a == a[::-1], lst)))


############# Question 5

import functools
lst = [1, 2, 3, 4, 5]

try:
    print(functools.reduce(lambda a, b: a*b, lst))
except ValueError:
    print("Invalid list")

############# Question 6

lst = ["adaming", "badam", "faaf", "dam", "ama"]

try:
    print(list(filter(lambda a: a[-3:] == "ing", lst)))
except ValueError:
    print("Invalid list")
