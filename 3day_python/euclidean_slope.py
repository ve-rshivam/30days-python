# Slope is (m = y2-y1/x2-x1). 
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope = (y2 - y1) / (x2 - x1)
dis1 = (x2 - x1) ** 2
dis2 = (y2 - y1) ** 2
distance = (dis1 + dis2) ** 0.5

print('Slope between point (2, 2) and point (6,10): ',slope)
print('Euclidean distance between point (2, 2) and point (6,10): ',distance)