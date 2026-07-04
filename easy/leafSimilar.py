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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def findLeaves(node, finallist):
            if node == None:
                return
            
            if node.left == None and node.right == None:
                finallist.append(node.val)
                return node
            
            findLeaves(node.left, finallist)
            findLeaves(node.right, finallist)

            return finallist
        

        list1 = [] 
        findLeaves(root1, list1)
        list2 = []
        findLeaves(root2, list2)

        return list1 == list2
     

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.leafSimilar(test_input))