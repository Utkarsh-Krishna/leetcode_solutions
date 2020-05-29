class Solution:
    def countBits(self, num: int) -> List[int]:
        fa = [0,1]
        bits = int(num**(1/2)) + 1
        cnt=2
        
        #print(bits)
        
        for i in range(bits):
            if cnt > num:
                return fa[:num+1]
            
            tc = cnt
            for j in range(tc):
                if cnt > num:
                    return fa[:num+1]
                
                fa.append(fa[j]+1)
                cnt+=1
            
            
