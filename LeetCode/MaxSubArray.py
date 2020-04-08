#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        curr_sum=nums[0]
        max_so_far=nums[0]
        for i in range(1,len(nums)):
            curr_sum=max(nums[i],curr_sum+nums[i])
            max_so_far = max(max_so_far,curr_sum) 
        return max_so_far
