class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        n = len(nums)+1
        dp = [[0]*n for _ in range(2)]
        # dp[0][0] = -float('inf')
        # dp[1][0] = float('inf')
        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1]*nums[i-1],nums[i-1],dp[1][i-1]*nums[i-1])
            dp[1][i] = min(dp[1][i-1]*nums[i-1],nums[i-1],dp[0][i-1]*nums[i-1])
        res = -float('inf')
        for i in range(0,n):
            res = max(res,dp[0][i])
        return res