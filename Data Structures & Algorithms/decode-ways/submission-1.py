class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        dp = [0]*(len(s)+1)
        dp[0], dp[1] = 1, 1
        for i in range(2,len(s)+1):
            sdig = int(s[i-1:i])
            ddig = int(s[i-2:i])
            if sdig != 0:
                dp[i] += dp[i-1]
            if 9 < ddig <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
            