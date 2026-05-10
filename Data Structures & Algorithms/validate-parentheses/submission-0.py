class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[': 
                stack.append(c)
            else: 
                if not stack: return False
                top = stack.pop()
                if c == ')' and top == '(': continue
                elif c == '}' and top == '{': continue
                elif c == ']' and top == '[': continue
                else: return False
        if not stack: return True
        return False