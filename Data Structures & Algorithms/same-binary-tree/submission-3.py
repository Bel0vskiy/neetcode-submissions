# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = self.makeQ(p)
        q2 = self.makeQ(q)
        return q1 == q2

    def makeQ(self, t):
        if not t:
            return []
        q = deque([t])
        arr = []
        while q:
            node = q.popleft()
            if node:
                arr.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                arr.append(None)
        return arr