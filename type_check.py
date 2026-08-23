# Check if type of '10' is equal to type of 10

x = '10'
y = 10
type1 = type(x)
type2 = type(2)

print(f"{x} is a {type1}.")
print(f"{y} is a {type2}.")

comp = type1 == type2

compare = {
    True: "Both having same type.",
    False: "Both having not same type."
}[x == y]
print(compare)