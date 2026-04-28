class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keymap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in keymap:
                return [keymap[diff], i]
            keymap[n] = i
        return []