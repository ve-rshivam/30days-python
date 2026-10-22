num = int(input('Enter a number: '))
def fact():
    i = 0
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2,num + 1):
        result *= i
    print(result)
fact()                

# using import function
from math import *
print(factorial(num))