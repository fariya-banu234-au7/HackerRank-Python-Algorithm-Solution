#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    choco = 0
    print(m)
    for i in range(len(s)):
        n = 0
        count = 0
        while n < m:
            count = count + s[i+n]
            n = n + 1 
        if count == d:
            choco = choco + 1
        if i+n == len(s):
            break
    return choco

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
