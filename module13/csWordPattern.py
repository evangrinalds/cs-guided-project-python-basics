"""
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in a.
"""


"""
Understand
input: pattern and a (string)
output: boolean (true/false)

Plan
"""


def csWordPattern(pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
