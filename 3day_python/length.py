# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

x = len('python')
y = len('dragon')

print("Length of python word: ",x)
print("Length of dragon word: ",y)

compare = {
    True: "Both having same length of word.",
    False: "Both having not same length of word."
}[x == y]
print(compare)