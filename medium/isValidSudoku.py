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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and board[i].count(board[i][j]) >= 2:
                    return False

        for i in range(9):
            vertical = []
            for j in range(9):
                vertical.append(board[j][i])
            for k in vertical:
                if k != '.' and vertical.count(k) >= 2:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                arr = []
                arr.append(board[i][j])
                arr.append(board[i][j+1])
                arr.append(board[i][j+2])
                arr.append(board[i+1][j])
                arr.append(board[i+1][j+1])
                arr.append(board[i+1][j+2])
                arr.append(board[i+2][j])
                arr.append(board[i+2][j+1])
                arr.append(board[i+2][j+2])
                for k in arr:
                    if k != '.' and arr.count(k) >= 2:
                        return False
        return True

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    test_input = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    
    print(sol.isValidSudoku(test_input))