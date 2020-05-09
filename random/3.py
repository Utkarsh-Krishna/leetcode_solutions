class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        
        hm={}
        cnt=-1
        start=0
        i=1
        hm[s[0]]=0
        while i<len(s):
            if s[i] in hm and hm[s[i]]>=start:
                cnt=max(cnt,i-start)
                start=hm[s[i]]+1
            
            hm[s[i]]=i
            i+=1
            if i==len(s):
                cnt=max(cnt,i-start)
        
        if cnt==-1:
            return len(s)
        return cnt
