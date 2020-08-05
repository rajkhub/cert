#Input: "A man, a plan, a canal: Panama"
#Output: true

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
        
