# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution(object):
    def spiralOrder(self, matrix):
        start_row,end_row,start_col,end_col = 0,len(matrix),0,len(matrix[0])
        output=[]
        
        while start_row< end_row or start_col < end_col:
            #right
            if start_row< end_row:
                for i in range(start_col,end_col):
                    output.append(matrix[start_row][i])
                start_row +=1
                
            #down
            if start_col< end_col:
                for i in range(start_row,end_row):
                    output.append(matrix[i][end_col-1])
                end_col -=1
            
            #left
            if start_row< end_row:
                for i in range(end_col-1,start_col-1,-1):
                    output.append(matrix[end_row-1][i])
                end_row -=1
            
            #up
            if start_col< end_col:
                for i in range(end_row-1,start_row-1,-1):
                    output.append(matrix[i][start_col])
                start_col +=1
         
        return output
