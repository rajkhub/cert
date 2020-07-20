#Input: nums = [2,3,1,1,4]
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


def canJump(self, nums):

    lastIndex = len(nums)-1
    for i in reversed(range(len(nums)-1)): 
        print i
        diff = lastIndex - i
        if nums[i]>=diff:
            lastIndex = i 
    return lastIndex ==0



#1st Soln
def canJump(self, nums):
    jumplen = 0
    for i in range(len(nums)):
        if i>jumplen:
            return False
        jumplen = max(nums[i]+i, jumplen)
    return True

#2nd Soln
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
