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
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = i
        return False
    


if __name__ == "__main__":
    solver = Solution()

    testcase = [1, 3, 4, 7, 10, 2]
    print(solver.containsDuplicate(testcase))