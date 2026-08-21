# Find an Euclidean distance between (2, 3) and (10, 8).
# point 1 (2, 3)
x1 = 2
y1 = 3
# point 2 (10, 8)
x2 = 10
y2 = 8
dis1 = (x2 - x1) ** 2
dis2 = (y2 - y1) ** 2
distance = (dis1 + dis2) ** 0.5
print("Euclidean Distance:",distance)