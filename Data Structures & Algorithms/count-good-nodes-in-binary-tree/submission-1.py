class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, path_max):
            # Base Case: The void contains 0 good nodes.
            if not node: 
                return 0
            
            # 1. PROCESS: Am I a good node? (Score is 1 if True, 0 if False)
            my_score = 1 if node.val >= path_max else 0
            
            # 2. UPDATE: The new max for my children
            new_max = max(path_max, node.val)
            
            # 3. THE PLUNGE (Arguments go DOWN, answers come UP)
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)
            
            # 4. BUBBLE UP: Return the total sum of this entire branch
            return my_score + left_count + right_count
            
        # Kick off the traversal! The initial max is just the root's value.
        return dfs(root, root.val)