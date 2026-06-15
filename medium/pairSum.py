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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1

        valset = {}
        curr = head
        for i in range(size):
            if i < (size / 2):
                valset[i] = curr.val
            else:
                valset[size - i - 1] += curr.val
            curr = curr.next

        return max(valset.values())
            


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.pairSum(test_input))