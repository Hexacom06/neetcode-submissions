class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Base case
        if len(nums) == 1: return nums[0]
        
        # We start our sliding window at the first element
        prev_max = nums[0]
        prev_min = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # The exact same transition branches you wrote!
            curr_max = max(prev_max * num, num, prev_min * num)
            curr_min = min(prev_min * num, num, prev_max * num)
            
            # Slide the window
            prev_max = curr_max
            prev_min = curr_min
            
            global_max = max(global_max, curr_max)
            
        return global_max