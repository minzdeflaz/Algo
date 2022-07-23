#https://leetcode.com/problems/meeting-rooms-ii/

import heapq
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 0:
            return 0
        heap = [intervals[0][1]]

        for start, end in intervals[1::]:
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)