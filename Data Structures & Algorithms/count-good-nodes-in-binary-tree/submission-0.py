# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx=-101
        c=0
        def dfs(root,maxx):
            nonlocal c
            if root:
                if maxx<=root.val:
                    maxx=root.val
                    c+=1
                
                
                dfs(root.left,maxx)
                
                dfs(root.right,maxx)
        dfs(root,maxx)
        
        return c






        