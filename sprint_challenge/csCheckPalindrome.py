"""
# Understand
input string
output true/false

# Plan
remove special symbols
for char in x
if char in special symbols
input str replace into string
input str lower letters
reverse input str
Str == input str


# Execute

# Review
"""

#def csCheckPalindrome(input_str):
    #return input_str == "".join(reversed(input_str))
    
# for loop method

def csCheckPalindrome(input_str):
    
    specChars =  ''' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''  
    
    for char in input_str:
        if char in specChars:
            input_str = input_str.replace(char,"")
    input_str = input_str.lower()
    
    Str = input_str[::-1]
    return Str == input_str
