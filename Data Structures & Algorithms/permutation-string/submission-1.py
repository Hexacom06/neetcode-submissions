class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ht = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        mult = 1
        if len(s2)<len(s1): return False
        for c in s1:
            mult *= ht[ord(c) - ord('a')]
        check = 1
        for i in range(0,len(s1)):
            check *= ht[ord(s2[i])-ord('a')]
        if check == mult:
            return True
        for i in range(len(s1), len(s2)):
            check *= ht[ord(s2[i])-ord('a')]
            check //= ht[ord(s2[i-len(s1)])-ord('a')]
            if check ==  mult: return True
        return False