class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    cnt+=1
                    def dfs(i, j):
                        grid[i][j] = '0'
                        for x, y in dirs:
                            if 0 <= i+x < rows and 0<= j+y < cols:
                                if grid[i+x][j+y] == '1':
                                    dfs(i+x, j+y)
                        return
                    dfs(i, j)
        return cnt
    
