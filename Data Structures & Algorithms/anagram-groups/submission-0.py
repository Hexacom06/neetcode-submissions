class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        start = ord('a')
        hshmp = {}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)- start]+=1
            signature = tuple(count)
            if signature not in hshmp:
                hshmp[signature] = []
            hshmp[signature].append(s)
        
        return list(hshmp.values())

            
            
            