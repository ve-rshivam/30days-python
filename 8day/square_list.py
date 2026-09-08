squares =[]
for x in range(10):
    squares.append(x ** 2)
print(squares)    
squares = list(map(lambda x: x**2, range(15)))
print(squares)
squares = [x**2 for x in range(13)]
print(squares)