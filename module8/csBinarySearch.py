"""
Understand
input = [-1, 0, 3, 5, 9, 12] 
target = 9
output = 4
9 exists in nums and its index is 4

Plan
1. Declare min = 0 and max = length of array -1
2. Figure out the guess value by getting the middle integer between min and max
3. if array[guess] equals the target, we found the element, return the index
4. if the guess was too low, reset min to be one more than the guess
5. if the guess was too high, reset max to be one less than the guess
6. go back to step 2 (while not max<min)
"""

def csBinarySearch(nums, target):
    min = 0 
    max = len(nums) - 1
    while not max < min:
        guess = (max + min) // 2
        if nums[guess] == target:
            return guess
        elif nums[guess] < target:
            min = guess + 1
        else:
            max = guess - 1
    return -1 
