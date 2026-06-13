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
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        stack = [(-1, 1, 0)] #parent, node, depth
        parentmap = {1: -1} #node: parent

        maxdepth = -1
        target = -1
        while stack:
            parent, node, depth = stack.pop()

            if depth > maxdepth:
                maxdepth = depth
                target = node
            
            for neighbor in adj[node]:
                if neighbor != parent:
                    parentmap[neighbor] = node
                    stack.append((node, neighbor, depth+1))

        path = []
        curr = target
        while curr != -1:
            path.append(curr)
            curr = parentmap[curr]
        
        path.reverse()
        
        MOD = 10**9 + 7
        
        return pow(2, maxdepth-1, MOD)
    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]]))