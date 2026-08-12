class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(node, prev):
            if node in visited:
                return False
            else:
                visited.add(node)
            for n in adj[node]:
                if n != prev:
                    if not dfs(n, node):
                        return False
            return True
        if dfs(0, -1) and not len(visited) < n:
            return True
        else:
            return False

