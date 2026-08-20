class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 1:
            return intervals
        i = 1
        while i < len(intervals):
            a,b = intervals[i][0], intervals[i][1]
            c, d = intervals[i-1][0], intervals[i-1][1]
            if a <= d:
                intervals[i] = [c, max(d, b)]
                del intervals[i-1]
            else:
                i+=1
        return intervals