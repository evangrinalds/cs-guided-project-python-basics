def csSquareAllDigits(n):

# Sudo code
# split the text
# for each word in the line:
# print the word
    
   square = ''.join(str(int(char)**2) for char in str(n))
   return int(square)
    
print(csSquareAllDigits("9119"))
print(csSquareAllDigits("2483"))
