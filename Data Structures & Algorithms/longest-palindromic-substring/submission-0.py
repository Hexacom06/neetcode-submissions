class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        ind = (0,0)
        for i in range(len(s)):
            # Odd Length Palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pal = r-l+1
                if longest < pal:
                    longest = pal
                    ind = (l,r)
                l -= 1
                r += 1
            # Even length palindromes    
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pal = r-l+1
                if longest < pal:
                    longest = pal
                    ind = (l,r)
                l -= 1
                r += 1
        return s[ind[0]:ind[1]+1]  


