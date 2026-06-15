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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node
        # prev.next equals slow

        prev.next = slow.next
        return head


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.deleteMiddle(test_input))