"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120

# we can times minutes by 60 to get seconds
"""
def convert(minutes:int):
    # Your code here
    # return the value of the expression minutes * 60 to the caller
    return minutes * 60


print(convert(5))
print(convert(3))
print(convert(2))

