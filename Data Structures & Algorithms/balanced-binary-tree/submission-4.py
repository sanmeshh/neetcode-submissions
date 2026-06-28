# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balance=True
        def dfs(root):
            nonlocal balance
            if not root:
                return 0
            
            left=dfs(root.left)+1
            right=dfs(root.right)+1

            sub =left-right
            if abs(sub)>=2:
                balance=False
                
           
            return max(left,right)
  
        dfs(root)
        
        return balance
                                                                                                                                                                                                                                                                                                                                                                 
        