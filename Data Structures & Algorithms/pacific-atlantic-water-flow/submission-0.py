class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      R = len(heights)
      C = len(heights[0])
      # water = [[0]*C for _ in range(R)]
      pacvis, atlvis = set(), set()
      q = deque()
      for i in range(R):
        pacvis.add((i,0))
        # water[i][0] = 1
        q.append((i,0,heights[i][0]))
      for j in range(C):
        pacvis.add((0,j))
        # water[0][j] = 1
        q.append((0,j,heights[0][j]))

      dr = [-1, 1, 0, 0]
      dc = [0, 0, -1, 1]
      while q:
        r,c,val = q.popleft()
        for i in range(4):
          nr = r + dr[i]
          nc = c + dc[i]
          if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in pacvis:
            if heights[nr][nc] >= val:
              pacvis.add((nr,nc))
              # water[nr][nc] = 1
              q.append((nr,nc,heights[nr][nc]))
      
      for i in range(R):
        atlvis.add((i,C-1))
        # water[i][C-1] += 1
        q.append((i,C-1,heights[i][C-1]))
      for j in range(C):
        atlvis.add((R-1,j))
        # water[R-1][j] += 1
        q.append((R-1,j,heights[R-1][j]))
      
      while q:
        r,c,val = q.popleft()
        for i in range(4):
          nr = r + dr[i]
          nc = c + dc[i]
          if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in atlvis:
            if heights[nr][nc] >= val:
              atlvis.add((nr,nc))
              # water[nr][nc] += 1
              q.append((nr,nc,heights[nr][nc]))
      res = []
      for i in range(R):
        for j in range(C):
          if (i,j) in pacvis and (i,j) in atlvis:
            res.append([i,j])
      
      return res

        


            
          
          

