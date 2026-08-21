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
            for i in range(0, len(intervals)):
                if not occupation or occupation[0] > intervals[i].start:
                    heapq.heappush(occupation, intervals[i].end)
                else:
                    heapq.heappop(occupation)
                    heapq.heappush(occupation, intervals[i].end)
                rooms = max(rooms, len(occupation))
        return rooms



