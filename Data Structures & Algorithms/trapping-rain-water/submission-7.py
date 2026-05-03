class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxl, maxr = height[l], height[r]
        area = 0
        if height==[]: return 0
        while l < r:
            if height[l] <= height[r]:
                l+=1
                maxl = max(maxl, height[l])
                area += maxl - height[l]
            else: 
                r-=1
                maxr = max(maxr, height[r])
                area += maxr - height[r]
        return area