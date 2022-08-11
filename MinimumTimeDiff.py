# https://leetcode.com/problems/minimum-time-difference/
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(time[0:2])*60 + int(time[3:5]) for time in timePoints]
        timePoints.sort()
        minDiff = 24*60 + timePoints[0] - timePoints[-1]
        for id in range(len(timePoints) - 1):
            diff = timePoints[id + 1] - timePoints[id]
            minDiff = min(minDiff, diff)
        return minDiff
