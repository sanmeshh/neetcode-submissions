# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
     
        q=collections.deque()
        q.append(root)
        ans=[]
        while q:
            level=[]
            length=len(q)
            for i in range(length):
                node=q.popleft()
                if node:
                    if i==length-1:
                        ans.append(node.val)
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        
        return ans
      


        