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
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket = {} # key: num // width, value: the num in the original list nums
        width = valueDiff if valueDiff != 0 else 1 # if valueDiff = 0, the problem gets reduced 
                                                   # to the previous problem in this set
        for i, num in enumerate(nums):
            index = num // width # because we are looking for numbers that are in a range, 
                                 # the key of the bucket is an integer division
            if index in bucket:
                return True # we have two numbers in the given window that are at most valueDiff apart

            bucket[index] = num

            if index-1 in bucket and abs(num - bucket[index-1]) <= valueDiff:
                return True
        
            if index+1 in bucket and abs(num - bucket[index+1]) <= valueDiff:
                return True
            
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // width]

        return False

if __name__ == "__main__":
    solver = Solution()
    
    nums = [1, 15, 4, 7, 10, -10]
    indexdiff = 5
    valuediff = 2

    print(solver.containsNearbyAlmostDuplicate(nums, indexdiff, valuediff))