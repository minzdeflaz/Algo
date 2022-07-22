# Link: https://leetcode.com/problems/course-schedule-iii/

from heapq import *

def scheduleCourse(courses: list[list[int]]) -> int:
        
        courses = sorted(courses, key=lambda x: x[1])
        heap = []
        start = 0
        for c in courses:
            if start + c[0] > c[1]:
                if not heap: 
                    continue
                largest = -heappop(heap)
                if largest < c[0] or start - largest + c[0] > c[1]:
                    heappush(heap, -largest)
                else:
                    heappush(heap, -c[0])  
                    start = start - largest + c[0]
            else:
                heappush(heap, -c[0])
                start += c[0]
        return len(heap)

if __name__ == "__main__":
  input = [[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]
  print(scheduleCourse(input))
