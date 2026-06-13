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
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 2:
            return max(nums) - min(nums)
        
        result = 0
        while k>0:
            min_ind = nums.index(min(nums))
            max_ind = nums.index(max(nums))

            amount = min(k, min(min_ind, max_ind) + (n - max(min_ind, max_ind)))
            
            result += amount * (max(nums) - min(nums))
            k -= amount
            if min_ind != max_ind:
                del nums[max(min_ind, max_ind)]
                del nums[min(min_ind, max_ind)]
            else:
                del nums[min_ind]
        return result



if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.maxTotalValue([4,2,5,1], 3))