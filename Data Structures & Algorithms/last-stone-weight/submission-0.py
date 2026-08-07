class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y, x = - heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if x == y:
                continue 
            if x < y:
                y = y - x
                heapq.heappush(max_heap, -y)
        if len(max_heap) == 1:
            return -max_heap[0]
        return 0