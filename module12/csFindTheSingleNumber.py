"""
Understand
input: [1, 1, 2, 1]
output: [2]

Plan
1. Create dictionary
2. for num in nums
3. for key, value in dic items
4. if value = 1 return key
"""

def csFindTheSingleNumber(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1 
    for key, value in dic.items():
        if value == 1:
            return key
