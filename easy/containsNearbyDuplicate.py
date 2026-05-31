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
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # queue = deque()
        # for i in range(len(nums)):
        #     if i <= k:
        #         if nums[i] in queue:
        #             return True
        #         queue.append(nums[i])      Time limit exceeded 
        #     else:                          because searching a deque is O(n)
        #         queue.popleft()
        #         if nums[i] in queue:
        #             return True
        #         queue.append(nums[i])
        # return False

        window = set()
        for i, num in enumerate(nums):
            if i<=k:
                if num in window:
                    return True
                window.add(num)
            else:
                window.remove(nums[i - k - 1])
                if num in window:
                    return True
                window.add(num)
        return False

if __name__ == "__main__":
    solver = Solution()

    testcase = [1, 3, 2, 1, 10, 4]
    k = 3
    print(solver.containsNearbyDuplicate(testcase, k))