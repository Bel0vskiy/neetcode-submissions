# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        m = defaultdict(list)
        q = deque([(root, 0)])
        ma = 0
        while q:
            for i in range(len(q)):
                node, l = q.popleft()
                m[l].append(node.val)
                if node.left:
                    q.append((node.left, l+1))
                if node.right:
                    q.append((node.right, l+1))
                ma = max(ma, l)
        ans = [0] * (ma + 1)
        for i, arr in m.items():
            ans[i] = arr[len(arr)-1]
        return ans