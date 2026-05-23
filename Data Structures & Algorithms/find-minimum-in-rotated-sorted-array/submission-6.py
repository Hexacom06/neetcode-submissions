class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        res = float('inf')
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] <= nums[hi]: 
                res = min(nums[mid],res)
                hi = mid - 1
            else: 
                res = min(nums[lo],res)
                lo = mid + 1
        return res