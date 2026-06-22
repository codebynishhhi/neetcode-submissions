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

        # create hashmap to store old node-> new node mapping
        # hmap = {A:A', B:B'...ETC}
        hmap = {}

        # 1. create all new copy nodes and store in hashmap
        curr = head
        while curr :
            hmap[curr] = Node(curr.val)
            curr = curr.next 
        
        curr = head
        while curr:
            # When you write copy = hmap[curr], 
            # you are telling Python:"Look at the original node 
            # that curr is currently standing on."
            # "Go to the hmap dictionary and find that exact original node's name.
            # ""Grab the brand-new cloned node (A', B', etc.) 
            # that we paired up with it during our first loop pass.
            # ""Make the variable copy point directly to that fresh cloned node in memory."
            copy = hmap[curr]
            copy.next = hmap.get(curr.next)
            copy.random = hmap.get(curr.random)

            curr = curr.next
        return hmap[head]



        