# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            if not node:
                return 0
            good = 1 if node.val >= m else 0
            m = max(node.val, m)
            return good + dfs(node.left, m) + dfs(node.right, m)

        return dfs(root, float('-inf'))