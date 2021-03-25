"""
Understand
"crazy" --> "dsbaz"
shift one to the right

Plan 
define index as 0
define output as string
define letters in alphabet
for loop iterate through input
check is input is lowercase
index 
"""
    
def alphabeticShift(input_string):
    index = 0
    new_word = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzacd"

    for i in input_string.lower():
        if i.islower(): #check if i s letter
            index = alphabet.index(i) + 1 #get the index of the following letter
            new_word += alphabet[index]    
        else: #if not letter
            new_word += i    
    return new_word
