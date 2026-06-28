# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
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

        

            


        

        


        