# Check if int('9.8') is equal to 10
num1 = int(float('9.8'))
num2 = 10

compare = {
    True: "'9.8' is equal to 10 after converting in to integer.",
    False: f"'9.8' is not equal to 10 after converting in to integer and '9.8' = {num1}."
}[num1 == num2]
print(compare)