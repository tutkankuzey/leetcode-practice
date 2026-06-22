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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        ans = 0
        def dfs(node, depth):
            nonlocal ans
            if node.left == None and node.right == None:
                ans = max(ans, depth)
                return

            if node.left != None:
                dfs(node.left, depth+1)
            
            if node.right != None:
                dfs(node.right, depth+1)
            
        dfs(root, 1)
        return ans

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.maxDepth(test_input))