import sys
import os
import math
import random
import bisect
import heapq
import collections
import itertools
import functools
import operator
import re

from typing import *
from collections import deque, Counter, defaultdict
from heapq import heapify, heappush, heappop
from bisect import bisect_left, bisect_right
from functools import lru_cache

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
    
        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        bucket = {}
        min_maxGap = math.ceil((max_val - min_val) / (len(nums) - 1))
        for num in nums:
            value = (num - min_val) // min_maxGap
            if value not in bucket:
                bucket[value] = [num, num]
            elif num > bucket[value][1]:
                bucket[value][1] = num
            elif num < bucket[value][0]:
                bucket[value][0] = num
        
        ans = 0
        prev_max = None
        for key in sorted(bucket.keys()):
            if prev_max != None:
                ans = max(ans, bucket[key][0] - prev_max)
            prev_max = bucket[key][1]
        return ans

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    test_input = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 2, 3, 3, 3, 3, 3]
    print(sol.maximumGap(test_input))