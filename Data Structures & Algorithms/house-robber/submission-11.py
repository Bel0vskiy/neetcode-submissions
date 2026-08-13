class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, total):
            if i >= len(nums):
                return total
            if (i, total) not in memo:
                memo[(i, total)] = max(dfs(i+1, total), dfs(i+2, total + nums[i]))
            return memo[(i, total)]
        return dfs(0, 0)