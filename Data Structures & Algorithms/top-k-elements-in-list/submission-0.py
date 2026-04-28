class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap, out = {}, []
        for val in nums:
            if val in hashmap: 
                hashmap[val] += 1
            else: 
                hashmap[val] = 1
        hashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse = True)[:k]
        out = [key for key,_ in hashmap]
        return out