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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head
        while curr:
            if curr not in visited:
                visited.add(curr)
            else:
                return curr
            curr = curr.next
        return None
        

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.detectCycle(test_input))