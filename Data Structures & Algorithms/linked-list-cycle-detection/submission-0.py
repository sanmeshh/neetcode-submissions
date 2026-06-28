# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pos=0
        temp=head
        checker=[]
        
        if temp:
            while temp.next:
                pos+=1
                checker.append(temp)
            
                for pointer in checker:
                    if temp.next==pointer:
                        return True
                temp=temp.next
       
        return False



        