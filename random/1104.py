import math
from collections import deque
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        depth=int(math.log(label,2))+1
        nodeList=deque()
        nodeList.appendleft(label)
        
        for i in range(depth, 1, -1):
            val=2**i
            label=(val-1 + val//2 - label)//2
            nodeList.appendleft(label)
            
        return nodeList
