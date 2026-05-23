class DSU:
  def __init__(self,length):
    self.parent = [i for i in range(length)]
    self.rank = [1]*length
  
  def find(self,node):
    while node != self.parent[node]:
      node = self.parent[node]
    return node
  
  def union(self,node1,node2):
    root_x = self.find(node1)
    root_y = self.find(node2)

    if root_x == root_y: return False

    if self.rank[root_x] < self.rank[root_y]:
      self.parent[root_x] = root_y
      return root_y
    elif self.rank[root_x] > self.rank[root_y]:
      self.parent[root_y] = root_x
      return root_x
    else:
      self.parent[root_x] = root_y
      self.rank[root_x] += 1
      return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adj = [[] for _ in range(n)] 
        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        dsu = DSU(n)
        components = n

        for u,v in edges:
            if dsu.union(u,v):
                components -= 1
        return components

        