class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        start = ord('a')
        hshmp = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)- start]+=1
            hshmp[tuple(count)].append(s)
        
        return list(hshmp.values())

            
            
            