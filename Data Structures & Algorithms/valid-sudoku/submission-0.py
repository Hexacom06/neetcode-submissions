class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap_g = [[0] * 9 for _ in range(9)]
        for i in range(9):
            hashmap_r = [0]*9
            hashmap_c = [0]*9
            hashmap = [[0] * 9 for _ in range(9)]
            for j in range(9):
                if board[i][j] != ".":
                    if  hashmap_r[int(board[i][j])-1] >= 1:
                        return False
                    hashmap_r[int(board[i][j])-1] += 1
                if board[j][i] != ".":
                    if  hashmap_c[int(board[j][i])-1] >= 1:
                        return False
                    hashmap_c[int(board[j][i])-1] += 1

                if board[i][j] != ".":
                    val = int(board[i][j]) - 1
                    box_index = (i // 3) * 3 + (j // 3)
                    
                    if hashmap_g[box_index][val] > 0:
                        return False
                    hashmap_g[box_index][val] += 1
        return True