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
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        pass

if __name__ == "__main__":
    solver = Solution()
    
    nums = [1, 2, 4, 7, 10, -10]
    indexdiff = 5
    valuediff = 10

    print(solver.containsNearbyAlmostDuplicate(nums, indexdiff, valuediff))