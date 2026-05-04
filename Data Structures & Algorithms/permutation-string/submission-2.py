class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        freq = [0] * 26
        window = [0] * 26
        for c in s1:
            freq[ord(c)-ord('a')] += 1
        for c in s2[:len(s1)]:
            window[ord(c)-ord('a')] += 1
        if freq == window: return True
        
        for i in range(len(s1),len(s2)):
            window[ord(s2[i-len(s1)])-ord('a')] -= 1
            window[ord(s2[i])-ord('a')] += 1
            if freq == window: return True
        return False        