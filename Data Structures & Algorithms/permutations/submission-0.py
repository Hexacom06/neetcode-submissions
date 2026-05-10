class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        freq = [False]*len(nums)
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i] = True
                    cur.append(nums[i])
                    dfs(cur)
                    cur.pop()
                    freq[i] = False
        dfs(cur)
        return res
