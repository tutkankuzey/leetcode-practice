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
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
                

        finallist = []
        def inOrder(node):

            if node == None:
                return
        
            inOrder(node.left)
            finallist.append(node.val)
            inOrder(node.right)
            
            return
        
        inOrder(root)

        
       
            


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.balanceBST(test_input))