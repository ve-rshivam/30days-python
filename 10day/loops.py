#                               LOOPS
# While loop
count = 0
while count < 5:
    print(count)
    count += 1              # it print 0 to 4 

print('\nwhile and else')
count = 0
while count < 5:
    print(count)            # it will only print from 0 to 4 and then while loop return false in false condition it print 5 in else condition
    count += 1
else:
    print(count)

# break and continue
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:          # when condition hit it break 3 will not printed
        break

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)                # in this case it will only print 0 1 2 and 4 and at 3 it will skip them 
    count += 1

print('for loop')
# FOR Loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

language = 'Python'
for letters in language:
    print(letters)
print('2nd method')
for i in range(len(language)):
    print(language[i])
# using for loop in tuple 
numbers = (0, 1, 2, 3, 4, 5)    
for number in numbers:
    print(number)

# using for loop in dictonaries
person ={
    'first_name' : 'Shivam',
    'last_name' : 'Kumar',
    'age' : 20,
    'country' : 'India',
    'is_married' : False,
    'skills' : ['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street' : 'Unknown',
        'pin_code' : '110001'
    }
}    
for key in person:
    print(key)
for key, value in person.items():
    print(key, value)    
# using loop in set 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle'}    
for company in it_companies:
    print(company)

# Break and continue part 2
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be', number + 1) if number != 5 else print("loop's end")
print("Outside 's loop")    
# The Range Function
# the range() function is used to return a list of numbers. The range (start, end, step) takes three parameters: starting, ending and increment ,
# by default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end)
lst = list(range(11))
print(lst)
st =set(range(1, 11))       # 2 argument indicate start and end of the sequence, step set to default 1
print(st)
lst = list(range(0, 11, 2))
print(lst)
st = set(range(0,11,2))
print(st)
lst = list(range(11,0,-2))
print(lst)
for number in range(0,11,1):
    print(number)               # not include 11 it will print only till 10
person ={
    'first_name' : 'Shivam',
    'last_name' : 'Kumar',
    'age' : 20,
    'country' : 'India',
    'is_married' : False,
    'skills' : ['Javascript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street' : 'Unknown',
        'pin_code' : '110001'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)    

# for else
for number in range(0,11,1):
    print(number)
else:
    print('The loop stops at', number)
        