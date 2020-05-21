class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        sm=0
        rows=len(matrix)
        cols=len(matrix[0])
        
        for i in range(0,rows):
            for j in range(0,cols):
                if i==0 or j==0:
                    if matrix[i][j]==1:
                        sm+=1
                else:
                    if matrix[i][j]:
                        matrix[i][j]+=min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
                    
                    sm+=matrix[i][j]
        
        return sm
