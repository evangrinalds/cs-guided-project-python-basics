def csShortestWord(input_str):
# Sudo code
# define the variable with split 
# sort the variable with length
# return index 1 

    words = input_str.split(' ')
    words.sort(key=len)
    return len(words[0])
