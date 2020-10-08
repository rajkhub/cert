#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]

class Solution(object):
    def intersect(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        res =[]
        
        dic ={}
        
        for ele in nums1:
            dic[ele] = nums1.count(ele)
        print dic
        for i in range(l2):
            if nums2[i] in dic.keys() and dic[nums2[i]]>0:
                res.append(nums2[i])
                dic[nums2[i]] -=1
        return res
