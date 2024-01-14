#https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        visited = set()
        nums = set(nums)
        max_length = 0
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            length = 1
            temp = num-1
            while temp in nums:
                visited.add(temp)
                length +=1
                temp-=1
            temp = num+1
            while temp in nums:
                visited.add(temp)
                length +=1
                temp+=1
            max_length = max(max_length, length)
        return max_length
#O(n)


# #https://leetcode.com/problems/longest-consecutive-sequence/
# import heapq
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         h = []
#         seen = set()
#         for i in nums:
#             if i not in seen:
#                 seen.add(i)
#                 heapq.heappush(h, i)
        
#         max_length = 1
#         length = 1
#         last = heapq.heappop(h)
#         while h:
#             curr = heapq.heappop(h)
#             if curr == last+1:
#                 length+=1
#             else:
#                 max_length = max(max_length, length)
#                 length=1
#             last = curr
#         return max(max_length, length)
## O(nlogn)