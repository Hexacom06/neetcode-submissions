class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def hourstaken(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours        
        
        lo, hi = 1, max(piles)
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if hourstaken(mid) <= h: 
                hi = mid - 1 # It works, but try slower
            else: 
                lo = mid + 1 # Too slow, must eat faster
                
        return lo # 'lo' will magically rest on the minimum valid speed!