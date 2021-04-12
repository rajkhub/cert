#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
 

 class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        low = 0 
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high)//2
            
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid -1
        return -1
 
 
 
 def search(self, nums, target):
     first = 0
     last = len(nums)-1
     
     while first <= last:
         mid = (first+last)/2
         if nums[mid] ==target:
             return mid
         else:
             if nums[mid] >= nums[first]: 
                 if nums[first] <=  target  <= nums[mid]:
                     last = mid -1
                 else:
                     first = mid +1 
             elif nums[mid] <= nums[last]: 
                 if nums[mid] <=  target  <= nums[last]:
                     first = mid +1
                 else:
                     last = mid -1 

     return -1 
