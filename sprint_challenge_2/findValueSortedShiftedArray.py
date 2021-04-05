"""
Understand
return the target value's index, if not present return -1
input: sorted array [4, 5, 6, 7, 0, 1, 2] target = 0
output: [4]

Plan
1. Loop through each item in the input array
2. Check if the item at the current index is equal to the target
3. Return the current index as the match
4. If we were able to loop through the entire array, the target is not present
"""

def findValueSortedShiftedArray(nums, target):
    for idx in range(len(nums)):
        if nums[idx] == target:
            return idx
    return -1 
