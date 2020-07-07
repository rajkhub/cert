#longestSubstring('aaabb',3)
#longestSubstring('ababccda',2)
#aaa
#ababcc

def longestSubstring(s, k):
    for c in set(s):
        if s.count(c) < k:
            for ele in s.split(c):
                print ele
                return longestSubstring(ele,k)
    return len(s)
