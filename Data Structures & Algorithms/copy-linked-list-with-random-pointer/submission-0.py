"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        temp=head
        hmap={None:None}
        while temp:
            node=Node(temp.val)
            hmap[temp]=node
            temp=temp.next



        temp=head
        while temp:
            node=hmap[temp]
            node.next=hmap[temp.next]
            node.random=hmap[temp.random]
            temp=temp.next
        
        return hmap[head]


        

