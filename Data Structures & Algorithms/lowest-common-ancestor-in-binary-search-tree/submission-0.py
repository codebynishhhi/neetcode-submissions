# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # pointer for traversal
        curr = root
        
        while curr:

            # case 1 : if p & q both are small val than curr node, move left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # case 2 : if p & q both are greater val than curr node, move right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right 

            # case 3 : 
            # if one value either p/q is small,and other is larger
            # eg - p = 3 , q= 8, then LCA is curr node
            # bcz the curr node is the split 
            else:
                return curr
        