"""
Understand
input: a string with "[()]"
output: boolean (true/false)

Plan
"""

def validBracketSequence(sequence):
    ref = []
    left = "([{"
    
    for c in sequence:
        if c in left:
            ref.append(c)
            continue
            
    if len(ref) > 0:
        if c == ")" and ref[len(ref)-1] != "(":
            return False
        elif c == "]" and ref[len(ref)-1] != "[":
            return False
        elif c == "}" and ref[len(ref)-1] != "{":
            return False
        else:
            ref.pop()
    
    if len(ref) > 0:
        print(ref)
        return False
    
    return True
