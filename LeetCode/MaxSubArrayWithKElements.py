#Max SubArray with Atleast K numbers
#nums=[-4, -2, 1, -3]
#x =2
#output = -1

def maxSubArray(nums,x):
    output = 0 
    maxsum=0
    last = x-1
    for i in range(0,x):
        output =  output+nums[i]
    
    maxsum = output
    for j in range(x,len(nums)):
        maxsum = maxsum + nums[j] - nums[j-x] 
        output = max(maxsum,output)
    return output
