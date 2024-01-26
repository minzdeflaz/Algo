# https://leetcode.com/problems/find-median-from-data-stream/
import heapq
class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, heapq.heappop(self.left) * -1)
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, heapq.heappop(self.right) * -1)

    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        elif len(self.right) < len(self.left):
            return self.left[0] * -1
        else:
            return (self.left[0] * -1 + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
