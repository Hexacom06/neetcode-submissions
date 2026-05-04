class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l, r = 0, 0, 0
        lookup = set()
        for r in range(len(s)):
            if s[r] in lookup:
                while l <= r:    
                    if s[l] == s[r]:
                        lookup.remove(s[l])
                        l += 1
                        break    
                    lookup.remove(s[l])
                    l += 1
            lookup.add(s[r])
            longest = max(longest,r-l+1)
        return longest          