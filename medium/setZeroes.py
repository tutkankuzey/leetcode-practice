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
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        TrueRow = set()
        TrueCol = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    TrueRow.add(i)
                    TrueCol.add(j) 

        for row in range(m):
            for col in range(n):
                if row in TrueRow or col in TrueCol:
                    matrix[row][col] = 0


if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.setZeroes(test_input))