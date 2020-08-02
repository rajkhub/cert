#longestSubstring('aaabb',3)
#longestSubstring('ababccda',2)
#aaa
#ababcc

def longestSubstring(s, k):
    for c in set(s):
        if s.count(c) < k:
            res =0
            for ele in s.split(c): 
                print ele
                res =  max(res,longestSubstring(ele,k))
            return res
    return len(s)
