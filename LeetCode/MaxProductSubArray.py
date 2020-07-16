#Input: [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
 
 def maxProduct(self, nums):
     
     if len(nums)==0:
         return 0
     
     res = nums[0]
     for i in range(len(nums)):
         cnt =1
         for j in range(i,len(nums)):
             cnt = cnt * nums[j]
             res = max(cnt,res)
     return res
