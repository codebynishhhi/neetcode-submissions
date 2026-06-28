# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # this is actually Same Tree + DFS 
        # IF each tree in root is a sameTree as subroot 

        # step1 : sameTree 
        def isSameTree(p, q):
            
            # base case 1: both none --> true
            if not p and not q:
                return True
            
            # base case 2 : any one None --> false
            if not p or not q:
                return False

            if p.val != q.val:
                return False 
            
            return (
                isSameTree(p.left, q.left) 
                and 
                isSameTree(p.right, q.right)
                )
        
        # step 2: dfs search to find same tree
        def dfs(node):
            
            # base case
            if not node:
                return False
            
            if isSameTree(node, subRoot):
                return True
            
            return (
                dfs(node.left) 
                or 
                dfs(node.right)
            )
        return dfs(root)
            

        