# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs using recurssion
        diameter = 0

        def dfss(node):

            nonlocal diameter

            if not node:
                return 0
            left = dfss(node.left)
            right = dfss(node.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfss(root)
        return diameter 
            
        

        