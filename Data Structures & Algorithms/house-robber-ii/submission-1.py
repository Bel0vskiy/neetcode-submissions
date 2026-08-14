class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        wfirst = nums[1:]
        wlast = nums[0:len(nums)-1]
        memof = {}
        memol = {}
        def dfs(arr, i, t):
            if i >= len(arr):
                return 0
            if t:
                if i in memof:
                    return memof[i]
                else:
                    memof[i] = max(dfs(wfirst, i+2, True) + wfirst[i], dfs(wfirst, i+1, True))
                    return memof[i]
            else:
                if i not in memol:
                    memol[i] = max(dfs(wlast, i+2, False) + wlast[i], dfs(wlast, i+1, False))
                    return memol[i]
                else:
                    return memol[i]
        return max(dfs(wfirst, 0, True), dfs(wlast, 0, False))