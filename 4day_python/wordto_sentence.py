# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word1 = 'Thirty'
word2= 'Days'
word3 = 'Of'
word4 = 'Python'
space = ' '
sentence = word1 + space + word2 + space + word3 + space + word4
print(sentence)

# Using join function
word = ['Thirty', 'Days', 'Of', 'Python']
sentence1 = ' '.join(word)
print(sentence1)