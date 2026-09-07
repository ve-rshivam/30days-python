#                                                           SET
# set is a collection of item and it is a collection of unordered and unidexed distinct elements.
# in python set is used to store unique items and 
# it is possible to find it's union, intersection, difference, symmetric difference, subset, super set and
# disjoint set among sets.
# set never follows a sequence the value we entered we get in a random sequence 
# if there are multiple same number exist in set then it is not necessary that we get that value same times that was 
# entered at the time of intializaton

# set usage a concept called hash and using hash we improve the performance we want to fetch elements as fast as possible
# # in set indexing  is not supported 

# Creating a set 
fruits = {'lemon', 'orange', 'apple', 'kiwi'}                   # initalization of set 
print(fruits)

# Getting set length
print(len(fruits))

# Checking item in set 
print('kiwi' in fruits)
print('mango' in fruits)

# Adding item to set 
fruits.add('mango')
print(fruits)
# adding multiple item in set using update() in set, update() allow multiple item addition in set
fruits.update(['banana', 'grapes', 'watermelon'])
print(fruits)

# Removing a item from set
# for removing item from set we can use remove() but it gives error when item is not found in set 
# for better we can use discard to remove a item from set 
fruits = {'lemon', 'kiwi', 'orange', 'banana', 'mango', 'grapes', 'apple', 'watermelon'}
fruits.remove('lemon')
print(fruits)
# fruits.remove('papaya')                           # it will give KeyError
print(fruits)
fruits.discard(('mango'))
print(fruits)
fruits.discard('papaya')
print(fruits)

# We can use pop() to remove random item from set
fruits = {'watermelon', 'orange', 'grapes', 'banana', 'kiwi', 'mango', 'apple'}
fruits.pop()
print(fruits)

# clearing item in a set
# it will clear or empty the set 
fruits = {'watermelon', 'orange', 'grapes', 'banana', 'kiwi', 'mango', 'apple'}
fruits.clear()
print(fruits)

# Deleting a set
# if we want to delete a set itself then we use del() operator
fruits = {'watermelon', 'orange', 'grapes', 'banana', 'kiwi', 'mango', 'apple'}
del fruits
# print(fruits)                  # Give a NameError


# converting list to set
# we can convert set to list and list to set, converting set to list remove all the duplicates and keeps only unique item
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits)
print(fruits)

# Joining sets 
# we can join two or more sets using union(), update() or | symbol 
# Union method return a new set 
fruits = {'banana', 'mango', 'kiwi', 'lemon'}
vegetables = {'carrot', 'onion', 'patato', 'tamato'}
fruits_vegetables = fruits.union(vegetables)
print(fruits_vegetables)

# update method update a set to the given set
fruits = {'banana', 'mango', 'kiwi', 'lemon'}
vegetables = {'carrot', 'onion', 'patato', 'tamato'}
fruits.update(vegetables)
print(fruits)

#Finding a intersection 
# intersection return a set item which are in both set or using & symbol 
set1 = {'item1', 'item2', 'item3', 'item4'}
set2 = {'item2', 'item3', 'item5'}
# set1.intersection(set2)               # when we use intersection like this then it intersection will be lost 
set1.intersection_update(set2)          # by using intersection_update() it will update the set1 by both set intersection 
print(set1)

# Checking subset and super set 
# A set can be subset and superset of other set
# subset: issubset()
# superset: issuperset()
whole_number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_number = {0, 2, 4, 6, 8}
print(whole_number.issubset(even_number))
print(whole_number.issuperset(even_number))

# Checking the difference of two sets
# it return the difference two set or using - symbol
whole_number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_number = {0, 2, 4, 6, 8, 10}
print(whole_number.difference(even_number))

# Finding symmetric difference between two sets
# it return the symmetric difference between two sets. It means that it return a set of containing all the items from both sets,
# except items that are present in both sets, mathematically (A\B) U (B\A)
whole_number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_number = {1, 2, 3, 4, 5}
print(whole_number.symmetric_difference(some_number))

# Joining two sets 
# if two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint
# using isdisjoint() method
even_number = {0, 2, 4, 6, 8, 10}
odd_number = {1, 3, 5, 7, 9}
print(even_number.isdisjoint(odd_number))