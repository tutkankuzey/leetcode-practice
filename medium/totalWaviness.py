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
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for i in range(num1, num2 + 1):
            if i <= 99:
                continue

            num = str(i)

            for j in range(0, len(num) - 2):
                if (num[j+1] > num[j] and num[j+1] > num[j+2]) or (num[j+1] < num[j] and num[j+1] < num[j+2]):
                    ans = ans + 1
        
        return ans

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.totalWaviness(4848, 4848))