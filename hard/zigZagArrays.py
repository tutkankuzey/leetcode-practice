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
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        
        V = r - l + 1

        # Normalize the bounds to start at 0
        l, r = 0, V - 1

        u = [1] * V
        d = [1] * V
        MOD = 10**9 + 7
        for i in range(n-1):
            new_u = [0] * V
            new_d = [0] * V

            updiff = 0
            for j in range(r-1, -1, -1):
                updiff = (updiff + d[j+1]) % MOD
                new_u[j] += updiff

            downdiff = 0
            for k in range(1, r+1, 1):
                downdiff = (downdiff + u[k-1]) % MOD
                new_d[k] += downdiff

            u = new_u
            d = new_d
            
        return (sum(u) + sum(d)) % MOD

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.zigZagArrays(test_input))