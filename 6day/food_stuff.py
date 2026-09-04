#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('mango', 'apple', 'orange', 'lemon')
vegetables = ('carrot', 'tamato', 'onion', 'potato')
animal_product = ('product1', 'product2', 'product3')
print(fruits)
print(vegetables)
print(animal_product)
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt = ['mango', 'apple', 'orange', 'lemon', 'carrot', 'tamato', 'onion', 'potato', 'product1', 'product2', 'product3']
del food_stuff_lt[len(food_stuff_lt) // 2]                              # tamato
print(food_stuff_lt)
# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[0:3]
print(first_three)
food_stuff_lt = ['mango', 'apple', 'orange', 'lemon', 'carrot', 'onion', 'potato', 'product1', 'product2', 'product3']
last_three = food_stuff_lt[7:]
print(last_three)
# Delete the food_stuff_tp tuple completely

del food_stuff_tp
# print(food_stuff_tp)                              # now it will give NameError
# Check if an item exists in tuple:
food_stuff_tps = ('mango', 'apple', 'orange', 'lemon', 'carrot', 'tamato', 'onion', 'potato', 'product1', 'product2', 'product3')
print('carrot' in food_stuff_tps)
print('kiwi' in food_stuff_tps)