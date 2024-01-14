#https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        freq = defaultdict(lambda:0)
        for i in nums:
            freq[i]+=1
        for key, val in freq.items():
            heapq.heappush(h, (-val, key))
        res = [heapq.heappop(h)[1] for _ in range(k)]
        return res
            
# #https://leetcode.com/problems/top-k-frequent-elements/
# import heapq
# from collections import defaultdict
# class HeapNode:
#     def __init__(self, key, val):
#         self.key, self.val = key,val
#     def __lt__(self, node):
#         return self.val > node.val
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         h = []
#         freq = defaultdict(lambda:0)
#         for i in nums:
#             freq[i]+=1
#         for key, val in freq.items():
#             heapq.heappush(h, HeapNode(key, val))
#         res = [heapq.heappop(h).key for _ in range(k)]
#         return res
            
