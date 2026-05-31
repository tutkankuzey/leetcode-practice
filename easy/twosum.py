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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            new_target = target - nums[i]
            if new_target in seen:
                return [i, seen[new_target]]
            seen[num] = i

if __name__ == "__main__":
    solver = Solution()
    
    nums = [1, 2, 4, 7, 10, -10]
    target = 0

    print(solver.twoSum(nums, target))