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
    def processStr(self, s: str) -> str:
        result = ""

        special = ["*", "#", "%"]
        for char in s:
            if char not in special:
                result += char
            elif char == "*" and result != "":
                result = result[:-1]
            elif char == "#":
                result *= 2
            else:
                result = result[::-1]

        return result
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.processStr("a#b%*"))