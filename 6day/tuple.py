#                                                            Tuples 
# Tuples is collection of different kind of data types which is ordered and immutable or unchangeable .
# tuples are written in small brakets () and once they are created then it can be change i.e. add, insert, remove all these 
# operations can't be perform in tuples but likely list tuple has also it's own methods:
# tuple(): to create an empty tuple
# count(): to count the number of specified item in a tuple
# index(): to find the index of specified item 
# + operator: to join two or more tuple and create a new tuple 

# Creating a empty tuple 
empty_tuple = tuple()
# tuple with initial value
fruits = ('banana', 'mango', 'orange', 'kiwi')
# tuple length 
print(len(fruits))
# accessing tuple using index value 
# positive index 
first = fruits[0]
print(first)
second = fruits[1]
print(second)
third = fruits[2]
print(third)
fourth = fruits[3]
print(fourth)

# negative index 
first = fruits[-1]
print(first)
second = fruits[-2]
print(second)
third = fruits[-3]
print(third)
fourth = fruits[-4]
print(fourth)

# Slicing a tuple 
# We can slice a tuple into a sub-tuple by specifying a index that where to start and where to end 
# and the return value will be a new tuple with the specified item
# range of positive index 
fruits = ('banana', 'mango', 'orange', 'kiwi', 'lemon')
all_fruits = fruits[0:5]
all_fruits1 = fruits[0:]
middle_two = fruits[1:3]                # it does not include index 3 it will print only index 1 and 2 value
print(all_fruits)
print(all_fruits1)
print(middle_two)

# range of negative index
fruits = ('banana', 'mango', 'orange', 'kiwi', 'lemon')
all_fruits11 = fruits[-4:]
middle_two1 = fruits[-3:-1]                  # it does not include index -1 and it only print -3 and -2 index value 
print(all_fruits11)
print(middle_two1)

# Changing tuple to list
# we can change tuple to list and list to tuple by using type-casting. Tuple is immutable if we want to modify tuple then 
# we have to convert in list 
fruits = ('banana', 'mango', 'orange', 'kiwi', 'lemon')
print(fruits)
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)

# Checking a item in tuple 
# we can check if a item exists or not in tuple by using 'in' and return a boolean
fruits = ('banana', 'mango', 'orange', 'kiwi', 'lemon')
print('orange' in fruits)
print('apple' in fruits)
# fruits[0] = 'apple'                     # it will give a TypeError because tuple does'nt support item asignment

# Joinig two tuple
# we can join two tuple using + operator
fruits = ('banana', 'mango', 'orange', 'kiwi', 'lemon')
vegetables = ('onion', 'potato', 'tamato', 'carrot')
print(fruits)
print(vegetables)
fruits_vegetables = fruits + vegetables
print(fruits_vegetables)

# Deleting tuples
# it is not possible to remove a  single item of tuple but it is possible to delete a tuple itself using del.
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
# print(fruits)               # now it will give a NameError because fruits is deleted 