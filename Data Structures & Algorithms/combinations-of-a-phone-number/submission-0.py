class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(k, curr):
            if k == len(digits):
                res.append(curr)
                return
            for i in range(len(mapping[digits[k]])):
                dfs(k+1,curr+mapping[digits[k]][i])
        
        dfs(0,"")
        return res



