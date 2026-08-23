# Use and operator to check if 'on' is found in both 'python' and 'dragon'

name1 = 'python'
name2 = 'dragon'

is_avi = ('on' in name1 and 'on' in name2)

compare = {
    True: "Both having 'on' in it.",
    False: "Both don't have 'on' in it."
}[ is_avi ]

print(compare)