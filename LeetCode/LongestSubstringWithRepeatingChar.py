#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 

def lengthOfLongestSubstring(self, s):
    lst = list()
    for i in s:
        lst.append(i)
        if len(set(lst))< len(lst):
            lst.pop(0)
    return len(lst)
