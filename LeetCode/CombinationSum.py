# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

class Solution(object):
    def combinationSum(self, candidates, target):
        
        self.res= []
        candidates.sort()
        self.combination([],candidates,target)
        return self.res
        
    def combination(self,temp,candidates,target): 
        for i in candidates:
            if i> target:
                break
            temp.append(i)  
            if i == target:
                self.res.append(list(temp))
                temp.pop()
                break
            else:
                index = candidates.index(i)
                self.combination(temp,candidates[index:],target-i) 
            temp.pop()
            print("pop",  temp)
            print("target",  target)
