class Solution:

    def encode(self, strs: List[str]) -> str:
        coded=""
        for s in strs:
            coded += str(len(s))+'#'+s
        return coded
    def decode(self, s: str) -> List[str]:
        i,length,strlen = 0,len(s),0
        strs = []
        while i < length:
            j = i
            while j < length:
                if s[j] == '#':
                    strlen = int(s[i:j])
                    strs.append(s[j+1:j+strlen+1])
                    i = j+strlen+1
                    break
                j+=1
        return strs