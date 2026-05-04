class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        most,longest, l = 0, 0, 0
        for r in range(0,len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            most = max(most, freq[ord(s[r]) - ord('A')])
            diff = r-l+1 - most
            if k < diff:
                freq[ord(s[l]) - ord('A')] -= 1
                l+=1
                continue
            longest = max(longest, r-l+1)
        return longest