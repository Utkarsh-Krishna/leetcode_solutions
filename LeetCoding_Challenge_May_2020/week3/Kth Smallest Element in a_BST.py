# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stk=[]
        
        while True:
            while root:
                stk.append(root)
                root=root.left
            
            root=stk.pop()
            k-=1
            
            if not k:
                return root.val
            
            root=root.right
            
