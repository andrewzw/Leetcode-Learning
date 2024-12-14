#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

import string as s

P = 131
M = pow(10, 9) + 7
APPENDS = [""] + list(s.ascii_letters) + [str(d) for d in range(10)]


def calcHash(string):
    total = 0
    for c in range(len(string)):
        equation = ord(string[c]) * pow(P, (len(string) - (c + 1)))
        total += equation
    return total % M


def authEvents(events):
    ans = []
    for event, value in events:
        if event == "setPassword":
            good_hashs = set()
            for x in APPENDS:
                good_hashs.add(calcHash(value + x))
        else:
            assert event == "authorize"
            if int(value) in good_hashs:
                ans.append(1)
            else:
                ans.append(0)
    return ans


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
