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
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        
        leftarray = []
        rightarray = []

        appendright = 0
        for i in nums:
            appendright += i
        
        appendleft = 0
        for i in range(len(nums)):
            rightarray.append(appendright - nums[i])
            leftarray.append(appendleft)
            appendright -= nums[i]
            appendleft += nums[i]
        
        ans = []
        for i in range(len(nums)):
            ans.append(abs(rightarray[i] - leftarray[i]))
        return ans

if __name__ == "__main__":
    nums = [10,4,8,3]
    sol = Solution()
    print(sol.LeftRightDifference(nums))