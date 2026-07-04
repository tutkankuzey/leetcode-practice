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
    def __init__(self, x):
        self.val = x
        self.right = None 
        self.left = None 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        parent = {root: None}
        pdepth = -1
        qdepth = -1
        
        def dfs(parent_node, node, depth):
            nonlocal pdepth, qdepth
            if node == None:
                return
            
            # Map node object -> parent node object
            parent[node] = parent_node
            
            if node == p:
                pdepth = depth
            elif node == q:
                qdepth = depth

            if pdepth != -1 and qdepth != -1:
                return

            dfs(node, node.left, depth + 1)
            dfs(node, node.right, depth + 1)
        
        dfs(None, root, 0)

        # Track the actual node objects, not their integer values!
        deeper = p if pdepth >= qdepth else q
        shallower = p if pdepth < qdepth else q

        diff = abs(pdepth - qdepth)

        # Lift the deeper node up to the same level
        for _ in range(diff):
            deeper = parent[deeper]

        # Walk them up together until they collide
        while deeper != shallower:
            deeper = parent[deeper]
            shallower = parent[shallower]

        return deeper
            

       



if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.lowestCommonAncestor(test_input))