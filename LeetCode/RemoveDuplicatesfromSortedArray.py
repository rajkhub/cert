#Given nums = [1,1,2],
#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

def removeDuplicates(self, nums):
    i = 0
    j = 1
    for j in range(1,len(nums)):
        if(nums[i] != nums[j]):
            i += 1
            nums[i] =nums[j]
    return j
