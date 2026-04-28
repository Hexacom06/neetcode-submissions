class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind,num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return[hashmap[diff],ind]
            hashmap[num] = ind
        return [-1,-1]