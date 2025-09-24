# 9. KthLargestElement.py
import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
