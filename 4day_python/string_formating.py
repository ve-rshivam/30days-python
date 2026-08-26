# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2

# 1st method of formating
formatted = 'The area of a circle with radius %d is %.2f meters square.' %(radius, area)
print(formatted)

# 2nd method of formating
formatted = 'The area of a circle with radius {}is {} meters square.'.format(radius, area)
print(formatted)

# 3rd method of formating
formatted = f'The area of a circle with radius {radius}is {area} meters square.'
print(formatted)