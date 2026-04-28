class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      mset = set(nums)
      if len(mset)<len(nums): return True
      else: return False  