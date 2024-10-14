import math
import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        s = 0
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        while k > 0:
            max_val = -heapq.heappop(max_heap)
            s += max_val
            heapq.heappush(max_heap, -math.ceil(max_val / 3))
            k -= 1
        return s
