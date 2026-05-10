class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        top = 0  # This acts as the size of our virtual stack
        
        for t in tokens:
            if t in "+-*/":
                # The numbers are sitting just behind our 'top' pointer
                num2 = int(tokens[top - 1])
                num1 = int(tokens[top - 2])
                
                if t == '+': res = num1 + num2
                elif t == '-': res = num1 - num2
                elif t == '*': res = num1 * num2
                elif t == '/': res = int(num1 / num2)  # Truncate toward zero
                
                # We consumed two numbers and produced one. 
                # Step the top pointer back by 1, and overwrite the position with the result.
                top -= 1
                tokens[top - 1] = res
                
            else:
                # It's a number. Overwrite the array at the 'top' pointer and move forward.
                tokens[top] = int(t)
                top += 1
                
        # The final answer is sitting at the very bottom of our virtual stack
        return int(tokens[0])