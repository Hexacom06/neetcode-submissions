class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        self.visited= set()
        def traverse(r,c):
            if (r,c) in self.visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or not int(grid[r][c]): return
            self.visited.add((r,c))
            traverse(r-1,c)
            traverse(r,c-1)
            traverse(r+1,c)
            traverse(r,c+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited and int(grid[i][j]):
                    # self.visited.add((i,j))
                    traverse(i,j)
                    islands += 1
        return islands



