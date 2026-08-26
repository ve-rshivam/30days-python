# Write a Python function find_max(a, b, c) to return the maximum of three numbers without using max().
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

def find_max(a,b,c):
    maximum = max(a, b ,c)
    print(maximum)
find_max(a,b,c)    