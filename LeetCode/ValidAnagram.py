# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution(object):
    def isAnagram(self, s, t):        
        s =sorted(s)
        t =sorted(t)
        
        if s ==t:
            return True
        else:
            return False


class Solution(object):
    def isAnagram(self, s, t):
        dic={}
        for ele in s:
            if ele not in dic:
                dic[ele] =1
            else:
                dic[ele] +=1
        for ele in t:
            if ele not in dic:
                return False
            else:
                dic[ele] -=1
        for k in dic:
            if dic[k]>0:
                return False    
        return True
      
      
