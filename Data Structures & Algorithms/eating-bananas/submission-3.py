class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hourstaken(k):
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/k)
            return hours        
        
        lo , hi, res = 1, 0, len(piles)
        for pile in piles:
            hi = max(pile,hi)
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if hourstaken(mid) <= h: 
                res = mid
                hi = mid - 1
            else: lo = mid + 1
        return res
        