"""
Understand
input: string a = "odd" b= "egg"
output: boolean = true/false
isomorphic = 

Plan


"""


def csIsomorphicStrings(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
