# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # EDGE CASE: Empty tree
        if not root:
            return []
            
        # Initialize the deque with the root node
        queue = deque([root])
        result = []
        
        # Keep running as long as the line isn't empty
        while queue:
            # THE SNAPSHOT: Lock in the number of nodes currently on this level
            level_size = len(queue)
            current_level = []
            
            # Process exactly that many nodes
            for _ in range(level_size):
                # O(1) removal from the front of the line
                node = queue.popleft() 
                
                current_level.append(node.val)
                
                # Add the children to the BACK of the line for the next iteration
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # The snapshot loop finished, meaning this level is done!
            result.append(current_level)
            
        return result
        
        
        
            