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
    def angleClock(self, hour: int, minutes: int) -> int:
        hourdegree = hour * 30 + minutes / 2
        minutedegree = minutes * 6
        candidate = max(hourdegree, minutedegree) - min(hourdegree, minutedegree)
        return min(candidate, 360 - candidate)

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.angleClock(12, 30))