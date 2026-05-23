class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])
        def traversal(r,c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or not grid[r][c] or (r,c) in visited: return 0
            visited.add((r,c))
            return traversal(r-1,c) + traversal(r,c-1) + traversal(r+1,c) + traversal(r,c+1) + 1
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] and (i,j) not in visited:
                    area = traversal(i,j)
                    maxArea = max(area, maxArea)
        return maxArea