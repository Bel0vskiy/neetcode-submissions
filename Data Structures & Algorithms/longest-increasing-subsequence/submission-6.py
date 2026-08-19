class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if i >= len(nums):
                return 0
            if (i, j) in memo:
                return memo[i, j]
            #option 1: skip
            res = dfs(i+1, j)
            #option 2: valid subsequence
            if j == -1 or nums[i] > nums[j]:
                memo[(i, j)] = max(res, 1 + dfs(i+1, i))
                return memo[(i, j)]
            return res
        return dfs(0, -1)