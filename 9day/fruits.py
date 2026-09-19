# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
user_input = input('Enter a fruits name: ')

if user_input in fruits:
    print('That fruit already exist in the list.')
else:
    fruits.append(user_input)
    print(fruits)    