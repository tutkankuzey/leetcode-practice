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
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            curry, currx, ans = queue.popleft()

            for dy, dx in directions:
                newx, newy = currx + dx, curry + dy

                if 0 <= newy < m and 0 <= newx < n and maze[newy][newx] == ".":

                    if newy == 0 or newy == m-1 or newx == 0 or newx == n-1:
                        return ans + 1
                    
                    maze[newy][newx] = "+"
                    queue.append((newy, newx, ans+1))

        return -1
        



    
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    maze = [["+","+",".","+"],
            [".",".",".","+"],
            ["+","+","+","."]] 
    
    entrance = [1,2]
    print(sol.nearestExit(maze, entrance))