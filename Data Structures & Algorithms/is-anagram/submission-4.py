class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        start = ord('a')
        for char in s:
            count[ord(char.lower()) -  start]+=1
        for char in t:
            count[ord(char.lower()) -  start]-=1
        for val in count:
            if val != 0:
                return False
        return True
        
        
        