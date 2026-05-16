class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        self.visited= set()
        def traverse(r,c):
            if (r,c) in self.visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or not int(grid[r][c]): return 0
            self.visited.add((r,c))
            a = 0
            a += traverse(r-1,c)
            a += traverse(r,c-1)
            a += traverse(r+1,c)
            a += traverse(r,c+1)
            return a + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited and int(grid[i][j]):
                    area = traverse(i,j)
                    maxarea = max(area,maxarea)
        return maxarea