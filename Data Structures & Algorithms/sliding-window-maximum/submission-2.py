class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()
        
        for i in range(len(nums)):
            
            # RULE 1: Ruthlessly kill ALL smaller numbers at the back.
            # This replaces your entire if/elif/else logic!
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
                
            # RULE 2: Always append the new guy to the back. 
            # (If he was the biggest, the loop above just emptied the whole 
            # deque for him, so the "back" is also the "front"!)
            q.append(i)
            
            # RULE 3: Remove the front if it's expired
            bound = i - k + 1
            if q[0] < bound:  # 'if' is safe here, only 1 element expires per step
                q.popleft()
                
            # RULE 4: Record the max once the window is full
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res