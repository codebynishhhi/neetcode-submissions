# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # using dfs Recurssion 
        # if not root:
        #     return 0

        # depth = 0
        # # first ask left subtree , what is your length then right subtree
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # depth += 1 

        # # combine length/ depth from both side
        # return 1 + max(left, right)

        # using BFS - Queue
        if not root :
            return 0

        new_q = deque([root])
        depth = 0

        while new_q:
            level_size = len(new_q)
            for _ in range(level_size):
                # pop the first node, 
                curr_node = new_q.popleft()

                # check for left and right children, if yes add to queue
                if curr_node.left:
                    new_q.append(curr_node.left)
                if curr_node.right:
                    new_q.append(curr_node.right)

            # as for loop completes 1 level completed so inc depth 
            depth += 1
        return depth


        