# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        temp=head

        length=0
        while temp.next:
            length+=1
            temp=temp.next
            

        n=length-n
        tmp=head
        
        new=-1
        while n!=new:
            prev=tmp
            tmp=tmp.next
            new+=1
    
        if tmp==head:
            head=head.next
        else:
            prev.next=tmp.next


        return head
    


      

        


        