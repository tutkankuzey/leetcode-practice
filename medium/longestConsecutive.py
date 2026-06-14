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
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        dict = set(nums)

        result = 1
        for num in dict:
            if num-1 not in dict and num+1 in dict:
                curr = num
                while curr + 1 in dict:
                    curr += 1
                result = max(result, curr + 1 - num)
            else:
                continue

        return result
    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))