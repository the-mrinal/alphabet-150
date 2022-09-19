"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def __init__(self):
        self.cache = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def cloneHelper(root):
            if not root:
                return None
            
            if root in self.cache:
                return self.cache[root]
            
            clone_root = Node(root.val,[])
            
            self.cache[root] = clone_root
            
            for child in root.neighbors:
                clone_root.neighbors.append(cloneHelper(child))
            
            return clone_root
        
        return cloneHelper(node)