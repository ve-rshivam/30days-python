# A list is a type of data which can be ordered and mutable which means we can simply change it 
# A list can be empty and can have different types of data types 
# creation of list 
lst = list()                

empty_list = list()                     # it's a creation of empty list
print(len(empty_list))               

# for creating list we use square brackets []
lst = []                                #syntax
empty_list = []                         # it's a creation of empty list
print(len(empty_list))
fruits = ['mango', 'banana', 'orange', 'lemon']         # creation of a list 
print(fruits)
vegetables = ['potato', 'onion', 'tomato', 'carrot']
print(vegetables[1])                    # printing using positive index value
print(vegetables[-2])                   # printing using negative index value
# negatibe index value count from right to left and it start from -1
# list can have different types of data types 
intro = ['Shivam Kumar',19, True, None, 5.11,{'Country': 'India', 'City': 'New Delhi'}]
print(intro)

# unpacking elements 
web_techs = ['HTML', 'CSS', 'Talwind', 'Python']
number1, number2, number3, *number4 = web_techs
print(number1)
print(number2)
print(number3)
print(number4)         # it's for remaining all the item which is present in web_techs or in a list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)                         # if we use * on  any key or variable naming it store all the upcoming variable value in them until unless we create a another variable after *rest that value store in that variable 
print(tenth)

# slicing positive index 
tech_stacks = ['HTML', 'CSS', 'Python', 'Java', 'C++', 'JS']
print(tech_stacks[0:4])                     # it wil print all the first four 
print(tech_stacks[0:])                      # it will print all 
print(tech_stacks[1:5])                     # it will not include the index zero and print upto 5 that means print only until index value 4
print(tech_stacks[1:])                      # it will print all the elements after index 0 and index 0 is not included
print(tech_stacks[::2])                     # it will take every 2 elements of the list starting from index 0 

# slicing positive index 
tech = ['HTML', 'CSS', 'Python', 'Java', 'C++', 'JS']
print(tech[-4:])                # it will print last 4 
print(tech[-3:-1])              # it does'nt include last index number which is -1
print(tech[-3:])                # it will give last 3 from end 
print(tech[::-1])               # it will give all in reverse order
print(type(tech))

# modify list 
# a list can be mutable or modifiable ordered collection of item 
fruits = ['mango', 'banana', 'lemon', 'orange']
fruits[0] = 'avocado'
print(fruits[0])
fruits[1] = 'apple'
print(fruits[1])
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits[last_index])

# checking item in the list 
fruits = ['mango', 'banana', 'lemon', 'orange']
print('mango' in fruits)
print('lime' in fruits)

# adding item to the list using append
fruits.append('apple')
print(fruits)             # in list wenever we add any item in it. it add in the last index 
fruits.append('lime')
print(fruits)

# adding item in list using index number  while using this it help us to to insert the value where we want 

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'lime')                # first we assign the index number then add the item which we want to add 
print(fruits)
fruits.insert(3,'apple')
print(fruits)

# removing a item from a list 
# the remove methods is used for removing a specific item from list 

fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

# removing the item using pop from a specific index and if the index is not stated then it pop out the last index item
fruits = ['apple', 'orange', 'mango', 'banana', 'lemon', 'lime']
fruits.pop(3)                   # here the index is defined so his index item is removed or pop out
print(fruits)
fruits.pop()                    # here the index is not defined s othe last index item will be poped out
print(fruits)

# removing items using del 
# del() is used to remove item using index value and also used to delete item in range of index and also used to delete entire list when the index number is not defined
fruits = ['apple', 'orange', 'mango', 'banana', 'lemon', 'lime', 'kiwi']
del fruits[1]
print(fruits)
del fruits[1:3]                 # here last index is for upto not included
print(fruits)
del fruits
# print(fruits)              # now it will give name error and fruits is not defined 

# Clearing the list 
# the clear method is used to empty the list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)                           # now the list is empty it will print []

# Copying a list 
# it is possible to copying a list and assign into new variable: list2 = list1. now the list2 is a refrence of list1 any change 
# made in list2 will be modify in original, but in lots of case we don't need to modify the original instead we like a like to have a
# different copy that's why we use copy() from the above problem

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)


# Joining a list 
# there are several way to join, or concatenate two or more than two list 
# Using plus operator(+)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# Using .extend()   this allow to append list 
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

# Counting a item in a list 
# counting is basically used to count that how many some item appear in the list 

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           

# Finding a index of item 
# index() is uses to find the index number of a item 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   
ages = [22, 19, 24, 25, 26, 24, 25, 24]                 # if the some is repeating many time then it will give the first item index number 
print(ages.index(24))

# Reversing a list 
# this method is used to reverse a list 
fruits = ['mango', 'lemon', 'banana', 'apple']
fruits.reverse()
print(fruits)
number = [23, 19, 24, 25, 26, 24, 25,24]
number.reverse()
print(number)

# Sorting the item 
# To sort a list we use sort() or sorted() which will cause to sortthe list in ascending order or modifies the original list.
# if an argument of sort method reverse is equal to true then it give the list in descending order

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)                                       # it will sort the item in alphabetically order of first letter
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)                                         # ascending order
ages.sort(reverse=True)
print(ages)                                         # decending order