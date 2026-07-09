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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        finallist = [0] * len(temperatures)
        stack = collections.deque()
        stack.append(0)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ind = stack.pop()
                finallist[ind] = i - ind

            stack.append(i)

        return finallist
        
    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.dailyTemperatures(test_input))