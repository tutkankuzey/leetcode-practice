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
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
  
        # 1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000 given
        timeland = 3000
        timewater = 3000

        # find the minimum times to finish each type of ride
        for i in range(len(landDuration)):
            timeland = min(timeland, landDuration[i] + landStartTime[i])

        for i in range(len(waterDuration)):
            timewater = min(timewater, waterDuration[i] + waterStartTime[i])

        # find the minimum time to finish a land ride, given you have just rode the earliest finishing water ride
        time3 = 3000
        for i in range(len(landStartTime)):
            if landStartTime[i] <= timewater:
                time3 = min(time3, timewater + landDuration[i])
            else:
                time3 = min(time3, landStartTime[i] + landDuration[i])

        # find the minimum time to finish a water ride, given you have just rode the earliest finishing land ride 
        time4 = 3000
        for i in range(len(waterStartTime)):
            if waterStartTime[i] <= timeland:
                time4 = min(time4, timeland + waterDuration[i])
            else:
                time4 = min(time4, waterStartTime[i] + waterDuration[i])
        
        return min(time3, time4)

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    landStartTime = [2,8]
    landDuration = [4,1]
    waterStartTime = [6]
    waterDuration = [3]
    print(sol.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
