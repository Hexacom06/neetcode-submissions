# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p,q))

        while queue:
            nodep, nodeq = queue.popleft()
            # SAFETY CHECK 1: Did we just pop two None values? 
            # That means this branch matches perfectly. Skip to the next pair!
            if not nodep and not nodeq:
                continue
                
            # SAFETY CHECK 2: Is only ONE of them None?
            # Because Check 1 passed, if this triggers, it means one is real and one is None.
            if not nodep or not nodeq:
                return False
                
            # Now it is 100% safe to check the values!
            if nodep.val != nodeq.val: 
                return False
            if nodep.val != nodeq.val: return False
            if nodep.left or nodeq.left:
                queue.append((nodep.left,nodeq.left))
            if nodep.right or nodeq.right: 
                queue.append((nodep.right,nodeq.right))
        return True
