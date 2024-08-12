# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    count_0 = 0
    passing_cars = 0
    n = len(A)
    if n == 1 or sum(A) == n or sum(A) == 0:
        return 0
    for i in range(n):
        if A[i] == 0:
            passing_cars = passing_cars + (n-i-1) - count_0
            count_0 += 1
    if passing_cars > 1000000000:
        return -1
    else:
        return passing_cars
