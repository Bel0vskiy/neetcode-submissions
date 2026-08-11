"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        m = {}
        q = deque([node])
        visited = set()
        val = node.val
        while q:
            n = q.popleft()
            if n not in visited:
                visited.add(n)
                m[n.val] = n
                for nn in n.neighbors:
                    if nn not in visited:
                        q.append(nn)
        m_new = {}
        for k in m:
            m_new[k] = Node(k)
        for k, v in m.items():
            for n in v.neighbors:
                m_new[k].neighbors.append(m_new[n.val])
        return m_new[val]