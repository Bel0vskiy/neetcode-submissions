class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        dirs = [(1, 0), (0, 1)]
        def dfs(i, j):
            if i == m -1 and j == n -1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                memo[(i, j)] = 0
                for x,y in dirs:
                    if 0 <= i + x < m and 0<= j + y < n:
                        memo[(i, j)] += dfs(i+x, j+y)
            return memo[i, j]
        return dfs(0, 0)
        
