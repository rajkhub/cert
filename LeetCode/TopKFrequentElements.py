#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

from collections import Counter
def topKFrequent(nums, k):
    res=[]
    
    # dic = Counter(nums)  
    dic ={}
    for ele in nums:
        if ele not in dic:
            dic[ele]=1
        else:
            dic[ele] +=1
    
    while k>0:
        max_freq=0
        max_key=0
        for key in dic:
            if dic[key]>max_freq:
                max_key = key
                max_freq = dic[key]
        res.append(max_key)
        del dic[max_key]
        k-=1
    return res

#         s = sorted(dic.items(),key=lambda x: x[1],reverse=True)
#         l =[]
#         for x in range(0,k):
#             print(s[x][0])
#             l.append(s[x][0])
#         return l
