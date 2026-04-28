class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      mset = set(nums)
      return len(mset)<len(nums)