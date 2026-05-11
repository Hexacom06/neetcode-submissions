class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        def dfs(k):
            if k == len(s): 
                res.append(path[:])
                return
            for i in range(k,len(s)):
                sliced = s[k:i+1]
                if sliced == sliced[::-1]:
                    path.append(sliced)
                    dfs(i+1)
                    path.pop()
        dfs(0)    
        return res

