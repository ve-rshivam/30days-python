# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.

x =float(input('Enter the x: '))
y = x ** 2 + 6 * x + 9
print('Value of y: ',y)

comparison = {
    True: f"At x = {x} the value of y = 0.",
    False:  "Y is not equal to 0."
}[y == 0]

print(comparison)