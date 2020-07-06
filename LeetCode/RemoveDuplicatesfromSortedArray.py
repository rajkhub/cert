#Given nums = [1,1,2],
#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

def removeDuplicates(nums):
    if len(nums)==1: return 1
    j = 1  #slow pointer
    for i in range(1,len(nums)): #Fast Pointer
        if(nums[i] != nums[i-1]):
            nums[j] =nums[i]
            j += 1
    return j
