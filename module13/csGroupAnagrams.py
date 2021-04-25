"""
Understand
input: array of str
output: array of str

Plan
"""

def csGroupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    def convert(s):
        res = [0]*26
        for char in s:
            res[ord(char)-ord('a')] += 1
        return tuple(res)
    rec = {}
    res = []
    for s in strs:
        t = convert(s)
        if t in rec:
            res[rec[t]].append(s)
        else:
            res.append([s])
            rec[t] = len(res)-1
    return res 
