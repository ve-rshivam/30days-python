# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.

# Abbrevation:- this is use for any shorten version of word or pharse   like Dr. and application turs into 'App'
# Acronym:- a spercial type of abberevation where we take only first letter of phrase like USA

sent1 = 'Python For Everyone'
sent2 = 'Coding For All'
word1 = sent1.split()
acronym1 = word1[0][0] + word1[1][0] + word1[2][0]
word2 = sent2.split()
acronym2 = word2[0][0] + word2[1][0] + word2[2][0]
print(acronym1)
print(acronym2)

print(sent2.index('C'))
print(sent2.index('F'))
sent = 'Coding For All People'
print(sent.rfind('l'))