# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        ans = []
        q = deque([root]) # No need to store the depth tuple anymore!
        
        while q:
            level_length = len(q) # How many nodes are on this specific level
            current_level = []
            
            # Pop exactly the number of nodes on this level
            for _ in range(level_length):
                node = q.popleft()
                current_level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Add the completed level directly to the final answer
            ans.append(current_level)
            
        return ans
