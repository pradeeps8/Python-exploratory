"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

def jump(nums):
	res = [-1]*len(nums)
	return jumped(nums, 0,  len(nums)-1, res)

def jumped(nums, index, size, res):
	if index >= size:
		return 0
	print(index)
	if res[index] == -1:
		res[index] =  min(jumped(nums, index+1, size, res) + 1, jumped(nums, nums[index] + index, size, res) + 1)
	return res[index]
	
nums = [2,3,1,1,4]
print(jump(nums))


