# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(N):
    if math.sqrt(N) == int(math.sqrt(N)):
        return int(4*math.sqrt(N))
    n = int(math.sqrt(N))
    for i in range(n):
        if N % (n-i) == 0:
            return 2*((n-i) + int(N / (n-i)))
