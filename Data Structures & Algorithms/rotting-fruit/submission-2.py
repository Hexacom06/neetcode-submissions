class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    time = 0
    fresh = 0
    visited = set()
    q = deque()
    R, C = len(grid), len(grid[0])
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 2:
          visited.add((i,j)) 
          q.append((i,j))
        if grid[i][j] == 1:
          fresh += 1
    while q and fresh > 0:
      lenq = len(q)
      for _ in range(lenq):
        r,c = q.popleft()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
          nr = r+dr[i]
          nc = c+dc[i]
          if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in visited:
            if grid[nr][nc] == 1: 
              fresh -= 1
              visited.add((nr,nc))
              q.append((nr,nc))
      time += 1
    return time if not fresh else -1
            