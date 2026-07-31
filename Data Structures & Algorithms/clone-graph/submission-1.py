"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 

        copies_hmap = {}

        # dfs for the node from input on graph traversal
        def dfs(node):
            
            # base condition 
            # as i traverse - the given node if in copies hmap
            # meaning its already in dict return the value
            if node in copies_hmap :
                return copies_hmap[node]
            
            # base condition fails - new copy node found
            # create new copy node
            new_copy_node = Node(node.val)

            # store the new copy node
            copies_hmap[node] = new_copy_node

            # explore neighbhors of this node
            for neigh in node.neighbors:
                cloned_neighbour = dfs(neigh)
                new_copy_node.neighbors.append(cloned_neighbour)

            return new_copy_node
        return dfs(node)
        