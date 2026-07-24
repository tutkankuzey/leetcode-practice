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
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        visited.add(0)
        stack = [0]

        while stack:
            curr = stack.pop()
            for room in rooms[curr]:
                if room not in visited:
                    visited.add(room)
                    stack.append(room)
        if len(visited) == n:
            return True
        return False

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.canVisitAllRooms(test_input))