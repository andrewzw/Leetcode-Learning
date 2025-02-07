#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min, max = 0, 0
    arr.sort()
    
    for i in range(4):
        min += arr[i]
        
    for i in range(len(arr)-4, len(arr)):
        max += arr[-i]
            
    print(min, max)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
