# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))
if num1 > num2:
    print(f'{num1} is greater than {num2}.')
elif num1 < num2:    
    print(f'{num2} is greater than {num1}.')
else:
    print(f'{num1} is equal to {num2}.')