# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # LEVEL OREDR TRAVERSAL - BFS
        
        if not root :
            return []
        
        new_q = deque([root])
        result = []
        while new_q:
            curr_result = []
            for _ in range(len(new_q)):
                node = new_q.popleft()
                curr_result.append(node.val)
            
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                
            result.append(curr_result)
        return result

                

        