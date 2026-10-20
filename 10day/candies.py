avilable_candy = 10
x = int(input("How many candies do you candies do you want?"))
i = 1
while i<= x:
    if i > avilable_candy:
        print("Out of stock!")
        break
    print("Candy")
    i += 1
print("Get Lost")    