class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i in range(len(nums)):
            if i > m:
                return False
            m = max(m, i + nums[i])
            if m >= len(nums)-1:
                return True
        return False
                
            