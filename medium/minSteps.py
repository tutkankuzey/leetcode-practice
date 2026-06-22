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
    def minSteps(self, n: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            while n % i == 0:
                n = n // i
                ans += i
            if n == 1:
                break
        return ans

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.minSteps(16))