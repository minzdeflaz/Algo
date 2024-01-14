#https://leetcode.com/problems/course-schedule/

from collections import defaultdict

def solution(numCourses: int , prerequisites: list[list[int]]) -> bool:
    prereq_map = defaultdict(set)
    for course, prereq in prerequisites:
        prereq_map[course].add(prereq)

    all_course = set(i for i in range(numCourses))
    taken = set()
    current = -1
    while left:= all_course - taken:
        if current == -1:
            current = left.pop()
        if prereq_map[current]:
            if not_taken := prereq_map[current] - taken:
                current = not_taken.pop()
            else:
                taken.add(current)
                current = 0
        else:
            taken.add(current)
            current = 0
        

if __name__ == "__main__":
    assert solution(2, [[1,0]]) == True
    assert solution(2, [[1,0], [0,1]]) == True