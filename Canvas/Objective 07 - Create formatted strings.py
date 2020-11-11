"""
1. Assign three different types of data to the three variables "a", "b", and "c".

A few of the common argument specifiers are:

%s - String (or any object with a string representation)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the dot's right.
%x/%X - Integers in hexadecimal (lowercase/uppercase)

2. Use a format string to inject the data from your three variables into the string.
"""
# Modify the code below to meet the requirements above.
a = "Oranges"
b = 100
c = 1.99

# Oranges (id: 100) are currently $1.99
print("%s (id: %d) are currently $%.2f." % (a, b, c))
