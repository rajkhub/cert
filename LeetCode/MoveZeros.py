#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt +=1
        
        while cnt < len(nums):
            nums[cnt] = 0
            cnt += 1
        
        return nums
