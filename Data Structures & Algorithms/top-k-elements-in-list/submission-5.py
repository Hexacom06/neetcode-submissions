class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        top_k=[]
        for num in nums:
            count[num] = 1+count.get(num,0)
        for key,val in count.items():
            freq[val].append(key)
        for numlist in freq[::-1]:
            top_k.extend(numlist)
            if len(top_k) >= k:
                return top_k[:k]
