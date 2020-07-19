#Input: nums = [2,3,1,1,4]
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

def canJump(nums):
    if len(nums) ==1:
        return True
    
    for i in range(len(nums)):
        nextIndex = i +1
        if i + nums[i] >= len(nums)-1:
            return True
        
        if nums[i] ==0 :
            return False
        
        if i + nums[i] > nums[nextIndex] +i:
            nums[nextIndex] = nums[i] -1
