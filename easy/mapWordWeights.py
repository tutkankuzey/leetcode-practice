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
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        MOD = 26

        final_chars = []

        for word in words:
            value = 0
            for char in word:
                idx = ord(char) - 97

                value += weights[idx]
            value = value % MOD

            final_chars.append(ALPHABET[len(ALPHABET) - value - 1])

        return "".join(final_chars)
    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))