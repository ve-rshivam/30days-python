# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

a = 7
b = 3

floor = 7 // 3              # floor division operator

integer = int(2.7)

check = integer == floor

compare = {
    True:  "Floor division value and converted value are equal.",
    False: "Floor division value and converted value are not equal."
}[check]
print(compare)


