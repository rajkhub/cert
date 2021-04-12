#Input: "A man, a plan, a canal: Panama"
#Output: true

class Solution(object):
    def isPalindrome(self, s):
        l =0
        r = len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l +=1
            while l < r and not s[r].isalnum():
                 r -=1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l +=1
            r -=1
        return True


import re
class Solution(object):
    def isPalindrome(self, s):
        s =lower(s)
        s = re.sub("[^A-Za-z0-9]","",s)
        i = 0
        j = len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return False 
            j -=1
            i +=1
        return True 
        
