class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            # if not stack: stack.append((i,h))
            ind = i
            while stack and stack[-1][1] > h:
                area = (i - stack[-1][0]) * stack[-1][1]
                max_area = max(max_area, area)
                ind, _ = stack.pop()
            stack.append((ind, h))
        for i,h in stack:
            area = (len(heights) - i)*h
            max_area = max(max_area, area)
        return max_area
