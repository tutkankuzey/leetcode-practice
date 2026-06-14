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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def checkBeginning(word, wordDict) -> List[str]:
            list = []
            for elem in wordDict:
                targetLength = len(elem)
                wordLength = len(word)
                if wordLength < targetLength:
                    continue
                elif word[0: targetLength] == elem:
                    list.append(elem)
            return list
        
        memory = {}
        def search(s):
            length = len(s)
            if length == 0:
                return True
            elif s in memory:
                return memory[s]
            else:
                candidates = checkBeginning(s, wordDict)
                for candidate in candidates:
                    if search(s[len(candidate):]):
                        memory[s] = True
                        return True
            
            memory[s] = False
            return False
        
        return search(s)

                 

if __name__ == "__main__":
    # Local Test Execution
    sol = Solution()
    print(sol.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))