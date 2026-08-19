class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev_idx):
            if i >= len(nums):
                return 0
            if (i, prev_idx) in memo:
                return memo[(i, prev_idx)]
            
            res = dfs(i + 1, prev_idx)
            
            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                res = max(res, 1 + dfs(i + 1, i))
            
            memo[(i, prev_idx)] = res
            return res
        
        return dfs(0, -1)