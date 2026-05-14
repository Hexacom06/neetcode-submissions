# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node: return (True,0)
            
            lbal, lht = check(node.left)
            if not lbal: return (False,0)
            rbal, rht = check(node.right)
            if not rbal: return (False,0)

            if abs(lht-rht) > 1: return (False,0)
            return (True, max(lht,rht)+1)
        balanced,height = check(root)
        return balanced

