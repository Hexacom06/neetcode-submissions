class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)+1
        prev2 = 0
        prev1 = nums[0]
        for i in range(2,n):
          current = max(prev2+nums[i-1], prev1)
          prev2 = prev1
          prev1 = current
        return prev1