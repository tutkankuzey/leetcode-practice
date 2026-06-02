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
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        
        #Transpose the matrix (swap across the diagonal)
        for i in range(n):
            for j in range(i + 1, n):  # start at i + 1 so we don't swap elements twice
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
            
if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    # print(sol.rotate(test_input))