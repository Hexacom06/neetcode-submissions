# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inord = {val: i for i, val in enumerate(inorder)}
        def build(l,r):
            if l > r: return None
            node_val = preorder.pop(0)
            node = TreeNode(node_val)
            node.left = build(l,inord[node_val]-1)
            node.right = build(inord[node_val]+1,r)
            return node
        return build(0,len(preorder)-1)
        
