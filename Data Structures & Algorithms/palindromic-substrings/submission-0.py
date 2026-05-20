class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            # odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1

            #even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:  
                total += 1
                l -= 1
                r += 1
        return total

