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

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def buildTree(index, currentList):
            if index == len(nums):
                return Node(currentList)
  
            root = Node(currentList)

            root.left = buildTree(index + 1, currentList + [nums[index]])
            root.right = buildTree(index + 1, currentList)

            return root

        def collectLeaves(node, powerset):
            if node.left == None and node.right == None:
                powerset.append(node.data)
                return
            
            collectLeaves(node.left, powerset)
            collectLeaves(node.right, powerset)

        powerset = []
        tree = buildTree(0, [])
        collectLeaves(tree, powerset)

        return powerset

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()

    print(sol.subsets([1,2,3]))