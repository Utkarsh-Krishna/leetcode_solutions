# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        even=odd=None
        cnt=1
        skip=1
        start=head
        while head.next!=None:
            hd=head
            tmp=head
            
            for i in range(skip):
                tmp=tmp.next
            
            even=tmp.next
            #print(even.val)
            if not tmp or not tmp.next:
                break
            tmp.next=tmp.next.next
            even.next=head.next
            hd.next=even
            
            if tmp.next==None:
                break
            skip+=1
            cnt+=1
            head=head.next
            
        return start
