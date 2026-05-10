class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in bracket_map: 
                if not stack: return False
                top = stack.pop()
                if bracket_map[c] != top: return False 
            else:
                stack.append(c)
        return not stack 
                