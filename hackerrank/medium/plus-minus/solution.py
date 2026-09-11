#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive=0
    negative=0
    zeroes=0
    m=len(arr)
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        elif i==0:
            zeroes+=1
    p=positive/m
    n=negative/m
    z=zeroes/m
    return f"{p}\n{n}\n{z}\n"
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr))
