# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # using dfs Recurssion 
        if not root:
            return 0

        depth = 0
        # first ask left subtree , what is your length then right subtree
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        depth += 1 

        # combine length/ depth from both side
        return 1 + max(left, right)
        