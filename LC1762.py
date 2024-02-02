#https://leetcode.com/problems/buildings-with-an-ocean-view/submissions/1164137961/
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        st = collections.deque([0])
        for i in range(1,len(heights)):
            h = heights[i]
            while st and h >= heights[st[0]]:
                st.popleft()
            st.appendleft(i)
        out = []
        while st:
            out.append(st.pop())
        return out