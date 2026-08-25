# Write a program that takes integer num and prints "Positive", "Negative", or "Zero".
number = int(input("Enter a number: "))

if(number < 0):
    print("Negative")
elif(number > 0):
    print("Positive")
else:
    print("Zero")        