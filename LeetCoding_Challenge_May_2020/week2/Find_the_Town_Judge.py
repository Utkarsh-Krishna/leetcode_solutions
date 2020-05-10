class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dct=collections.defaultdict(int)
        dct2=collections.defaultdict(int)
        
        for i in trust:
            dct[i[0]]+=1
            dct2[i[1]]+=1
            
        for i in range(1,N+1):
            if i not in dct and dct2[i]==N-1:
                return i
        return -1
        
// T(n) = O(NC2 + N)
