############# Question 1

import random
randomlist = random.sample(range(0, 1000), 100)

randomlist.sort()
print(randomlist)

print(sorted(randomlist, reverse=True))


############# Question 2


def bubbleSort(lst):
    n = len(lst)
    swapped = False

    for i in range(n-1):

        for j in range(0, n-i-1):
 
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
         
        if not swapped:
            return


bubbleSort(randomlist)
print(randomlist)


def selectionSort(lst):
    
    for ind in range(len(lst)):
        min_index = ind
 
        for j in range(ind + 1, len(lst)):

            if lst[j] > lst[min_index]:
                min_index = j

        (lst[ind], lst[min_index]) = (lst[min_index], lst[ind])


selectionSort(randomlist)
print(randomlist)