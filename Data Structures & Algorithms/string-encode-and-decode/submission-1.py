class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code = code + str(len(s)) + '#' + s
        return code

    def decode(self, s: str) -> List[str]:
        strs, i = [], 0
        while i < len(s): 
            j = i
            while s[j] != '#':
                j += 1
            strlen = int(s[i:j])
            strs.append(s[j+1:j+strlen+1])
            i = j+strlen+1
        return strs