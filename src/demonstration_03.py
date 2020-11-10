"""
Challenge #3:

Create a function that takes a string and returns it as an integer.
We can use the int() constructor to convert other data types to an Integer

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # return the int value of txt to the caller
    return int(txt)

print(string_int("6"))
print(string_int("1000"))
print(string_int("12"))


