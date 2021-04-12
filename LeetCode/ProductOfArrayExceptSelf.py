# Product of Array Except Self
#input =[1,2,3,4]
# Output = [24, 12, 8, 6]
arr=[1,2,3,4]


class Solution(object):
    def productExceptSelf(self, nums):
        ans=[0]*len(nums)
        ans[0]=1
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        R=1
        for i in reversed(range(len(nums))):
            ans[i]= ans[i]*R
            R *= nums[i]
        return ans




def multiply(arr):
    res = []
    for i in range(len(arr)):
        cnt =1
        for j in range(1,len(arr)):
            if i !=j:
                cnt = cnt * arr[j]
            if j == len(arr)-1:
                res.append(cnt)
    return res
