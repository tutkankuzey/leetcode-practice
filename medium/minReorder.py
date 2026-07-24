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
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        isConnected = collections.defaultdict(list)
        for start, end in connections:
            isConnected[start].append((end, 1))
            isConnected[end].append((start, 0))
            
        visited = set()
        visited.add(0)
        stack = [0]
        ans = 0

        while stack:
            curr = stack.pop()
            for neighbor, cost in isConnected[curr]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                stack.append(neighbor)
                ans += cost
        return ans

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.minReorder(test_input))