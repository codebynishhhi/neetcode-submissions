"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return None
        
        hmap = {}
        curr = head
        while curr:
            # 1. create all new copy nodes and store in hmap and map
            hmap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr :
            copy = hmap[curr]
            copy.next = hmap.get(curr.next)
            copy.random = hmap.get(curr.random)
            curr = curr.next
        return hmap[head]



        