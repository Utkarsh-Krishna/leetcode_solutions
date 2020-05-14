class Solution:    
    def removeKdigits(self, num: str, k: int) -> str:
        if k>= len(num):
            return "0"
        
        stk=[-1]*len(num)
        
        top=-1
        st="0"
        cnt=0
        for i in num:
            if stk==None:
                stk.append(i)
                top+=1
            else:
                while k>0 and top>=0 and stk[top]>i:
                    #print(stk[top])
                    top-=1
                    k-=1
                
                top+=1
                stk[top]=i
                
            cnt+=1
            if k==0 or cnt==len(num):
                for j in range(0,top+1):
                    st+=stk[j]
                    
                #print(st, stk)
                st+=num[cnt:]
                break
            
            
        
        if k>0:
            #print("aA",st, k, len(num))
            
            st=st[0:len(st)-k]
        #print(st)
        return str(int(st))
                
                
