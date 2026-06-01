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
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 0
        dict = {}
        left = 0
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= left:
                left = dict[s[i]] + 1
    
            dict[s[i]] = i
            ans = max(ans, i - left + 1)

        return ans

if __name__ == "__main__":
    solver = Solution()
    s = "aabcdefabcdefa"
    print(solver.lengthOfLongestSubstring(s))