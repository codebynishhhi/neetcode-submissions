# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # node val before curr node should be small
        # or curr node values should be greater than all previous nodes including root val
        def dfs_traversal(curr_node, max_val_up):

            # base case
            if not curr_node:
                return 0

            # all values before the curr node should small
            if curr_node.val >= max_val_up:
                is_good = 1
            else :
                is_good = 0

            # compare always with the max value & always update it 
            max_val_up = max(max_val_up, curr_node.val)

            left_good = dfs_traversal(curr_node.left, max_val_up)
            right_good = dfs_traversal(curr_node.right, max_val_up)
            
            return is_good + right_good + left_good

        return dfs_traversal(root, root.val)
    

        