# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        new_q = deque([root])
        result = []
        while new_q:
            level_size = len(new_q)
            for i in range(level_size):
                node = new_q.popleft()

                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)

        return result