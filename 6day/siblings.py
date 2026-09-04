# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

brother = ('brother1', 'brother2', 'brother')
sister = ('sister1', 'sister2')
siblings = brother + sister
print(brother)
print(sister)
print(siblings)
print(len(siblings))
list_siblings = list(siblings)
print(siblings)
list_siblings.append('father')
print(list_siblings)
list_siblings.append('mother')
print(list_siblings)
family_member = tuple(list_siblings)
print(family_member)