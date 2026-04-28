class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed = set()
        for item in nums:
            if item in hashed:
                return True
            hashed.add(item)
        return False