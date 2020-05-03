#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

def twoSum(self, nums, target):
    dic ={}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in dic:
            return [dic[x],i]
        dic[nums[i]] =i
