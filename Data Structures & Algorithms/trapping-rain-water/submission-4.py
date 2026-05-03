class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxl, maxr = height[l], height[r]
        area = 0
        if height==[]: return 0
        while l < r:
            if height[l] <= height[r]:
                l+=1
                if maxl-height[l]>0:
                    area+=maxl-height[l]
                if maxl < height[l]: maxl=height[l]
            else: 
                r-=1
                if maxr-height[r]>0:
                    area+=maxr-height[r]
                if maxr < height[r]: maxr=height[r]
        return area

        