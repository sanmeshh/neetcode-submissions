# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        start=ListNode(None,None)
        curr=start
        value=0
        temp=l1
        temp2=l2
        n=1
        m=1
        while temp.next:
            n+=1
            temp=temp.next
        while temp2.next:
            m+=1
            temp2=temp2.next

        if n>m:
            while m!=n:
                temp2.next=ListNode(0)
                temp2=temp2.next
                m+=1
        elif m>n:
            while n!=m:
                temp.next=ListNode(0)
                temp=temp.next
                n+=1
        


        while l1 and l2:
            value=value+(l1.val+l2.val)
            
            
            if value>9:
                if l1.next:
                    curr.next=ListNode(value%10)
                    value=int(value/10)
                else:
                    curr.next=ListNode(value%10)
                    curr=curr.next
                    curr.next=ListNode(int(value/10))
                    
            else:
                
                curr.next=ListNode(value)
                value=0

            l1=l1.next
            l2=l2.next
            curr=curr.next

        return start.next

        
    