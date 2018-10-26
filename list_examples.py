num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using max(iterable, *iterables, key)
print('Maximum is:', max(num, num1, num2, key=len))


def test_max_len_list():
    assert [15, 300, 2700, 821] == max(num, num1, num2, key=len)


def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

# using max(arg1, arg2, *args, key)
print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit))

# using max(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print('Maximum is:', max(num, key=sumDigit))

"""
all()	Return True if all elements of the list are true (or if the list is empty).
any()	Return True if any element of the list is true. If the list is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	Return the length (the number of items) in the list.
list()	Convert an iterable (tuple, string, set, dictionary) to a list.
max()	Return the largest item in the list.
min()	Return the smallest item in the list
sorted()	Return a new sorted list (does not sort the list itself).
sum()	Return the sum of all elements in the list.
"""

# Python Program to find numbers divisible by thirteen from a list using anonymous function

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)