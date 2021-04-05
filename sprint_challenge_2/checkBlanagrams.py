"""
Understand
input: string --> output: boolean (true/false)

Plan
1. Use sorted function with input
2. if / else for true / false output
"""

def checkBlanagrams(word1, word2):

# the sorted strings are checked  
    if(sorted(word1)== sorted(word2)): 
        return False
    else: 
        return True
