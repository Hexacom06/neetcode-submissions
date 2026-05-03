class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = [0]*len(height)
        n,left,right = len(height),0,0
        for h in height:
            if left < h:
                left = h
            left_max.append(left)
        for i in range(n-1, -1, -1):
            if right < height[i]:
                right = height[i]
            right_max[i] = right
        area = 0
        for i in range(n):
            temp = min(left_max[i],right_max[i])-height[i]
            # if temp > 0:
            area += temp
        return area