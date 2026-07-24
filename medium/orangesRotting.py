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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rottens = []
        fresh = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottens.append((i, j))
                elif grid[i][j] == 1:
                    fresh.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0

        queue = deque(rottens)
        while queue and fresh:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh.remove((nx, ny))
            ans += 1

        return ans if not fresh else -1

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    grid = [[2,1,0],
            [0,2,1],
            [0,0,0]]
    print(sol.orangesRotting(grid))