# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:

            # case 1 - both p and q are small, move left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # case 2 - both p and q are big, move right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            else:
                return curr

        