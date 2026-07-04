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
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currmax):
            isgood = 0
            if node == None:
                return 0
            
            if node.val >= currmax:
                currmax = node.val
                isgood = 1


            return isgood + dfs(node.left, currmax) + dfs(node.right, currmax)

        
        return dfs(root, root.val)

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.goodNodes(test_input))