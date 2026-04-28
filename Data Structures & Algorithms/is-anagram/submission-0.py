class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        if(len(s) != len(t)): return False
        for char in s:
            letters[ord(char)-ord('a')] += 1
        for char in t:
            letters[ord(char)-ord('a')] -= 1
        for values in letters:
            if values: return False
        return True
        
        return True
        