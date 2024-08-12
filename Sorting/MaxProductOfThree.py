# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A.sort()
    n = len(A)
    if A[0] * A[n-1] < 0:
        if A[0] * A[1] * A[n-1] > A[n-3] * A[n-2] * A[n-1]:
            return A[0] * A[1] * A[n-1]
        else:
            return A[n-3] * A[n-2] * A[n-1]
    elif A[0] * A[n-1] >= 0:
        return A[n-3] * A[n-2] * A[n-1]



