# Exercise-1
numbers = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def even_no():
    for i in numbers:
        if i % 2 == 0:
            print(i)
even_no()


# Exercise-2.1
lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
squares = [x for x in lst if x**2 > 150]


# Exercise 2.2
numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
unique = set(numbers)
unique = [i for i in unique if i % 2 == 0]
print(unique)

def my_function(y):
    y = y + x
    x = 2
    y = y + x
    return y

x = 3
y = 10
y = my_function(x)







