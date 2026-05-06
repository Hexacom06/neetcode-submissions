class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for num in nums: #O(n)
            num *= -1
        for i in range(k): #O(k)
            heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])

        for i in range(k,len(nums)): #O(n-k+1) = O(n)
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res  

