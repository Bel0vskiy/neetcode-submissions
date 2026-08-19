class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordDict = set(wordDict)
        def dfs(i, j, ref):
            if len(ref) == 0:
                return True
            if i >= len(s) or j >= len(s):
                return False
            temp = s[i:j+1]
            if (i, j) in memo:
                return memo[(i, j)]
            if temp in wordDict:
                temp = ref
                ref = s[j+1:len(s)]
                if dfs(j+1, j+1, ref) or dfs(i, j+1, temp):
                    memo[(i, j)] = True
                    return True
                else:
                    memo[(i, j)] = False
            return dfs(i, j+1, ref)
        return dfs(0, 0, s)
            
            