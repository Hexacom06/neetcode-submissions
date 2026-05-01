class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)  
        result = 0

        for num in numbers:
            
            if num-1 not in numbers:
                seq = 1
                while num+seq in numbers:
                    seq+=1
                if seq > result: result = seq
        return result