# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

column = int(input("Enter how many rows you want: "))
rows = int(input("Enter how many rows you want: "))

for column in range(1, rows + 1):
    print(f"{column} {column ** 0}  {column ** 1} {column ** 2} {column ** 3}")
