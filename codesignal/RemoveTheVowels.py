def csRemoveTheVowels(input_str):
    
# Sudo code
# define the input_str
# define the vowels
# for loop
# if statement with replace

    for i in "aeiouAEIOU":
        input_str = input_str.replace(i,"")
    return input_str

print("Lambda School is awesome!")
