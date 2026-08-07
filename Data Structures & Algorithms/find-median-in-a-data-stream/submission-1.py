import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # Stores the larger half of the numbers
        self.max_heap = [] # Stores the smaller half of the numbers (negated)

    def addNum(self, num: int) -> None:
        # 1. Push to max_heap (as negative)
        heapq.heappush(self.max_heap, -num)
        
        # 2. Balance: ensure the largest in max_heap is <= smallest in min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # 3. Balance sizes: max_heap can have equal size or 1 extra element compared to min_heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
        