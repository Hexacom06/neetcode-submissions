class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.visited = set()
        def traverse(r,c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]): return (True,[])
            if board[r][c] == 'X' or (r,c) in self.visited: return (False,[])
            self.visited.add((r,c))
            change = [[r,c]]
            b1,c1 = traverse(r-1,c)
            b2,c2 = traverse(r,c-1)
            b3,c3 = traverse(r+1,c)
            b4,c4 = traverse(r,c+1)
            change.extend(c1+c2+c3+c4)
            return (b1 or b2 or b3 or b4, change)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    flag,group = traverse(i,j)
                    if not flag:
                        for r,c in group:
                            board[r][c] = 'X'
                        
