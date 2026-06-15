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
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        greater = []

        pivot_count = 0
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                pivot_count += 1
        
        ans = smaller + [pivot] * pivot_count + greater
        return ans

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.pivotArray(test_input))