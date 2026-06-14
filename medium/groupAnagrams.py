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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1:
            return [[strs[0]]]
        
        dict = defaultdict(list)

        for word in strs:
            sortedword = "".join(sorted(word))
            dict[sortedword].append(word)

        return list(dict.values())

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.groupAnagrams((["eat","tea","tan","ate","nat","bat"])))