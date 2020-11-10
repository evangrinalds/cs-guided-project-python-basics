#!/usr/bin/python
# Sudo code
# if input_str has numbers && has no letters, return true
# if input_str has letters && has no numbers, return true
# else return false

def csAlphanumericRestriction(input_str):

    if input_str.isalpha() == True:
        return True
    elif input_str.isnumeric() == True:
        return True
    else:
        return False

print(csAlphanumericRestriction("Bold"))
print(csAlphanumericRestriction("123454321"))
print(csAlphanumericRestriction("H3LL0"))



