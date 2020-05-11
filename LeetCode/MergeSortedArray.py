#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6]       n = 3
#Output: [1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1
