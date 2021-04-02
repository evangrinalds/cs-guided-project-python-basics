"""
Understand
Input: [6, 7, 1, 2, 3, 4, 5]
Target = 1
Output: 2
Linear Search

Plan
1. Loop through each item in the input array
2. Check if the item at the current index is equal to the target
3. Return the current index as the match
4. If we were able to loop through the entire array, the target is not present
"""

def csSearchRotatedSortedArray(nums, target):
    for idx in range(len(nums)):
        if nums[idx] == target:
            return idx
    return -1 
