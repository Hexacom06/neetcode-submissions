from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pac_q = deque()
        atl_q = deque()
        pac_vis = set()
        atl_vis = set()
        
        # 1. Gather all sources simultaneously
        for r in range(ROWS):
            pac_q.append((r, 0)); pac_vis.add((r, 0))
            atl_q.append((r, COLS - 1)); atl_vis.add((r, COLS - 1))
            
        for c in range(COLS):
            pac_q.append((0, c)); pac_vis.add((0, c))
            atl_q.append((ROWS - 1, c)); atl_vis.add((ROWS - 1, c))
            
        # 2. The Reusable BFS Engine
        def bfs(queue, visited):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If out of bounds, already visited, or TOO SHORT to flow uphill -> Skip
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or 
                        (nr, nc) in visited or 
                        heights[nr][nc] < heights[r][c]):
                        continue
                        
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        # 3. Fire the engines
        bfs(pac_q, pac_vis)
        bfs(atl_q, atl_vis)
        
        # 4. The Pythonic Intersection
        # The '&' operator instantly finds all coordinates that exist in BOTH sets
        return list(pac_vis & atl_vis)