"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        occupation = []
        rooms = 0
        if len(intervals) == 1:
            return 1
        else:
            for interval in intervals:
                if occupation and occupation[0] <= interval.start:
                    heapq.heappop(occupation)
                heapq.heappush(occupation, interval.end)
        return len(occupation)



