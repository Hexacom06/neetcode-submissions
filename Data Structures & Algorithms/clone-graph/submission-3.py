"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new = {}
        def dfs(curr):
          if curr in new: return new[curr]
          new[curr] = Node(curr.val)
          for node in curr.neighbors:
            new[curr].neighbors.append(dfs(node))
          return new[curr]
        return dfs(node) if node else None
        

              



