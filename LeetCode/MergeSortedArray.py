#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6]       n = 3
#Output: [1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1
    
    
class Solution(object):
    def merge(self, nums1, m, nums2, n): 
        # nums1[:] = sorted(nums1[:m] + nums2)
        # return nums1
        while m >0 and n >0:
            if nums1[m-1]> nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -=1
            
        if n >0:
            nums1[:n] = nums2[:n]
