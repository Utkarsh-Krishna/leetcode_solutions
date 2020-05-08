# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1=""
        
        while l1:
            n1=str(l1.val) + n1
            l1=l1.next
        
        n2=""
        
        while l2:
            n2=str(l2.val) + n2
            l2=l2.next
        
        n1=int(n1)
        n2=int(n2)
        
        sm=str(n1+n2)[::-1]
        
        root=ListNode(int(sm[0]))
        head=root
        for i in range(1,len(sm)):
            newNode=ListNode(int(sm[i]))
            head.next=newNode
            head=newNode
            
        return root
