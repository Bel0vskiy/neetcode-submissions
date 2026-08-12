class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            else:
                visited.add(node)
                for new_node in graph[node]:
                    if new_node != parent:
                        dfs(new_node, node)
        dfs(0, -1)
        count = 1
        while len(visited) != n:
            for i in range(n):
                if i not in visited:
                    dfs(i, -1)
                    count+=1


        return count

