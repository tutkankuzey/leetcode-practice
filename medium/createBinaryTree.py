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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = {}

        children = set()
        
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            
            if child not in nodes:
                nodes[child] = TreeNode(child)

            children.add(child)

            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for node in nodes:
            if node not in children:
                return nodes[node]

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.createBinaryTree(test_input))