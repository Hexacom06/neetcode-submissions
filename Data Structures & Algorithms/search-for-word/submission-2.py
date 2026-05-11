class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i,j,ind):
            #Goal
            if ind == len(word): return True
            
            #Constraints
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return False
            if word[ind] != board[i][j]: return False
            if (i,j) in visited: return False

            #Choices
            #CHOOSE
            visited.add((i,j))
            #EXPLORE
            res = traverse(i+1,j,ind+1) or traverse(i-1,j,ind+1) or traverse(i,j+1,ind+1) or traverse(i,j-1,ind+1)
            #UNCHOOSE
            visited.remove((i,j))

            return res

        visited = set()
        for i,row in enumerate(board):
            for j,c in enumerate(row):
                if c == word[0]:
                   if traverse(i,j,0):
                    return True
        return False

        




