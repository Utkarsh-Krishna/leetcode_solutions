# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    r1=None
    r2=None
    depth1=0
    depth2=0
    def iscous(self, root, x, y, cnt):
        if root==None:
            return
        
        if root.left!=None:
            if root.left.val==x:
                self.r1=root
                self.depth1=cnt+1
        
            if root.left.val==y:
                self.r2=root
                self.depth2=cnt+1
        
        
        if root.right!=None:
            if root.right.val==x:
                self.r1=root
                self.depth1=cnt+1
        
            if root.right.val==y:
                self.r2=root
                self.depth2=cnt+1
        
        if self.r1 and self.r2:
            return
        
        self.iscous(root.left, x, y, cnt+1)
        self.iscous(root.right, x, y, cnt+1)
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root==None:
            return False
        
        self.iscous(root, x, y, 0)
        
        if self.depth1==self.depth2 and self.r1!=self.r2:
            return True
        
        return False
        
        
