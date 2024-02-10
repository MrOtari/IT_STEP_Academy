############# Question 1

squared = tuple(i**2 for i in range(1, 11))
print(squared)

############# Question 2

tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7) 

def func(a, b):
    c = a + b

    combined_tuple = tuple(set(c))

    duplicated_values = []
    for i in combined_tuple:
        if c.count(i) > 1:
           duplicated_values.append(i)


    return combined_tuple, tuple(duplicated_values)

print(func(tuple1, tuple2))