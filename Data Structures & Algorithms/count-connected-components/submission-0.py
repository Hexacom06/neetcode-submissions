class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1]*n
        parent = [i for i in range(n)]
        components = n
        def find( x):
          if x == parent[x]: 
            return x
          parent[x] = find(parent[x])
          return parent[x]
        
        def union(x,y):
          root_x = find(x)
          root_y = find(y)

          if root_x == root_y: return False

          if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
          elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
          else: 
            parent[root_y] = root_x
            rank[root_x] += 1
          return True

        # Process the graph one edge at a time
        for u,v in edges:
          if union(u,v):
            components -= 1
        return components
        
          

