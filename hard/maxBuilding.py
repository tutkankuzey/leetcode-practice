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
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if len(restrictions) == 0:
            return n - 1
        has_restriction = {res[0]: res[1] for res in restrictions}

        restrictions.append([1, 0])

        if n not in has_restriction:
            restrictions.append([n, 10**9 + 1])


        restrictions.sort()
        for i in range(len(restrictions) - 1):
            restrictions[i+1][1] = min(restrictions[i+1][1], restrictions[i][1] + (restrictions[i+1][0] - restrictions[i][0]))

        
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + (restrictions[i+1][0] - restrictions[i][0]))
        
        ans = 0
        for i in range(len(restrictions) - 1):
            candidate =  (restrictions[i+1][0] - restrictions[i][0] + restrictions[i+1][1] + restrictions[i][1]) // 2

            ans = max(ans, candidate) 
        return ans
        

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.maxBuilding(5, [[2,1],[4,1]]))