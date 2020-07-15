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
