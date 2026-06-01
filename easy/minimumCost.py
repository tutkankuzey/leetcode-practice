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
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        length = len(cost)
        if length == 1:
            return cost[0]
        if length == 2:
            return cost[0] + cost[1]
        
        ans = 0
        for i in range(0, len(cost), 3):
            ans += cost[length - 1 - i] + cost[length - 2 - i]
            if length - 2 - i == 2:
                return ans + cost[0]
            elif length - 2 - i == 1:
                return ans
        return ans


if __name__ == "__main__":
    solver = Solution()
    nums = [1, 2, 3, 5, 6, 7, 9]
    print(solver.minimumCost(nums))




