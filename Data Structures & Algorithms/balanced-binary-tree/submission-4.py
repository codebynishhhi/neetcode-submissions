# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # dfs 
        # Bottom-up recurssive approach with post order traversal
        # recursive funstion returns -
        # height --> if balanced, -1 if unbalanced
        def dfss(node):

            # base case
            if not node :
                return 0

            left = dfss(node.left)
            right = dfss(node.right)

            #  if left or right subtree gives -1 , 
            # then don't compute difference return -1
            if left == -1:
                return -1
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return dfss(root)!= -1


            



            

        