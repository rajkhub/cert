def majorityElement(self, nums):
    dic ={}
    for ele in nums:
        if ele not in dic:
            dic[ele] = 1
        else:
            dic[ele] +=1
    x = max(dic.values())
    for k,v in dic.items():
        if v == x:
            return k 

def majorityElement(self, nums):
    cnt = collections.Counter(nums)
    return max(cnt.keys(),key = cnt.get)
#The majority element is the element that appears more than ⌊ n/2 ⌋ times. LeetCode
def majorityElement(self, nums):
    nums.sort()
    print nums
    print len(nums)//2
    return nums[len(nums)//2]
