class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        # dp = [0]*(len(s)+1)
        prev1, prev2= 1, 1
        for i in range(2,len(s)+1):
            current = 0
            sdig = int(s[i-1:i])
            ddig = int(s[i-2:i])
            if sdig != 0:
                current += prev1
            if 9 < ddig <= 26:
                current += prev2
            prev2 = prev1
            prev1 = current
        return prev1
            