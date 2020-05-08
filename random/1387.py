class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        even=lambda a : a/2
        odd=lambda a: 2*a + 1
        dct=collections.defaultdict(list)
        dct1=collections.defaultdict(int)
        
        for i in range(lo,hi+1):
            val=i
            cnt=0
            while 1==1:
                if val%2==0:
                    val=val/2
                else:
                    val=3*val + 1
                
                cnt+=1
                if val==1:
                    break
            
            dct[cnt].append(i)
            
        
        lst=sorted(dct.keys())
        lst2=[]
        for i in lst:
            lst2 = lst2 + sorted(dct[i])
        
        #print(lst2)
        return lst2[k-1]
