# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, m):
            if node.val >= m:
                m = node.val
                if node.left and node.right:
                    return 1 + dfs(node.left, m) + dfs(node.right, m)
                else:
                    if node.right:
                        return 1 + dfs(node.right, m)
                    elif node.left:
                        return 1 + dfs(node.left, m)
                    else:
                        return 1
            else:
                if node.left and node.right:
                    return dfs(node.left, m) + dfs(node.right, m)
                else:
                    if node.left:
                        return dfs(node.left, m)
                    if node.right:
                        return dfs(node.right, m)
            return 0
        cnt = dfs(root, float('-inf'))
        return cnt