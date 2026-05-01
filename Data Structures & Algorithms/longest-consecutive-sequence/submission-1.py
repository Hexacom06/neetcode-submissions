class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:
            numbers.add(num)
        
        result = 0
        for num in numbers:
            seq,i = 0,0
            if num-1 in numbers:
                continue
            while num+i in numbers:
                seq+=1
                i+=1
            if seq > result: result = seq
        return result