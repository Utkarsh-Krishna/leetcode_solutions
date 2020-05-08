class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dct={1:0}
        
        def findSteps(n):
            if n not in dct:
                if n%2==0:
                    dct[n]=findSteps(n/2) + 1
                else:
                    dct[n]=findSteps(3*n + 1) + 1
            
            return dct[n]
        
        arr=[]
        for i in range(lo,hi+1):
            arr.append((i,findSteps(i)))
        
        arr.sort(key=lambda x: x[1])
        return arr[k-1][0]
