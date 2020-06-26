#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 

def lengthOfLongestSubstring(self, s):
    ans =0
    sub = ''
    for ele in s:
        if ele not in sub:
            sub += ele
            ans = max(ans,len(sub))
        else:
            cut = sub.index(ele)
            sub = sub[cut+1:]+ele
    return ans


def lengthOfLongestSubstring(self, s):
    lst = list()
    for i in s:
        lst.append(i)
        if len(set(lst))< len(lst):
            lst.pop(0)
    return len(lst)
