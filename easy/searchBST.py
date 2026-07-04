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

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while current != None and current.val != val:
            if current.val < val:
                current = current.right
            else:
                current = current.left
        return current


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.searchBST(test_input))