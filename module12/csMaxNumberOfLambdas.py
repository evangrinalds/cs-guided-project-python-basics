def csMaxNumberOfLambdas(text):
    """
    Input: a string
    Output: int, number of 'lambdas' you can write with the letters in the input string
    """
    
    letters = {'l': 0, 'a': 0, 'm': 0, 'b': 0, 'd': 0, 'a':0}
    counts = []
    for letter in text:
        if letter in letters:
            letters[letter] += 1
    
    for key, value in letters.items():
        counts.append(value)
        
    return min(counts)
