A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Join A and B
A.update(B)
print(A)
# Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.intersection_update(B)
print(A)
# Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.issubset(B))
# Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.isdisjoint(B))
# Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print(A)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
B.update(A)
print(B)

# What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.symmetric_difference(B))
# Delete the sets completely
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
del A,B
# print(A)
# print(B)                      # both set has been deleted 