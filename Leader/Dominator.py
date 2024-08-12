# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(A):
    n = len(A)
    dictA = dict()
    for i in range(n):
        if not A[i] in dictA:
            dictA[A[i]] = []
        dictA[A[i]].append(i)
    for num in dictA:
        if len(dictA[num]) > math.floor(n/2):
            return dictA[num][0]
    return -1
        

