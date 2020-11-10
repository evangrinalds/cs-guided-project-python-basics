"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

To get the perimeter of a rectangle we could use either (l * 2 + w * 2) or (l + w) * 2

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length, width):
    # return the value of the expression (length + width) * 2
    return (length + width) * 2

print(find_perimeter(6, 7))
print(find_perimeter(20, 10))
print(find_perimeter(2, 9))

