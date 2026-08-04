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
        levels = defaultdict(list)
        q = deque([(root, 1)])
        m = 0
        while q:
            node, depth = q.popleft()
            levels[depth].append(node.val)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
            m = max(depth, m)
        arr = []
        for i in range(1, m+1):
            arr.append(levels[i])
        return arr
            
            
