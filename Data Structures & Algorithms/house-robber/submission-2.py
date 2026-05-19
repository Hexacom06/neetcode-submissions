class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)+1
        dp = [0] * n
        if len(nums) >= 2:
          dp[0], dp[1], dp[2] = 0, nums[0], nums[1]
        else: return nums[0]
        for i in range(3,n):
          for j in range(2,i+1):
            if i > 2:  
              dp[i] = max(dp[i],dp[i-j]+nums[i-1])
        return max(dp[n-1],dp[n-2])