# Write a Python function is_vowel(char) returning True if the input character is a vowel (a, e, i, o, u).

word = str(input("Enter a character: "))

def is_vowel(word):
    return word.lower() in 'aeiou'
print(is_vowel(word))
