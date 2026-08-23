# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input('Ente radius of circle: '))
PI = 3.14

area = PI * radius ** 2
circum = 2 * PI * radius

print("Area of circle: ",area)
print("Circumference of circle: ",circum)