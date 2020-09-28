#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=[]
        res2=[]
        if s =="":
            return ""
        
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                res.append(s[i:j])
        
        for ele in res:
            rev = ele[::-1]
            if ele == rev:
                res2.append(ele)
        return max(res2,key=len)
