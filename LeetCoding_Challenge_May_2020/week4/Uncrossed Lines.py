class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        matrix= [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        
        #print(matrix)
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1]==B[j-1]:
                    matrix[i][j]=matrix[i-1][j-1]+1
                else:
                    matrix[i][j]=max(matrix[i-1][j], matrix[i][j-1])
        
        return matrix[len(A)][len(B)]
