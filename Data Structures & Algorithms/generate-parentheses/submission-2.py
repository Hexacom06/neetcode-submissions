class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []
        def backtrack(openN,closedN):
            #Goal
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            #Constraints
            if openN < n:
                #Choices
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            #Constraints
            if closedN < openN:
                #Choices
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()

        backtrack(0,0)
        return res
            
