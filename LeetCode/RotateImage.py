# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution(object):
    def rotate(self, matrix):
        self.transpose(matrix)
        self.flip(matrix)
        
    def transpose(self,matrix):
        n= len(matrix)
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix
    
    def flip(self,matrix):
        n = len(matrix)
        for lst in matrix:
            for i in range(len(matrix)/2):
                tmp =lst[i]
                lst[i]=lst[len(lst)-i-1]
                lst[len(lst)-i-1] = tmp
        return matrix
