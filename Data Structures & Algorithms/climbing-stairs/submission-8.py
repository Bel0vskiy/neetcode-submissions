class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def search(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            if curr in memo:
                return memo[curr]
            memo[curr] = search(curr+1) + search(curr+2)
            return memo[curr]
            
        return search(0)