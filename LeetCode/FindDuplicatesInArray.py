 def findDuplicate(self, nums):
     s = set()
     for ele in nums:
         if ele not in s:
             s.add(ele)
         else:
             return ele
