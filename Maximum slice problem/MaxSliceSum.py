# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)
    result = None
    last_max = None
    for i in range(n):
        if i == 0:
            result = A[i]
            last_max = max(0,A[i])
        else:
            #print(result, last_max + A[i])
            result = max(result, last_max + A[i])
            last_max = max(last_max+A[i], 0)
    return result

