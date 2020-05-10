class Solution:        
    def longestPalindrome(self, s: str) -> str:
        if s=="":
            return s
        size=len(s)
        
        cnt=1
        x=0
        y=1
        
        for i in range(1,size):
            l=i-1
            r=i+1
            
            check=False
            while l>=0 and r<size and s[l]==s[r]:
                l-=1
                r+=1
                check=True
            
            if check:
                mx=r-l
                if mx>cnt:
                    x=l+1
                    y=r
                    cnt=mx
                check=False

            l=i-1
            r=i
            
            while l>=0 and r<size and s[l]==s[r]:
                l-=1
                r+=1
                check=True
            
            if check:
                mx=r-l
                if mx>cnt:
                    x=l+1
                    y=r
                    cnt=mx
                check=False
        return s[x:y]
