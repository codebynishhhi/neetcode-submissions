# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # This code runs only once at the very beginning when you first call isValidBST.
        # It is a guard rail. If someone hands your function a completely 
        # empty tree (None), it returns False immediately.
        if not root:
            return False

        def validate(node, min_val, max_val):
            # This code runs dozens of times as the algorithm walks down the tree. 
            # Every single valid node with fewer than two children will trigger this line when checking its empty gaps.

            if not node:
                # returns False for empty leaf spaces, a perfectly valid single node tree gets rejected as invalid. 
                # Changing it to True means your code says: "An empty leaf child does not violate BST rules; it is safe to keep checking."
                return True

            if not (min_val < node.val < max_val):
                return False

            return (validate(node.left, min_val, node.val ) and validate(node.right, node.val, max_val))
        
        
        return validate(root, float('-inf'), float('inf'))

        
