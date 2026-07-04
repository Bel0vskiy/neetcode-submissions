class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m = 0
        while(l < r):
            cur = min(heights[l], heights[r]) * (r-l)
            if cur > m:
                m = cur
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return m
                    