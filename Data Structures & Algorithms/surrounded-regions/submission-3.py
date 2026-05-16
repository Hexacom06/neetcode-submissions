class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # self.visited = set()
        def traverse(r, c):
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]) or board[r][c] == 'X' or board[r][c] == 'T': return
            board[r][c] = 'T'
            traverse(r-1,c)
            traverse(r,c-1)
            traverse(r+1,c)
            traverse(r,c+1)
        for i in range(len(board)):
            if board[i][0] == 'O':
                traverse(i,0)
            if board[i][len(board[0])-1] == 'O':
                traverse(i,len(board[0])-1)
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                traverse(0,i)
            if board[len(board)-1][i] == 'O':
                traverse(len(board)-1,i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' :
                    board[i][j] = 'X'
                if board[i][j] == 'T' :
                    board[i][j] = 'O'       


