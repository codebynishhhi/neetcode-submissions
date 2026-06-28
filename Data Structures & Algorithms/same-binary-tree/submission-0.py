# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        new_p = deque([p])
        new_q = deque([q])

        while new_p and new_q:
            curr_p = new_p.popleft()
            curr_q = new_q.popleft()

            # if str for both are same
            if not curr_p and not curr_q:
                continue
            
            if not curr_p or not curr_q or curr_p.val != curr_q.val:
                return False 

            # append left in queue
            new_p.append(curr_p.left)
            new_q.append(curr_q.left)

            # append right in queue
            new_p.append(curr_p.right)
            new_q.append(curr_q.right)
        return True

             


        