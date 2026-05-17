"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        newg = Node(node.val)
        visited = {}
        visited[node] = newg
        stack = [node]
        while stack:
          curr = stack.pop()
          for e in curr.neighbors:
            if e not in visited:
              visited[e] = Node(e.val)
              stack.append(e)
            visited[curr].neighbors.append(visited[e])
        return newg

              



