#Understand
"Two strings with lowercase letters"
"returns new sorted string with any characters only appearing once"

#Plan
"Combine two lists and drop duplicates"

# Execute

def csLongestPossible(str_1, str_2): # 0(n) 
    return "".join(sorted(set(str_1 + str_2)))

#Review
