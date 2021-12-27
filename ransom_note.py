#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'checkMagazine' function below.
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
#  Space complexity: N


def checkMagazine(magazine, note):
    # Write your code here
    # magazine_list = magazine.split(' ')
    magazine_dict = {}

    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        else:
            magazine_dict[word] = 1

    passing = True
    for word in note:
        if word in magazine_dict:
            if magazine_dict[word] < 1:
                passing = False
                break
            else:
                magazine_dict[word] -= 1
        else:
            passing = False
            break

    if passing:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
