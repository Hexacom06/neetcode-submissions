class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pt = []
        for i in range(len(speed)):
            pt.append((position[i], (target-position[i])/speed[i]))
        pt.sort()
        stack = []
        for e in pt:
            while stack and stack[-1] <= e[1]:
                stack.pop()
            stack.append(e[1]) 
        return len(stack)
                