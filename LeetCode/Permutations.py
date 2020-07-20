#Input: [1,2,3]
#Output:
#[
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]


def permute(nums):
    out = []
    remList=[]
    if len(nums) ==0:
        return []
    if len(nums) ==1:
        return [nums]
    
    for i in range(len(nums)):
        m = nums[i]
        remList = nums[:i] + nums[i+1:]
    
        for p in permute(remList): 
            out.append([m] + p) 
    return out 



            
            
            
