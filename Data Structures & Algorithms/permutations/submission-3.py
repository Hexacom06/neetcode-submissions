class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(k):
            if k == len(nums):
                res.append(nums[:])
                return
            for i in range(k, len(nums)):
                nums[k], nums[i] = nums[i], nums[k]
                dfs(k+1)
                nums[i], nums[k] = nums[k], nums[i]

        dfs(0)
        return res

