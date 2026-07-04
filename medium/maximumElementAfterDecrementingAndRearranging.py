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
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)

        current_max = 0
        ans = 0
        for i in range(len(arr)):
            if arr[i] > current_max:
                ans += 1
                current_max += 1
            else:
                continue
        return ans

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    test_input = [1,2,3,4,5]
    print(sol.maximumElementAfterDecrementingAndRearranging(test_input))