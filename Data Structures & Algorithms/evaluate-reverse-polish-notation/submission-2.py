class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                top = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(top)

            elif token == "-":
                top = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(top)

            elif token == "*":
                top = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(top)

            elif token == "/":
                top = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(top))

            else: stack.append(int(token))
        return stack[-1]