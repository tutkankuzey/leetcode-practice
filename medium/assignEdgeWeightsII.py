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
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(len(edges) + 2)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        depths = [0] * (len(edges) + 2)
        parentmap = [0] * (len(edges) + 2) 

        def dfs(parent, node, depth):
            depths[node] = depth
            for neighbor in adj[node]:
                if neighbor != parent:
                    parentmap[neighbor] = node
                    dfs(node, neighbor, depth+1)

        dfs(0, 1, 0)
        MOD = 10**9 + 7
        
        # Find Last Common Ancestor
        def findLCA(u, v, depths, parentmap):
            while depths[u] > depths[v]:
                u = parentmap[u]
            while depths[v] > depths[u]:
                v = parentmap[v]

            while u != v:
                u = parentmap[u]
                v = parentmap[v]

            return u

        finallist = []
        for start, goal in queries:

            if start == goal:
                finallist.append(0)
                continue
            
            lca = findLCA(start, goal, depths, parentmap)
            finallist.append(pow(2, depths[start] + depths[goal] - 2 * depths[lca] - 1, MOD))
        
        return finallist
    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.assignEdgeWeights([[1,2],[1,3],[3,4],[3,5]], [[1,4],[3,4],[2,5]]))