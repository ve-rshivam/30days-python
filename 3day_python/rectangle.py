# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"{area} is the area of rectangle.")
print(f"{perimeter} is the perimeter of rectangle.")