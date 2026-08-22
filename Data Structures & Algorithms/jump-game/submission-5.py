class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i == len(nums) -1 :
                return True
            if i >= len(nums) or nums[i] == 0:
                return False
            jumps = nums[i]
            m = 0
            opt = 0
            for j in range(1, jumps+1):
                if i + j <= len(nums)-1:
                    temp = m
                    m = max(i+j+nums[i+j], m)
                    if m != temp:
                        opt = j
            if opt == 0:
                return False
            return dfs(i+opt)
        return dfs(0)

                
            