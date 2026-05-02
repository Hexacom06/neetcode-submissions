class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j:
            # Move i forward until it hits an alphanumeric char
            while i < j and not s[i].isalnum():
                i += 1
            # Move j backward until it hits an alphanumeric char
            while i < j and not s[j].isalnum():
                j -= 1
                
            # Compare the characters
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            
        return True