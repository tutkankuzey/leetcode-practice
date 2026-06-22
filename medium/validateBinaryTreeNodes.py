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
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        seen = set()
        for i in range(n):
            if leftChild[i] != -1 and leftChild[i] in seen:
                return False
            if rightChild[i] != -1 and rightChild[i] in seen:
                return False
            
            seen.add(leftChild[i])
            seen.add(rightChild[i])

        candidates = (set(range(n)) - seen)

        if len(candidates) != 1:
            return False
        stack = [candidates.pop()]

        visited = set()

        while stack:
            node = stack.pop()
            if node == -1:
                continue
            if node in visited: # we visited the same node twice
                return False
            
            visited.add(node)

            stack.append(leftChild[node])
            stack.append(rightChild[node])

        return visited == set(range(n))  


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.validateBinaryTreeNodes())
