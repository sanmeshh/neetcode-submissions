# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ans=[]
        maxx=-101
        def dfs(root,maxx):
    
            if not root:
                return 
            
            if root.val>=maxx:
                maxx=root.val
                ans.append(maxx)
                
            dfs(root.left,maxx)
            dfs(root.right,maxx)
        dfs(root,-101)
       
        return len(ans)
      





        