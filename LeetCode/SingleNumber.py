#Example 
#Input: [2,2,1]
#Output: 1
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        ini = nums[0]
        for i in range(1,len(nums)):
            ini = ini^nums[i]
        return ini
