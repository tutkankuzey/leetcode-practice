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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        
        def dfs(node, totalsum):
            if node == None:
                return 0
            pathcount = 0

            totalsum += node.val
            if totalsum == targetSum:
                pathcount += 1


            return pathcount + dfs(node.left, totalsum) + dfs(node.right, totalsum)


        here = dfs(root, 0)
        left = self.pathSum(root.left, targetSum)
        right = self.pathSum(root.right, targetSum)

        return here + left + right
    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.pathSum(test_input))