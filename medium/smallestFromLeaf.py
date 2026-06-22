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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        ans = "z" * 8501
        def traverse(node, message):
            nonlocal ans
            if (node.left == None and node.right == None):
                ans = min(ans, chr(node.val + 97) + message)
                return
            
            if node.left != None:
                traverse(node.left, chr(node.val + 97) + message)
            if node.right != None:
                traverse(node.right, chr(node.val + 97) + message)
                
        traverse(root, "")
        return ans
            




if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.smallestFromLeaf([1, 1, 1, 1]))