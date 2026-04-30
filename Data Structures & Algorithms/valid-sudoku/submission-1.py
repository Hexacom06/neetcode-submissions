import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create dictionaries where the default value is a new, empty set
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # Key will be a tuple: (r // 3, c // 3)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Rule Check: Is the value already in our tracking sets?
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[(r // 3, c // 3)]):
                    return False
                
                # If not, add the value to all three tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
                
        # If we check every cell and find no duplicates, the board is valid
        return True