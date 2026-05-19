class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums1 = nums[1:]
        prev2 = 0
        prev1 = nums1[0]
        for i in range(2,len(nums)):
          current = max(prev2+nums1[i-1], prev1)
          prev2 = prev1
          prev1 = current

        nums2 = nums[:-1]
        prev4 = 0
        prev3 = nums2[0]
        for i in range(2,len(nums)):
          current = max(prev4+nums2[i-1], prev3)
          prev4 = prev3
          prev3 = current

        return max(prev1, prev3)