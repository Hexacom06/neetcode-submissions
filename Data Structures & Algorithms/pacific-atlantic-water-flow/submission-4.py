class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        
        R, C = len(heights), len(heights[0])
        pac_vis, atl_vis = set(), set()
        
        def dfs(r,c,visited,prev):
            if r < 0 or c < 0 or r == R or c == C or (r,c) in visited or heights[r][c] < prev: return
            visited.add((r,c))
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for i in range(4):
              dfs(r+dr[i],c+dc[i],visited,heights[r][c])

        for i in range(R):
          dfs(i,0,pac_vis,heights[i][0])
          dfs(i, C - 1, atl_vis, heights[i][C-1])
        for j in range(C):  
          dfs(0,j,pac_vis,heights[0][j])
          dfs(R - 1, j, atl_vis, heights[R-1][j])
        
        return list(pac_vis & atl_vis)