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
    def maxNumberOfBalloons(self, text: str) -> int:
        dictletters = {"a": 0, "b": 0, "l":0, "o":0, "n":0}
        for char in text:
            if char in dictletters:
                dictletters[char] +=1

        dictletters["l"] = dictletters["l"] // 2
        dictletters["o"] = dictletters["o"] // 2
        return min(dictletters.values())


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.maxNumberOfBalloons("loonbalxballpoon"))