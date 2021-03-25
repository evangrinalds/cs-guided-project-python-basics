"""
Understand
string of () --> boolean (true/false)

Plan 
define 3 different parentheses types
stack
for loop c in string
if statement c in d
stack.append c


defin
"""


def validParenthesesSequence(s):
    d = {'{':'}', '(':')', '[':']'}
    stack = []
    for c in s:
        if c in d:
            stack.append(c)
        elif not stack or c != d[stack.pop()]:
            return False
    return not stack
