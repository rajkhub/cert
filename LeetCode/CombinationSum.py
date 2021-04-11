# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.


class Solution(object):
    def combinationSum(self,candidates, target):
        result= []
        path=[]
        def backtrack(path,target,index):
            if target ==0:
                result.append(path)
                return
            if target <0:
                return
            for i in range(index,len(candidates)):
                backtrack(path+[candidates[i]],target-candidates[i],i)
#                 //backtrack([2],5,0)
#                     //backtrack([2,2],3,0)  
#                         //backtrack([2,2,2],1,0)   
#                             //backtrack([2,2,2,2],-1,0) XX
#                             //backtrack([2,2,2,3],-2,1) XX
#                             //backtrack([2,2,2,6],-5,2) XX
#                             //backtrack([2,2,2,7],-6,3) XX
#                     //backtrack([2,2,3],0,1)                 
#                 //backtrack([2,3],4,1)
#                     //backtrack([2,3,3],1,1)
#                     //backtrack([2,3,3,3],-2,1)
                
        backtrack(path,target,0)
        return result

    

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
