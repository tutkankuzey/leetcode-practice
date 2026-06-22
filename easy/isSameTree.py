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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def inOrder(nodep, nodeq):

            if nodep == None and nodeq == None:
                return True
            elif (nodep == None and nodeq != None) or (nodeq == None and nodep != None):
                return False
            
            if nodep.val != nodeq.val:
                return False
        
            if not inOrder(nodep.left, nodeq.left):
                return False
            if not inOrder(nodep.right, nodeq.right):
                return False
            
            return True
        
        return inOrder(p, q)

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.isSameTree(test_input))