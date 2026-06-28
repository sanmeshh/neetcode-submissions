# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow,fast=head,head.next

        while fast and fast.next:

            fast=fast.next.next
            slow=slow.next

        sec=slow.next
        slow.next=None
        prev=None
        while sec:
            nex=sec.next
            sec.next=prev
            prev=sec
            sec=nex

        first,sec=head,prev
        while sec:
            nexf,nexs=first.next,sec.next
            first.next=sec
            sec.next=nexf
            first=nexf
            sec=nexs



        
        