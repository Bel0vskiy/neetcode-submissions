class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0,-1), (0, 1)]
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] == word[0]:
                    used = set()
                    used.add((i, j))
                    def dfs(i, j, num, used):
                        if num == len(word)-1:
                            return True
                        for x, y in dirs:
                            if 0 <= (i+x) < rows and 0 <= (j+y) < cols:
                                if board[i+x][j+y] == word[num+1] and (i+x, j+y) not in used:
                                    if dfs(i+x, j+y, num+1, used | {(i+x, j+y)}):
                                        return True
                        return False
                    if dfs(i, j, 0, used) == True:
                        return True
        return False
                    
