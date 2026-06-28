# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # following dfs using recurssion 

        # base case 
        # if not root :
        #     return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # using BFS queue data structure - level wise traversal
        if not root:
            return

        # initialization
        new_q = deque([root])
        while new_q:
            # curr pointer points to the first ele of queue always
            curr = new_q.popleft()

            # swap logic using tuple assignment in python
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                new_q.append(curr.left)
            if curr.right:
                new_q.append(curr.right)
        return root
