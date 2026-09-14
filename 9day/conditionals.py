#                                                       Conditionals
# by default python script are executed sequentially from top to bottom 
# conditional execution: a block of one or more statement will be ececuted if a certain expression is true 
# repetitive execution: a block of one and more statement will be repetitive executed as long as the expression is true 

# if condition 
a = 3
if a > 0:
    print('A is a Positive number.')

# if else condition 
a = 3
if a < 0:
    print('A is a negative number.')
else:
    print('A is a positive number.')    

# if elif else
a = 0
if a > 0:
    print('A is a positive number.')
elif a < 0:
    print('A is a negative number.')    
else:
    print('A is zero.')

# Short hand
a = 3
print('A is a positive number.') if a > 0 else print('A is a negative number.')

# Nested condition
# Condition can be nested
a = 3
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer.')
    else:
        print('A is a positive number.')    
elif a == 0:
    print('A is Zero.')        
else:
    print('A is a negative number.')    

# if condition and logical operators
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer.")
elif a > 0 and a % 2 != 0:
    print('A is a positive integer.')    
elif a == 0:
    print('A is Zero.')    
else: 
    print('A is negative.')    

# if and or logical operators
user = 'james'    
access_level = 3
if user == 'james' or access_level >= 4:
    print('Access Granted!')
else:
    print('Access Denied!')    