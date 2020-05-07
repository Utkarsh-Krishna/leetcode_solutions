import math
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label==1:
            return [1]
        
        depth=int(math.log(label,2))
        
        arr=[0]
        arr.append(1)
        level=2
        x=2
        for i in range(1,depth+1):
            val=2*x - 1
            val2=x
            x=x*2
            ar1=[]
            if level%2!=0:
                ar1=list(range(val2,val+1))
            else:
                ar1=list(range(val,val2-1,-1))
                
            arr=arr+ar1
            level+=1
        
        #print(arr)
        pos=0
        for i in range(len(arr)-1, -1, -1):
            if arr[i]==label:
                pos=i
                break
        
        nodeList=[]
        
        while pos>=1:
            nodeList.append(arr[pos])
            pos=pos//2
        
        nodeList.reverse()
        return nodeList
