class Solution:
  def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    dist = 1
    visited = set()
    q = deque()
    R, C = len(grid), len(grid[0])
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 0:
          visited.add((i,j)) 
          q.append((i,j))
        # if grid[i][j] == 1:
        #   fresh += 1
    while q:
      lenq = len(q)
      for _ in range(lenq):
        r,c = q.popleft()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
          nr = r+dr[i]
          nc = c+dc[i]
          if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in visited:
            if grid[nr][nc] == 2147483647: 
              visited.add((nr,nc))
              grid[nr][nc] = dist
              q.append((nr,nc))
      dist += 1
    return