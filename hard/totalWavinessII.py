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
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_sum = 0
        
        prev_num_str = ""
        prev_waviness = 0
        
        # Helper function to count waviness only within a targeted window range
        def count_zone_waviness(s: str, start_j: int) -> int:
            zone_count = 0
            # We only scan from the start of the affected zone to the end of the string
            for j in range(max(1, start_j), len(s) - 1):
                if (s[j] > s[j-1] and s[j] > s[j+1]) or (s[j] < s[j-1] and s[j] < s[j+1]):
                    zone_count += 1
            return zone_count

        for i in range(num1, num2 + 1):
            if i < 100:
                continue
            num_str = str(i)
            
            # Case A: First number, or the number of digits changed (e.g., 999 -> 1000)
            if not prev_num_str or len(num_str) != len(prev_num_str):
                current_waviness = count_zone_waviness(num_str, 1)
            
            # Case B: The Shortcut Optimization
            else:
                # Find the first digit that changed (mismatch index)
                mismatch_idx = 0
                for k in range(len(num_str)):
                    if num_str[k] != prev_num_str[k]:
                        mismatch_idx = k
                        break
                
                # The affected zone starts 1 index to the left of the mismatch
                affected_start = mismatch_idx - 1
                
                # Rollback the old suffix waviness, then add the new suffix waviness
                old_suffix_score = count_zone_waviness(prev_num_str, affected_start)
                new_suffix_score = count_zone_waviness(num_str, affected_start)
                
                current_waviness = prev_waviness - old_suffix_score + new_suffix_score
            
            # Add this number's total to our global answer
            total_sum += current_waviness
            
            # Save state for the next number
            prev_waviness = current_waviness
            prev_num_str = num_str
            
        return total_sum

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.totalWaviness(3844051, 7526943))