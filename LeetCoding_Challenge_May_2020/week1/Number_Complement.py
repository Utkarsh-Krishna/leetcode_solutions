class Solution:
    def findComplement(self, num: int) -> int:
        if num==1:
            return 0
        
        bnum=str(bin(num)[2:])
        
        st=""
        
        for i in bnum:
            if i=='1':
                st+='0'
            else:
                st+='1'
        
        return int(st,2)
