#Input: [100, 4, 200, 1, 3, 2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0 
        nums = sorted(nums)
        print nums
        curr_l=1
        long_l =1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    curr_l +=1
                else:
                    long_l = max(long_l,curr_l)
                    curr_l =1
        return max(long_l,curr_l)
