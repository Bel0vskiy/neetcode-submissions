class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        new_intervals = []
        for interval in intervals:
            if not new_intervals or not interval[0] < new_intervals[-1][1]:
                new_intervals.append(interval)
            else:
                if interval[1] < new_intervals[-1][1]:
                    new_intervals.pop()
                    new_intervals.append(interval)
        return abs(len(intervals) - len(new_intervals))