class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])
        def traversal(r,c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or not int(grid[r][c]) or (r,c) in visited: return 0
            visited.add((r,c))
            dr = [1, -1, 0, 0]
            dc = [0, 0, 1, -1]
            for i in range(4):
                traversal(r+dr[i], c+dc[i])
        for i in range(ROW):
            for j in range(COL):
                if int(grid[i][j]) and (i,j) not in visited:
                    traversal(i,j)
                    islands += 1
        return islands




