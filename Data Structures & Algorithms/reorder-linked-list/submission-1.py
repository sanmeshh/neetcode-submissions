# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        n=0
        while fast:
            fast=fast.next
            n+=1
        slow=head
        k=0
        while k!=int(n/2):
            k+=1
            slow=slow.next
        
        temp=slow.next
        slow.next=None
        prev=None
        while temp:
            nex=temp.next
            temp.next=prev
            prev=temp
            temp=nex

            
        temp1=head
        temp2=prev
        while temp1 and temp2:

            nex1=temp1.next
            nex2=temp2.next

            temp1.next=temp2
            temp2.next=nex1

            temp1=nex1
            temp2=nex2

        

            


        

        


        