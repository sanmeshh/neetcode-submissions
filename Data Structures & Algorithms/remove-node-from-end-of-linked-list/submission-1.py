# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast=head
        N=0
        while fast:
            fast=fast.next
            N+=1
        
   
        N=N-n
        if N==0:
            head=head.next
            return head
        else:
            slow=head
            while N!=1:
                N-=1
                slow=slow.next
            
            slow.next=slow.next.next
            return head

            
            

        

        




        