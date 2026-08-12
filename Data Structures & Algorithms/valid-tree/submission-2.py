class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            else:
                visited.add(node)
            for i, nodes in enumerate(edges):
                if i == prev:
                    continue
                if nodes[0] == node:
                    if not dfs(nodes[1], i):
                        return False
                if nodes[1] == node:
                    if not dfs(nodes[0], i):
                        return False
            return True
        if dfs(0, -1) and not len(visited) < n:
            return True
        else:
            return False

