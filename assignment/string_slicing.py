# Create a function that takes a string input and returns the string completely reversed (using slicing).

input_word = str(input("Enter a string: "))

def slicing_reverse(input_word):
    print(input_word[::-1])

slicing_reverse(input_word)