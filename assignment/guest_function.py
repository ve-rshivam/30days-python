# Define function greet_user(name="Guest") that returns "Hello, !". Call it with and without args.
name = str(input("Enter your name: "))
def greet_user(name):
    print(f"Hello,{name} !")
greet_user(name)    