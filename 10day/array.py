from array import *
vals = array("i",[5,6,7,-8,9])
print(vals.buffer_info())             # here the first output will be the address and second one is the size
print(vals.typecode)
# for reversing the array we need to store them first 
# vals.reverse()
print(vals)
# now printing all the array one by one using for loop
for i in vals:
    print(i)
# using the character
val = array('u',['a','e','i'])
for e in val:
    print(e)    
vals = array("i",[5,6,7,8,9,2])
newArr = array(vals.typecode, (a for a in vals))
# printing using for loop
for e in newArr:
    print(e)

# printing using while loop
i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1
