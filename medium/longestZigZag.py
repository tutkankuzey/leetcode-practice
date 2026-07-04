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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def doZigZag(node, depth, direction):
            if node == None:
                self.ans = max(self.ans, depth-1)
                return

            if direction == "r":
                doZigZag(node.right, depth + 1, "l")
                doZigZag(node.left, 0, "l")
            else:
                doZigZag(node.left, depth + 1, "r")
                doZigZag(node.right, 0, "r")

        doZigZag(root, 0, "l")
        doZigZag(root, 0, "r")

        return self.ans
    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    #print(sol.longestZigZag(test_input))