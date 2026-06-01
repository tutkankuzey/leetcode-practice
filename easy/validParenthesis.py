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
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        hashmap = {'(': ')', '[': ']', '{': '}'}
        arr = []
        for char in s:
            if char not in hashmap:
                if len(arr) == 0:
                    return False
                topelement = arr.pop()
                if hashmap[topelement] != char:
                    return False
            else:
                arr.append(char)
        return len(arr) == 0

if __name__ == "__main__":
    solver = Solution()
    
    teststring = "([[[[]]]){}{}([])"

    print(solver.isValid(teststring))