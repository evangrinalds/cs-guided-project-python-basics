"""
# Understand
output removes all duplicates from input

# Plan
split input_str into individual words
return and check for duplicates
 
# Execute
"""

def csRemoveDuplicateWords(input_str):
    words = input_str.split()
    return (" ".join(sorted(set(words), key=words.index)))
