class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def hourstaken(k):
            hours = 0
            for pile in piles:
                hours += (pile+k-1)//k
            return hours
        def check(hours):
            return hours <= h
        lo, hi = 1, 10**9
        while lo <= hi:
            mid = (lo+hi)//2
            if check(hourstaken(mid)): hi = mid - 1
            else: lo = mid + 1
        return lo 
        