class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean = "".join(char.lower() for char in s if char.isalnum())
        n = len(s)
        # for i in range((n//2)):
        #     if clean[i] != clean[n-1-i]:
        #         return False
        # return True
        i, j = 0, n-1
        while i < n and j >= 0 and i < j:
            if not s[i].isalnum():
                i+=1
                continue
            elif not s[j].isalnum():
                j-=1
                continue
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i+=1 
                j-=1
        return True
