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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        visited = set()
        n = len(isConnected)

        for i in range(n):
            if i not in visited:
                stack = [i]
                while stack:
                    curr = stack.pop()
                    if curr not in visited:
                        visited.add(curr)
                        for j in range(n):
                            if isConnected[curr][j] == 1:
                                stack.append(j)
                
                ans += 1
            else:
                pass
        return ans

        

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.findCircleNum(test_input))