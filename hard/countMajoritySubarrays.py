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
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] != target:
                nums[i] = -1
            else:
                nums[i] = 1
        

        ans = 0
        total = 0
        freq = defaultdict(int)
        freq[0] = 1
        valid_starts = 0

        for i in nums:
            if i == -1:
                total -= 1
                valid_starts -= freq[total]
                ans += valid_starts
                freq[total] += 1
            else:
                valid_starts += freq[total]
                ans += valid_starts
                total += 1
                freq[total] += 1
        return ans


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.countMajoritySubarrays(test_input))