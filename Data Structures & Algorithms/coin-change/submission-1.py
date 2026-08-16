class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = {}
        def dfs(amount):
            if amount==0:
                return 0
            if amount in m:
                return m[amount]
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1+dfs(amount-coin))
                    m[amount] = res
            return res
        mc = dfs(amount)
        return -1 if mc == 1e9 else mc