class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for item in range(len(nums)-1):
            if(nums[item] == nums[item+1]):
                return True
        return False