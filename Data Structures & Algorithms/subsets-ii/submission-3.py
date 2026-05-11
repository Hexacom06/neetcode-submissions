class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        def dfs(start_index, path):
            # 1. THE GOAL: In subsets, EVERY state is a valid subset!
            res.append(path[:])
            
            # 2. THE CHOICES: Loop through all remaining options
            for i in range(start_index, len(nums)):
                
                # 3. THE CONSTRAINT (Pruning Duplicates):
                # If we are looking at a number we just decided NOT to use 
                # at this current depth level, skip it!
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                    
                # CHOOSE, EXPLORE, UN-CHOOSE
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
                
        dfs(0, [])
        return res