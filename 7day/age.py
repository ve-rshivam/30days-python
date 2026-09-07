age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(type(age))
set_age = set(age)
if len(age) == len(set_age):
    print('Both having same length.')
elif len(age) > len(set_age):
    print('List length is greater than set.')
else:
    print('Set length is greater than List')
print(len(age))
print(len(set_age))    