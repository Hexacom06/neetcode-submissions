class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fprod, bprod = 1, 1
        l = len(nums)
        forward, backward, result = [1]*l, [1]*l, []
        forward[0] = 1
        backward[l-1] = 1
        for i in range(1,l):
            fprod *= nums[i-1]
            forward[i] = fprod
            bprod *= nums[l-i]
            backward[l-i-1] = bprod
        for i in range(l):
            result.append(forward[i]*backward[i])
        return result
            