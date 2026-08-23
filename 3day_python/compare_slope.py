# Compare both slope

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# X-Intercept: where y = 0
# Y-Intercept: where x = 0
# y = mx + c       m = 2, c = -2

# For the equation y = 2x - 2
m = 2
c = -2

# 1. Slope is directly the value of m
slope1 = m

# 2. y-intercept is directly the value of c (when x = 0)
y_intercept = c

# 3. x-intercept is calculated by setting y = 0 (0 = mx + c -> x = -c / m)
x_intercept = -c / m

# Display the results
print(f"Slope: {slope1}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

#  Second slope 

# Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope2 = (y2 - y1) / (x2 - x1)

print('Slope between point (2, 2) and point (6,10): ',slope2)

if slope1 == slope2:
    print('Both Slope 1 and Slope 2 are equal.')
else:
    print('Both Slope 1 and Slope 2 are not equal.')    