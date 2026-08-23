# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
is_avi = ('jargon' in sentence)
compare = {
    True: "'jargon' is present in sentence.",
    False: "'jargon' is not present in sentence."
}[is_avi]

print(compare)