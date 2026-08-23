# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?

number = float(input("Enter a number: "))
even = number % 2 == 0

compare = {
    True: f"{number} is an even number.",
    False: f"{number} is an odd number."
}[even]
print(compare)