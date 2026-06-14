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
    def letterCombinations(self, digits: str) -> List[str]:
        
        length = len(digits)

        PHONE = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
                 "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        finallist = []
        def dfs(idx, value):
            if idx != length:
                currentdigit = digits[idx]
                for char in PHONE[currentdigit]:
                    dfs(idx + 1, value + char)
            else:
                finallist.append(value)
                return

        dfs(0, "")
        return finallist



if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.letterCombinations("23"))