import numpy as np

# matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
# matrix_np = np.array(matrix)
# matrix_2 = matrix_np.tolist()
# print(matrix)

# !/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
# Source:
# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

def flippingMatrix(matrix):
    # Write your code here
    matrix_np = np.array(matrix)
    tot_len = len(matrix_np[0])
    sub_len = int(len(matrix_np[0]) / 2)

    sum = 0
    for row in range(sub_len):
        for col in range(sub_len):
            sum += np.max([matrix_np[row, col],
                           matrix_np[tot_len-1-row, col],
                           matrix_np[row, tot_len-1-col],
                           matrix_np[tot_len-1-row, tot_len-1-col]
            ])

    return sum
    # change = True
    # while change:
    #     change = False
    #     for col in range(0, tot_len):
    #         if np.sum(matrix_np[0:sub_len,col]) < np.sum(matrix_np[sub_len:,col]):
    #             matrix_np[:,col] = np.flip(matrix_np[:,col])
    #             change = True
    #     for row in range(0, sub_len):
    #         if np.sum(matrix_np[row][0:sub_len]) < np.sum(matrix_np[row][sub_len:]):
    #             matrix_np[row][:] = np.flip(matrix_np[row][:])
    #             change = True
    # sum_total = np.sum(matrix_np[0:sub_len,0:sub_len])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # q = int(input().strip())
    #
    # for q_itr in range(q):
    #     n = int(input().strip())
    #
    #     matrix = []
    #
    #     for _ in range(2 * n):
    #         matrix.append(list(map(int, input().rstrip().split())))
    #
    #     result = flippingMatrix(matrix)
    #
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()

    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    result = flippingMatrix(matrix)
    print(result)
