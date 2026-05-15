# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traversal(node, a , b):
            if not node: return None
            if (a <= node.val and b >= node.val) or (a >= node.val and b <= node.val): return node
            elif a < node.val and b < node.val: return traversal(node.left,a,b)
            elif a > node.val and b > node.val: return traversal(node.right,a,b)
        return traversal(root, p.val, q.val)