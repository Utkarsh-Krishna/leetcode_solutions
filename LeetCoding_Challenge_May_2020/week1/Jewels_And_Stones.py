class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dct=collections.defaultdict(int)
        
        for i in J:
            dct[i]=1
            
        for i in S:
            if i in dct:
                dct[i]+=1
        
        lst=list(dct.values())
        return sum(lst) - len(lst)
