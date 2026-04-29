class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fprod, bprod = 1, 1
        l = len(nums)
        result = []

        for i in range(l):
            result.append(fprod)
            fprod *= nums[i]
        for i in range(l-1,-1,-1):
            result[i] *= bprod
            bprod *= nums[i]
        
        return result