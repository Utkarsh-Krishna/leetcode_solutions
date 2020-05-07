class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct1=collections.defaultdict(int)
            
        a=len(ransomNote)
        b=len(magazine)
        size=0
        size=max(a,b)
        
        for i in ransomNote:
            dct1[i]+=1
            
        for i in magazine:
            if i in dct1:
                dct1[i]-=1
        
        for i in dct1:
            if dct1[i] > 0:
                return False
        
        return True
