#Input: 5
#Output:
#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]

class Solution(object):
    def generate(self, numRows):
        if numRows ==0:
            return []
        elif numRows ==1:
            return [[1]]
        pas = [[1]]
        for i in range(1,numRows):
            row=[1]
            for j in range(1,i):
                row.append(pas[i-1][j-1] + pas[i-1][j])
            row.append(1) 
            pas.append(row)
        return pas
