#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = 0
    
    hours = int(s[:2])
    mins_sec = s[2:8]
    am_pm = s[-2:]
    
    if am_pm == "PM" and hours != 12:
        hours+=12
            
    elif am_pm == "AM" and hours == 12:
        hours = 0
    time = f"{hours:02d}{mins_sec}"
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
