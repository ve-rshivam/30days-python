# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 'You cannot end a sentence with because because because is a conjunction'.

statement = 'You cannot end a sentence with because because because is a conjunction'
print(statement.index('because'))
print(statement.find('because'))
print(statement.rfind('because'))
remove = statement.index('because because because')
remove1 = remove + len("because because because")
print(statement[remove:remove1])
print(statement.find('because'))