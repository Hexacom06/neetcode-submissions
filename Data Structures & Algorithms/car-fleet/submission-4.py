class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pt = []
        for i in range(len(speed)):
            pt.append((position[i], (target-position[i])/speed[i]))
        pt.sort(reverse = True)
        stack = []
        for p, t in pt:
            if not stack or t > stack[-1]:
                stack.append(t) 
        return len(stack)
                