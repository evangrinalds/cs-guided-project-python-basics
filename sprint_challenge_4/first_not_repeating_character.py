"""
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
"""

"""
Understand
input: str = "abacabad"
output: char = 'c'

Plan
1. create dictionary
2. iterate thru with for loop
3. return index in string if equals 1 if not '_'

"""

def first_not_repeating_character(s):
    c = {}
    for i in s:
        c[i] = c.get(i, 0) + 1
    return next((i for i in s if c[i] == 1), '_')
