############# Question 1

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
sum = mylist[2] + mylist[8] + mylist[13]
print(sum)


############# Question 2

import random

list = []
list = random.sample(range(0, 100), 10)
print(list)

print(max(list))
print(min(list))

############# Question 3

my_llist = [43, '22', 12, 66, 210, ["hi"]]

print(my_llist.index(210))

my_llist[-1].append("hello")
print(my_llist)

my_llist.remove(my_llist[2])
print(my_llist)

my_llist2 = my_llist.copy() 
my_llist2.clear()
print(my_llist)
print(my_llist2)


############# Question 4

matrix1 = [[1,2,3], 
           [4,5,6], 
           [7,8,9]]

matrix2 = [[1,2,3], 
           [4,5,6], 
           [7,8,9]]

add_matrix = [[0,0,0],
          [0,0,0],
          [0,0,0]]


for i in range(len(matrix1)):   
    for j in range(len(matrix1[0])):
        add_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

print(add_matrix)



############# Question 5

matrix3 = [[1,2,3], 
           [4,5,6], 
           [7,8,9]]

tran_matrix = [[0,0,0],
               [0,0,0],
               [0,0,0]]

for i in range(len(matrix3)):
   for j in range(len(matrix3[0])):
       tran_matrix[j][i] = matrix3[i][j]

print(tran_matrix)