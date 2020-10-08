Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

class Solution(object):
    def intersection(self, nums1, nums2):
        s=set(nums1)
        s1=set(nums2)
        return list(s & s1)
