class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct1={}
        
        for i in s:
            if i in dct1:
                dct1[i]+=1
            else:
                dct1[i]=1
        
        for i in range(0,len(s)):
            if dct1[s[i]]==1:
                return i
            
        return -1
