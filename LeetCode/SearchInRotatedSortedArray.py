#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
 
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
