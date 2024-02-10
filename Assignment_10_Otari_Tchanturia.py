############# Question 1

import random
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)


### Linear Search

def linear_search(lst, value):
    for i, num in enumerate(lst):
        if num == value:
            return i
    return -1

print(linear_search(randomlist, 26))


### Sorting

def selectionSort(lst):
    
    for ind in range(len(lst)):
        min_index = ind
 
        for j in range(ind + 1, len(lst)):

            if lst[j] > lst[min_index]:
                min_index = j

        (lst[ind], lst[min_index]) = (lst[min_index], lst[ind])


selectionSort(randomlist)


### Binary Search

def binary_search(lst, value):
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(binary_search(randomlist, 18))


############# Question 2

lambda_function = lambda x: x % 3 == 0

def three_multipliers(lst, lamb):
    new_lst = []
    for i, num in enumerate(lst):
        if lamb(num):
           new_lst.append(i)
    return new_lst

print(three_multipliers(randomlist, lambda_function))
